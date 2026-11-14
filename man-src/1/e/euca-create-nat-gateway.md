---
title: "euca-create-nat-gateway(1)"
name: "euca-create-nat-gateway"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-nat-gateway/"
description: "euca-create-nat-gateway – Create a new VPC NAT gateway"
---

<h2>NAME</h2>
<p> euca-create-nat-gateway &#8211; Create a new VPC NAT gateway</p>
<h2>SYNOPSIS</h2>
<p> euca-create-nat-gateway <code>-s</code> SUBNET <code>-a</code> ALLOC [&#8211;client-token TOKEN]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Create a new VPC NAT gateway</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> SUBNET, <code>&#8211;subnet-id</code> SUBNET</p>
<dd> the subnet in which to create the new NAT gateway (required)</p>
<dt><code>-a</code> ALLOC, <code>&#8211;allocation-id</code> ALLOC</p>
<dd> the allocation ID of the Elastic IP address to associate with the NAT gateway (required)</p>
<dt><code>&#8211;client-token</code> TOKEN</p>
<dd> unique identifier to ensure request idempotency</p>
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
