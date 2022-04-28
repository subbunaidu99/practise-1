IMPORT BOTO 3
import json
client = boto3.client("ec2")
vpcs = client.describe_vpcs()
print(vpcs)
