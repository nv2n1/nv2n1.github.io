---

title: "euca-describe-internet-gateways(1)"
name: "euca-describe-internet-gateways"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-internet-gateways/"
description: "euca-describe-internet-gateways – Describe one or more VPC Internet gateways"
---

<p> euca-describe-internet-gateways &#8211; Describe one or more VPC Internet gateways</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-internet-gateways [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [IGATEWAY [IGATEWAY &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Describe one or more VPC Internet gateways</p>
<h3>positional arguments:</h3>
<dl>
<dt>IGATEWAY</dt>
<dd> limit results to one or more Internet gateways</dd></dl>
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
<dt><code>&#8211;filter</code> NAME=VALUE</dt>
<dd>
</dd><dd>restrict results to those that meet criteria</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd></dl>
<h3>allowed filter names:</h3>
<dl>
<dt>attachment.state</dt>
<dd> if the Internet gateway is attached to a VPC, its attachment state (available)</dd>
<dt>attachment.vpc-id</dt>
<dd> ID of the VPC the Internet gateway is attached to internet-gateway-id tag-key key of a tag assigned to the Internet gateway tag-value value of a tag assigned to the Internet gateway</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination </dd>
</dl>
