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
<p> <code>rdate</code> [-p] [-s] [-u] [-l] [-t sec] [host&#8230;]</p>
<p> <code>rdate</code> connects to an RFC 868 time server over a TCP/IP network, printing the returned time and/or setting the system clock.</p>
<h3>OPTIONS</h3>
<dl>
<dt><i>-p</i></dt>
<dd> Print the time returned by the remote machine.</dd>
<dt><i>-s</i></dt>
<dd> Set the system time to the returned time.</dd>
<dt><i>-u</i></dt>
<dd> Use UDP instead of TCP as the transport.</dd>
<dt><i>-l</i></dt>
<dd> Use syslog to output errors (cron.warning) and output (cron.info).</dd>
<dt><i>-t</i></dt>
<dd> Set timeout in seconds for every attempt to retrieve date.</dd></dl>
<h2>HISTORY</h2>
<dl>
<dt>2004-03-16 Johan Nilsson &lt;joh-nils [at] dsv.su.se&gt;</dt>
<dd> Timeout support added.</dd>
<dt>2002-11-06 Elliot Lee &lt;sopwith [at] redhat.com&gt;</dt>
<dd> Patch from Tomek Orzechowski &lt;orzech [at] pld.org.pl&gt; &#8211; alarm(10) to not wait forever for connections.</dd>
<dt>2001-05-23 Phil Knirsch &lt;pknirsch [at] redhat.com&gt;</dt>
<dd> Added UDP protocol support. Close the connection after message handling in conformance to RFC 868.</dd>
<dt>2002-03-07 Elliot Lee &lt;sopwith [at] redhat.com&gt;</dt>
<dd> Add syslog functionality.</dd>
<dt>2000-02-04 Elliot Lee &lt;sopwith [at] redhat.com&gt;</dt>
<dd> Wrote it (previous incarnation had license problems, all 200 lines of it). </dd>
</dl>
