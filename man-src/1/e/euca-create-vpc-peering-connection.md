---
title: "euca-create-vpc-peering-connection(1)"
name: "euca-create-vpc-peering-connection"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-vpc-peering-connection/"
description: "euca-create-vpc-peering-connection – Request a peering connection between two VPCs"
---

<h2>NAME</h2>
<p> euca-create-vpc-peering-connection &#8211; Request a peering connection between two VPCs</p>
<h2>SYNOPSIS</h2>
<p> euca-create-vpc-peering-connection <code>-c</code> VPC <code>-p</code> VPC [-o ACCOUNT]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Request a peering connection between two VPCs</p>
<h2>DESCRIPTION</h2>
<p> The owner of the VPC you wish to peer with must accept the peering request to activate the peering connection</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> VPC, <code>&#8211;vpc</code> VPC</p>
<dd> the VPC to request a peering connection from (required)</p>
<dt><code>-p</code> VPC, <code>&#8211;peer-vpc</code> VPC</p>
<dd> the VPC to request a peering connection to (required)</p>
<dt><code>-o</code> ACCOUNT, <code>&#8211;peer-owner-id</code> ACCOUNT</p>
<dd> account ID of the peer VPC&#8217;s owner (default: current user&#8217;s account ID)</p>
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
