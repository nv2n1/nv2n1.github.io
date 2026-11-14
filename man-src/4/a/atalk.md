---
title: "atalk(4)"
name: "atalk"
section: "4"
letter: "a"
url: "/docs/linux/man/4-atalk/"
description: "atalk – AppleTalk protocol family"
---

<p>atalk &#8211; AppleTalk protocol family</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/types.h&gt;
#include &lt;netatalk/at.h&gt;</code></pre>
<h2>Description</h2>
<p>The AppleTalk protocol family is a collection of protocols layered above the Datagram Delivery Protocol (DDP), and using AppleTalk address format. The AppleTalk family may provide SOCK_STREAM (ADSP), SOCK_DGRAM (DDP), SOCK_RDM (ATP), and SOCK_SEQPACKET (ASP). Currently, only DDP is implemented in the kernel; ATP and ASP are implemented in user level libraries; and ADSP is planned.</p>
<h2>Addressing</h2>
<p>AppleTalk addresses are three byte quantities, stored in network byte order. The include file &lt;<code>netatalk/at.h</code>&gt; defines the AppleTalk address format. </p>
<p> Sockets in the AppleTalk protocol family use the following address structure: </p>
<dl>
<dd>
<pre>struct sockaddr_at {
 short sat_family;
 u_char sat_port;
 struct at_addr sat_addr;
 char sat_zero[ 8 ];
};</pre>
</dl>
<p> The port of a socket may be set with <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). The node for <code>bind</code> must always be <code>ATADDR_ANYNODE</code>: &#8220;this node.&#8221; The net may be <code>ATADDR_ANYNET</code> or <code>ATADDR_LATENET</code>. <code>ATADDR_ANYNET</code> coresponds to the machine&#8217;s &#8220;primary&#8221; address (the first configured). <code>ATADDR_LATENET</code> causes the address in outgoing packets to be determined when a packet is sent, i.e. determined late. <code>ATADDR_LATENET</code> is equivalent to opening one socket for each network interface. The port of a socket and either the primary address or <code>ATADDR_LATENET</code> are returned with <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8). </p>
