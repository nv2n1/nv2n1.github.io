---
title: "euscale-set-desired-capacity(1)"
name: "euscale-set-desired-capacity"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-set-desired-capacity/"
description: "euscale-set-desired-capacity – Set an auto-scaling group’s desired capacity"
---

<h2>NAME</h2>
<p> euscale-set-desired-capacity &#8211; Set an auto-scaling group&#8217;s desired capacity</p>
<h2>SYNOPSIS</h2>
<p> euscale-set-desired-capacity <code>-c</code> DESIREDCAPACITY [-h] [-H] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [&#8211;help] ASGROUP</dl>
<h2>DESCRIPTION</h2>
<p> Set an auto-scaling group&#8217;s desired capacity</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</p>
<dd> name of the auto-scaling group to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> DESIREDCAPACITY, <code>&#8211;desired-capacity</code> DESIREDCAPACITY</p>
<dd> new capacity setting for the group (required)</p>
<dt><code>-h</code>, <code>&#8211;honor-cooldown</code></p>
<dd> reject the request if the group is in cooldown (default: override any cooldown period)</p>
<dt><code>-H</code>, <code>&#8211;no-honor-cooldown</code></p>
<dd> override any cooldown period (this is the default)</p>
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
<dt><code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
