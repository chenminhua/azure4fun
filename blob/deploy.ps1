az group delete -n "blahblahrg"
az group create -n "blahblahrg" --location "eastasia"
az deployment group create -n "blobdeploy" -g "blahblahrg" --template-file ./azuredeploy.json --parameters ./azuredeploy.parameters.json