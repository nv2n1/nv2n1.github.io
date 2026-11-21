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
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] RESOURCE [RESOURCE &#8230;]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Delete tags from one or more resources</p>
<h3>positional arguments:</h3>
<dl>
<dt>RESOURCE</dt>
<dd> ID(s) of the resource(s) to un-tag (at least 1 required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;tag</code> KEY[=[VALUE]]</dt>
<dd> key and optional value of the tag to delete, separated by an &quot;=&quot; character. If you specify a value then the tag is deleted only if its value matches the one you specified. If you specify the empty string as the value (e.g. &quot;&#8211;tag foo=&quot;) then the tag is deleted only if its value is the empty string. If you do not specify a value (e.g. &quot;&#8211;tag foo&quot;) then the tag is deleted regardless of its value. (at least 1 required)</dd>
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
