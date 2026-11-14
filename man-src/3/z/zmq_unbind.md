---
title: "zmq_unbind(3)"
name: "zmq_unbind"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_unbind/"
description: "zmq_unbind – Stop accepting connections on a socket"
---

<p>zmq_unbind &#8211; Stop accepting connections on a socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_unbind(void *socket, const char *endpoint);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_unbind()</i> function shall unbind a socket specified by the <i>socket</i> argument from the endpoint specified by the <i>endpoint</i> argument. </p>
<p> The <i>endpoint</i> argument is as described in <code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3)</p>
<h3>Unbinding wild-card addres from a socket</h3>
<p>When wild-card * <i>endpoint</i> (described in <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7) and <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7)) was used in <i>zmq_bind()</i>, the caller should use real <i>endpoind</i> obtained from the ZMQ_LAST_ENDPOINT socket option to unbind this <i>endpoint</i> from a socket.</p>
<h2>Return Value</h2>
<p>The <i>zmq_unbind()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The endpoint supplied is invalid.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
<p> <code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<h2>Examples</h2>
<p><code>Unbind a subscriber socket from a TCP transport</code>. /* Create a ZMQ_SUB socket */<br />
void *socket = zmq_socket(context, ZMQ_SUB);<br />
assert(socket);<br />
/* Bind it to the system-assigned ephemeral port using a TCP transport */<br />
rc = zmq_bind(socket, &quot;tcp://127.0.0.1:*&quot;);<br />
assert(rc == 0);<br />
/* Obtain real endpoint */<br />
const size_t buf_size = 32;<br />
char buf[buf_size];<br />
rc = zmq_getsockopt(socket, ZMQ_LAST_ENDPOINT, buf, (size_t *)&amp;buf_size);<br />
assert(rc == 0);<br />
/* Unbind socket by real endpoint */<br />
rc = zmq_unbind(socket, buf);<br />
assert(rc == 0);<br />
 <code>Unbind wild-card * binded socket</code>. </p>
<pre><code>/* Create a ZMQ_SUB socket */
void *socket = zmq_socket(context, ZMQ_SUB);
assert(socket);
/* Bind it to the system-assigned ephemeral port using a TCP transport */
rc = zmq_bind(socket, &quot;tcp://127.0.0.1:*&quot;);
assert(rc == 0);
/* Obtain real endpoint */
const size_t buf_size = 32;
char buf[buf_size];
rc = zmq_getsockopt(socket, ZMQ_LAST_ENDPOINT, buf, (size_t *)&amp;buf_size);
assert(rc == 0);
/* Unbind socket by real endpoint */
rc = zmq_unbind(socket, buf);
assert(rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
