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
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] PEERCON</dd></dl>
<h2>DESCRIPTION</h2>
<p> Reject a request for a VPC peering connection</p>
<h2>DESCRIPTION</h2>
<p> To delete an active VPC peering connection or a peering connection request you created, use <a href="/docs/linux/man/1-euca-delete-vpc-peering-connection/">euca-delete-vpc-peering-connection</a>(1).</p>
<h3>positional arguments:</h3>
<dl>
<dt>PEERCON</dt>
<dd> the VPC peering connection to reject (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
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
