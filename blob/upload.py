from azure.storage.blob import ContainerClient, BlobClient

# container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="images")

# container_client.create_container()

blob = BlobClient.from_connection_string(conn_str="连接字符串", container_name="images", blob_name="blahblahsa")

with open("./azuredeploy.json", "rb") as data:
    blob.upload_blob(data)
