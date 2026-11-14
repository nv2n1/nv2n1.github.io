---
title: "zmq_recvmsg(3)"
name: "zmq_recvmsg"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_recvmsg/"
description: "zmq_recvmsg – receive a message part from a socket"
---

<p>zmq_recvmsg &#8211; receive a message part from a socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_recvmsg(void *socket, zmq_msg_t *msg, int flags);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_recvmsg()</i> function shall receive a message part from the socket referenced by the <i>socket</i> argument and store it in the message referenced by the <i>msg</i> argument. Any content previously stored in <i>msg</i> shall be properly deallocated. If there are no message parts available on the specified <i>socket</i> the <i>zmq_recvmsg()</i> function shall block until the request can be satisfied. The <i>flags</i> argument is a combination of the flags defined below: </p>
<p> <code>ZMQ_DONTWAIT</code></p>
<dl>
<dd>Specifies that the operation should be performed in non-blocking mode. If there are no messages available on the specified <i>socket</i>, the <i>zmq_recvmsg()</i> function shall fail with <i>errno</i> set to EAGAIN.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> this API method is deprecated in favor of <a href="/docs/linux/man/3-zmq_msg_recv/">zmq_msg_recv</a>(3). </p>
</dl>
<h3>Multi-part messages</h3>
<p>A 0MQ message is composed of 1 or more message parts. Each message part is an independent <i>zmq_msg_t</i> in its own right. 0MQ ensures atomic delivery of messages: peers shall receive either all <i>message parts</i> of a message or none at all. The total number of message parts is unlimited except by available memory. </p>
<p> An application that processes multi-part messages must use the <i>ZMQ_RCVMORE</i> <code><a href="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></code>(3) option after calling <i>zmq_recvmsg()</i> to determine if there are further parts to receive.</p>
<h2>Return Value</h2>
<p>The <i>zmq_recvmsg()</i> function shall return number of bytes in the message if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EAGAIN</code></p>
<dl>
<dd>Non-blocking mode was requested and no messages are available at the moment.</dl>
<p> <code>ENOTSUP</code></p>
<dl>
<dd>The <i>zmq_recvmsg()</i> operation is not supported by this socket type.</dl>
<p> <code>EFSM</code></p>
<dl>
<dd>The <i>zmq_recvmsg()</i> operation cannot be performed on this socket at the moment due to the socket not being in the appropriate state. This error may occur with socket types that switch between several states, such as ZMQ_REP. See the <i>messaging patterns</i> section of <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for more information.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
<p> <code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<p> <code>EINTR</code></p>
<dl>
<dd>The operation was interrupted by delivery of a signal before a message was available.</dl>
<p> <code>EFAULT</code></p>
<dl>
<dd>The message passed to the function was invalid.</dl>
<h2>Example</h2>
<p><code>Receiving a message from a socket</code>. int more;<br />
size_t more_size = sizeof(more);<br />
do {<br />
    /* Create an empty 0MQ message to hold the message part */<br />
    zmq_msg_t part;<br />
    int rc = zmq_msg_init(&amp;part);<br />
    assert(rc == 0);<br />
    /* Block until a message is available to be received from socket */<br />
    rc = zmq_recvmsg(socket, &amp;part, 0);<br />
    assert(rc != -1);<br />
    /* Determine if more message parts are to follow */<br />
    rc = zmq_getsockopt(socket, ZMQ_RCVMORE, &amp;more, &amp;more_size);<br />
    assert(rc == 0);<br />
    zmq_msg_close(&amp;part);<br />
} while (more);<br />
 <code>Receiving a multi-part message</code>. </p>
<pre><code>int more;
size_t more_size = sizeof(more);
do {
    /* Create an empty 0MQ message to hold the message part */
    zmq_msg_t part;
    int rc = zmq_msg_init(&amp;part);
    assert(rc == 0);
    /* Block until a message is available to be received from socket */
    rc = zmq_recvmsg(socket, &amp;part, 0);
    assert(rc != -1);
    /* Determine if more message parts are to follow */
    rc = zmq_getsockopt(socket, ZMQ_RCVMORE, &amp;more, &amp;more_size);
    assert(rc == 0);
    zmq_msg_close(&amp;part);
} while (more);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3) <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) <code><a href="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></code>(3) <code><a href="/docs/linux/man/7-zmq_socket/">zmq_socket</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
