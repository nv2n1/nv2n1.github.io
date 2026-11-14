---
title: "euca-delete-tags(1)"
name: "euca-delete-tags"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-delete-tags/"
description: "euca-delete-tags – Delete tags from one or more resources"
---

<h2>NAME</h2>
<p> euca-delete-tags &#8211; Delete tags from one or more resources</p>
<h2>SYNOPSIS</h2>
<p> euca-delete-tags <code>&#8211;tag</code> KEY[=[VALUE]] [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] RESOURCE [RESOURCE &#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> Delete tags from one or more resources</p>
<h3>positional arguments:</h3>
<dl>
<dt>RESOURCE</p>
<dd> ID(s) of the resource(s) to un-tag (at least 1 required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;tag</code> KEY[=[VALUE]]</p>
<dd> key and optional value of the tag to delete, separated by an &quot;=&quot; character. If you specify a value then the tag is deleted only if its value matches the one you specified. If you specify the empty string as the value (e.g. &quot;&#8211;tag foo=&quot;) then the tag is deleted only if its value is the empty string. If you do not specify a value (e.g. &quot;&#8211;tag foo&quot;) then the tag is deleted regardless of its value. (at least 1 required)</p>
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
