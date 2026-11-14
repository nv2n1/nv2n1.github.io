---
title: "euca-describe-vpn-gateways(1)"
name: "euca-describe-vpn-gateways"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-vpn-gateways/"
description: "euca-describe-vpn-gateways – Show information about virtual private gateways"
---

<h2>NAME</h2>
<p> euca-describe-vpn-gateways &#8211; Show information about virtual private gateways</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-vpn-gateways [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [VGATEWAY [VGATEWAY &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about virtual private gateways</p>
<h3>positional arguments:</h3>
<dl>
<dt>VGATEWAY</p>
<dd> limit results to specific virtual private gateways</dl>
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
<dl>
<dt>attachment.state</p>
<dd> state of attachment with a VPC</p>
<dt>attachment.vpc-id</p>
<dd> ID of a VPC the virtual private gateway is attached to</p>
<dt>availability-zone</p>
<dd> availability zone in which the virtual private gateway resides</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the customer gateway</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the customer gateway</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>type</p>
<dd> the type of virtual private gateway (ipsec.1)</p>
<dt>vpn-gateway-id</p>
<dd> ID of the virtual private gateway </p>
</dl>
<h2>Index</h2>
