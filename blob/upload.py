from azure.storage.blob import ContainerClient, BlobClient

# container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="images")

# container_client.create_container()

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=blahblahsa;AccountKey=OGDldoiJybwwxMF8BwPVzxQ/R/u0eyza0nuxu71X6Tb15E0gb50E2VO1RSAI46lS+r4bylX00ipPTHdJaro2CA==;EndpointSuffix=core.windows.net", container_name="logs", blob_name="video.mp4")

with open("./video.mp4", "rb") as data:
    blob.upload_blob(data)
