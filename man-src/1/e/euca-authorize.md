---
title: "euca-authorize(1)"
name: "euca-authorize"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-authorize/"
description: "euca-authorize – Add a rule to a security group that allows traffic to pass"
---

<h2>NAME</h2>
<p> euca-authorize &#8211; Add a rule to a security group that allows traffic to pass</p>
<h2>SYNOPSIS</h2>
<p> euca-authorize [&#8211;egress] [-P PROTOCOL] [-p RANGE] [-t TYPE:CODE]</p>
<dl>
<dt>[-s CIDR | <code>-o</code> GROUP] [-u ACCOUNT] [&#8211;show-empty-fields]</dt>
<dd> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] GROUP</dd></dl>
<h2>DESCRIPTION</h2>
<p> Add a rule to a security group that allows traffic to pass</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</dt>
<dd> name or ID of the security group to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;egress</code></dt>
<dd> [VPC only] manage an egress rule, which controls traffic leaving the group</dd>
<dt><code>-P</code> PROTOCOL, <code>&#8211;protocol</code> PROTOCOL</dt>
<dd> the protocol to affect (Non-VPC: tcp, udp, icmp) (VPC only: tcp, udp, icmp, <code>-1</code>/all, other protocol numbers) (default: tcp)</dd>
<dt><code>-p</code> RANGE, <code>&#8211;port-range</code> RANGE</dt>
<dd> range of ports (specified as &quot;from-to&quot;) or a single port number (required for tcp and udp)</dd>
<dt><code>-t</code> TYPE:CODE, <code>&#8211;icmp-type-code</code> TYPE:CODE</dt>
<dd> ICMP type and code (specified as &quot;type:code&quot;) (required for icmp)</dd>
<dt><code>-s</code> CIDR, <code>&#8211;cidr</code> CIDR</dt>
<dd> IP range (default: 0.0.0.0/0)</dd>
<dt><code>-o</code> GROUP</dt>
<dd> [Non-VPC only] name of a security group with which to affect network communication</dd>
<dt><code>-u</code> ACCOUNT</dt>
<dd> ID of the account that owns the security group specified with <code>-o</code></dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
