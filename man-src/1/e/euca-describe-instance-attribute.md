---
title: "euca-describe-instance-attribute(1)"
name: "euca-describe-instance-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-instance-attribute/"
description: "euca-describe-instance-attribute – Show one of an instance’s attributes."
---

<h2>NAME</h2>
<p> euca-describe-instance-attribute &#8211; Show one of an instance&#8217;s attributes.</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-instance-attribute</p>
<dl>
<dt>(<code>-b</code> | <code>&#8211;disable-api-termination</code> | <code>&#8211;ebs-optimized</code> | <code>-g</code> | <code>-p</code> | <code>&#8211;instance-initiated-shutdown-behavior</code> | <code>-t</code> | <code>&#8211;kernel</code> | <code>&#8211;ramdisk</code> | <code>&#8211;root-device-name</code> | <code>&#8211;source-dest-check</code> | <code>&#8211;user-data</code>)</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Show one of an instance&#8217;s attributes.</p>
<h2>DESCRIPTION</h2>
<p> Note that exactly one attribute may be shown at a time.</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> ID of the instance to show info for (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;block-device-mapping</code></p>
<dd> show block device mappings</p>
<dt><code>&#8211;disable-api-termination</code></p>
<dd> show whether termination is disabled</p>
<dt><code>&#8211;ebs-optimized</code></p>
<dd> show whether the root volume is optimized for EBS I/O</p>
<dt><code>-g</code>, <code>&#8211;group-id</code></p>
<dd> show the security groups the instance belongs to</p>
<dt><code>-p</code>, <code>&#8211;product-code</code></p>
<dd> show any associated product codes</p>
<dt><code>&#8211;instance-initiated-shutdown-behavior</code></p>
<dd> show whether the instance stops or terminates when shut down</p>
<dt><code>-t</code>, <code>&#8211;instance-type</code></p>
<dd> show the instance&#8217;s type</p>
<dt><code>&#8211;kernel</code></p>
<dd> show the ID of the kernel image associated with the instance</p>
<dt><code>&#8211;ramdisk</code></p>
<dd> show the ID of the ramdisk image associated with the instance</p>
<dt><code>&#8211;root-device-name</code></p>
<dd> show the name of the instance&#8217;s root device (e.g. &#8216;/dev/sda1&#8217;)</p>
<dt><code>&#8211;source-dest-check</code></p>
<dd> [VPC only] show whether source/destination checking is enabled for the instance</p>
<dt><code>&#8211;user-data</code></p>
<dd> show the instance&#8217;s user-data</p>
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
