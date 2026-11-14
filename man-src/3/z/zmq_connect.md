---
title: "zmq_connect(3)"
name: "zmq_connect"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_connect/"
description: "zmq_connect – create outgoing connection from socket"
---

<p>zmq_connect &#8211; create outgoing connection from socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_connect(void *socket, const char *endpoint);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_connect()</i> function connects the <i>socket</i> to an <i>endpoint</i> and then accepts incoming connections on that endpoint. The <i>endpoint</i> is a string consisting of a <i>transport</i>:// followed by an <i>address</i>. The <i>transport</i> specifies the underlying protocol to use. The <i>address</i> specifies the transport-specific address to connect to. 0MQ provides the the following transports: <i>tcp</i></p>
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
<p> Every 0MQ socket type except <i>ZMQ_PAIR</i> supports one-to-many and many-to-one semantics. The precise semantics depend on the socket type and are defined in <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3).</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 for most transports and socket types the connection is not performed immediately but as needed by 0MQ. Thus a successful call to <i>zmq_connect()</i> does not mean that the connection was or could actually be established. Because of this, for most transports and socket types the order in which a <i>server</i> socket is bound and a <i>client</i> socket is connected to it does not matter. The first exception is when using the inproc:// transport: you must call <i>zmq_bind()</i> before calling <i>zmq_connect()</i>. The second exception are <i>ZMQ_PAIR</i> sockets, which do not automatically reconnect to endpoints. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 following a <i>zmq_connect()</i>, for socket types except for ZMQ_ROUTER, the socket enters its normal <i>ready</i> state. By contrast, following a <i>zmq_bind()</i> alone, the socket enters a <i>mute</i> state in which the socket blocks or drops messages according to the socket type, as defined in <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3). A ZMQ_ROUTER socket enters its normal <i>ready</i> state for a specific peer only when handshaking is complete for that peer, which may take an arbitrary time. </p>
<h2>Return Value</h2>
<p>The <i>zmq_connect()</i> function returns zero if successful. Otherwise it returns -1 and sets <i>errno</i> to one of the values defined below.</p>
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
<p><code>Connecting a subscriber socket to an in-process and a TCP transport</code>. </p>
<pre><code>/* Create a ZMQ_SUB socket */
void *socket = zmq_socket(context, ZMQ_SUB);
assert(socket);
/* Connect it to an in-process transport with the address 'my_publisher' */
int rc = zmq_connect(socket, &quot;inproc://my_publisher&quot;);
assert(rc == 0);
/* Connect it to the host server001, port 5555 using a TCP transport */
rc = zmq_connect(socket, &quot;tcp://server001:5555&quot;);
assert(rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
