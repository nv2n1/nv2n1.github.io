---
title: "nfreplay(1)"
name: "nfreplay"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfreplay/"
description: "nfreplay – netflow replay program"
---

<h2>NAME</h2>
<p> nfreplay &#8211; netflow replay program</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nfreplay [options] [filter]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>nfreplay</code></p>
<dd>is the netflow replay program of the nfdump tool set. It reads data from files stored by nfcapd and sents the netflow data to a host or a multicat group. The filter syntax is equivalent to nfdump. If a filter is supplied, only the matching flows are sent. See the <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1) man page for a detailed description of the filter syntax. All records are sent as netflow version 5. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H </code><i>remotehost</i></p>
<dd> Send all flows to this remote host. Accepts a symbolic name or a IPv4/IPv6 IP address. Defaults to IPv4 localhost 127.0.0.1.</p>
<dt><code>-j </code><i>mcastgroup</i></p>
<dd> Join this multicast group and send all flows to this group host. Accepts a symbolic name or multicast IPv4/IPv6 IP address.</p>
<dt><code>-p </code><i>port</i></p>
<dd> Send all flows to this port on the remote side. Default is 9995.</p>
<dt><code>-4</code></p>
<dd> Forces nfreplay to send flows to a IPv4 address only. Can be used together with -i if the remote host has an IPv4 and IPv6 address record.</p>
<dt><code>-6</code></p>
<dd> Forces nfreplay to send flows to a IPv6 address only. Can be used together with -i if the remote host has an IPv4 and IPv6 address record.</p>
<dt><code>-v </code><i>num</i></p>
<dd> Send flows as netflow version <i>num</i>. <code>5</code> and <code>9</code> are supported. The default is sending the flows as netflow version 5. In version 5 mode, IPv6 flows, are skipped and 64bit counters are truncated to 32bit.</p>
<dt><code>-d </code><i>usec</i></p>
<dd> Delay each record by <i>usec</i> mirco seconds, to avoid overrun on the remote side. Default is 10.</p>
<dt><code>-b </code><i>buffersize</i></p>
<dd> Set send buffer size in bytes. Useful for large data to transfer. Default is system dependent.</p>
<dt><code>-r </code><i>inputfile</i></p>
<dd> Read input data from <i>inputfile</i>. Default is read from stdin.</p>
<dt><code>-t </code><i>timewin</i></p>
<dd> Send only flows, which fall in the time window <i>timewin</i>, where <i>timewin</i> is YYYY/MM/dd.hh:mm:ss[-YYYY/MM/dd.hh:mm:ss]. Any parts of the time spec may be omitted e.g YYYY/MM/dd expands to YYYY/MM/dd.00:00:00-YYYY/MM/dd.23:59:59 and sends all flow from a given day.</p>
<dt><code>-c </code><i>num</i></p>
<dd> Limit number of records to send to the first <i>num</i> flows.</p>
<dt><code>-V</code></p>
<dd> Print nfreplay version and exit.</p>
<dt><code>-h</code></p>
<dd> Print help text on stdout with all options and exit.</dl>
<h2>RETURN VALUE</h2>
<p> Returns</p>
<dl>
<dt>
<dd>
<p> 0 No error. </p>
<p> 255 Initialization failed. </p>
<p> 254 Error in filter syntax. </p>
<p> 250 Internal error.</dl>
<h2>NOTES</h2>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1), <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1), <a href="/docs/linux/man/1-nfprofile/">nfprofile</a>(1)</p>
<h2>BUGS</h2>
<h2>Index</h2>
