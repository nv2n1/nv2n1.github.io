---
title: "euca-create-group(1)"
name: "euca-create-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-group/"
description: "euca-create-group – Create a new security group"
---

<h2>NAME</h2>
<p> euca-create-group &#8211; Create a new security group</p>
<h2>SYNOPSIS</h2>
<p> euca-create-group <code>-d</code> DESC [-c VPC] [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] GROUP</dl>
<h2>DESCRIPTION</h2>
<p> Create a new security group</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</p>
<dd> name of the new group (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</p>
<dd> description of the new group (required)</p>
<dt><code>-c</code> VPC, <code>&#8211;vpc</code> VPC</p>
<dd> [VPC only] ID of the VPC to create the group in</p>
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
