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
<dt>[&#8211;show-long]</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Manually terminate an auto-scaling instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> ID of the instance to terminate (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;decrement-desired-capacity</code></p>
<dd> also reduce the desired capacity of the auto-scaling group by 1</p>
<dt><code>-D</code>, <code>&#8211;no-decrement-desired-capacity</code></p>
<dd> leave the auto-scaling group&#8217;s desired capacity as-is. A new instance may be launched to compensate for the one being terminated.</p>
<dt><code>&#8211;show-long</code></p>
<dd> show extra info about the instance being terminated</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
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
