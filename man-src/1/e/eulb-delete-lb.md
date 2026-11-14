---
title: "eulb-delete-lb(1)"
name: "eulb-delete-lb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-delete-lb/"
description: "eulb-delete-lb – Delete a load balancer"
---

<h2>NAME</h2>
<p> eulb-delete-lb &#8211; Delete a load balancer</p>
<h2>SYNOPSIS</h2>
<p> eulb-delete-lb [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dl>
<dt>[&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger]</p>
<dd> [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Delete a load balancer</p>
<h2>DESCRIPTION</h2>
<p> If the load balancer does not exist, this command still succeeds.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to delete (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> load balancing service endpoint URL</p>
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
