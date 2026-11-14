---
title: "euca-describe-group(1)"
name: "euca-describe-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-group/"
description: "euca-describe-group – Show information about security groups"
---

<h2>NAME</h2>
<p> euca-describe-group &#8211; Show information about security groups</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-group [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [GROUP [GROUP &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about security groups</p>
<h2>DESCRIPTION</h2>
<p> Note that filters are matched on literal strings only, so &quot;&#8211;filter ip-permission.from-port=22&quot; will *not* match a group with a port range of 20 to 30.</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</p>
<dd> limit results to specific security groups</dl>
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
<dt>description</p>
<dd> group description group-id group-name ip-permission.cidr CIDR IP range granted permission by the group ip-permission.from-port</p>
<dt>start of TCP/UDP port range, or ICMP type</p>
<dd> number</p>
<dt>ip-permission.group-name</p>
<dd> name of another group granted permission by this group</p>
<dt>ip-permission.group-id</p>
<dd> ID of another group granted permission by this group</p>
<dt>ip-permission.protocol</p>
<dd> IP protocol for the permission</p>
<dt>ip-permission.to-port</p>
<dd> end of TCP/UDP port range, or ICMP code</p>
<dt>ip-permission.user-id</p>
<dd> ID of an account granted permission</p>
<dt>owner-id</p>
<dd> account ID of the group&#8217;s owner</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the group</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the group</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>vpc-id</p>
<dd> [VPC only] ID of a VPC the group belongs to </p>
</dl>
<h2>Index</h2>
