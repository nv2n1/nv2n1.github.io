---

title: "euca-describe-instance-attribute(1)"
name: "euca-describe-instance-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-instance-attribute/"
description: "euca-describe-instance-attribute – Show one of an instance’s attributes."
---

<p> euca-describe-instance-attribute &#8211; Show one of an instance&#8217;s attributes.</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-instance-attribute</p>
<dl>
<dt>(<code>-b</code> | <code>&#8211;disable-api-termination</code> | <code>&#8211;ebs-optimized</code> | <code>-g</code> | <code>-p</code> | <code>&#8211;instance-initiated-shutdown-behavior</code> | <code>-t</code> | <code>&#8211;kernel</code> | <code>&#8211;ramdisk</code> | <code>&#8211;root-device-name</code> | <code>&#8211;source-dest-check</code> | <code>&#8211;user-data</code>)</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show one of an instance&#8217;s attributes.</p>
<h2>DESCRIPTION</h2>
<p> Note that exactly one attribute may be shown at a time.</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> ID of the instance to show info for (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;block-device-mapping</code></dt>
<dd> show block device mappings</dd>
<dt><code>&#8211;disable-api-termination</code></dt>
<dd> show whether termination is disabled</dd>
<dt><code>&#8211;ebs-optimized</code></dt>
<dd> show whether the root volume is optimized for EBS I/O</dd>
<dt><code>-g</code>, <code>&#8211;group-id</code></dt>
<dd> show the security groups the instance belongs to</dd>
<dt><code>-p</code>, <code>&#8211;product-code</code></dt>
<dd> show any associated product codes</dd>
<dt><code>&#8211;instance-initiated-shutdown-behavior</code></dt>
<dd> show whether the instance stops or terminates when shut down</dd>
<dt><code>-t</code>, <code>&#8211;instance-type</code></dt>
<dd> show the instance&#8217;s type</dd>
<dt><code>&#8211;kernel</code></dt>
<dd> show the ID of the kernel image associated with the instance</dd>
<dt><code>&#8211;ramdisk</code></dt>
<dd> show the ID of the ramdisk image associated with the instance</dd>
<dt><code>&#8211;root-device-name</code></dt>
<dd> show the name of the instance&#8217;s root device (e.g. &#8216;/dev/sda1&#8217;)</dd>
<dt><code>&#8211;source-dest-check</code></dt>
<dd> [VPC only] show whether source/destination checking is enabled for the instance</dd>
<dt><code>&#8211;user-data</code></dt>
<dd> show the instance&#8217;s user-data</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
