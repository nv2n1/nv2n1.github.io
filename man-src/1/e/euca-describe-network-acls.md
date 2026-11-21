---
title: "euca-describe-network-acls(1)"
name: "euca-describe-network-acls"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-network-acls/"
description: "euca-describe-network-acls – Describe one or more network ACLs"
---

<h2>NAME</h2>
<p> euca-describe-network-acls &#8211; Describe one or more network ACLs</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-network-acls [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [NACL [NACL &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Describe one or more network ACLs</p>
<h3>positional arguments:</h3>
<dl>
<dt>NACL</dt>
<dd> limit results to one or more network ACLs</dd></dl>
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
<dt>association.association-id</dt>
<dd> ID of an association ID for a network ACL</dd>
<dt>association.network-acl-id</dt>
<dd> ID of the network ACL involved in an association</dd>
<dt>association.subnet-id</dt>
<dd> ID of the subnet involved in an association</dd>
<dt>default</dt>
<dd> whether the network ACL is the default for its VPC</dd>
<dt>entry.cidr</dt>
<dd> CIDR range for a network ACL entry</dd>
<dt>entry.egress</dt>
<dd> whether an entry applies to egress traffic</dd>
<dt>entry.icmp.code</dt>
<dd> ICMP code for a network ACL entry</dd>
<dt>entry.icmp.type</dt>
<dd> ICMP type for a network ACL entry</dd>
<dt>entry.port-range.from</dt>
<dd> start of the port range for a network ACL entry</dd>
<dt>entry.port-range.to</dt>
<dd> end of the port range for a network ACL entry</dd>
<dt>entry.protocol</dt>
<dd> protocol for a network ACL entry</dd>
<dt>entry.rule-action</dt>
<dd> whether a network ACL entry allows or denies traffic</dd>
<dt>entry.rule-number</dt>
<dd> rule number of a network ACL entry network-acl-id tag-key key of a tag assigned to the network ACL tag-value value of a tag assigned to the network ACL tag:KEY specific tag key/value combination vpc-id the VPC&#8217;s ID </dd>
</dl>
