---
title: "euca-replace-route(1)"
name: "euca-replace-route"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-replace-route/"
description: "euca-replace-route – Replace a route in a VPC route table"
---

<h2>NAME</h2>
<p> euca-replace-route &#8211; Replace a route in a VPC route table</p>
<h2>SYNOPSIS</h2>
<p> euca-replace-route <code>-r</code> CIDR</p>
<dl>
<dt>(<code>-g</code> GATEWAY | <code>-i</code> INSTANCE | <code>-n</code> NETWORKINTERFACEID | <code>-p</code> PEERCON)</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] RTABLE</dl>
<h2>DESCRIPTION</h2>
<p> Replace a route in a VPC route table</p>
<h3>positional arguments:</h3>
<dl>
<dt>RTABLE</p>
<dd> ID of the route table to affect (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code> CIDR, <code>&#8211;cidr</code> CIDR</p>
<dd> destination prefix for route lookup</p>
<dt><code>-g</code> GATEWAY, <code>&#8211;gateway-id</code> GATEWAY</p>
<dd> ID of an Internet gateway to target</p>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance</code> INSTANCE</p>
<dd> ID of a NAT instance to target</p>
<dt><code>-n</code> NETWORKINTERFACEID, <code>&#8211;network-interface</code> NETWORKINTERFACEID</p>
<dd> ID of a network interface to target</p>
<dt><code>-p</code> PEERCON, <code>&#8211;vpc-peering-connection</code> PEERCON</p>
<dd> ID of a VPC peering connection to target</p>
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
