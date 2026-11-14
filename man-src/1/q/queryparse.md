---
title: "queryparse(1)"
name: "queryparse"
section: "1"
letter: "q"
url: "/docs/linux/man/1-queryparse/"
description: "queryparse – extract DNS queries from pcap capture files."
---

<h2>NAME</h2>
<p> queryparse &#8211; extract DNS queries from pcap capture files.</p>
<h2>SYNOPSIS</h2>
<p> <code>queryparse [-i </code> <i>input file</i> <code>] [-o</code> <i>output file</i> <code>] [-r</code> <i>recursion only</i> <code>] [-R</code> <i>parse responses</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>queryparse</code> is a tool designed to extract DNS queries from pcap-formatted packet capture files and save them in a form suitable for input to Nominum&#8217;s dnsperf or resperf benchmarking tools. <code>queryparse</code> will only examine UDP packets, and currently supports Ethernet and Cisco HDLC frame types.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-i filename</p>
<dd> Attempt to extract DNS queries from <i>filename,</i> which should be a pcap-formatted packet capture session (e.g., a file created by tcpdump or ethereal).</p>
<dt>-o filename</p>
<dd> Write queries to <i>filename</i> in a format suitable for input to Nominum&#8217;s dnsperf or resperf benchmarking tools.</p>
<dt>-r</p>
<dd> Keep queries that do not have the RD (recursion desired) flag set. This is useful when parsing packet captures from authoritative nameservers. When parsing captures from caching nameservers, do not use it unless you also want to parse the outgoing queries from the nameserver. Defaults to discarding queries with RD=0.</p>
<dt>-R</p>
<dd> Parse responses (QR=1) instead of queries (QR=0).</dl>
<h2>FILES</h2>
<p> None</p>
<h2>ENVIRONMENT</h2>
<p> None</p>
<h2>DIAGNOSTICS</h2>
<p> None</p>
<h2>BUGS</h2>
<p> None</p>
<h2>AUTHOR</h2>
<p> Nominum, Inc.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dnsperf/">dnsperf</a></code>(1), <code><a href="/docs/linux/man/1-resperf/">resperf</a></code>(1), <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3), <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8) </p>
<h2>Index</h2>
