---
title: "zmq_tcp(7)"
name: "zmq_tcp"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq_tcp/"
description: "zmq_tcp – 0MQ unicast transport using TCP"
---

<p>zmq_tcp &#8211; 0MQ unicast transport using TCP</p>
<h2>Synopsis</h2>
<p>TCP is an ubiquitous, reliable, unicast transport. When connecting distributed applications over a network with 0MQ, using the TCP transport will likely be your first choice.</p>
<h2>Addressing</h2>
<p>A 0MQ endpoint is a string consisting of a <i>transport</i>:// followed by an <i>address</i>. The <i>transport</i> specifies the underlying protocol to use. The <i>address</i> specifies the transport-specific address to connect to. </p>
<p> For the TCP transport, the transport is tcp, and the meaning of the <i>address</i> part is defined below.</p>
<h3>Assigning a local address to a socket</h3>
<p>When assigning a local address to a socket using <i>zmq_bind()</i> with the <i>tcp</i> transport, the <i>endpoint</i> shall be interpreted as an <i>interface</i> followed by a colon and the TCP port number to use. </p>
<p> An <i>interface</i> may be specified by either of the following: </p>
<dl>
<dd>&bull; The wild-card *, meaning all available interfaces.</dl>
<dl>
<dd>&bull; The primary IPv4 or IPv6 address assigned to the interface, in its numeric representation.</dl>
<dl>
<dd>&bull; The non-portable interface name as defined by the operating system.</dl>
<p> The TCP port number may be specified by: </p>
<dl>
<dd>&bull; A numeric value, usually above 1024 on POSIX systems.</dl>
<dl>
<dd>&bull; The wild-card *, meaning a system-assigned ephemeral port.</dl>
<p> When using ephemeral ports, the caller should retrieve the actual assigned port using the ZMQ_LAST_ENDPOINT socket option. See <code><a href="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></code>(3) for details.</p>
<h3>Unbinding wild-card addres from a socket</h3>
<p>When wild-card * <i>endpoint</i> was used in <i>zmq_bind()</i>, the caller should use real <i>endpoind</i> obtained from the ZMQ_LAST_ENDPOINT socket option to unbind this <i>endpoint</i> from a socket using <i>zmq_unbind()</i>.</p>
<h3>Connecting a socket</h3>
<p>When connecting a socket to a peer address using <i>zmq_connect()</i> with the <i>tcp</i> transport, the <i>endpoint</i> shall be interpreted as a <i>peer address</i> followed by a colon and the TCP port number to use. You can optionally specify a <i>source_endpoint</i> which will be used as the source address for your connection; tcp://<i>source_endpoint</i>;&#8217;endpoint&#8217;, see the <i>interface</i> description above for details. </p>
<p> A <i>peer address</i> may be specified by either of the following: </p>
<dl>
<dd>&bull; The DNS name of the peer.</dl>
<dl>
<dd>&bull; The IPv4 or IPv6 address of the peer, in its numeric representation.</dl>
<p> Note: A description of the ZeroMQ Message Transport Protocol (ZMTP) which is used by the TCP transport can be found at m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:15">http://rfc.zeromq.org/spec:15</a></code>m[]</p>
<h2>Examples</h2>
<p><code>Assigning a local address to a socket</code>. </p>
<pre><code>//  TCP port 5555 on all available interfaces
rc = zmq_bind(socket, &quot;tcp://*:5555&quot;);
assert (rc == 0);
//  TCP port 5555 on the local loop-back interface on all platforms
rc = zmq_bind(socket, &quot;tcp://127.0.0.1:5555&quot;);
assert (rc == 0);
//  TCP port 5555 on the first Ethernet network interface on Linux
rc = zmq_bind(socket, &quot;tcp://eth0:5555&quot;);
assert (rc == 0);</code></pre>
<p> <code>Connecting a socket</code>. </p>
<pre><code>//  Connecting using an IP address
rc = zmq_connect(socket, &quot;tcp://192.168.1.1:5555&quot;);
assert (rc == 0);
//  Connecting using a DNS name
rc = zmq_connect(socket, &quot;tcp://server1:5555&quot;);
assert (rc == 0);
//  Connecting using a DNS name and bind to eth1
rc = zmq_connect(socket, &quot;tcp://eth1:0;server1:5555&quot;);
assert (rc == 0);
//  Connecting using a IP address and bind to an IP address
rc = zmq_connect(socket, &quot;tcp://192.168.1.17:5555;192.168.1.1:5555&quot;);
assert (rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/7-zmq_pgm/">zmq_pgm</a></code>(7) <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7) <code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
