---
title: "euca-describe-image-attribute(1)"
name: "euca-describe-image-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-image-attribute/"
description: "euca-describe-image-attribute – Show information about an attribute of an image"
---

<h2>NAME</h2>
<p> euca-describe-image-attribute &#8211; Show information about an attribute of an image</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-image-attribute</p>
<dl>
<dt>(<code>-l</code> | <code>-p</code> | <code>-B</code> | <code>&#8211;kernel</code> | <code>&#8211;ramdisk</code> | <code>&#8211;description</code>)</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IMAGE</dl>
<h2>DESCRIPTION</h2>
<p> Show information about an attribute of an image</p>
<h3>positional arguments:</h3>
<dl>
<dt>IMAGE</p>
<dd> image to describe</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;launch-permission</code></p>
<dd> display launch permissions</p>
<dt><code>-p</code>, <code>&#8211;product-codes</code></p>
<dd> list associated product codes</p>
<dt><code>-B</code>, <code>&#8211;block-device-mapping</code></p>
<dd> describe block device mappings</p>
<dt><code>&#8211;kernel</code></p>
<dd> show associated kernel image ID</p>
<dt><code>&#8211;ramdisk</code></p>
<dd> show associated ramdisk image ID</p>
<dt><code>&#8211;description</code></p>
<dd> show the image&#8217;s description</p>
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
