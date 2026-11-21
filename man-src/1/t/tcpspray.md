---
title: "tcpspray(1)"
name: "tcpspray"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcpspray/"
description: "tcpspray – TCP/IP bandwidth measurement tool (Discard and Echo client)"
---

<h2>NAME</h2>
<p> tcpspray &#8211; TCP/IP bandwidth measurement tool (Discard and Echo client)</p>
<h2>SYNOPSIS</h2>
<p> <code>tcpspray</code> [<code>-46ev</code>] [<code>-b block_size</code>] [<code>-d wait_81s</code>] [ <code>-f filename</code>] [<code>-n count</code>] &lt;<code>hostname</code>&gt; [<code>port</code>] </p>
<h2>DESCRIPTON</h2>
<p> <code>tcpspray</code> uses the <i>Discard</i> resp. <i>Echo</i> protocol (RFC 863 resp. RFC 862) to perform bandwidth measurements of <i>TCP</i> sessions between the local system, and a <i>Discard</i> resp. <i>Echo</i> server. </p>
<p> Unix-based hosts can provide a Discard and/or Echo servers with the Internet <i>super-server</i> <code>inetd</code>. On Windows NT, the <i>simple network protocols</i> optional component will do the same. </p>
<p> The name or address of the server node must be specified. tcpspray will automatically try to use IPv6 when available. If not, or if it fails, it will fallback to IPv4. However, tcpspray4 resp. tcpspray6 only try to use IPv4 resp. IPv6. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code> or <code>&#8211;ipv4</code></dt>
<dd> Force usage of TCP over IPv4. </dd>
<dt><code>-6</code> or <code>&#8211;ipv6</code></dt>
<dd> Force usage of TCP over IPv6. </dd>
<dt><code>-b block_size</code> or <code>&#8211;bsize block_size</code></dt>
<dd> Send block of the specified byte size (default: 1024). </dd>
<dt><code>-d wait_81s</code> or <code>&#8211;delay wait_81s</code></dt>
<dd> Waits for the given amount of microseconds after any given was sent before attempting to send the next one. There is no delay by default. </dd>
<dt><code>-e</code> or <code>&#8211;echo</code></dt>
<dd> Use the Echo protocol instead of Discard. tcpspray will measure the time required to send data and receive it back, instead of simply sending it. </dd>
<dt><code>-f filename</code> or <code>&#8211;fill filename</code></dt>
<dd> Read data from the specified file to fill sent blocks with. If the file is smaller than the size of blocks, or if no file were specified, the remaining trailing bytes are all set to zero. </dd>
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd> Display some help and exit. </dd>
<dt><code>-n block_count</code> or <code>&#8211;count block_count</code></dt>
<dd> Send the specified amount of data blocks for the measurements (default: 100). </dd>
<dt><code>-V</code> or <code>&#8211;version</code></dt>
<dd> Display program version and license and exit. </dd>
<dt><code>-v</code> or <code>&#8211;verbose</code></dt>
<dd> Display more verbose informations. In particular, tcpspray will print a dot each time a block is sent. If the Echo protocol is used (option -e), dots will be erased as data is received back. </dd>
</dl>
<h2>DIAGNOSTICS</h2>
<p> If you get no response while you know the remote host is up, it is most likely that it has no Discard/Echo service running, or that these services are blocked by a firewall. Running tcptraceroute6(8) resp. tcptraceroute(8) toward the IPv6 resp. IPv4 remote host might help detecting such a situation. </p>
<h2>SECURITY</h2>
<p> tcpspray does not require any privilege to run. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-tcp/">tcp</a>(7), inetd(8), tcptraceroute6(8), tcptraceroute(8) </p>
<h2>AUTHOR</h2>
<p> R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a> </p>
