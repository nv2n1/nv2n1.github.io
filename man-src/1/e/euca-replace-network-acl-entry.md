---
title: "euca-replace-network-acl-entry(1)"
name: "euca-replace-network-acl-entry"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-replace-network-acl-entry/"
description: "euca-replace-network-acl-entry – Replace an entry in a VPC network ACL"
---

<h2>NAME</h2>
<p> euca-replace-network-acl-entry &#8211; Replace an entry in a VPC network ACL</p>
<h2>SYNOPSIS</h2>
<p> euca-replace-network-acl-entry <code>-n</code> INT (<code>&#8211;allow</code> | <code>&#8211;deny</code>) <code>-r</code> CIDR</p>
<dl>
<dt>[-P PROTOCOL] [&#8211;egress] [-p RANGE]</p>
<dd> [-t TYPE:CODE] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] NACL</dl>
<h2>DESCRIPTION</h2>
<p> Replace an entry in a VPC network ACL</p>
<h3>positional arguments:</h3>
<dl>
<dt>NACL</p>
<dd> ID of the network ACL to add the entry to (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> INT, <code>&#8211;rule-number</code> INT</p>
<dd> rule number for the new entry (required)</p>
<dt><code>&#8211;allow</code></p>
<dd> make the new entry allow the traffic it matches</p>
<dt><code>&#8211;deny</code></p>
<dd> make the new entry block the traffic it matches</p>
<dt><code>-r</code> CIDR, <code>&#8211;cidr</code> CIDR</p>
<dd> CIDR address range the entry should affect (required)</p>
<dt><code>-P</code> PROTOCOL, <code>&#8211;protocol</code> PROTOCOL</p>
<dd> protocol the entry should apply to (default: all)</p>
<dt><code>&#8211;egress</code></p>
<dd> make the entry affect outgoing (egress) network traffic (default: affect incoming (ingress) traffic)</p>
<dt><code>-p</code> RANGE, <code>&#8211;port-range</code> RANGE</p>
<dd> range of ports (specified as &quot;from-to&quot;) or a single port number (required for tcp and udp)</p>
<dt><code>-t</code> TYPE:CODE, <code>&#8211;icmp-type-code</code> TYPE:CODE</p>
<dd> ICMP type and code (specified as &quot;type:code&quot;) (required for icmp)</p>
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
