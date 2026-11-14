---
title: "zmq_ctx_shutdown(3)"
name: "zmq_ctx_shutdown"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_ctx_shutdown/"
description: "zmq_ctx_shutdown – shutdown a 0MQ context"
---

<p>zmq_ctx_shutdown &#8211; shutdown a 0MQ context</p>
<h2>Synopsis</h2>
<pre><code>int zmq_ctx_shutdown(void *context);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_ctx_shutdown()</i> function shall shutdown the 0MQ context <i>context</i>. </p>
<p> Context shutdown will cause any blocking operations currently in progress on sockets open within <i>context</i> to return immediately with an error code of ETERM. With the exception of <i>zmq_close()</i>, any further operations on sockets open within <i>context</i> shall fail with an error code of ETERM. </p>
<p> This function is optional, client code is still required to call the <code><a href="/docs/linux/man/3-zmq_ctx_term/">zmq_ctx_term</a></code>(3) function to free all resources allocated by zeromq.</p>
<h2>Return Value</h2>
<p>The <i>zmq_ctx_shutdown()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EFAULT</code></p>
<dl>
<dd>The provided <i>context</i> was invalid.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7) <code><a href="/docs/linux/man/3-zmq_init/">zmq_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_ctx_term/">zmq_ctx_term</a></code>(3) <code><a href="/docs/linux/man/3-zmq_close/">zmq_close</a></code>(3) <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
