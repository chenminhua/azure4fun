### How Functions App works in Azure

- Pay only for the time your code runs and trust azure to scale as needed.
- Functions are great for processing data, integrating systems, working with IOT, building simple APIs.

### How much does functions cost

- Consumption Plan: pay for the time that your code runs.
- App Service Plan: Run your function just like your web app.

## Deployment

```sh
az account list-locations
az group create -n "funcrg" --location "eastasia"
az deployment group create -n "funcdeploy" -g "funcrg" --template-file "./azuredeploy.json" --parameters ./azuredeploy.parameters.json
```

deployed component

- App Service plan
- App Serviceï¼š è¿™ä¸ªå°±æ˜¯ä½ çš„ Function Appã€‚
- Storage Account
