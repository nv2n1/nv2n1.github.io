---
title: "euca-describe-network-interface-attribute(1)"
name: "euca-describe-network-interface-attribute"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-network-interface-attribute/"
description: "euca-describe-network-interface-attribute – Show an attribute of a VPC network interface"
---

<h2>NAME</h2>
<p> euca-describe-network-interface-attribute &#8211; Show an attribute of a VPC network interface</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-network-interface-attribute</p>
<dl>
<dt>(<code>-d</code> | <code>&#8211;source-dest-check</code> | <code>&#8211;group-set</code> | <code>-a</code>)</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INTERFACE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show an attribute of a VPC network interface</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</dt>
<dd> ID of the network interface to show info for (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;description</code></dt>
<dd> show the interface&#8217;s description</dd>
<dt><code>&#8211;source-dest-check</code></dt>
<dd> show whether source/destination checking is enabled</dd>
<dt><code>&#8211;group-set</code></dt>
<dd> show the security groups the network interface belongs to</dd>
<dt><code>-a</code>, <code>&#8211;attachment</code></dt>
<dd> show info about the interface&#8217;s attachment (if any)</dd>
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
