---

title: "zmq_proxy_steerable(3)"
name: "zmq_proxy_steerable"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_proxy_steerable/"
description: "zmq_proxy_steerable – built-in 0MQ proxy with control flow"
---

<p>zmq_proxy_steerable &#8211; built-in 0MQ proxy with control flow </p>
<p> <code>int zmq_proxy_steerable (const void </code><i>*frontend</i><code>, const void </code><i>*backend</i><code>, const void </code><i>*capture</i><code>, const void </code><i>*control</i><code>);</code>  </p>
<p>The <i>zmq_proxy_steerable()</i> function starts the built-in 0MQ proxy in the current application thread, as <i>zmq_proxy()</i> do. Please, refer to this function for the general description and usage. We describe here only the additional control flow provided by the socket passed as the fourth argument &quot;control&quot;. </p>
<p>If the control socket is not NULL, the proxy supports control flow. If <i>PAUSE</i> is received on this socket, the proxy suspends its activities. If <i>RESUME</i> is received, it goes on. If <i>TERMINATE</i> is received, it terminates smoothly. At start, the proxy runs normally as if zmq_proxy was used. </p>
<p>If the control socket is NULL, the function behave exactly as if zmq_proxy had been called. </p>
<p>Refer to <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for a description of the available socket types. Refer to <code><a href="/docs/linux/man/3-zmq_proxy/">zmq_proxy</a></code>(3) for a description of the zmq_proxy.  </p>
<h2>EXAMPLE USAGE</h2>
<p>cf zmq_proxy  </p>
<h2>RETURN VALUE</h2>
<p>The <i>zmq_proxy_steerable()</i> function returns 0 if TERMINATE is sent to its control socket. Otherwise, it returns -1 and <i>errno</i> set to <code>ETERM</code> (the 0MQ <i>context</i> associated with either of the specified sockets was terminated).  </p>
<h2>EXAMPLE</h2>
<p> <code>Creating a shared queue proxy</code>. </p>
<dl>
<dd> <pre><code>// Create frontend, backend and control sockets
void *frontend = zmq_socket (context, ZMQ_ROUTER);
assert (backend);
void *backend = zmq_socket (context, ZMQ_DEALER);
assert (frontend);
void *control = zmq_socket (context, ZMQ_SUB);
assert (control);
// Bind sockets to TCP ports
assert (zmq_bind (frontend, &quot;tcp://*:5555&quot;) == 0);
assert (zmq_bind (backend, &quot;tcp://*:5556&quot;) == 0);
assert (zmq_connect (control, &quot;tcp://*:5557&quot;) == 0);
// Subscribe to the control socket since we have chosen SUB here
assert (zmq_setsockopt (control, ZMQ_SUBSCRIBE, &quot;&quot;, 0));
// Start the queue proxy, which runs until ETERM or &quot;TERMINATE&quot;
// received on the control socket
zmq_proxy_steerable (frontend, backend, NULL, control);
</code></pre>
 </dd></dl>
<p> <code>Set up a controller in another node, process or whatever</code>. </p>
<dl>
<dd> <pre><code>void *control = zmq_socket (context, ZMQ_PUB);
assert (control);
assert (zmq_bind (control, &quot;tcp://*:5557&quot;) == 0);
// pause the proxy
assert (zmq_send (control, &quot;PAUSE&quot;, 5, 0) == 0);
// resume the proxy
assert (zmq_send (control, &quot;RESUME&quot;, 6, 0) == 0);
// terminate the proxy
assert (zmq_send (control, &quot;TERMINATE&quot;, 9, 0) == 0);
---
SEE ALSO
</code></pre>
 </dd></dl>
<p> <code><a href="/docs/linux/man/3-zmq_proxy/">zmq_proxy</a></code>(3) <code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)  </p>
<h2>AUTHORS</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[]. </p>
