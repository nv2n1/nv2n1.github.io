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
<p> euca-attach-network-interface <code>-i</code> INSTANCE <code>-d</code> INT [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INTERFACE</dd></dl>
<p> Attach a VPC network interface to an instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</dt>
<dd> network interface to attach to the instance (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance</code> INSTANCE</dt>
<dd> instance to attach the network interface to (required)</dd>
<dt><code>-d</code> INT, <code>&#8211;device-index</code> INT</dt>
<dd> device index to attach the network interface with (required)</dd>
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
