---
title: "zmq_ctx_set(3)"
name: "zmq_ctx_set"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_ctx_set/"
description: "zmq_ctx_set – set context options"
---

<p>zmq_ctx_set &#8211; set context options</p>
<h2>Synopsis</h2>
<pre><code>int zmq_ctx_set(void *context, int option_name, int option_value);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_ctx_set()</i> function shall set the option specified by the <i>option_name</i> argument to the value of the <i>option_value</i> argument. The <i>zmq_ctx_set()</i> function accepts the following options:</p>
<h3>ZMQ_IO_THREADS: Set number of I/O threads</h3>
<p>The <i>ZMQ_IO_THREADS</i> argument specifies the size of the 0MQ thread pool to handle I/O operations. If your application is using only the <i>inproc</i> transport for messaging you may set this to zero, otherwise set it to at least one. This option only applies before creating any sockets on the context. </p>
<table>
<tr VALIGN=top>
<td> Default value </td>
<td> 1
</td>
</tr>
</table>
<h3>ZMQ_THREAD_SCHED_POLICY: Set scheduling policy for I/O threads</h3>
<p>The <i>ZMQ_THREAD_SCHED_POLICY</i> argument sets the scheduling policy for internal context&#8217;s thread pool. This option is not available on windows. Supported values for this option can be found in sched.h file, or at m[blue]<code><a rel="nofollow" href="http://man7.org/linux/man-pages/man2/sched_setscheduler.2.html">http://man7.org/linux/man-pages/man2/sched_setscheduler.2.html</a></code>m[]. This option only applies before creating any sockets on the context. </p>
<table>
<tr VALIGN=top>
<td> Default value </td>
<td> -1
</td>
</tr>
</table>
<h3>ZMQ_THREAD_PRIORITY: Set scheduling priority for I/O threads</h3>
<p>The <i>ZMQ_THREAD_PRIORITY</i> argument sets scheduling priority for internal context&#8217;s thread pool. This option is not available on windows. Supported values for this option depend on chosen scheduling policy. Details can be found in sched.h file, or at m[blue]<code><a rel="nofollow" href="http://man7.org/linux/man-pages/man2/sched_setscheduler.2.html">http://man7.org/linux/man-pages/man2/sched_setscheduler.2.html</a></code>m[]. This option only applies before creating any sockets on the context. </p>
<table>
<tr VALIGN=top>
<td> Default value </td>
<td> -1
</td>
</tr>
</table>
<h3>ZMQ_MAX_SOCKETS: Set maximum number of sockets</h3>
<p>The <i>ZMQ_MAX_SOCKETS</i> argument sets the maximum number of sockets allowed on the context. You can query the maximal allowed value with <code><a href="/docs/linux/man/3-zmq_ctx_get/">zmq_ctx_get</a></code>(3) using the <i>ZMQ_SOCKET_LIMIT</i> option. </p>
<table>
<tr VALIGN=top>
<td> Default value </td>
<td> 1024
</td>
</tr>
</table>
<h3>ZMQ_IPV6: Set IPv6 option</h3>
<p>The <i>ZMQ_IPV6</i> argument sets the IPv6 value for all sockets created in the context from this point onwards. A value of 1 means IPv6 is enabled, while 0 means the socket will use only IPv4. When IPv6 is enabled, a socket will connect to, or accept connections from, both IPv4 and IPv6 hosts. </p>
<table>
<tr VALIGN=top>
<td> Default value </td>
<td> 0
</td>
</tr>
</table>
<h2>Return Value</h2>
<p>The <i>zmq_ctx_set()</i> function returns zero if successful. Otherwise it returns -1 and sets <i>errno</i> to one of the values defined below.</p>
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
<p><code><a href="/docs/linux/man/3-zmq_ctx_get/">zmq_ctx_get</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
