---
title: "rdate(1)"
name: "rdate"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdate/"
description: "rdate – get the time via the network"
---

<h2>NAME</h2>
<p> rdate &#8211; get the time via the network</p>
<h2>SYNOPSIS</h2>
<p> <code>rdate</code> [-p] [-s] [-u] [-l] [-t sec] [host&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rdate</code> connects to an RFC 868 time server over a TCP/IP network, printing the returned time and/or setting the system clock.</p>
<h3>OPTIONS</h3>
<dl>
<dt><i>-p</i></p>
<dd> Print the time returned by the remote machine.</p>
<dt><i>-s</i></p>
<dd> Set the system time to the returned time.</p>
<dt><i>-u</i></p>
<dd> Use UDP instead of TCP as the transport.</p>
<dt><i>-l</i></p>
<dd> Use syslog to output errors (cron.warning) and output (cron.info).</p>
<dt><i>-t</i></p>
<dd> Set timeout in seconds for every attempt to retrieve date.</dl>
<h2>HISTORY</h2>
<dl>
<dt>2004-03-16 Johan Nilsson &lt;joh-nils [at] dsv.su.se&gt;</p>
<dd> Timeout support added.</p>
<dt>2002-11-06 Elliot Lee &lt;sopwith [at] redhat.com&gt;</p>
<dd> Patch from Tomek Orzechowski &lt;orzech [at] pld.org.pl&gt; &#8211; alarm(10) to not wait forever for connections.</p>
<dt>2001-05-23 Phil Knirsch &lt;pknirsch [at] redhat.com&gt;</p>
<dd> Added UDP protocol support. Close the connection after message handling in conformance to RFC 868.</p>
<dt>2002-03-07 Elliot Lee &lt;sopwith [at] redhat.com&gt;</p>
<dd> Add syslog functionality.</p>
<dt>2000-02-04 Elliot Lee &lt;sopwith [at] redhat.com&gt;</p>
<dd> Wrote it (previous incarnation had license problems, all 200 lines of it). </p>
</dl>
<h2>Index</h2>
