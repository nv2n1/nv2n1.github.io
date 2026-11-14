---
title: "euca-assign-private-ip-addresses(1)"
name: "euca-assign-private-ip-addresses"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-assign-private-ip-addresses/"
description: "euca-assign-private-ip-addresses – Assign one or more private IP addresses to a network interface"
---

<h2>NAME</h2>
<p> euca-assign-private-ip-addresses &#8211; Assign one or more private IP addresses to a network interface</p>
<h2>SYNOPSIS</h2>
<p> euca-assign-private-ip-addresses [-n INTERFACE]</p>
<dl>
<dt>(<code>&#8211;secondary-address</code> ADDRESS | <code>&#8211;secondary-count</code> COUNT)</p>
<dd> [&#8211;allow-reassignment] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Assign one or more private IP addresses to a network interface</p>
<h2>DESCRIPTION</h2>
<p> Note that an instance&#8217;s type may affect the number of addresses it can hold at once.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> INTERFACE, <code>&#8211;network-interface</code> INTERFACE</p>
<dd> ID of the network interface to assign addresses to (required)</p>
<dt><code>&#8211;secondary-address</code> ADDRESS, <code>&#8211;secondary-private-ip-address</code> ADDRESS</p>
<dd> assign a specific secondary private IP address to the network interface. Use this option multiple times to add additional addresses.</p>
<dt><code>&#8211;secondary-count</code> COUNT, <code>&#8211;secondary-private-ip-address-count</code> COUNT</p>
<dd> automatically assign a specific number of secondary private IP addresses to the network interface</p>
<dt><code>&#8211;allow-reassignment</code></p>
<dd> Allow addresses to be assigned even if they are already associated with other interfaces</p>
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
