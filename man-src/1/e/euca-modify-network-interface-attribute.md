---
title: "euca-modify-network-interface-attribute(1)"
name: "euca-modify-network-interface-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-modify-network-interface-attribute/"
description: "euca-modify-network-interface-attribute – Modify an attribute of a VPC network interface"
---

<h2>NAME</h2>
<p> euca-modify-network-interface-attribute &#8211; Modify an attribute of a VPC network interface</p>
<h2>SYNOPSIS</h2>
<p> euca-modify-network-interface-attribute</p>
<dl>
<dt>(<code>-d</code> DESC | <code>&#8211;source-dest-check</code> (true|false)</p>
<dd> | <code>&#8211;group-id</code> GROUP | <code>-a</code> ATTACHMENT) [&#8211;delete-on-termination (true|false)] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INTERFACE</dl>
<h2>DESCRIPTION</h2>
<p> Modify an attribute of a VPC network interface</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</p>
<dd> ID of the network interface to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</p>
<dd> set the interface&#8217;s description</p>
<dt><code>&#8211;source-dest-check</code> (true|false)</p>
<dd> set whether source/destination checking is enabled</p>
<dt><code>&#8211;group-id</code> GROUP</p>
<dd> set the security groups the network interface belongs to (use more than one to specify multiple groups)</p>
<dt><code>-a</code> ATTACHMENT, <code>&#8211;attachment</code> ATTACHMENT</p>
<dd> the ID of an attachment to modify. <code>&#8211;delete-ontermination</code> is required when this option is used.</p>
<dt><code>&#8211;delete-on-termination</code> (true|false)</p>
<dd> set whether the interface&#8217;s attachment will be deleted when the instance terminates (requires <code>-a</code>/&#8211;attachment)</p>
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
