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
<dt>(<code>-d</code> DESC | <code>&#8211;source-dest-check</code> (true|false)</dt>
<dd> | <code>&#8211;group-id</code> GROUP | <code>-a</code> ATTACHMENT) [&#8211;delete-on-termination (true|false)] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INTERFACE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Modify an attribute of a VPC network interface</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</dt>
<dd> ID of the network interface to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</dt>
<dd> set the interface&#8217;s description</dd>
<dt><code>&#8211;source-dest-check</code> (true|false)</dt>
<dd> set whether source/destination checking is enabled</dd>
<dt><code>&#8211;group-id</code> GROUP</dt>
<dd> set the security groups the network interface belongs to (use more than one to specify multiple groups)</dd>
<dt><code>-a</code> ATTACHMENT, <code>&#8211;attachment</code> ATTACHMENT</dt>
<dd> the ID of an attachment to modify. <code>&#8211;delete-ontermination</code> is required when this option is used.</dd>
<dt><code>&#8211;delete-on-termination</code> (true|false)</dt>
<dd> set whether the interface&#8217;s attachment will be deleted when the instance terminates (requires <code>-a</code>/&#8211;attachment)</dd>
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
