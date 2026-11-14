---
title: "euca-copy-image(1)"
name: "euca-copy-image"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-copy-image/"
description: "euca-copy-image – Copy an image from another region"
---

<h2>NAME</h2>
<p> euca-copy-image &#8211; Copy an image from another region</p>
<h2>SYNOPSIS</h2>
<p> euca-copy-image <code>-r</code> REGION <code>-s</code> IMAGE [-n NAME] [-d DESC] [-c TOKEN]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Copy an image from another region</p>
<h2>DESCRIPTION</h2>
<p> Run this command against the destination region, not the source region.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code> REGION, <code>&#8211;source-region</code> REGION</p>
<dd> name of the region to copy the image from (required)</p>
<dt><code>-s</code> IMAGE, <code>&#8211;source-ami-id</code> IMAGE</p>
<dd> ID of the image to copy (required)</p>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</p>
<dd> name to assign the new copy of the image</p>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</p>
<dd> description to assign the new copy of the image</p>
<dt><code>-c</code> TOKEN, <code>&#8211;client-token</code> TOKEN</p>
<dd> unique identifier to ensure request idempotency</p>
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
