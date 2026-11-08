---
title: "EC2 Instance Control with IAM Tags: Allowing Developers to Start Only Dev Instances"
date: 2019-03-10 08:43:01 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-limit-shared-aws-ec2-accounts-access-to-view-and-start-all-vms-yet-stop-only-certain-vms/
---

Shared AWS accounts across multiple teams require careful access controls to prevent costly mistakes. A common requirement is allowing developers to view and start all instances, but restrict stopping to only non-production resources. IAM policies with resource tags give you fine-grained control over who can do what.

## The Problem

You have 50 production VMs and 25 development VMs under the same AWS account. Developers should be able to start any instance, but only stop the dev instances. This prevents accidental production outages while still giving necessary operational flexibility.

## IAM Architecture for This Use Case

AWS IAM uses a hierarchy to manage permissions:

- Users → User Groups → Policies → EC2 Actions on Tagged Resources

Users belong to groups, policies attach to groups, and policies use conditions to filter resources by tags. This approach scales better than managing individual user permissions and makes auditing access much easier.

## Creating the Policies

You’ll need two policies: one for listing and starting instances, and one for stopping only tagged dev instances. Create these via the AWS Console (IAM → Policies → Create Policy) or using the AWS CLI.

### Policy 1: ListAndStartInstances

This policy allows describing all EC2 resources and starting any instance:

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StartInstances",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:GetConsoleScreenshot"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*"
        },
        {
            "Sid": "ViewAllResources",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstanceAttribute",
                "ec2:DescribeInstanceCreditSpecifications",
                "ec2:DescribeTags",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeVolumes",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeImages",
                "ec2:DescribeAvailabilityZones"
            ],
            "Resource": "*"
        }
    ]
}
```

The first statement allows starting instances on any instance resource. The second statement grants read-only describe permissions on EC2 resources so users can see what they’re working with.

### Policy 2: StopDevInstances

This policy uses a condition to restrict stopping to instances tagged with `Environment: dev`:

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StopDevTaggedInstances",
            "Effect": "Allow",
            "Action": "ec2:StopInstances",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/Environment": "dev"
                }
            }
        }
    ]
}
```

The `Condition` block is critical here. It restricts the action to instances where the `Environment` tag equals `dev`. Make sure your dev instances are tagged correctly before applying this policy.

Create these policies via the CLI by saving them to JSON files and running:

``` bash
aws iam create-policy --policy-name ListAndStartInstances \
  --policy-document file://list-start-policy.json

aws iam create-policy --policy-name StopDevInstances \
  --policy-document file://stop-dev-policy.json
```

## Tagging Your Instances

Tag your instances before testing:

``` bash
aws ec2 create-tags --resources i-1234567890abcdef0 \
  --tags Key=Environment,Value=dev

aws ec2 create-tags --resources i-0987654321abcdef0 \
  --tags Key=Environment,Value=prod
```

Bulk-tag instances matching a filter:

``` bash
# Tag all instances with "dev" in their name
aws ec2 create-tags --resources $(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=*dev*" \
  --query 'Reservations[].Instances[].InstanceId' \
  --output text) \
  --tags Key=Environment,Value=dev
```

## Setting Up the User Group

Via the AWS Console:

1.  Navigate to IAM → User groups → Create group
2.  Enter group name: `developers`
3.  Click “Add permissions” → “Attach policies”
4.  Search for and select `ListAndStartInstances` and `StopDevInstances`
5.  Create the group

Via the CLI:

``` bash
aws iam create-group --group-name developers

aws iam attach-group-policy --group-name developers \
  --policy-arn arn:aws:iam::ACCOUNT-ID:policy/ListAndStartInstances

aws iam attach-group-policy --group-name developers \
  --policy-arn arn:aws:iam::ACCOUNT-ID:policy/StopDevInstances
```

## Adding Users to the Group

Create users if they don’t exist:

``` bash
aws iam create-user --user-name alice.smith
aws iam create-user --user-name bob.jones
```

Add them to the developers group:

``` bash
aws iam add-user-to-group --group-name developers --user-name alice.smith
aws iam add-user-to-group --group-name developers --user-name bob.jones
```

## Testing the Configuration

Have a user configure their AWS credentials and test these commands:

``` bash
# Should work — lists all instances
aws ec2 describe-instances

# Should work — starts any instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Should work — stops dev instance
aws ec2 stop-instances --instance-ids i-dev-instance

# Should fail with UnauthorizedOperation — stops prod instance
aws ec2 stop-instances --instance-ids i-prod-instance
```

If a user gets `UnauthorizedOperation` when stopping a production instance, the policy is working correctly.

## Important Considerations

**Tag consistency:** Tag every instance consistently. If an instance lacks the `Environment` tag, users with this policy won’t be able to stop it even if they should. Use AWS Config rules to enforce tagging at instance creation:

``` bash
aws configservice put-config-rule --config-rule file://tag-enforcement-rule.json
```

**Reboot vs Stop:** This policy doesn’t allow `ec2:RebootInstances`. If users need to reboot production instances, add a third policy:

``` json
{
    "Sid": "RebootAllInstances",
    "Effect": "Allow",
    "Action": "ec2:RebootInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*"
}
```

**Cross-region deployments:** The ARN `arn:aws:ec2:*:*:instance/*` applies to all regions. To restrict by region, use `arn:aws:ec2:us-east-1:ACCOUNT-ID:instance/*` instead.

**Cross-account access:** If using cross-account access, users assume roles via the CLI with `--role-arn`. The policies attach to the IAM role the same way, but the role’s trust relationship must allow the cross-account principal.

**Deny statements for extra safety:** Consider adding an explicit deny for production instance stops at the account or organization level to catch misconfigured policies:

``` json
{
    "Sid": "DenyStopProdInstances",
    "Effect": "Deny",
    "Action": "ec2:StopInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*",
    "Condition": {
        "StringEquals": {
            "ec2:ResourceTag/Environment": "prod"
        }
    }
}
```

**Audit access:** Enable CloudTrail to log all API calls. Monitor for stop attempts on prod instances:

``` bash
aws cloudtrail lookup-events --lookup-attributes \
  AttributeKey=EventName,AttributeValue=StopInstances \
  --query 'Events[?ErrorCode!=null]'
```

Set up CloudWatch alarms on failed `StopInstances` calls as a canary for misconfiguration or misuse.

## Extending This Pattern

You can apply the same tag-based approach to RDS databases, Lambda functions, and S3 buckets by changing the resource ARN and action names. For example, to restrict RDS database termination:

``` json
{
    "Sid": "StopDevRDSInstances",
    "Effect": "Allow",
    "Action": "rds:DeleteDBInstance",
    "Resource": "arn:aws:rds:*:ACCOUNT-ID:db/*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/Environment": "dev"
        }
    }
}
```

The same tagging strategy scales across your entire infrastructure. Use consistent tag keys and values across all resource types to simplify policy management and reduce the risk of configuration errors.
