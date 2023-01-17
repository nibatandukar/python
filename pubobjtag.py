#ops-test-ec
import boto3
client = boto3.client('s3')
response = client.put_object_tagging(
    Bucket='ops-test-ec',
    Key='Screenshot from 2023-01-06 13-48-00.png',
   # Key='/*',
   # VersionId='FQPf0LC1HaqvGYz0DRRjtowTKXAg8UZf',
   # ContentMD5='string',
 #   ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
    Tagging={
        'TagSet': [
            {
                'Key': 'env1',
                'Value': 'test11'
            },
        ]
    },
    ExpectedBucketOwner='366751107728',
    RequestPayer='requester'
)

