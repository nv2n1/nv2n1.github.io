---

title: "euca-describe-vpc-peering-connections(1)"
name: "euca-describe-vpc-peering-connections"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-vpc-peering-connections/"
description: "euca-describe-vpc-peering-connections – Show information about VPC peering connections"
---

<p> euca-describe-vpc-peering-connections &#8211; Show information about VPC peering connections</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-vpc-peering-connections [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [PEERCONN [PEERCONN &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about VPC peering connections</p>
<h3>positional arguments:</h3>
<dl>
<dt>PEERCONN</dt>
<dd> limit results to specific VPC peering connections</dd></dl>
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
<dt>accepter-vpc-info.cidr-block</dt>
<dd> the peer VPC&#8217;s CIDR address block</dd>
<dt>accepter-vpc-info.owner-id</dt>
<dd> the peer VPC&#8217;s owner&#8217;s account ID</dd>
<dt>accepter-vpc-info.vpc-id</dt>
<dd> the peer VPC&#8217;s ID</dd>
<dt>expiration-time</dt>
<dd> when the peering connection request expires</dd>
<dt>requester-vpc-info.cidr-block</dt>
<dd> the requester VPC&#8217;s CIDR address block</dd>
<dt>requester-vpc-info.owner-id</dt>
<dd> the requester VPC&#8217;s owner&#8217;s account ID</dd>
<dt>requester-vpc-info.vpc-id</dt>
<dd> the requester VPC&#8217;s ID</dd>
<dt>status-code</dt>
<dd> the peering connection&#8217;s status (active, deleted, expired, failed, pending-acceptance, provisioning, rejected)</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the peering connection</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the peering connection</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>vpc-peering-connection-id</dt>
<dd> the peering connection&#8217;s ID </dd>
</dl>
