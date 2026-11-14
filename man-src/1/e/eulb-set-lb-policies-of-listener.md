---
title: "eulb-set-lb-policies-of-listener(1)"
name: "eulb-set-lb-policies-of-listener"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-set-lb-policies-of-listener/"
description: "eulb-set-lb-policies-of-listener – Change the policy associated with a load balancer listener"
---

<h2>NAME</h2>
<p> eulb-set-lb-policies-of-listener &#8211; Change the policy associated with a load balancer listener</p>
<h2>SYNOPSIS</h2>
<p> eulb-set-lb-policies-of-listener <code>-l</code> PORT <code>-p</code> POLICY1,POLICY2,&#8230;</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Change the policy associated with a load balancer listener</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code> PORT, <code>&#8211;lb-port</code> PORT</p>
<dd> port of the listener to modify (required)</p>
<dt><code>-p</code> POLICY1,POLICY2,&#8230;, <code>&#8211;policy-names</code> POLICY1,POLICY2,&#8230;</p>
<dd> list of policies to associate with the listener (required)</p>
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
