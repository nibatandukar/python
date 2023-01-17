# S3 Put Object Tagging

This  code will hleps to add the s3 Put tag on the oject, the max tag that we can add is upto 10.


```
import boto3

s3_client = boto3.client('s3')

objects = s3_client.list_objects_v2(Bucket='<Bucket-Name>')

for obj in objects['Contents']:
    
    response = s3_client.get_object_tagging(
    Bucket='<Bucket-Name>',
   # Key='folder2/disk.sh',
    Key=obj['Key'],
    ExpectedBucketOwner='44455*******',
    RequestPayer='requester'
    )
    print(obj['Key'], '=',  response["TagSet"], sep = "\t")


```

