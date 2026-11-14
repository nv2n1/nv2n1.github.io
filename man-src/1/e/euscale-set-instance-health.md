---
title: "euscale-set-instance-health(1)"
name: "euscale-set-instance-health"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-set-instance-health/"
description: "euscale-set-instance-health – Manually set an auto-scaling instance’s health status"
---

<h2>NAME</h2>
<p> euscale-set-instance-health &#8211; Manually set an auto-scaling instance&#8217;s health status</p>
<h2>SYNOPSIS</h2>
<p> euscale-set-instance-health <code>-s</code> {Healthy,Unhealthy}</p>
<dl>
<dt>[&#8211;respect-grace-period]</p>
<dd> [&#8211;no-respect-grace-period] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Manually set an auto-scaling instance&#8217;s health status</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> ID of the instance to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> {Healthy,Unhealthy}, <code>&#8211;status</code> {Healthy,Unhealthy}</p>
<dd> new status (required)</p>
<dt><code>&#8211;respect-grace-period</code></p>
<dd> respect the associated auto-scaling group&#8217;s grace period (this is the default)</p>
<dt><code>&#8211;no-respect-grace-period</code></p>
<dd> ignore the associated auto-scaling group&#8217;s grace period (default: respect the group&#8217;s grace period)</p>
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
