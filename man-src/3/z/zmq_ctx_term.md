---
title: "zmq_ctx_term(3)"
name: "zmq_ctx_term"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_ctx_term/"
description: "zmq_ctx_term – destroy a 0MQ context"
---

<p>zmq_ctx_term &#8211; destroy a 0MQ context</p>
<h2>Synopsis</h2>
<pre><code>int zmq_ctx_term(void *context);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_ctx_term()</i> function shall destroy the 0MQ context <i>context</i>. </p>
<p> Context termination is performed in the following steps: </p>
<dl>
<dd>1. Any blocking operations currently in progress on sockets open within <i>context</i> shall return immediately with an error code of ETERM. With the exception of <i>zmq_close()</i>, any further operations on sockets open within <i>context</i> shall fail with an error code of ETERM.</dl>
<dl>
<dd>2. After interrupting all blocking calls, <i>zmq_ctx_term()</i> shall <i>block</i> until the following conditions are satisfied: </p>
<dl>
<dd>&bull; All sockets open within <i>context</i> have been closed with <i>zmq_close()</i>.</dl>
<dl>
<dd>&bull; For each socket within <i>context</i>, all messages sent by the application with <i>zmq_send()</i> have either been physically transferred to a network peer, or the socket&#8217;s linger period set with the <i>ZMQ_LINGER</i> socket option has expired.</dl>
</dl>
<p> For further details regarding socket linger behavior refer to the <i>ZMQ_LINGER</i> option in <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3). </p>
<p> This function replaces the deprecated function <code><a href="/docs/linux/man/3-zmq_term/">zmq_term</a></code>(3).</p>
<h2>Warning</h2>
<p>As <i>ZMQ_LINGER</i> defaults to &quot;infinite&quot;, by default this function will block indefinitely if there are any pending connects or sends. We strongly recommend to (a) set <i>ZMQ_LINGER</i> to zero on all sockets and (b) close all sockets, before calling this function.</p>
<h2>Return Value</h2>
<p>The <i>zmq_ctx_term()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EFAULT</code></p>
<dl>
<dd>The provided <i>context</i> was invalid.</dl>
<p> <code>EINTR</code></p>
<dl>
<dd>Termination was interrupted by a signal. It can be restarted if needed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7) <code><a href="/docs/linux/man/3-zmq_init/">zmq_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_close/">zmq_close</a></code>(3) <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
