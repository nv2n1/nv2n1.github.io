---
title: "euca-reject-vpc-peering-connection(1)"
name: "euca-reject-vpc-peering-connection"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-reject-vpc-peering-connection/"
description: "euca-reject-vpc-peering-connection – Reject a request for a VPC peering connection"
---

<h2>NAME</h2>
<p> euca-reject-vpc-peering-connection &#8211; Reject a request for a VPC peering connection</p>
<h2>SYNOPSIS</h2>
<p> euca-reject-vpc-peering-connection [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] PEERCON</dl>
<h2>DESCRIPTION</h2>
<p> Reject a request for a VPC peering connection</p>
<h2>DESCRIPTION</h2>
<p> To delete an active VPC peering connection or a peering connection request you created, use <a href="/docs/linux/man/1-euca-delete-vpc-peering-connection/">euca-delete-vpc-peering-connection</a>(1).</p>
<h3>positional arguments:</h3>
<dl>
<dt>PEERCON</p>
<dd> the VPC peering connection to reject (required)</dl>
<h3>optional arguments:</h3>
<dl>
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
