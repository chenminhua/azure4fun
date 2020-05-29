
[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fservice-fabric-secure-cluster-5-node-1-nodetype%2Fazuredeploy.json)  [![Visualize](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/visualizebutton.svg?sanitize=true)](http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fservice-fabric-secure-cluster-5-node-1-nodetype%2Fazuredeploy.json)


### 部署
部署一套 5Node, Single Node Type 的SF集群，运行在一个 standard_d2 的 vmss 上。

- 先运行 New-ServiceFabricClusterCertificate.ps1
  - 输入密码，比如1234qwer
  - 输入certDNSName: mhsfcert
  - 输入keyVaultName: azurekvStan ，注意，这个keyVault要提前建好
  - 输入keyVaultSecretName: sfSecret
- 上一步执行完成后，记录下返回的 source vault resource id, certificate url, certificate thumbprint
- 同时注意，你的目录下面多了一个文件 mhsfcert.pfx

```ps1
az group delete -n "sfrg"
az group create -n "sfrg" --location "eastasia"
az deployment group create -n "sfdeploy" -g "sfrg" --template-file ./azuredeploy.json --parameters ./azuredeploy.parameters.json
```

