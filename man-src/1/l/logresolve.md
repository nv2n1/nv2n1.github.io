---
title: "logresolve(1)"
name: "logresolve"
section: "1"
letter: "l"
url: "/docs/linux/man/1-logresolve/"
description: "logresolve – Resolve IP-addresses to hostnames in Apache log files"
---

<h2 class="name">NAME</h2>
<p> logresolve &#8211; Resolve IP-addresses to hostnames in Apache log files</p>
<h2>SYNOPSIS</h2>
<p>&nbsp; </p>
<p> <code>logresolve</code> [ &#8211;<code>s</code> <i>filename</i> ] [ &#8211;<code>c</code> ] &lt; <i>access_log</i> &gt; <i>access_log.new</i><br />
&nbsp; </p>
<h2>SUMMARY</h2>
<p>&nbsp; </p>
<p> <code>logresolve</code> is a post-processing program to resolve IP-addresses in Apache&#8217;s access logfiles. To minimize impact on your nameserver, logresolve has its very own internal hash-table cache. This means that each IP number will only be looked up the first time it is found in the log file.<br />
&nbsp; </p>
<p> Takes an Apache log file on standard input. The IP addresses must be the first thing on each line and must be separated from the remainder of the line by a space.<br />
&nbsp; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-s </code><i>filename</i></p>
<dd> Specifies a filename to record statistics.</p>
<dt><code>-c</code></p>
<dd> This causes <code>logresolve</code> to apply some DNS checks: after finding the hostname from the IP address, it looks up the IP addresses for the hostname and checks that one of these matches the original address.<br />
&nbsp; </p>
</dl>
<h2>Index</h2>
