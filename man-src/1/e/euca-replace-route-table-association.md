---
title: "euca-replace-route-table-association(1)"
name: "euca-replace-route-table-association"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-replace-route-table-association/"
description: "euca-replace-route-table-association – Change the route table associated with a VPC subnet"
---

<h2>NAME</h2>
<p> euca-replace-route-table-association &#8211; Change the route table associated with a VPC subnet</p>
<h2>SYNOPSIS</h2>
<p> euca-replace-route-table-association <code>-r</code> RTABLE [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] RTBASSOC</dl>
<h2>DESCRIPTION</h2>
<p> Change the route table associated with a VPC subnet</p>
<h3>positional arguments:</h3>
<dl>
<dt>RTBASSOC</p>
<dd> ID of the route table association to replace (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code> RTABLE</p>
<dd> route table to associate with the subnet (required)</p>
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
