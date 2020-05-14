az group delete -n "testrg"
az group create -n "testrg" --location "eastasia"
az deployment group create -n "testdeploy" -g "testrg" --template-file ./azuredeploy.json --parameters ./azuredeploy.parameters.json


todo: use keyvault to store the ssh-key