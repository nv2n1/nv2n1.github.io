---
title: "euca-attach-internet-gateway(1)"
name: "euca-attach-internet-gateway"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-attach-internet-gateway/"
description: "euca-attach-internet-gateway – Attach an Internet gateway to a VPC"
---

<h2>NAME</h2>
<p> euca-attach-internet-gateway &#8211; Attach an Internet gateway to a VPC</p>
<h2>SYNOPSIS</h2>
<p> euca-attach-internet-gateway <code>-c</code> VPC [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IGATEWAY</dl>
<h2>DESCRIPTION</h2>
<p> Attach an Internet gateway to a VPC</p>
<h3>positional arguments:</h3>
<dl>
<dt>IGATEWAY</p>
<dd> Internet gateway to attach (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> VPC, <code>&#8211;vpc</code> VPC</p>
<dd> VPC to attach the Internet gateway to (required)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
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
