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
<dt>[&#8211;respect-grace-period]</dt>
<dd> [&#8211;no-respect-grace-period] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Manually set an auto-scaling instance&#8217;s health status</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> ID of the instance to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> {Healthy,Unhealthy}, <code>&#8211;status</code> {Healthy,Unhealthy}</dt>
<dd> new status (required)</dd>
<dt><code>&#8211;respect-grace-period</code></dt>
<dd> respect the associated auto-scaling group&#8217;s grace period (this is the default)</dd>
<dt><code>&#8211;no-respect-grace-period</code></dt>
<dd> ignore the associated auto-scaling group&#8217;s grace period (default: respect the group&#8217;s grace period)</dd>
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
