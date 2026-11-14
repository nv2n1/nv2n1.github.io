---
title: "euscale-create-launch-config(1)"
name: "euscale-create-launch-config"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-create-launch-config/"
description: "euscale-create-launch-config – Create a new auto-scaling instance launch configuration"
---

<h2>NAME</h2>
<p> euscale-create-launch-config &#8211; Create a new auto-scaling instance launch configuration</p>
<h2>SYNOPSIS</h2>
<p> euscale-create-launch-config <code>-i</code> IMAGE <code>-t</code> TYPE</p>
<dl>
<dt>[&#8211;associate-public-ip-address {true,false}]</p>
<dd> [&#8211;block-device-mapping DEVICE1=MAPPED1,DEVICE2=MAPPED2,&#8230;] [&#8211;ebs-optimized] [&#8211;group GROUP1,GROUP2,&#8230;] [&#8211;iam-instance-profile PROFILE] [&#8211;kernel KERNEL] [&#8211;key KEYPAIR] [&#8211;monitoring-enabled] [&#8211;monitoring-disabled] [&#8211;ramdisk RAMDISK] [&#8211;spot-price PRICE] [-d DATA | <code>&#8211;user-data-force</code> DATA | <code>-f</code> FILE] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] LAUNCHCONFIG</dl>
<h2>DESCRIPTION</h2>
<p> Create a new auto-scaling instance launch configuration</p>
<h3>positional arguments:</h3>
<dl>
<dt>LAUNCHCONFIG</p>
<dd> name of the new launch configuration (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> IMAGE, <code>&#8211;image-id</code> IMAGE</p>
<dd> machine image to use for instances (required)</p>
<dt><code>-t</code> TYPE, <code>&#8211;instance-type</code> TYPE</p>
<dd> instance type for use for instances (required)</p>
<dt><code>&#8211;associate-public-ip-address</code> {true,false}</p>
<dd> [VPC only] whether to assign instances public IP addresses</p>
<dt><code>&#8211;block-device-mapping</code> DEVICE1=MAPPED1,DEVICE2=MAPPED2,&#8230;</p>
<dd> a comma-separated list of block device mappings for the image, in the form DEVICE=MAPPED, where &quot;MAPPED&quot; is &quot;none&quot;, &quot;ephemeral(0-3)&quot;, or &quot;[SNAPID]:[GiB]:[true|false]</p>
<dt><code>&#8211;ebs-optimized</code></p>
<dd> whether the instance is optimized for EBS I/O</p>
<dt><code>&#8211;group</code> GROUP1,GROUP2,&#8230;</p>
<dd> a comma-separated list of security groups with which to associate instances. Either all group names or all group IDs are allowed, but not both.</p>
<dt><code>&#8211;iam-instance-profile</code> PROFILE</p>
<dd> ARN of the instance profile associated with instances&#8217; IAM roles</p>
<dt><code>&#8211;kernel</code> KERNEL</p>
<dd> kernel image to use for instances</p>
<dt><code>&#8211;key</code> KEYPAIR</p>
<dd> name of the key pair to use for instances</p>
<dt><code>&#8211;monitoring-enabled</code></p>
<dd> enable detailed monitoring (enabled by default)</p>
<dt><code>&#8211;monitoring-disabled</code></p>
<dd> disable detailed monitoring (enabled by default)</p>
<dt><code>&#8211;ramdisk</code> RAMDISK</p>
<dd> ramdisk image to use for instances</p>
<dt><code>&#8211;spot-price</code> PRICE</p>
<dd> maximum hourly price for any spot instances launched</p>
<dt><code>-d</code> DATA, <code>&#8211;user-data</code> DATA</p>
<dd> user data to make available to instances</p>
<dt><code>&#8211;user-data-force</code> DATA</p>
<dd> same as <code>-d</code>/&#8211;user-data, but without checking if a file by that name exists first</p>
<dt><code>-f</code> FILE, <code>&#8211;user-data-file</code> FILE</p>
<dd> file containing user data to make available to instances</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> auto-scaling service endpoint URL</p>
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
