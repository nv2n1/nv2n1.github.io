---
title: "zmq_close(3)"
name: "zmq_close"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_close/"
description: "zmq_close – close 0MQ socket"
---

<p>zmq_close &#8211; close 0MQ socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_close(void *socket);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_close()</i> function shall destroy the socket referenced by the <i>socket</i> argument. Any outstanding messages physically received from the network but not yet received by the application with <i>zmq_recv()</i> shall be discarded. The behaviour for discarding messages sent by the application with <i>zmq_send()</i> but not yet physically transferred to the network depends on the value of the <i>ZMQ_LINGER</i> socket option for the specified <i>socket</i>.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The default setting of <i>ZMQ_LINGER</i> does not discard unsent messages; this behaviour may cause the application to block when calling <i>zmq_term()</i>. For details refer to <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) and <code><a href="/docs/linux/man/3-zmq_term/">zmq_term</a></code>(3). </p>
<h2>Return Value</h2>
<p>The <i>zmq_close()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/3-zmq_term/">zmq_term</a></code>(3) <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
