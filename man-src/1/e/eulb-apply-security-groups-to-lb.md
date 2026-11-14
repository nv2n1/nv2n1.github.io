---
title: "eulb-apply-security-groups-to-lb(1)"
name: "eulb-apply-security-groups-to-lb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-apply-security-groups-to-lb/"
description: "eulb-apply-security-groups-to-lb – [VPC only] Associate one or more security groups with a load balancer. All previous associations with security groups will be replaced."
---

<h2>NAME</h2>
<p> eulb-apply-security-groups-to-lb &#8211; [VPC only] Associate one or more security groups with a load balancer. All previous associations with security groups will be replaced.</p>
<h2>SYNOPSIS</h2>
<p> eulb-apply-security-groups-to-lb <code>-g</code> GROUP1,GROUP2,&#8230;</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> [VPC only] Associate one or more security groups with a load balancer. All previous associations with security groups will be replaced.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> GROUP1,GROUP2,&#8230;, <code>&#8211;security-groups</code> GROUP1,GROUP2,&#8230;</p>
<dd> security groups to associate the load balancer with (required)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
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
