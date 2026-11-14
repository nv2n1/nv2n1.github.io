---
title: "zmq_recv(3)"
name: "zmq_recv"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_recv/"
description: "zmq_recv – receive a message part from a socket"
---

<p>zmq_recv &#8211; receive a message part from a socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_recv(void *socket, void *buf, size_t len, int flags);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_recv()</i> function shall receive a message from the socket referenced by the <i>socket</i> argument and store it in the buffer referenced by the <i>buf</i> argument. Any bytes exceeding the length specified by the <i>len</i> argument shall be truncated. If there are no messages available on the specified <i>socket</i> the <i>zmq_recv()</i> function shall block until the request can be satisfied. The <i>flags</i> argument is a combination of the flags defined below: </p>
<p> <code>ZMQ_DONTWAIT</code></p>
<dl>
<dd>Specifies that the operation should be performed in non-blocking mode. If there are no messages available on the specified <i>socket</i>, the <i>zmq_recv()</i> function shall fail with <i>errno</i> set to EAGAIN.</dl>
<h3>Multi-part messages</h3>
<p>A 0MQ message is composed of 1 or more message parts. 0MQ ensures atomic delivery of messages: peers shall receive either all <i>message parts</i> of a message or none at all. The total number of message parts is unlimited except by available memory. </p>
<p> An application that processes multi-part messages must use the <i>ZMQ_RCVMORE</i> <code><a href="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></code>(3) option after calling <i>zmq_recv()</i> to determine if there are further parts to receive.</p>
<h2>Return Value</h2>
<p>The <i>zmq_recv()</i> function shall return number of bytes in the message if successful. Note that the value can exceed the value of the <i>len</i> parameter in case the message was truncated. If not successful the function shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EAGAIN</code></p>
<dl>
<dd>Non-blocking mode was requested and no messages are available at the moment.</dl>
<p> <code>ENOTSUP</code></p>
<dl>
<dd>The <i>zmq_recv()</i> operation is not supported by this socket type.</dl>
<p> <code>EFSM</code></p>
<dl>
<dd>The <i>zmq_recv()</i> operation cannot be performed on this socket at the moment due to the socket not being in the appropriate state. This error may occur with socket types that switch between several states, such as ZMQ_REP. See the <i>messaging patterns</i> section of <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for more information.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
<p> <code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<p> <code>EINTR</code></p>
<dl>
<dd>The operation was interrupted by delivery of a signal before a message was available.</dl>
<h2>Example</h2>
<p><code>Receiving a message from a socket</code>. </p>
<pre><code>char buf[256];
nbytes = zmq_recv(socket, buf, 256, 0);
assert(nbytes != -1);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) <code><a href="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></code>(3) <code><a href="/docs/linux/man/7-zmq_socket/">zmq_socket</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
