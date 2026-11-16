---
title: "euca-reset-image-attribute(1)"
name: "euca-reset-image-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-reset-image-attribute/"
description: "euca-reset-image-attribute – Reset an attribute of an image to its default value"
---

<h2>NAME</h2>
<p> euca-reset-image-attribute &#8211; Reset an attribute of an image to its default value</p>
<h2>SYNOPSIS</h2>
<p> euca-reset-image-attribute <code>-l</code> [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IMAGE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Reset an attribute of an image to its default value</p>
<h3>positional arguments:</h3>
<dl>
<dt>IMAGE</dt>
<dd> ID of the image whose attribute should be reset (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;launch-permission</code></dt>
<dd> reset launch permissions</dd>
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
