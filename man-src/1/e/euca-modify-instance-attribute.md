---
title: "euca-modify-instance-attribute(1)"
name: "euca-modify-instance-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-modify-instance-attribute/"
description: "euca-modify-instance-attribute – Modify an attribute of an instance"
---

<h2>NAME</h2>
<p> euca-modify-instance-attribute &#8211; Modify an attribute of an instance</p>
<h2>SYNOPSIS</h2>
<p> euca-modify-instance-attribute (<code>-b</code> DEVICE=::(true|false) |</p>
<dl>
<dt><code>&#8211;disable-api-termination</code> {true,false} |</p>
<dd> <code>&#8211;ebs-optimized</code> {true,false} | <code>-g</code> GROUP | <code>&#8211;instance-initiated-shutdown-behavior</code> {stop,terminate} | <code>-t</code> INSTANCETYPE | <code>&#8211;kernel</code> IMAGE | <code>&#8211;ramdisk</code> IMAGE | <code>&#8211;source-dest-check</code> {true,false} | <code>&#8211;sriov</code> simple | <code>&#8211;user-data</code> DATA | <code>&#8211;user-data-file</code> FILE) [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Modify an attribute of an instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> ID of the instance to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-b</code> DEVICE=::(true|false), <code>&#8211;block-device-mapping</code> DEVICE=::(true|false)</p>
<dd> change whether a volume attached to the instance will be deleted upon the instance&#8217;s termination</p>
<dt><code>&#8211;disable-api-termination</code> {true,false}</p>
<dd> change whether or not the instance may be terminated</p>
<dt><code>&#8211;ebs-optimized</code> {true,false}</p>
<dd> change whether or not the instance should be optimized for EBS I/O</p>
<dt><code>-g</code> GROUP, <code>&#8211;group-id</code> GROUP</p>
<dd> [VPC only] Change the security group(s) the instance is in</p>
<dt><code>&#8211;instance-initiated-shutdown-behavior</code> {stop,terminate}</p>
<dd> whether to stop or terminate the EBS instance when it shuts down (instance-store instances are always terminated)</p>
<dt><code>-t</code> INSTANCETYPE, <code>&#8211;instance-type</code> INSTANCETYPE</p>
<dd> change the instance&#8217;s type</p>
<dt><code>&#8211;kernel</code> IMAGE</p>
<dd> change the instance&#8217;s kernel image</p>
<dt><code>&#8211;ramdisk</code> IMAGE</p>
<dd> change the instance&#8217;s ramdisk image</p>
<dt><code>&#8211;source-dest-check</code> {true,false}</p>
<dd> change whether source/destination address checking is enabled</p>
<dt><code>&#8211;sriov</code> simple</p>
<dd> enable enhanced networking for the instance and its descendants</p>
<dt><code>&#8211;user-data</code> DATA</p>
<dd> change the instance&#8217;s user data (must be base64-encoded)</p>
<dt><code>&#8211;user-data-file</code> FILE</p>
<dd> change the instance&#8217;s user data to the contents of a file</p>
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
