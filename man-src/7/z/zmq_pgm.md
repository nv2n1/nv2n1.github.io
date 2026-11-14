---
title: "zmq_pgm(7)"
name: "zmq_pgm"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq_pgm/"
description: "zmq_pgm – 0MQ reliable multicast transport using PGM"
---

<p>zmq_pgm &#8211; 0MQ reliable multicast transport using PGM</p>
<h2>Synopsis</h2>
<p>PGM (Pragmatic General Multicast) is a protocol for reliable multicast transport of data over IP networks.</p>
<h2>Description</h2>
<p>0MQ implements two variants of PGM, the standard protocol where PGM datagrams are layered directly on top of IP datagrams as defined by RFC 3208 (the <i>pgm</i> transport) and &quot;Encapsulated PGM&quot; or EPGM where PGM datagrams are encapsulated inside UDP datagrams (the <i>epgm</i> transport). The <i>pgm</i> and <i>epgm</i> transports can only be used with the <i>ZMQ_PUB</i> and <i>ZMQ_SUB</i> socket types. Further, PGM sockets are rate limited by default. For details, refer to the <i>ZMQ_RATE</i>, and <i>ZMQ_RECOVERY_IVL</i> options documented in <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3).</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The <i>pgm</i> transport implementation requires access to raw IP sockets. Additional privileges may be required on some operating systems for this operation. Applications not requiring direct interoperability with other PGM implementations are encouraged to use the <i>epgm</i> transport instead which does not require any special privileges. </p>
<h2>Addressing</h2>
<p>A 0MQ endpoint is a string consisting of a <i>transport</i>:// followed by an <i>address</i>. The <i>transport</i> specifies the underlying protocol to use. The <i>address</i> specifies the transport-specific address to connect to. </p>
<p> For the PGM transport, the transport is pgm, and for the EPGM protocol the transport is epgm. The meaning of the <i>address</i> part is defined below.</p>
<h3>Connecting a socket</h3>
<p>When connecting a socket to a peer address using <i>zmq_connect()</i> with the <i>pgm</i> or <i>epgm</i> transport, the <i>endpoint</i> shall be interpreted as an <i>interface</i> followed by a semicolon, followed by a <i>multicast address</i>, followed by a colon and a port number. </p>
<p> An <i>interface</i> may be specified by either of the following: </p>
<dl>
<dd>&bull; The interface name as defined by the operating system.</dl>
<dl>
<dd>&bull; The primary IPv4 address assigned to the interface, in its numeric representation.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Interface names are not standardised in any way and should be assumed to be arbitrary and platform dependent. On Win32 platforms no short interface names exist, thus only the primary IPv4 address may be used to specify an <i>interface</i>. The <i>interface</i> part can be omitted, in that case the default one will be selected. </p>
</dl>
<p> A <i>multicast address</i> is specified by an IPv4 multicast address in its numeric representation.</p>
<h2>Wire Format</h2>
<p>Consecutive PGM datagrams are interpreted by 0MQ as a single continuous stream of data where 0MQ messages are not necessarily aligned with PGM datagram boundaries and a single 0MQ message may span several PGM datagrams. This stream of data consists of 0MQ messages encapsulated in <i>frames</i> as described in <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7).</p>
<h3>PGM datagram payload</h3>
<p>The following ABNF grammar represents the payload of a single PGM datagram as used by 0MQ: </p>
<dl>
<dd>
<pre>datagram = (offset data)
offset = 2OCTET
data = *OCTET</pre>
</dl>
<p> In order for late joining consumers to be able to identify message boundaries, each PGM datagram payload starts with a 16-bit unsigned integer in network byte order specifying either the offset of the first message <i>frame</i> in the datagram or containing the value 0xFFFF if the datagram contains solely an intermediate part of a larger message. </p>
<p> Note that offset specifies where the first message begins rather than the first message part. Thus, if there are trailing message parts at the beginning of the packet the offset ignores them and points to first initial message part in the packet. </p>
<p> The following diagram illustrates the layout of a single PGM datagram payload: </p>
<dl>
<dd>
<pre>+------------------+----------------------+
| offset (16 bits) | data |
+------------------+----------------------+</pre>
</dl>
<p> The following diagram further illustrates how three example 0MQ frames are laid out in consecutive PGM datagram payloads: </p>
<dl>
<dd>
<pre>First datagram payload
+--------------+-------------+---------------------+
| Frame offset | Frame 1 | Frame 2, part 1 |
| 0x0000 | (Message 1) | (Message 2, part 1) |
+--------------+-------------+---------------------+
Second datagram payload
+--------------+---------------------+
| Frame offset | Frame 2, part 2 |
| 0xFFFF | (Message 2, part 2) |
+--------------+---------------------+
Third datagram payload
+--------------+----------------------------+-------------+
| Frame offset | Frame 2, final 8 bytes | Frame 3 |
| 0x0008 | (Message 2, final 8 bytes) | (Message 3) |
+--------------+----------------------------+-------------+</pre>
</dl>
<h2>Example</h2>
<p><code>Connecting a socket</code>. </p>
<pre><code>//  Connecting to the multicast address 239.192.1.1, port 5555,
//  using the first Ethernet network interface on Linux
//  and the Encapsulated PGM protocol
rc = zmq_connect(socket, &quot;epgm://eth0;239.192.1.1:5555&quot;);
assert (rc == 0);
//  Connecting to the multicast address 239.192.1.1, port 5555,
//  using the network interface with the address 192.168.1.1
//  and the standard PGM protocol
rc = zmq_connect(socket, &quot;pgm://192.168.1.1;239.192.1.1:5555&quot;);
assert (rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7) <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7) <code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
