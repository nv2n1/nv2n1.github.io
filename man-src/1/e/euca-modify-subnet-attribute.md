---
title: "euca-modify-subnet-attribute(1)"
name: "euca-modify-subnet-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-modify-subnet-attribute/"
description: "euca-modify-subnet-attribute – Modify an attribute of a subnet"
---

<h2>NAME</h2>
<p> euca-modify-subnet-attribute &#8211; Modify an attribute of a subnet</p>
<h2>SYNOPSIS</h2>
<p> euca-modify-subnet-attribute <code>-m</code> (true|false) [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] SUBNET</dl>
<h2>DESCRIPTION</h2>
<p> Modify an attribute of a subnet</p>
<h3>positional arguments:</h3>
<dl>
<dt>SUBNET</p>
<dd> ID of the subnet to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-m</code> (true|false), <code>&#8211;map-public-ip-on-launch</code> (true|false)</p>
<dd> whether or not new instances in the subnet should be assigned public addresses</p>
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
