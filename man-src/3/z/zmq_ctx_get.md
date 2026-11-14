---
title: "zmq_ctx_get(3)"
name: "zmq_ctx_get"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_ctx_get/"
description: "zmq_ctx_get – get context options"
---

<p>zmq_ctx_get &#8211; get context options</p>
<h2>Synopsis</h2>
<pre><code>int zmq_ctx_get(void *context, int option_name);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_ctx_get()</i> function shall return the option specified by the <i>option_name</i> argument. </p>
<p> The <i>zmq_ctx_get()</i> function accepts the following option names:</p>
<h3>ZMQ_IO_THREADS: Get number of I/O threads</h3>
<p>The <i>ZMQ_IO_THREADS</i> argument returns the size of the 0MQ thread pool for this context.</p>
<h3>ZMQ_MAX_SOCKETS: Get maximum number of sockets</h3>
<p>The <i>ZMQ_MAX_SOCKETS</i> argument returns the maximum number of sockets allowed for this context.</p>
<h3>ZMQ_SOCKET_LIMIT: Get largest configurable number of sockets</h3>
<p>The <i>ZMQ_SOCKET_LIMIT</i> argument returns the largest number of sockets that <code><a href="/docs/linux/man/3-zmq_ctx_set/">zmq_ctx_set</a></code>(3) will accept.</p>
<h3>ZMQ_IPV6: Set IPv6 option</h3>
<p>The <i>ZMQ_IPV6</i> argument returns the IPv6 option for the context.</p>
<h2>Return Value</h2>
<p>The <i>zmq_ctx_get()</i> function returns a value of 0 or greater if successful. Otherwise it returns -1 and sets <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The requested option <i>option_name</i> is unknown.</dl>
<h2>Example</h2>
<p><code>Setting a limit on the number of sockets</code>. </p>
<pre><code>void *context = zmq_ctx_new();
zmq_ctx_set(context, ZMQ_MAX_SOCKETS, 256);
int max_sockets = zmq_ctx_get(context, ZMQ_MAX_SOCKETS);
assert(max_sockets == 256);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_ctx_set/">zmq_ctx_set</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
