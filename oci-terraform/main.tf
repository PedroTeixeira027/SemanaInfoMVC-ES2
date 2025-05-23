terraform {
  required_providers {
    oci = {
      source = "oracle/oci"
      version = "6.35.0"
    }
  }
}

provider "oci" {
  tenancy_ocid        = var.tenancy_ocid
  user_ocid           = var.user_ocid
  fingerprint         = var.fingerprint
  region              = var.region
}

# Obtém todos os domínios de disponibilidade no compartimento
data "oci_identity_availability_domains" "ads" {
  compartment_id = var.compartment_ocid
}

resource "oci_core_virtual_network" "vcn" {
  compartment_id = var.compartment_ocid
  display_name   = "VCN_TERRAFORM"
  cidr_block     = "10.6.0.0/16"
  dns_label      = "vcnterraform"
}

resource "oci_core_internet_gateway" "igw" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "Internet Gateway"
}

resource "oci_core_nat_gateway" "nat_gateway" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "NAT Gateway"
}

resource "oci_core_service_gateway" "service_gateway" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "Service Gateway"

  services {
    service_id = "your_service_ocid_here" # All GRU Services In Oracle Services Network
  }
}

resource "oci_core_route_table" "public_route" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "Public Route Table"

  route_rules {
    destination       = "0.0.0.0/0"
    destination_type  = "CIDR_BLOCK"
    network_entity_id = oci_core_internet_gateway.igw.id
  }
}

resource "oci_core_route_table" "private_route" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "Private Route Table"

  route_rules {
    destination       = "0.0.0.0/0"
    destination_type  = "CIDR_BLOCK"
    network_entity_id = oci_core_nat_gateway.nat_gateway.id
  }

  route_rules {
    destination       = "all-gru-services-in-oracle-services-network"
    destination_type  = "SERVICE_CIDR_BLOCK"
    network_entity_id = oci_core_service_gateway.service_gateway.id
  }
}

resource "oci_core_subnet" "public_subnet" {
  compartment_id      = var.compartment_ocid
  vcn_id              = oci_core_virtual_network.vcn.id
  display_name        = "Public Subnet"
  cidr_block          = "10.6.0.0/24"
  route_table_id      = oci_core_route_table.public_route.id
  security_list_ids   = [oci_core_security_list.public_security_list.id]
  dns_label           = "publicsubnet"
}

resource "oci_core_subnet" "private_subnet" {
  compartment_id      = var.compartment_ocid
  vcn_id              = oci_core_virtual_network.vcn.id
  display_name        = "Private Subnet"
  cidr_block          = "10.6.1.0/24"
  route_table_id      = oci_core_route_table.private_route.id
  security_list_ids   = [oci_core_security_list.private_security_list.id]
  dns_label           = "privatesubnet"
}

resource "oci_core_security_list" "public_security_list" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "Public Security List"

  ingress_security_rules {
    source      = "0.0.0.0/0"
    protocol    = "all"
  }

  egress_security_rules {
    destination = "0.0.0.0/0"
    protocol    = "all"
  }
}

resource "oci_core_security_list" "private_security_list" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "Private Security List"

  ingress_security_rules {
    source      = "0.0.0.0/0"
    protocol    = "all"
  }

  egress_security_rules {
    destination = "0.0.0.0/0"
    protocol    = "all"
  }
}

resource "oci_core_network_security_group" "nsg" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_virtual_network.vcn.id
  display_name   = "NSG_TERRAFORM"
}

resource "oci_core_network_security_group_security_rule" "nsg_rule" {
  network_security_group_id = oci_core_network_security_group.nsg.id
  direction                 = "INGRESS"
  protocol                  = "all"
  source_type               = "CIDR_BLOCK"
  source                    = "0.0.0.0/0"
}

resource "oci_core_instance" "ubuntu_vm" {
  compartment_id      = var.compartment_ocid
  availability_domain = tolist(data.oci_identity_availability_domains.ads.availability_domains)[0].name
  shape               = "VM.Standard.E5.Flex"
  display_name        = "Ubuntu Server VM"

  create_vnic_details {
    subnet_id          = oci_core_subnet.public_subnet.id
    assign_public_ip   = true
    display_name       = "Terraform Ubuntu VM VNIC"
    hostname_label     = "ubuntuvm"
    nsg_ids            = [oci_core_network_security_group.nsg.id]
  }

  source_details {
    source_type = "image"
    source_id   = var.ubuntu_image_ocid 
  }

  metadata = {
    ssh_authorized_keys = <<EOF
your_pub_ssh_key_here
EOF
  }

  shape_config {
    ocpus = 1
    memory_in_gbs = 8
  }
}

resource "oci_core_volume" "additional_disk" {
  compartment_id      = var.compartment_ocid
  availability_domain = tolist(data.oci_identity_availability_domains.ads.availability_domains)[0].name
  display_name        = "Ubuntu Disk"
  size_in_gbs         = 50
}

resource "oci_core_volume_attachment" "volume_attachment" {
  instance_id    = oci_core_instance.ubuntu_vm.id
  volume_id      = oci_core_volume.additional_disk.id
  attachment_type = "paravirtualized"
}

## Zabbix Server

resource "oci_core_instance" "zabbix_vm" {
  compartment_id      = var.compartment_ocid
  availability_domain = tolist(data.oci_identity_availability_domains.ads.availability_domains)[0].name
  shape               = "VM.Standard.E5.Flex"
  display_name        = "Zabbix Server VM"

  create_vnic_details {
    subnet_id          = oci_core_subnet.public_subnet.id
    assign_public_ip   = true
    display_name       = "Terraform Zabbix VM VNIC"
    hostname_label     = "zabbixvm"
    nsg_ids            = [oci_core_network_security_group.nsg.id]
  }

  source_details {
    source_type = "image"
    source_id   = var.ubuntu_image_ocid
  }

  metadata = {
    ssh_authorized_keys = <<EOF
your_key_here
  }

  shape_config {
    ocpus = 1
    memory_in_gbs = 4
  }
}

resource "oci_core_volume" "zabbix_disk" {
  compartment_id      = var.compartment_ocid
  availability_domain = tolist(data.oci_identity_availability_domains.ads.availability_domains)[0].name
  display_name        = "Zabbix Disk"
  size_in_gbs         = 50
}

resource "oci_core_volume_attachment" "zabbix_volume_attachment" {
  instance_id    = oci_core_instance.zabbix_vm.id
  volume_id      = oci_core_volume.zabbix_disk.id
  attachment_type = "paravirtualized"
}
