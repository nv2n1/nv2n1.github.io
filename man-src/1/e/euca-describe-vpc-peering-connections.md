---
title: "euca-describe-vpc-peering-connections(1)"
name: "euca-describe-vpc-peering-connections"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-vpc-peering-connections/"
description: "euca-describe-vpc-peering-connections – Show information about VPC peering connections"
---

<h2>NAME</h2>
<p> euca-describe-vpc-peering-connections &#8211; Show information about VPC peering connections</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-vpc-peering-connections [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [PEERCONN [PEERCONN &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about VPC peering connections</p>
<h3>positional arguments:</h3>
<dl>
<dt>PEERCONN</p>
<dd> limit results to specific VPC peering connections</dl>
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
<dt>accepter-vpc-info.cidr-block</p>
<dd> the peer VPC&#8217;s CIDR address block</p>
<dt>accepter-vpc-info.owner-id</p>
<dd> the peer VPC&#8217;s owner&#8217;s account ID</p>
<dt>accepter-vpc-info.vpc-id</p>
<dd> the peer VPC&#8217;s ID</p>
<dt>expiration-time</p>
<dd> when the peering connection request expires</p>
<dt>requester-vpc-info.cidr-block</p>
<dd> the requester VPC&#8217;s CIDR address block</p>
<dt>requester-vpc-info.owner-id</p>
<dd> the requester VPC&#8217;s owner&#8217;s account ID</p>
<dt>requester-vpc-info.vpc-id</p>
<dd> the requester VPC&#8217;s ID</p>
<dt>status-code</p>
<dd> the peering connection&#8217;s status (active, deleted, expired, failed, pending-acceptance, provisioning, rejected)</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the peering connection</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the peering connection</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>vpc-peering-connection-id</p>
<dd> the peering connection&#8217;s ID </p>
</dl>
<h2>Index</h2>
