---
title: "eulb-modify-lb-attributes(1)"
name: "eulb-modify-lb-attributes"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-modify-lb-attributes/"
description: "eulb-modify-lb-attributes – Modify a load balancer’s attributes"
---

<h2>NAME</h2>
<p> eulb-modify-lb-attributes &#8211; Modify a load balancer&#8217;s attributes</p>
<h2>SYNOPSIS</h2>
<p> eulb-modify-lb-attributes [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dl>
<dt>[-S KEY] [&#8211;security-token TOKEN] [&#8211;debug]</dt>
<dd> [&#8211;debugger] [&#8211;version] [-h] ELB ATTR=VALUE [ATTR=VALUE &#8230;]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Modify a load balancer&#8217;s attributes</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> the load balancer to describe (required)</dd>
<dt>ATTR=VALUE</dt>
<dd> name and new value of each attribute to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> load balancing service endpoint URL</dd>
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
