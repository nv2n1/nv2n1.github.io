---
title: "zmq_disconnect(3)"
name: "zmq_disconnect"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_disconnect/"
description: "zmq_disconnect – Disconnect a socket"
---

<p>zmq_disconnect &#8211; Disconnect a socket</p>
<h2>Synopsis</h2>
<pre><code>int zmq_disconnect(void *socket, const char *endpoint);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_disconnect()</i> function shall disconnect a socket specified by the <i>socket</i> argument from the endpoint specified by the <i>endpoint</i> argument. Any outstanding messages physically received from the network but not yet received by the application with <i>zmq_recv()</i> shall be discarded. The behaviour for discarding messages sent by the application with <i>zmq_send()</i> but not yet physically transferred to the network depends on the value of the <i>ZMQ_LINGER</i> socket option for the specified <i>socket</i>. The <i>endpoint</i> argument is as described in <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3)</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The default setting of <i>ZMQ_LINGER</i> does not discard unsent messages; this behaviour may cause the application to block when calling <i>zmq_term()</i>. For details refer to <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) and <code><a href="/docs/linux/man/3-zmq_term/">zmq_term</a></code>(3). </p>
<h2>Return Value</h2>
<p>The <i>zmq_disconnect()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
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
<p> <code>ENOENT</code></p>
<dl>
<dd>The provided endpoint is not connected.</dl>
<h2>Example</h2>
<p><code>Connecting a subscriber socket to an in-process and a TCP transport</code>. </p>
<pre><code>/* Create a ZMQ_SUB socket */
void *socket = zmq_socket(context, ZMQ_SUB);
assert(socket);
/* Connect it to the host server001, port 5555 using a TCP transport */
rc = zmq_connect(socket, &quot;tcp://server001:5555&quot;);
assert(rc == 0);
/* Disconnect from the previously connected endpoint */
rc = zmq_disconnect(socket, &quot;tcp://server001:5555&quot;);
assert(rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
