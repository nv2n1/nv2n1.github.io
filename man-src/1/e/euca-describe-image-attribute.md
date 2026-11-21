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
<dt>(<code>-l</code> | <code>-p</code> | <code>-B</code> | <code>&#8211;kernel</code> | <code>&#8211;ramdisk</code> | <code>&#8211;description</code>)</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IMAGE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about an attribute of an image</p>
<h3>positional arguments:</h3>
<dl>
<dt>IMAGE</dt>
<dd> image to describe</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;launch-permission</code></dt>
<dd> display launch permissions</dd>
<dt><code>-p</code>, <code>&#8211;product-codes</code></dt>
<dd> list associated product codes</dd>
<dt><code>-B</code>, <code>&#8211;block-device-mapping</code></dt>
<dd> describe block device mappings</dd>
<dt><code>&#8211;kernel</code></dt>
<dd> show associated kernel image ID</dd>
<dt><code>&#8211;ramdisk</code></dt>
<dd> show associated ramdisk image ID</dd>
<dt><code>&#8211;description</code></dt>
<dd> show the image&#8217;s description</dd>
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
