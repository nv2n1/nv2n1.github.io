---
title: "euca-describe-nat-gateways(1)"
name: "euca-describe-nat-gateways"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-nat-gateways/"
description: "euca-describe-nat-gateways – Describe one or more VPC NAT gateways"
---

<h2>NAME</h2>
<p> euca-describe-nat-gateways &#8211; Describe one or more VPC NAT gateways</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-nat-gateways [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [NGATEWAY [NGATEWAY &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> Describe one or more VPC NAT gateways</p>
<h3>positional arguments:</h3>
<dl>
<dt>NGATEWAY</p>
<dd> limit results to one or more NAT gateways</dl>
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
<dt><code>&#8211;filter</code> NAME=VALUE</p>
<dd>
<dd>restrict results to those that meet criteria</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</dl>
<h3>allowed filter names:</h3>
<p> nat-gateway-id state the state of the NAT gateway subnet-id the ID of the subnet in which the NAT gateway resides</p>
<dl>
<dt>vpc-id</p>
<dd> the ID of the VPC in which the NAT gateway resides</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination </p>
</dl>
<h2>Index</h2>
