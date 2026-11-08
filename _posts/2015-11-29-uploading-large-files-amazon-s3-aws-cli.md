---
title: "Optimizing Large File Uploads to S3 with AWS CLI"
date: 2015-11-29 01:01:40 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /uploading-large-files-amazon-s3-aws-cli/
---

Install AWS CLI v2 through your system’s package manager for production deployments.

On Debian/Ubuntu:

``` bash
sudo apt-get update
sudo apt-get install awscli
```

On RHEL/CentOS/Fedora:

``` bash
sudo dnf install awscli
```

Or use the official installer directly:

``` bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscli-v2.zip"
unzip awscli-v2.zip
sudo ./aws/install
```

Verify installation:

``` bash
aws --version
```

## Configure AWS CLI credentials

Set up credentials interactively:

``` bash
aws configure
```

You’ll be prompted for AWS Access Key ID, Secret Access Key, default region, and output format. Credentials are stored in `~/.aws/credentials` and `~/.aws/config`.

For multiple environments, use named profiles:

``` bash
aws configure --profile production
aws configure --profile development
aws configure --profile staging
```

Reference the profile when running commands:

``` bash
aws s3 cp file.data s3://bucket/path/ --profile production
```

**For EC2 instances:** Use IAM instance roles instead of stored credentials. IAM roles provide temporary credentials automatically, eliminating the need to manage long-lived access keys. Configure your EC2 instance profile with the appropriate IAM role, and AWS CLI will use those credentials without additional setup.

## Upload large files to S3

AWS CLI handles multipart uploads automatically for large files. For a 150GB file:

``` bash
aws s3 cp ./150GB.data s3://bucket-name/store_dir/
```

The tool automatically:

- Splits the file into configurable chunks (default 8MB for files over 100MB)
- Uploads parts in parallel with automatic retry
- Reassembles on S3

Progress output shows:

    Completed 1234 of 9896 part(s) with 1 file(s) remaining
    upload: ./150GB.data to s3://bucket-name/store_dir/150GB.data

Individual parts can fail and retry without restarting the entire upload.

## Optimize upload performance

Control parallelism, part size, and bandwidth by editing `~/.aws/cli/config`:

``` ini
[default]
s3 =
    max_concurrent_requests = 20
    max_queue_size = 10000
    max_bandwidth = 100MB/s
    multipart_threshold = 64MB
    multipart_chunksize = 16MB
    max_in_memory_upload_chunks = 10
```

Tuning these values depends on your network and system resources:

- **max_concurrent_requests:** Higher values (10-20) improve throughput on fast networks; lower values reduce memory usage
- **multipart_chunksize:** Larger chunks (32MB-64MB) reduce overhead for gigabit networks; smaller chunks (8MB) work better on constrained connections
- **max_bandwidth:** Limit concurrent bandwidth to avoid saturating your network connection
- **multipart_threshold:** Files smaller than this threshold use a single request
- **max_in_memory_upload_chunks:** Limits the number of parts buffered in memory; reduce this if you’re memory-constrained

Example upload with explicit settings and metadata:

``` bash
aws s3 cp ./150GB.data s3://bucket-name/store_dir/ \
  --region us-west-2 \
  --metadata "uploaded-by=automation,timestamp=$(date +%s)"
```

For faster uploads across regions, enable S3 Transfer Acceleration on the bucket:

``` bash
aws s3api put-bucket-accelerate-configuration \
  --bucket bucket-name \
  --accelerate-configuration Status=Enabled
```

Then use the accelerated endpoint:

``` bash
aws s3 cp ./150GB.data s3://bucket-name/store_dir/ \
  --region us-west-2 \
  --expected-size 161061273600
```

Transfer Acceleration uses CloudFront edge locations but incurs additional costs. Test whether it improves performance for your specific use case.

## Monitor uploads

Check transfer progress with verbose logging:

``` bash
aws s3 cp ./150GB.data s3://bucket-name/store_dir/ --debug 2>&1 | grep -i "transfer"
```

The `--debug` flag outputs detailed HTTP requests and responses. For large files this generates substantial output; redirect to a file for later review:

