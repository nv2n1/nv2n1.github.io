---
title: "euca-delete-bundle(1)"
name: "euca-delete-bundle"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-delete-bundle/"
description: "euca-delete-bundle – Delete a previously-uploaded bundle"
---

<h2>NAME</h2>
<p> euca-delete-bundle &#8211; Delete a previously-uploaded bundle</p>
<h2>SYNOPSIS</h2>
<p> euca-delete-bundle [&#8211;clear] <code>-b</code> BUCKET[/PREFIX]</p>
<dl>
<dt>(<code>-m</code> MANIFEST | <code>-p</code> MANIFEST | <code>&#8211;local-manifest</code> FILE)</p>
<dd> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Delete a previously-uploaded bundle</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;clear</code></p>
<dd> attempt to delete the bucket as well</p>
<dt><code>-b</code> BUCKET[/PREFIX], <code>&#8211;bucket</code> BUCKET[/PREFIX]</p>
<dd> the bucket that contains the bundle, with an optional path prefix (required)</p>
<dt><code>-m</code> MANIFEST, <code>&#8211;manifest</code> MANIFEST</p>
<dd> the manifest&#8217;s complete file name, not including any path that may be specified using <code>-b</code></p>
<dt><code>-p</code> MANIFEST, <code>&#8211;prefix</code> MANIFEST</p>
<dd> the portion of the manifest&#8217;s file name that precedes &quot;.manifest.xml&quot;</p>
<dt><code>&#8211;local-manifest</code> FILE</p>
<dd> use a manifest on disk and ignore any that appear on the server</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> object storage service endpoint URL</p>
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
