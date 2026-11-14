---
title: "euca-attach-network-interface(1)"
name: "euca-attach-network-interface"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-attach-network-interface/"
description: "euca-attach-network-interface – Attach a VPC network interface to an instance"
---

<h2>NAME</h2>
<p> euca-attach-network-interface &#8211; Attach a VPC network interface to an instance</p>
<h2>SYNOPSIS</h2>
<p> euca-attach-network-interface <code>-i</code> INSTANCE <code>-d</code> INT [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INTERFACE</dl>
<h2>DESCRIPTION</h2>
<p> Attach a VPC network interface to an instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</p>
<dd> network interface to attach to the instance (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance</code> INSTANCE</p>
<dd> instance to attach the network interface to (required)</p>
<dt><code>-d</code> INT, <code>&#8211;device-index</code> INT</p>
<dd> device index to attach the network interface with (required)</p>
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
