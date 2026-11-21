---

title: "euca-describe-group(1)"
name: "euca-describe-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-group/"
description: "euca-describe-group – Show information about security groups"
---

<p> euca-describe-group &#8211; Show information about security groups</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-group [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [GROUP [GROUP &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about security groups</p>
<h2>DESCRIPTION</h2>
<p> Note that filters are matched on literal strings only, so &quot;&#8211;filter ip-permission.from-port=22&quot; will *not* match a group with a port range of 20 to 30.</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</dt>
<dd> limit results to specific security groups</dd></dl>
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
<dt>description</dt>
<dd> group description group-id group-name ip-permission.cidr CIDR IP range granted permission by the group ip-permission.from-port</dd>
<dt>start of TCP/UDP port range, or ICMP type</dt>
<dd> number</dd>
<dt>ip-permission.group-name</dt>
<dd> name of another group granted permission by this group</dd>
<dt>ip-permission.group-id</dt>
<dd> ID of another group granted permission by this group</dd>
<dt>ip-permission.protocol</dt>
<dd> IP protocol for the permission</dd>
<dt>ip-permission.to-port</dt>
<dd> end of TCP/UDP port range, or ICMP code</dd>
<dt>ip-permission.user-id</dt>
<dd> ID of an account granted permission</dd>
<dt>owner-id</dt>
<dd> account ID of the group&#8217;s owner</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the group</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the group</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>vpc-id</dt>
<dd> [VPC only] ID of a VPC the group belongs to </dd>
</dl>
