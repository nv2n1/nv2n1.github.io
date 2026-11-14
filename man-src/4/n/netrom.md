---
title: "netrom(4)"
name: "netrom"
section: "4"
letter: "n"
url: "/docs/linux/man/4-netrom/"
description: "AF_NETROM – NET/ROM amateur packet radio protocol family"
---

<p>AF_NETROM &#8211; NET/ROM amateur packet radio protocol family</p>
<h2>Description</h2>
<p><code>NET/ROM</code> is a protocol used extensively by radio amateurs. The Linux NET/ROM protocol family permits access to these protocols via the standard networking <code>socket</code> metaphor. </p>
<p> The NET/ROM protocol layer only supports connected mode. IP traffic may be stacked on top of NET/ROM frames using a non-standard extension to the NET/ROM protocol. </p>
<p> The only mode of operation is connected mode which is the mode used for a socket of type SOCK_SEQPACKET (stream sockets are not available in NET/ROM). This requires that the user ensures output data is suitably packetised, and that input data is read a packet at a time into a buffer of suitable size. </p>
<p> NET/ROM addresses consist of 6 ascii characters and a number called the SSID. These are encoded into a sockaddr_ax25 structure which is provided to the relevant system calls. </p>
<p> NET/ROM has some unusual properties. Notably in a multi-user system an AX.25 address is often associated with a user, and some users may not have such an association. a set of ioctl calls are provided to manage an association table. </p>
<p> NET/ROM supports the following socket options for SOL_NETROM. NETROM_T1 is the T1 timer in 1/10ths of a second, NETROM_T2 is the T2 timer in 1/10ths of a second. NETROM_N2, the retry counter is also configurable. There is no &#8216;infinite retry&#8217; option supported however. It is possible for an application to request that the NET/ROM layer return the NET/ROM header as well as the application data, this is done via the NETROM_HDRINCL socket option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2),</code> <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a>(2),</code> <code><a href="/docs/linux/man/5-nrbroadcast/">nrbroadcast</a></code>(5), <code><a href="/docs/linux/man/5-nrports/">nrports</a></code>(5), <code><a href="/docs/linux/man/8-netromd/">netromd</a></code>(8), <code><a href="/docs/linux/man/8-noderest/">noderest</a></code>(8), <code><a href="/docs/linux/man/8-nodesave/">nodesave</a></code>(8), <code><a href="/docs/linux/man/8-nrctl/">nrctl</a></code>(8), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8). </p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