``` bash
aws s3 cp ./150GB.data s3://bucket-name/store_dir/ --debug > transfer.log 2>&1
```

List in-progress multipart uploads:

``` bash
aws s3api list-multipart-uploads --bucket bucket-name
```

Output:

``` json
{
    "Uploads": [
        {
            "UploadId": "...",
            "Key": "store_dir/150GB.data",
            "Initiated": "2025-11-15T10:30:00Z",
            "StorageClass": "STANDARD",
            "Owner": {"DisplayName": "...", "ID": "..."}
        }
    ]
}
```

Check parts already uploaded:

``` bash
aws s3api list-parts \
  --bucket bucket-name \
  --key store_dir/150GB.data \
  --upload-id <upload-id>
```

## Sync directories and batch operations

Upload entire directories with change detection:

``` bash
aws s3 sync ./local/directory/ s3://bucket-name/remote/
```

Sync compares local file modification times with S3 object metadata and uploads only changed files.

Common sync options:

- **–delete:** Remove S3 objects not present in local directory (dangerous—test first)
- \**–exclude “*.tmp”:\*\* Skip files matching the pattern
- \**–include “*.log”:\*\* Upload only matching files (when combined with –exclude)
- **–no-progress:** Suppress per-file progress output
- **–storage-class GLACIER:** Use Glacier for cheaper long-term storage

Always use `--dryrun` before `--delete`:

``` bash
aws s3 sync ./local/directory/ s3://bucket-name/remote/ --delete --dryrun
```

## Handle interrupted uploads

Incomplete multipart uploads remain in S3 and incur storage charges. List them:

``` bash
aws s3api list-multipart-uploads --bucket bucket-name
```

Abort a specific upload:

``` bash
aws s3api abort-multipart-upload \
  --bucket bucket-name \
  --key store_dir/150GB.data \
  --upload-id <upload-id>
```

Prevent accidental charges by configuring a bucket lifecycle policy to delete incomplete uploads older than 7 days:

``` bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket bucket-name \
  --lifecycle-configuration '{
    "Rules": [{
      "Id": "AbortIncompleteUploads",
      "Status": "Enabled",
      "AbortIncompleteMultipartUpload": {
        "DaysAfterInitiation": 7
      }
    }]
  }'
```

Alternatively, retry the upload command; AWS CLI will resume from the last successful part if the connection dropped.

## Encryption and security

Always enable encryption for sensitive data. S3-managed encryption (AES256) is free and transparent:

``` bash
aws s3api put-bucket-encryption \
  --bucket bucket-name \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'
```

For compliance requirements, use customer-managed KMS keys:

``` bash
aws s3 cp ./150GB.data s3://bucket-name/store_dir/ \
  --sse aws:kms \
  --sse-kms-key-id arn:aws:kms:region:account:key/key-id
```

Block public access at the bucket level:

``` bash
aws s3api put-public-access-block \
  --bucket bucket-name \
  --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
```

## Common upload options

- **–storage-class GLACIER:** Archive to cheaper long-term storage (retrieval has delay)
- **–storage-class INTELLIGENT_TIERING:** Automatic cost optimization based on access patterns
- **–sse AES256:** Enable server-side encryption with S3-managed keys
- **–acl private:** Set object permissions (avoid `--acl public-read` in production)
- **–metadata key=value:** Add custom metadata for tracking and automation
- **–region:** Specify AWS region explicitly (overrides default config)
- **–expected-size:** Hint to AWS CLI the file size for better progress estimation

## Monitoring and cost management

Monitor CloudWatch metrics for PutObject requests and data transfer costs. Enable access logging to audit S3 operations:

``` bash
aws s3api put-bucket-logging \
  --bucket bucket-name \
  --bucket-logging-status '{
    "LoggingEnabled": {
      "TargetBucket": "log-bucket",
      "TargetPrefix": "logs/"
    }
  }'
```

For production workflows handling large volumes, test your configuration with smaller files first. Consider S3 Transfer Acceleration if standard multipart uploads don’t meet latency requirements, but measure the performance gain against additional costs.
