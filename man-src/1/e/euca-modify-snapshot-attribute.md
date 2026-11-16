---
title: "euca-modify-snapshot-attribute(1)"
name: "euca-modify-snapshot-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-modify-snapshot-attribute/"
description: "euca-modify-snapshot-attribute – Modify an attribute of a snapshot"
---

<h2>NAME</h2>
<p> euca-modify-snapshot-attribute &#8211; Modify an attribute of a snapshot</p>
<h2>SYNOPSIS</h2>
<p> euca-modify-snapshot-attribute <code>-c</code> [-a ENTITY] [-r ENTITY]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] SNAPSHOT</dd></dl>
<h2>DESCRIPTION</h2>
<p> Modify an attribute of a snapshot</p>
<h3>positional arguments:</h3>
<dl>
<dt>SNAPSHOT</dt>
<dd> ID of the snapshot to modify</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;create-volume-permission</code></dt>
<dd> grant/revoke volume creation permission with <code>-a</code>/-r</dd>
<dt><code>-a</code> ENTITY, <code>&#8211;add</code> ENTITY</dt>
<dd> account to grant permission, or &quot;all&quot; for all accounts</dd>
<dt><code>-r</code> ENTITY, <code>&#8211;remove</code> ENTITY</dt>
<dd> account to remove permission from, or &quot;all&quot; for all accounts</dd>
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
