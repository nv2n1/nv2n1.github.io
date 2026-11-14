---
title: "zmq_msg_send(3)"
name: "zmq_msg_send"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_send/"
description: "zmq_msg_send – send a message part on a socket"
---

<p>zmq_msg_send &#8211; send a message part on a socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_send(zmq_msg_t *msg, void *socket, int flags);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_send()</i> function is identical to <code><a href="/docs/linux/man/3-zmq_sendmsg/">zmq_sendmsg</a></code>(3), which shall be deprecated in future versions. <i>zmq_msg_send()</i> is more consistent with other message manipulation functions. </p>
<p> The <i>zmq_msg_send()</i> function shall queue the message referenced by the <i>msg</i> argument to be sent to the socket referenced by the <i>socket</i> argument. The <i>flags</i> argument is a combination of the flags defined below: </p>
<p> <code>ZMQ_DONTWAIT</code></p>
<dl>
<dd>For socket types (DEALER, PUSH) that block when there are no available peers (or all peers have full high-water mark), specifies that the operation should be performed in non-blocking mode. If the message cannot be queued on the <i>socket</i>, the <i>zmq_msg_send()</i> function shall fail with <i>errno</i> set to EAGAIN.</dl>
<p> <code>ZMQ_SNDMORE</code></p>
<dl>
<dd>Specifies that the message being sent is a multi-part message, and that further message parts are to follow. Refer to the section regarding multi-part messages below for a detailed description.</dl>
<p> The <i>zmq_msg_t</i> structure passed to <i>zmq_msg_send()</i> is nullified during the call. If you want to send the same message to multiple sockets you have to copy it using (e.g. using <i>zmq_msg_copy()</i>). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> A successful invocation of <i>zmq_msg_send()</i> does not indicate that the message has been transmitted to the network, only that it has been queued on the <i>socket</i> and 0MQ has assumed responsibility for the message. You do not need to call <i>zmq_msg_close()</i> after a successful <i>zmq_msg_send()</i>. </p>
</dl>
<h3>Multi-part messages</h3>
<p>A 0MQ message is composed of 1 or more message parts. Each message part is an independent <i>zmq_msg_t</i> in its own right. 0MQ ensures atomic delivery of messages: peers shall receive either all <i>message parts</i> of a message or none at all. The total number of message parts is unlimited except by available memory. </p>
<p> An application that sends multi-part messages must use the <i>ZMQ_SNDMORE</i> flag when sending each message part except the final one.</p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_send()</i> function shall return number of bytes in the message if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EAGAIN</code></p>
<dl>
<dd>Non-blocking mode was requested and the message cannot be sent at the moment.</dl>
<p> <code>ENOTSUP</code></p>
<dl>
<dd>The <i>zmq_msg_send()</i> operation is not supported by this socket type.</dl>
<p> <code>EFSM</code></p>
<dl>
<dd>The <i>zmq_msg_send()</i> operation cannot be performed on this socket at the moment due to the socket not being in the appropriate state. This error may occur with socket types that switch between several states, such as ZMQ_REP. See the <i>messaging patterns</i> section of <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for more information.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
<p> <code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<p> <code>EINTR</code></p>
<dl>
<dd>The operation was interrupted by delivery of a signal before the message was sent.</dl>
<p> <code>EFAULT</code></p>
<dl>
<dd>Invalid message.</dl>
<p> <code>EHOSTUNREACH</code></p>
<dl>
<dd>The message cannot be routed.</dl>
<h2>Example</h2>
<p><code>Filling in a message and sending it to a socket</code>. /* Send a multi-part message consisting of three parts to socket */<br />
rc = zmq_msg_send (&amp;part1, socket, ZMQ_SNDMORE);<br />
rc = zmq_msg_send (&amp;part2, socket, ZMQ_SNDMORE);<br />
/* Final part; no more parts to follow */<br />
rc = zmq_msg_send (&amp;part3, socket, 0);<br />
 <code>Sending a multi-part message</code>. </p>
<pre><code>/* Send a multi-part message consisting of three parts to socket */
rc = zmq_msg_send (&amp;part1, socket, ZMQ_SNDMORE);
rc = zmq_msg_send (&amp;part2, socket, ZMQ_SNDMORE);
/* Final part; no more parts to follow */
rc = zmq_msg_send (&amp;part3, socket, 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3) <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_recv/">zmq_msg_recv</a></code>(3) <code><a href="/docs/linux/man/7-zmq_socket/">zmq_socket</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
