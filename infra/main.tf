locals {
  openai_location = "eastus"
}

variable "resource_prefix" {
  description = "Prefix for all resources"
  type        = string
}

variable "azure_subscription_id" {
  description = "Azure subscription id"
  type        = string
}

data "azurerm_subscription" "primary" {}
data "azurerm_client_config" "current" {}


resource "azurerm_resource_group" "resource_group" {
  name     = "${var.resource_prefix}_text_extraction_rg"
  location = "East US 2"
}
