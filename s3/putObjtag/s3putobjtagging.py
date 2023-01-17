import boto3

s3_client = boto3.client('s3')

objects = s3_client.list_objects_v2(Bucket='ops-test-ec')

for obj in objects['Contents']:
    print(obj['Key'])
    response = s3_client.put_object_tagging(
    Bucket='ops-test-ec',
    Key=obj['Key'],
   # Key='/*',
   # VersionId='FQPf0LC1HaqvGYz0DRRjtowTKXAg8UZf',
   # ContentMD5='string',
 #   ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
    Tagging={
        'TagSet': [
            {
                'Key': 'env1',
                'Value': 'fullandinewtest11'
            },
        ]
    },
    ExpectedBucketOwner='366751107728',
    RequestPayer='requester'
    )


