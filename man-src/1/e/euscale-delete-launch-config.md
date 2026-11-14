---
title: "euscale-delete-launch-config(1)"
name: "euscale-delete-launch-config"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-delete-launch-config/"
description: "euscale-delete-launch-config – Delete an auto-scaling instance launch configuration"
---

<h2>NAME</h2>
<p> euscale-delete-launch-config &#8211; Delete an auto-scaling instance launch configuration</p>
<h2>SYNOPSIS</h2>
<p> euscale-delete-launch-config [-U URL] [&#8211;region USER [at] REGION]</p>
<dl>
<dt>[-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] LAUNCHCONFIG</dl>
<h2>DESCRIPTION</h2>
<p> Delete an auto-scaling instance launch configuration</p>
<h3>positional arguments:</h3>
<dl>
<dt>LAUNCHCONFIG</p>
<dd> name of the launch configuration to delete (required)</dl>
<h3>optional arguments:</h3>
<dl>
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
