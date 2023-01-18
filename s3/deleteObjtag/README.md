# S3 Delete Object Tagging

This  code will hleps to add the s3 Delete tag on the oject, the max tag that we can add is upto 10.


```
import boto3

s3_client = boto3.client('s3')

objects = s3_client.list_objects_v2(Bucket='<Bucket-Name>')

for obj in objects['Contents']:
    
    response = s3_client.delete_object_tagging(
    Bucket='<Bucket-Name>',
    Key=obj['Key'],
    ExpectedBucketOwner='<AWS-AccountID>',
    )


```

