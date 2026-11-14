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
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [NACL [NACL &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Describe one or more network ACLs</p>
<h3>positional arguments:</h3>
<dl>
<dt>NACL</p>
<dd> limit results to one or more network ACLs</dl>
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
<dt>association.association-id</p>
<dd> ID of an association ID for a network ACL</p>
<dt>association.network-acl-id</p>
<dd> ID of the network ACL involved in an association</p>
<dt>association.subnet-id</p>
<dd> ID of the subnet involved in an association</p>
<dt>default</p>
<dd> whether the network ACL is the default for its VPC</p>
<dt>entry.cidr</p>
<dd> CIDR range for a network ACL entry</p>
<dt>entry.egress</p>
<dd> whether an entry applies to egress traffic</p>
<dt>entry.icmp.code</p>
<dd> ICMP code for a network ACL entry</p>
<dt>entry.icmp.type</p>
<dd> ICMP type for a network ACL entry</p>
<dt>entry.port-range.from</p>
<dd> start of the port range for a network ACL entry</p>
<dt>entry.port-range.to</p>
<dd> end of the port range for a network ACL entry</p>
<dt>entry.protocol</p>
<dd> protocol for a network ACL entry</p>
<dt>entry.rule-action</p>
<dd> whether a network ACL entry allows or denies traffic</p>
<dt>entry.rule-number</p>
<dd> rule number of a network ACL entry network-acl-id tag-key key of a tag assigned to the network ACL tag-value value of a tag assigned to the network ACL tag:KEY specific tag key/value combination vpc-id the VPC&#8217;s ID </p>
</dl>
<h2>Index</h2>
