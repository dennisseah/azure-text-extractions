# Infrastructure

## Terraform
install terraform from [here](https://learn.hashicorp.com/tutorials/terraform/install-cli)


## Azure CLI
install azure cli from [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

## Azure Login

```bash
az login
az account set --subscription <SUBSCRIPTION_ID>
az account show
```
make sure you have the correct subscription selected

## Terraform Init, validate and plan

copy `terraform.tfvars.sample` to `terraform.tfvars`.
Add a variable `resource_prefix = <uniq-name>`, for example your handle like 'joesmith' or 'janedoe'

run this script to initialize terraform and validate the configuration

```bash
terraform init
terraform validate
terraform plan -out=plan.tfplan
```

## Terraform Apply

```bash
terraform apply "plan.tfplan"
```

After deployment, you will see the outputs which will help you to setup the `.env` file for the project.

# Remove all resources

```bash
terraform destroy
```