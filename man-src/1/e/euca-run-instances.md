---
title: "euca-run-instances(1)"
name: "euca-run-instances"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-run-instances/"
description: "euca-run-instances – Launch instances of a machine image"
---

<h2>NAME</h2>
<p> euca-run-instances &#8211; Launch instances of a machine image</p>
<h2>SYNOPSIS</h2>
<p> euca-run-instances [-n MIN[-MAX]] [-g GROUP] [-k KEYPAIR]</p>
<dl>
<dt>[-d DATA | <code>&#8211;user-data-force</code> DATA | <code>-f</code> FILE]</p>
<dd> [&#8211;addressing {public,private}] [-t INSTANCETYPE] [-z ZONE] [&#8211;kernel KERNEL] [&#8211;ramdisk RAMDISK] [-b DEVICE=MAPPED] [-m] [&#8211;disable-api-termination] [&#8211;instance-initiated-shutdown-behavior {stop,terminate}] [&#8211;placement-group PLGROUP] [&#8211;tenancy {default,dedicated}] [&#8211;client-token TOKEN] [-s SUBNET] [&#8211;associate-public-ip-address ASSOCIATE_PUBLIC_IP_ADDRESS] [&#8211;private-ip-address ADDRESS] [&#8211;secondary-address ADDRESS | <code>&#8211;secondary-count</code> COUNT] [-a INTERFACE] [-p IPROFILE] [&#8211;ebs-optimized] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IMAGE</dl>
<h2>DESCRIPTION</h2>
<p> Launch instances of a machine image</p>
<h3>positional arguments:</h3>
<dl>
<dt>IMAGE</p>
<dd> ID of the image to instantiate (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> MIN[-MAX], <code>&#8211;instance-count</code> MIN[-MAX]</p>
<dd> number of instances to launch. If this number of instances cannot be launched, no instances will launch. If specified as a range (min-max), the server will attempt to launch the maximum number, but no fewer than the minimum number.</p>
<dt><code>-g</code> GROUP, <code>&#8211;group</code> GROUP</p>
<dd> security group(s) in which to launch the instances</p>
<dt><code>-k</code> KEYPAIR, <code>&#8211;key</code> KEYPAIR</p>
<dd> name of the key pair to use</p>
<dt><code>-d</code> DATA, <code>&#8211;user-data</code> DATA</p>
<dd> user data to make available to instances in this reservation</p>
<dt><code>&#8211;user-data-force</code> DATA</p>
<dd> same as <code>-d</code>/&#8211;user-data, but without checking if a file by that name exists first</p>
<dt><code>-f</code> FILE, <code>&#8211;user-data-file</code> FILE</p>
<dd> file containing user data to make available to the instances in this reservation</p>
<dt><code>&#8211;addressing</code> {public,private}</p>
<dd> [Eucalyptus only, non-VPC only] addressing scheme to launch the instance with. Use &quot;private&quot; to run an instance with no public address.</p>
<dt><code>-t</code> INSTANCETYPE, <code>&#8211;instance-type</code> INSTANCETYPE</p>
<dd> type of instance to launch</p>
<dt> <code>-z</code> ZONE, <code>&#8211;availability-zone</code> ZONE</p>
<dt><code>&#8211;kernel</code> KERNEL</p>
<dd>
<dd>ID of the kernel to launch the instance(s) with</p>
<dt><code>&#8211;ramdisk</code> RAMDISK</p>
<dd> ID of the ramdisk to launch the instance(s) with</p>
<dt><code>-b</code> DEVICE=MAPPED, <code>&#8211;block-device-mapping</code> DEVICE=MAPPED</p>
<dd> define a block device mapping for the instances, in the form DEVICE=MAPPED, where &quot;MAPPED&quot; is &quot;none&quot;, &quot;ephemeral(0-3)&quot;, or &quot;[SNAPID]:[GiB]:[true|false]:[standard|VOLTYPE[:IOPS]]&quot;</p>
<dt><code>-m</code>, <code>&#8211;monitor</code></p>
<dd> enable detailed monitoring for the instance(s)</p>
<dt><code>&#8211;disable-api-termination</code></p>
<dd> prevent API users from terminating the instance(s)</p>
<dt><code>&#8211;instance-initiated-shutdown-behavior</code> {stop,terminate}</p>
<dd> whether to &quot;stop&quot; (default) or terminate EBS instances when they shut down</p>
<dt><code>&#8211;placement-group</code> PLGROUP</p>
<dd> name of a placement group to launch into</p>
<dt><code>&#8211;tenancy</code> {default,dedicated}</p>
<dd> [VPC only] &quot;dedicated&quot; to run on single-tenant hardware</p>
<dt><code>&#8211;client-token</code> TOKEN</p>
<dd> unique identifier to ensure request idempotency</p>
<dt><code>-s</code> SUBNET, <code>&#8211;subnet</code> SUBNET</p>
<dd> [VPC only] subnet to create the instance&#8217;s network interface in</p>
<dt><code>&#8211;associate-public-ip-address</code> ASSOCIATE_PUBLIC_IP_ADDRESS</p>
<dd> [VPC only] whether or not to assign a public address to the instance&#8217;s network interface</p>
<dt><code>&#8211;private-ip-address</code> ADDRESS</p>
<dd> [VPC only] assign a specific primary private IP address to an instance&#8217;s interface</p>
<dt><code>&#8211;secondary-address</code> ADDRESS, <code>&#8211;secondary-private-ip-address</code> ADDRESS</p>
<dd> [VPC only] assign a specific secondary private IP address to an instance&#8217;s network interface. Use this option multiple times to add additional addresses.</p>
<dt><code>&#8211;secondary-count</code> COUNT, <code>&#8211;secondary-private-ip-address-count</code> COUNT</p>
<dd> [VPC only] automatically assign a specific number of secondary private IP addresses to an instance&#8217;s network interface</p>
<dt><code>-a</code> INTERFACE, <code>&#8211;network-interface</code> INTERFACE</p>
<dd> [VPC only] add a network interface to the new instance. If the interface already exists, supply its ID and a numeric index for it, separated by &quot;:&quot;, in the form &quot;eni-NNNNNNNN:INDEX&quot;. To create a new interface, supply a numeric index and subnet ID for it, along with (in order) an optional description, a primary private IP address, a list of security group IDs to associate with the interface, whether to delete the interface upon instance termination (&quot;true&quot; or &quot;false&quot;), a number of secondary private IP addresses to create automatically, and a list of secondary private IP addresses to assign to the interface, separated by &quot;:&quot;, in the form &quot;:INDEX:SUBNET:[DESCRIPT ION]:[PRIV_IP]:[GROUP1,GROUP2,&#8230;]:[true|false]:[SEC_I P_COUNT|:SEC_IP1,SEC_IP2,&#8230;]&quot;. You cannot specify both of the latter two. This option may be used multiple times. Each adds another network interface.</p>
<dt><code>-p</code> IPROFILE, <code>&#8211;iam-profile</code> IPROFILE</p>
<dd> name or ARN of the IAM instance profile to associate with the new instance(s)</p>
<dt><code>&#8211;ebs-optimized</code></p>
<dd> optimize the new instance(s) for EBS I/O</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;debug</code></p>
<dd>
<dd>show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
