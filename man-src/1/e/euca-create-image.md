---
title: "euca-create-image(1)"
name: "euca-create-image"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-image/"
description: "euca-create-image – Create an EBS image from a running or stopped EBS instance"
---

<h2>NAME</h2>
<p> euca-create-image &#8211; Create an EBS image from a running or stopped EBS instance</p>
<h2>SYNOPSIS</h2>
<p> euca-create-image <code>-n</code> NAME [-d DESC] [&#8211;no-reboot] [-b DEVICE=MAPPED]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Create an EBS image from a running or stopped EBS instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> instance from which to create the image (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</p>
<dd> name for the new image (required)</p>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</p>
<dd> description for the new image</p>
<dt><code>&#8211;no-reboot</code></p>
<dd> do not shut down the instance before creating the image. Image integrity may be affected.</p>
<dt><code>-b</code> DEVICE=MAPPED, <code>&#8211;block-device-mapping</code> DEVICE=MAPPED</p>
<dd> define a block device mapping for the image, in the form DEVICE=MAPPED, where &quot;MAPPED&quot; is &quot;none&quot;, &quot;ephemeral(0-3)&quot;, or &quot;[SNAP_ID]:[GiB]:[true|false]:[st andard|VOLTYPE[:IOPS]]&quot;</p>
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
