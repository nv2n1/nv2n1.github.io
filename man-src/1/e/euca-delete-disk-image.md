---
title: "euca-delete-disk-image(1)"
name: "euca-delete-disk-image"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-delete-disk-image/"
description: "euca-delete-disk-image – Delete a disk image used for an import task"
---

<h2>NAME</h2>
<p> euca-delete-disk-image &#8211; Delete a disk image used for an import task</p>
<h2>SYNOPSIS</h2>
<p> euca-delete-disk-image (<code>-t</code> TASK | <code>-u</code> MANIFEST_URL)</p>
<dl>
<dt>[&#8211;ignore-active-task] [&#8211;show-empty-fields]</p>
<dd> [&#8211;s3-url URL] [-o KEY_ID] [-w KEY] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Delete a disk image used for an import task</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> TASK, <code>&#8211;task</code> TASK</p>
<dd> ID of the task to delete the image from</p>
<dt><code>-u</code> MANIFEST_URL, <code>&#8211;manifest-url</code> MANIFEST_URL</p>
<dd> location of the import manifest</p>
<dt><code>&#8211;ignore-active-task</code></p>
<dd> delete the image even if the import task is active (only works with <code>-t</code>/&#8211;task)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>&#8211;s3-url</code> URL</p>
<dd> object storage service endpoint URL</p>
<dt><code>-o</code> KEY_ID, <code>&#8211;owner-akid</code> KEY_ID</p>
<dd> access key to use for the object storage service (default: same as that for the compute service)</p>
<dt><code>-w</code> KEY, <code>&#8211;owner-sak</code> KEY</p>
<dd> secret key to use for the object storage service (default: same as that for the compute service)</p>
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
