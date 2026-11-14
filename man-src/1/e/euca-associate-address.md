---
title: "euca-associate-address(1)"
name: "euca-associate-address"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-associate-address/"
description: "euca-associate-address – Associate an elastic IP address with a running instance"
---

<h2>NAME</h2>
<p> euca-associate-address &#8211; Associate an elastic IP address with a running instance</p>
<h2>SYNOPSIS</h2>
<p> euca-associate-address [-a ALLOC] (<code>-i</code> INSTANCE | <code>-n</code> INTERFACE)</p>
<dl>
<dt>[-p ADDRESS]</p>
<dd> [&#8211;allow-reassociation | <code>&#8211;no-allow-reassociation]</code> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ADDRESS]</dl>
<h2>DESCRIPTION</h2>
<p> Associate an elastic IP address with a running instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>ADDRESS</p>
<dd> [Non-VPC only] IP address to associate (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-a</code> ALLOC, <code>&#8211;allocation-id</code> ALLOC</p>
<dd> [VPC only] VPC allocation ID (required)</p>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance-id</code> INSTANCE</p>
<dd> ID of the instance to associate the address with</p>
<dt><code>-n</code> INTERFACE, <code>&#8211;network-interface</code> INTERFACE</p>
<dd> [VPC only] network interface to associate the address with</p>
<dt><code>-p</code> ADDRESS, <code>&#8211;private-ip-address</code> ADDRESS</p>
<dd> [VPC only] the private address to associate with the address being associated in the VPC (default: primary private IP)</p>
<dt><code>&#8211;allow-reassociation</code></p>
<dd> [VPC only] allow the address to be associated even if it is already associated with another interface</p>
<dt><code>&#8211;no-allow-reassociation</code></p>
<dd> [VPC only] do not allow the address to be associated if it is already associated with another interface</p>
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
