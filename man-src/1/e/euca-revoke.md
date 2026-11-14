---
title: "euca-revoke(1)"
name: "euca-revoke"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-revoke/"
description: "euca-revoke – Remove a rule from a security group"
---

<h2>NAME</h2>
<p> euca-revoke &#8211; Remove a rule from a security group</p>
<h2>SYNOPSIS</h2>
<p> euca-revoke [&#8211;egress] [-P PROTOCOL] [-p RANGE] [-t TYPE:CODE] [-s CIDR | <code>-o</code> GROUP] [-u ACCOUNT] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] GROUP</p>
<h2>DESCRIPTION</h2>
<p> Remove a rule from a security group</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</p>
<dd> name or ID of the security group to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;egress</code></p>
<dd> [VPC only] manage an egress rule, which controls traffic leaving the group</p>
<dt><code>-P</code> PROTOCOL, <code>&#8211;protocol</code> PROTOCOL</p>
<dd> the protocol to affect (Non-VPC: tcp, udp, icmp) (VPC only: tcp, udp, icmp, <code>-1</code>/all, other protocol numbers) (default: tcp)</p>
<dt><code>-p</code> RANGE, <code>&#8211;port-range</code> RANGE</p>
<dd> range of ports (specified as &quot;from-to&quot;) or a single port number (required for tcp and udp)</p>
<dt><code>-t</code> TYPE:CODE, <code>&#8211;icmp-type-code</code> TYPE:CODE</p>
<dd> ICMP type and code (specified as &quot;type:code&quot;) (required for icmp)</p>
<dt><code>-s</code> CIDR, <code>&#8211;cidr</code> CIDR</p>
<dd> IP range (default: 0.0.0.0/0)</p>
<dt><code>-o</code> GROUP</p>
<dd> [Non-VPC only] name of a security group with which to affect network communication</p>
<dt><code>-u</code> ACCOUNT</p>
<dd> ID of the account that owns the security group specified with <code>-o</code></p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;debug</code></p>
<dd>
<dd>show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
