---
title: "dnstcpbench(1)"
name: "dnstcpbench"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnstcpbench/"
description: "dnstcpbench – tool to perform TCP benchmarking of nameservers"
---

<h2 class="name">NAME</h2>
<p> dnstcpbench &#8211; tool to perform TCP benchmarking of nameservers </p>
<h2>SYNOPSIS</h2>
<p> <i>dnstcpbench</i> [&#8211;help] [&#8211;file=filename] [&#8211;verbose] [&#8211;udp-first, -u] [&#8211;workers] [&#8211;timeout-msec] remote-ip-address [remote-port]</p>
<h2>DESCRIPTION</h2>
<p> dnstcpbench reads DNS queries (by default from standard input) and sends them out in parallel to a remote nameserver. By default TCP/IP is used, but optionally, UDP is tried first, which allows for the benchmarking of TCP/IP fallback. </p>
<p> The input format is one query per line: qname single-space qtype. An example: <a rel="nofollow" href="http://www.powerdns.com">www.powerdns.com</a> ANY powerdns.com MX </p>
<p> When benchmarking extended runs, it may be necessary to enable TIME_WAIT recycling, as TCP/IP port tuples may otherwise run out. On Linux this is performed by running: </p>
<dl>
<dt>
<dd>
<pre>
# echo 1 &gt; /proc/sys/net/ipv4/tcp_tw_recycle
</pre>
</dl>
<p> The equivalent for IPv6 is not known.</p>
<h2>OPTIONS</h2>
<p> -f,&#8211;file</p>
<dl>
<dt>
<dd> Filename from which to read queries. Defaults to standard input if unspecified.</dl>
<p> -h,&#8211;help</p>
<dl>
<dt>
<dd> Provide a helpful message</dl>
<p> &#8211;timeout-msec</p>
<dl>
<dt>
<dd> Number of milliseconds to wait for an answer</dl>
<p> &#8211;udp-first, -u</p>
<dl>
<dt>
<dd> Attempt resolution via UDP first, only do TCP if truncated answer is received</dl>
<p> -v,&#8211;verbose</p>
<dl>
<dt>
<dd> Be wordy on what the program is doing</dl>
<p> &#8211;workers</p>
<dl>
<dt>
<dd> Number of parallel worker threads to use.</dl>
<p> Remote IP address can be IPv4 or IPv6. Remote port defaults to 53.</p>
<h2>STATISTICAL OUTPUT</h2>
<p> The program reports both mean and median numbers for queries per second and UDP and TCP latency. Each query only counts once, even if it is tried over UDP first. This effectively means that passing <i>-u</i> can lower query rates if many queries get shunted to TCP.</p>
<h2>BUGS</h2>
<p> Currently the timeout code does not actually perform non-blocking connects or writes. So a slow connect or slow writes will still cause low performance and delays. </p>
<p> Median queries per second statistics are reported as 0 for sub-second runs.</p>
<h2>AUTHOR</h2>
<p> Written by PowerDNS.COM BV, bert hubert, &lt;m[blue]<code>bert.hubert [at] netherlabs.nl</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>RESOURCES</h2>
<p> Website: m[blue]<code><a rel="nofollow" href="http://www.powerdns.com">http://www.powerdns.com</a></code>m[]</p>
<h2>COPYING</h2>
<p> Copyright &#169; 2013 PowerDNS.COM BV. Free use of this software is granted under the terms of the GNU General Public License (GPL) version 2.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> bert.hubert [at] netherlabs.nl</p>
<dl>
<dt>
<dd> mailto:bert.hubert [at] netherlabs.nl</dl>
</dl>
<h2>Index</h2>
