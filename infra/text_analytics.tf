

resource "azurerm_cognitive_account" "text-analytics" {
  name                  = "${var.resource_prefix}-text_extraction-service"
  location              = local.openai_location
  resource_group_name   = azurerm_resource_group.resource_group.name
  kind                  = "TextAnalytics"
  custom_subdomain_name = "${var.resource_prefix}textextract"
  sku_name              = "S"

  tags = {
    Acceptance = "Test"
  }
}
