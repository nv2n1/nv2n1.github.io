---
title: "euscale-delete-scheduled-action(1)"
name: "euscale-delete-scheduled-action"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-delete-scheduled-action/"
description: "euscale-delete-scheduled-action – Delete a scheduled action"
---

<h2>NAME</h2>
<p> euscale-delete-scheduled-action &#8211; Delete a scheduled action</p>
<h2>SYNOPSIS</h2>
<p> euscale-delete-scheduled-action <code>-g</code> ASGROUP [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ACTION</dd></dl>
<h2>DESCRIPTION</h2>
<p> Delete a scheduled action</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTION</dt>
<dd> name of the scheduled action to delete (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</dt>
<dd> name of the auto-scaling group the scheduled action is associated with (required)</dd>
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
<h2>Index</h2>
