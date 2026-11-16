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
<dt>[&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create an EBS image from a running or stopped EBS instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> instance from which to create the image (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</dt>
<dd> name for the new image (required)</dd>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</dt>
<dd> description for the new image</dd>
<dt><code>&#8211;no-reboot</code></dt>
<dd> do not shut down the instance before creating the image. Image integrity may be affected.</dd>
<dt><code>-b</code> DEVICE=MAPPED, <code>&#8211;block-device-mapping</code> DEVICE=MAPPED</dt>
<dd> define a block device mapping for the image, in the form DEVICE=MAPPED, where &quot;MAPPED&quot; is &quot;none&quot;, &quot;ephemeral(0-3)&quot;, or &quot;[SNAP_ID]:[GiB]:[true|false]:[st andard|VOLTYPE[:IOPS]]&quot;</dd>
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
<h2>Index</h2>
