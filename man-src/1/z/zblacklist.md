---
title: "zblacklist(1)"
name: "zblacklist"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zblacklist/"
description: "zblacklist – zmap IP blacklist tool"
---

<h2>NAME</h2>
<p> <code>zblacklist</code> &#8211; zmap IP blacklist tool</p>
<h2>SYNOPSIS</h2>
<p> zblacklist [ -b &lt;blacklist&gt; ] [ -w &lt;whitelist&gt; ] [ OPTIONS&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>ZBlacklist</i> is a network tool for limiting and deduplicating a list of IP addresses using a blacklist or whitelist.</p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;blacklist-file=path</code></p>
<dd> File of subnets to exclude, in CIDR notation, one-per line. It is recommended you use this to exclude RFC 1918 addresses, multicast, IANA reserved space, and other IANA special-purpose addresses. An example blacklist file <code>blacklist.conf</code> for this purpose.</p>
<dt><code>-w</code>, <code>&#8211;whitelist-file=name</code></p>
<dd> File of subnets to include, in CIDR notation, one-per line. All other subnets will be excluded.</p>
<dt><code>-l</code>, <code>&#8211;log-file=name</code></p>
<dd> File to log to.</p>
<dt><code>-v</code>, <code>&#8211;verbosity</code></p>
<dd> Level of log detail (0-5, default=3)</p>
<dt><code>&#8211;no-duplicate-checking</code></p>
<dd> Don&#8217;t deduplicate input addresses. Default is false.</p>
<dt><code>&#8211;ignore-blacklist-errors</code></p>
<dd> Ignore invalid entries in the blacklist. Default is false. </p>
</dl>
<h2>Index</h2>
