---
title: "AWS S3 Multipart Upload: Handling Large Objects"
date: 2018-03-24 08:22:40 +0000
author: "Eric Ma"
layout: post
categories: [design-patterns-architecture]
canonical: /maximum-size-of-s3-objects/
---

Amazon S3 has a maximum object size of 5TB per object. This limit applies uniformly across all storage classes and regions — there are no exceptions or workarounds.

## Understanding the 5TB Ceiling

The 5TB limit is a hard constraint at the API level. You cannot upload, copy, or restore an object larger than this. While this covers the vast majority of use cases, it’s worth knowing upfront if you’re dealing with extremely large datasets or specialized workloads that might exceed this threshold.

For objects at or near the 5TB boundary, you’ll need to split them before uploading or use alternative services like AWS DataSync or Snowball for transfer, then reassemble on the target side if needed.

## Multipart Upload Essentials

AWS recommends multipart upload for any object larger than 100MB. A single PUT request for a large file is slower, less reliable, and ties up resources unnecessarily. Multipart uploads give you parallelism, resumability, and better throughput.

The multipart API specifications:

- Maximum 10,000 parts per object
- Each part: 5MB to 5GB in size
- Last part can be smaller than 5MB
- Minimum final object size of 5MB

For a 5TB object with 5GB parts, you need about 1,024 parts — well under the 10,000 limit. Keep part count reasonable (ideally under 1,000) for better performance and simpler management.

## Uploading with AWS CLI

The CLI handles multipart uploads automatically for large files. Configure the threshold and other parameters as needed:

``` bash
aws s3 cp large-file.iso s3://bucket-name/ \
  --storage-class STANDARD_IA \
  --sse AES256 \
  --metadata "description=backup"
```

For fine-grained control, set multipart threshold and chunk size in your AWS config:

``` bash
[default]
s3 =
    multipart_threshold = 100MB
    multipart_chunksize = 256MB
    max_concurrent_requests = 10
```

The CLI also supports `--expected-size` to optimize the upload strategy upfront:

``` bash
aws s3 cp large-file.iso s3://bucket-name/ \
  --expected-size 2000000000 \
  --no-progress
```

## Python Uploads with Boto3

Use boto3’s resource API for automatic multipart handling with configurable thresholds:

``` python
import boto3
from botocore.config import Config

s3_resource = boto3.resource('s3')

bucket = s3_resource.Bucket('bucket-name')
bucket.upload_file(
    'large-file.iso',
    'key-name',
    Config=Config(
        multipart_threshold=100 * 1024 * 1024,
        multipart_chunksize=256 * 1024 * 1024,
        max_concurrent_requests=10
    )
)
```

For resumable uploads or custom retry logic, the client API with manual part management gives more control:

``` python
import boto3

s3_client = boto3.client('s3')

response = s3_client.create_multipart_upload(Bucket='bucket-name', Key='key-name')
upload_id = response['UploadId']

# Upload parts with retry logic
parts = []
with open('large-file.iso', 'rb') as f:
    part_num = 1
    while True:
        data = f.read(256 * 1024 * 1024)
        if not data:
            break

        part_response = s3_client.upload_part(
            Bucket='bucket-name',
            Key='key-name',
            PartNumber=part_num,
            UploadId=upload_id,
            Body=data
        )
        parts.append({
            'ETag': part_response['ETag'],
            'PartNumber': part_num
        })
        part_num += 1

s3_client.complete_multipart_upload(
    Bucket='bucket-name',
    Key='key-name',
    UploadId=upload_id,
    MultipartUpload={'Parts': parts}
)
```

## Managing Incomplete Uploads

Multipart uploads that fail or get interrupted leave orphaned parts in S3, which incur storage charges. Clean these up regularly:

``` bash
# List incomplete uploads
aws s3api list-multipart-uploads --bucket bucket-name

# Abort a specific upload
aws s3api abort-multipart-upload \
  --bucket bucket-name \
  --key object-key \
  --upload-id upload-id
```

Use S3 lifecycle policies to automatically clean up incomplete multipart uploads after a set number of days:

``` json
{
  "Rules": [
    {
      "Id": "cleanup-incomplete-uploads",
      "Status": "Enabled",
      "AbortIncompleteMultipartUpload": {
        "DaysAfterInitiation": 7
      }
    }
  ]
}
```

Apply the policy:

``` bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket bucket-name \
  --lifecycle-configuration file://lifecycle.json
```

## Network and Performance Considerations

S3 doesn’t throttle uploads by object size, but real-world throughput depends on:

- Available network bandwidth from your source
- Number of parallel connections and threads
- Geographic distance to the S3 region
- Endpoint type (regional vs. S3 Transfer Acceleration)

For multi-gigabyte uploads over slow or unreliable connections, consider AWS DataSync for automatic retry and monitoring, or AWS Snowball for offline transfer of massive datasets.

Enable S3 Transfer Acceleration for cross-region or international uploads:

``` bash
aws s3 cp large-file.iso s3://bucket-name/ \
  --region us-east-1 \
  --endpoint-url https://bucket-name.s3-accelerate.amazonaws.com
```

## Storage Class Behavior

The 5TB limit applies consistently across all storage classes: Standard, Intelligent-Tiering, Standard-IA, Glacier, and Glacier Deep Archive. Object size alone doesn’t influence which storage class to use — base that decision on access patterns and retention requirements instead.
