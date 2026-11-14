---
title: "zmq_bind(3)"
name: "zmq_bind"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_bind/"
description: "zmq_bind – accept incoming connections on a socket"
---

<p>zmq_bind &#8211; accept incoming connections on a socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_bind(void *socket, const char *endpoint);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_bind()</i> function binds the <i>socket</i> to a local <i>endpoint</i> and then accepts incoming connections on that endpoint. The <i>endpoint</i> is a string consisting of a <i>transport</i>:// followed by an <i>address</i>. The <i>transport</i> specifies the underlying protocol to use. The <i>address</i> specifies the transport-specific address to bind to. 0MQ provides the the following transports: <i>tcp</i></p>
<dl>
<dd>unicast transport using TCP, see <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7)</dl>
<p> <i>ipc</i></p>
<dl>
<dd>local inter-process communication transport, see <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7)</dl>
<p> <i>inproc</i></p>
<dl>
<dd>local in-process (inter-thread) communication transport, see <code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7)</dl>
<p> <i>pgm</i>, <i>epgm</i></p>
<dl>
<dd>reliable multicast transport using PGM, see <code><a href="/docs/linux/man/7-zmq_pgm/">zmq_pgm</a></code>(7)</dl>
<p> Every 0MQ socket type except <i>ZMQ_PAIR</i> supports one-to-many and many-to-one semantics. The precise semantics depend on the socket type and are defined in <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3). The <i>ipc</i> and <i>tcp</i> transports accept wildcard addresses: see <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7) and <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7) for details.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the address syntax may be different for <i>zmq_bind()</i> and <i>zmq_connect()</i> especially for the <i>tcp</i>, <i>pgm</i> and <i>epgm</i> transports. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 following a <i>zmq_bind()</i>, the socket enters a <i>mute</i> state unless or until at least one incoming or outgoing connection is made, at which point the socket enters a <i>ready</i> state. In the mute state, the socket blocks or drops messages according to the socket type, as defined in <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3). By contrast, following a libzmq:zmq_connect[3], the socket enters the <i>ready</i> state. </p>
<h2>Return Value</h2>
<p>The <i>zmq_bind()</i> function returns zero if successful. Otherwise it returns -1 and sets <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The endpoint supplied is invalid.</dl>
<p> <code>EPROTONOSUPPORT</code></p>
<dl>
<dd>The requested <i>transport</i> protocol is not supported.</dl>
<p> <code>ENOCOMPATPROTO</code></p>
<dl>
<dd>The requested <i>transport</i> protocol is not compatible with the socket type.</dl>
<p> <code>EADDRINUSE</code></p>
<dl>
<dd>The requested <i>address</i> is already in use.</dl>
<p> <code>EADDRNOTAVAIL</code></p>
<dl>
<dd>The requested <i>address</i> was not local.</dl>
<p> <code>ENODEV</code></p>
<dl>
<dd>The requested <i>address</i> specifies a nonexistent interface.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
<p> <code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<p> <code>EMTHREAD</code></p>
<dl>
<dd>No I/O thread is available to accomplish the task.</dl>
<h2>Example</h2>
<p><code>Binding a publisher socket to an in-process and a TCP transport</code>. </p>
<pre><code>/* Create a ZMQ_PUB socket */
void *socket = zmq_socket(context, ZMQ_PUB);
assert(socket);
/* Bind it to a in-process transport with the address 'my_publisher' */
int rc = zmq_bind(socket, &quot;inproc://my_publisher&quot;);
assert(rc == 0);
/* Bind it to a TCP transport on port 5555 of the 'eth0' interface */
rc = zmq_bind(socket, &quot;tcp://eth0:5555&quot;);
assert(rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
