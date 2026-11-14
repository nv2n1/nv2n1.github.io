---
title: "euca-reset-instance-attribute(1)"
name: "euca-reset-instance-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-reset-instance-attribute/"
description: "euca-reset-instance-attribute – Reset an attribute of an instance to its default value"
---

<h2>NAME</h2>
<p> euca-reset-instance-attribute &#8211; Reset an attribute of an instance to its default value</p>
<h2>SYNOPSIS</h2>
<p> euca-reset-instance-attribute</p>
<dl>
<dt>(<code>&#8211;kernel</code> | <code>&#8211;ramdisk</code> | <code>&#8211;source-dest-check</code>)</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Reset an attribute of an instance to its default value</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> ID of the instance to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;kernel</code></p>
<dd> reset the instance&#8217;s kernel image ID</p>
<dt><code>&#8211;ramdisk</code></p>
<dd> reset the instance&#8217;s ramdisk image ID</p>
<dt><code>&#8211;source-dest-check</code></p>
<dd> reset the instance&#8217;s SourceDestCheck to true</p>
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
