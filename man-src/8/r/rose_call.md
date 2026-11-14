---
title: "rose_call(8)"
name: "rose_call"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rose_call/"
description: "ax25_call, netrom_call, rose_call, tcp_call – make an AX.25, NET/ROM, ROSE or TCP connection"
---

<p>ax25_call, netrom_call, rose_call, tcp_call &#8211; make an AX.25, NET/ROM, ROSE or TCP connection</p>
<h2>Synopsis</h2>
<p><code>ax25_call [-c] [-i paclen] [-o paclen] port local_call remote_call [digipeaters &#8230;]</code> </p>
<p> <code>netrom_call [-c] [-i paclen] [-o paclen] port local_call remote_netrom_addr</code> </p>
<p> <code>rose_call [-c] [-i paclen] [-o paclen] port local_call remote_call remote_rose_addr</code> </p>
<p> <code>tcp_call [-c] [-i paclen] [-o paclen] remote_addr remote_port</code></p>
<h2>Description</h2>
<p><code>ax25_call, netrom_call, rose_call and tcp_call</code> establish an AX.25, NET/ROM, ROSE or a TCP connection in a manner suitable for calling from either the <code>ax25d</code> program directly, or from the <code>node</code> program as an external command. By setting the command line arguments appropriately it is possible to set the local callsign from which the call will be made. No translation of the end of lines is performed by this program. </p>
<p> For <code>netrom_call</code> the remote_netrom_addr parameter may either be in the form of a single callsign or as a NET/ROM alias and callsign pair separated by colon. For example NMCLUS:GB7BPQ. </p>
<p> For <code>rose_call</code> the remote_rose_addr parameter must be in the form of a ten digit ROSE address. </p>
<p> For <code>tcp_call</code> the remote_addr parameter must be a dotted-quad IP address or a hostname and the remote_port must be a service name (see <a href="/docs/linux/man/5-services/">services</a>(5)) or a port number.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Enables zlib based compression on the incoming connection. Compression algorithm is the same as in LinuxNode (see <a href="/docs/linux/man/8-node/">node</a>(8)).</p>
<dt><code>-i paclen</code></p>
<dd>The maximum frame length to be used on the incoming connection. The default is 256 for ax25_call and rose_call, 236 for netrom_call and 1024 for tcp_call.</p>
<dt><code>-o paclen</code></p>
<dd>The maximum frame length to be used on the outgoing connection. The default is 256 for ax25_call and rose_call, 236 for netrom_call and 1024 for tcp_call.</dl>
<h2>Files</h2>
<p>/etc/ax25/axports<br />
 /etc/ax25/nrports<br />
 /etc/ax25/rsports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ax25/">ax25</a>(4),</code><a href="/docs/linux/man/4-netrom/">netrom</a>(4),<code><a href="/docs/linux/man/4-rose/">rose</a>(4),</code><a href="/docs/linux/man/4-tcp/">tcp</a>(4).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;<br />
 Tomi Manninen OH2BNS &lt;oh2bns [at] sral.fi&gt;</p>
