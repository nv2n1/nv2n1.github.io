---
title: "logresolve(8)"
name: "logresolve"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logresolve/"
description: "logresolve – Resolve IP-addresses to hostnames in Apache log files"
---

<p>logresolve &#8211; Resolve IP-addresses to hostnames in Apache log files</p>
<h2>Synopsis</h2>
<p> <code>logresolve</code> [ &#8211;<code>s</code> <i>filename</i> ] [ &#8211;<code>c</code> ] &lt; <i>access_log</i> &gt; <i>access_log.new</i><br />
&nbsp;<wbr> </p>
<h2>Summary</h2>
<p>&nbsp;<wbr> </p>
<p> logresolve is a post-processing program to resolve IP-addresses in Apache&#8217;s access logfiles. To minimize impact on your nameserver, logresolve has its very own internal hash-table cache. This means that each IP number will only be looked up the first time it is found in the log file.<br />
&nbsp;<wbr> </p>
<p> Takes an Apache log file on standard input. The IP addresses must be the first thing on each line and must be separated from the remainder of the line by a space.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-s <i>filename</i></p>
<dd>Specifies a filename to record statistics.</p>
<dt>-c</p>
<dd>This causes logresolve to apply some DNS checks: after finding the hostname from the IP address, it looks up the IP addresses for the hostname and checks that one of these matches the original address.<br />
&nbsp;<wbr> </p>
</dl>
