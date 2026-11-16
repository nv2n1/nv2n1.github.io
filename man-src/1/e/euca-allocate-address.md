---
title: "euca-allocate-address(1)"
name: "euca-allocate-address"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-allocate-address/"
description: "euca-allocate-address – Allocate a public IP address"
---

<h2>NAME</h2>
<p> euca-allocate-address &#8211; Allocate a public IP address</p>
<h2>SYNOPSIS</h2>
<p> euca-allocate-address [-d vpc] [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Allocate a public IP address</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> vpc, <code>&#8211;domain</code> vpc</dt>
<dd> [VPC only] &quot;vpc&quot; to allocate the address for use in a VPC</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
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
