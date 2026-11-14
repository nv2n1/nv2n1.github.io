---
title: "zmq_ctx_new(3)"
name: "zmq_ctx_new"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_ctx_new/"
description: "zmq_ctx_new – create new 0MQ context"
---

<p>zmq_ctx_new &#8211; create new 0MQ context</p>
<h2>Synopsis</h2>
<pre><code>void *zmq_ctx_new();</code></pre>
<h2>Description</h2>
<p>The <i>zmq_ctx_new()</i> function creates a new 0MQ <i>context</i>. </p>
<p> This function replaces the deprecated function <code><a href="/docs/linux/man/3-zmq_init/">zmq_init</a></code>(3). </p>
<p> <code>Thread safety</code>. A 0MQ <i>context</i> is thread safe and may be shared among as many application threads as necessary, without any additional locking required on the part of the caller.</p>
<h2>Return Value</h2>
<p>The <i>zmq_ctx_new()</i> function shall return an opaque handle to the newly created <i>context</i> if successful. Otherwise it shall return NULL and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p>No error values are defined for this function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7) <code><a href="/docs/linux/man/3-zmq_ctx_set/">zmq_ctx_set</a></code>(3) <code><a href="/docs/linux/man/3-zmq_ctx_get/">zmq_ctx_get</a></code>(3) <code><a href="/docs/linux/man/3-zmq_ctx_term/">zmq_ctx_term</a></code>(3)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
