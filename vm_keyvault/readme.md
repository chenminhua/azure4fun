```sh
az group create -n "rg-azurekv" --location "eastasia"
az keyvault create -n "azurekvStan" -g "rg-azurekv" --location "eastasia" --enabled-for-deployment --enabled-for-disk-encryption --enabled-for-template-deployment
az keyvault secret set -n "sshpubkey" --vault-name "azurekvStan" --value "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC9L2uCKozX9AAbRlqa8MpMzctIbloMJCMa+Nq+ZnJ4T7czoEYqnRNFDa283luvcRzGGos6co/KMsqKR1JwYNINrrmNrQAiKIUgl5IPwkiq/f6fW99RisEH77SG4AcyH3l3O1ipmX1+bZ4LwGwsImJBdtxXpsD9bYR1T4BmJmxqELjqpuAJbnMOxvbwC0i0rUySa//z8DtFkPoCHCnTyci4suS7v35HwJkjyd93Em2FMf+WL3KsDL8Hcqeo9xmE6H8+jhQVXkoo18GRo4RiYKkMD3b9AWV4n9qAo3W73qDoGIT3w5iGDncXri1YSAJzL0oeQHzQFWZWFCYcRPAP4br/uyu33PISOAnqqKUEBkeSZbBiqcXQw0/4Z1CsYjcXnh3udXmiNraqCO/KbRD89oKqkhFf4CMxjoViDom9RuhANyQRhllRXUFUKovBcnOpNDkpE1fK70+DGXuKxdl4JQhTacCrE+keXLBe83hfcVfADxh3kHpGC1f0SA9sMrnJ4f8= chenminhua@chenminhuas-MacBook-Pro.local"

az group delete -n "testrg"
az group create -n "testrg" --location "eastasia"
az deployment group create -n "testdeploy" -g "testrg" --template-file ./azuredeploy.json --parameters ./azuredeploy.parameters.json
```


todo: use keyvault to store the ssh-key

