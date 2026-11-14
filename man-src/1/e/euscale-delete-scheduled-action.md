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
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ACTION</dl>
<h2>DESCRIPTION</h2>
<p> Delete a scheduled action</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTION</p>
<dd> name of the scheduled action to delete (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</p>
<dd> name of the auto-scaling group the scheduled action is associated with (required)</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> auto-scaling service endpoint URL</p>
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
