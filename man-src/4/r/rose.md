---
title: "rose(4)"
name: "rose"
section: "4"
letter: "r"
url: "/docs/linux/man/4-rose/"
description: "AF_ROSE – Rose amateur packet radio protocol family"
---

<p>AF_ROSE &#8211; Rose amateur packet radio protocol family</p>
<h2>Description</h2>
<p><code>Rose</code> is a protocol used extensively by radio amateurs. The Linux Rose protocol family permits access to these protocols via the standard networking <code>socket</code> metaphor. </p>
<p> The Rose protocol layer only supports connected mode. </p>
<p> The only mode of operation is connected mode which is the mode used for a socket of type SOCK_SEQPACKET (stream sockets are not available in Rose). This requires that the user ensures output data is suitably packetised, and that input data is read a packet at a time into a buffer of suitable size. </p>
<p> Rose addresses consist of 10 digits. These are encoded into a sockaddr_rose structure which is provided to the relevant system calls. </p>
<p> Rose has some unusual properties. Notably in a multi-user system an AX.25 address is often associated with a user, and some users may not have such an association. a set of ioctl calls are provided to manage an association table. </p>
<p> Rose supports the following socket options for SOL_ROSE. ROSE_T1 is the T11/T21 timer in 1/10ths of a second, ROSE_T2 is the T12/T22 timer in 1/10ths of a second. ROSE_T3, is the T13/T23 timer in 1/10ths of a second. It is possible for an application to request that the Rose layer return the Rose header as well as the application data, this is done via the ROSE_HDRINCL socket option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2),</code> <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a>(2),</code> <code><a href="/docs/linux/man/5-rsports/">rsports</a></code>(5), <code><a href="/docs/linux/man/8-rsctl/">rsctl</a></code>(8), <code><a href="/docs/linux/man/8-rsparms/">rsparms</a></code>(8). </p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
