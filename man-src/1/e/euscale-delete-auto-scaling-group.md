---

title: "euscale-delete-auto-scaling-group(1)"
name: "euscale-delete-auto-scaling-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-delete-auto-scaling-group/"
description: "euscale-delete-auto-scaling-group – Delete an auto-scaling group"
---

<p> euscale-delete-auto-scaling-group &#8211; Delete an auto-scaling group</p>
<h2>SYNOPSIS</h2>
<p> euscale-delete-auto-scaling-group [-d] [-U URL] [&#8211;region USER [at] REGION]</p>
<dl>
<dt>[-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dd></dl>
<h2>DESCRIPTION</h2>
<p> Delete an auto-scaling group</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</dt>
<dd> name of the auto-scaling group to delete (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;force-delete</code></dt>
<dd> delete the group and all of its instances without waiting for all instances to terminate</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> auto-scaling service endpoint URL</dd>
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
