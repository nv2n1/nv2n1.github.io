---
title: "euscale-terminate-instance-in-auto-scaling-group(1)"
name: "euscale-terminate-instance-in-auto-scaling-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-terminate-instance-in-auto-scaling-group/"
description: "euscale-terminate-instance-in-auto-scaling-group – Manually terminate an auto-scaling instance"
---

<h2>NAME</h2>
<p> euscale-terminate-instance-in-auto-scaling-group &#8211; Manually terminate an auto-scaling instance</p>
<h2>SYNOPSIS</h2>
<p> euscale-terminate-instance-in-auto-scaling-group (<code>-d</code> | <code>-D</code>)</p>
<dl>
<dt>[&#8211;show-long]</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Manually terminate an auto-scaling instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> ID of the instance to terminate (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;decrement-desired-capacity</code></dt>
<dd> also reduce the desired capacity of the auto-scaling group by 1</dd>
<dt><code>-D</code>, <code>&#8211;no-decrement-desired-capacity</code></dt>
<dd> leave the auto-scaling group&#8217;s desired capacity as-is. A new instance may be launched to compensate for the one being terminated.</dd>
<dt><code>&#8211;show-long</code></dt>
<dd> show extra info about the instance being terminated</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
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
