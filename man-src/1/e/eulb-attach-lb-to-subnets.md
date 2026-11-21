---
title: "eulb-attach-lb-to-subnets(1)"
name: "eulb-attach-lb-to-subnets"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-attach-lb-to-subnets/"
description: "eulb-attach-lb-to-subnets – [VPC only] Add a load balancer to one or more subnets"
---

<h2>NAME</h2>
<p> eulb-attach-lb-to-subnets &#8211; [VPC only] Add a load balancer to one or more subnets</p>
<h2>SYNOPSIS</h2>
<p> eulb-attach-lb-to-subnets <code>-s</code> SUBNET1,SUBNET2,&#8230; [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dd></dl>
<h2>DESCRIPTION</h2>
<p> [VPC only] Add a load balancer to one or more subnets</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> SUBNET1,SUBNET2,&#8230;, <code>&#8211;subnets</code> SUBNET1,SUBNET2,&#8230;</dt>
<dd> IDs of the subnets to add the load balancer to (required)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
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
