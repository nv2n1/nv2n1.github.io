---
title: "euca-unassign-private-ip-addresses(1)"
name: "euca-unassign-private-ip-addresses"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-unassign-private-ip-addresses/"
description: "euca-unassign-private-ip-addresses – Remove one or more private IP addresses from a network interface"
---

<h2>NAME</h2>
<p> euca-unassign-private-ip-addresses &#8211; Remove one or more private IP addresses from a network interface</p>
<h2>SYNOPSIS</h2>
<p> euca-unassign-private-ip-addresses [-n INTERFACE] <code>&#8211;secondary-address</code></p>
<dl>
<dt>ADDRESS [&#8211;show-empty-fields]</dt>
<dd> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Remove one or more private IP addresses from a network interface</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> INTERFACE, <code>&#8211;network-interface</code> INTERFACE</dt>
<dd> ID of the network interface to remove addresses from (required)</dd>
<dt><code>&#8211;secondary-address</code> ADDRESS, <code>&#8211;secondary-private-ip-address</code> ADDRESS</dt>
<dd> an IP address to remove from the network interface. Use this option multiple times to remove additional addresses.</dd>
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
