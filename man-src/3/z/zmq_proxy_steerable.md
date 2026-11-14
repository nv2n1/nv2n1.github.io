---
title: "zmq_proxy_steerable(3)"
name: "zmq_proxy_steerable"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_proxy_steerable/"
description: "zmq_proxy_steerable – built-in 0MQ proxy with control flow"
---

<p>zmq_proxy_steerable &#8211; built-in 0MQ proxy with control flow</p>
<h2>Synopsis</h2>
<pre><code>int zmq_proxy_steerable(const void *frontend, const void *backend, const void *capture, const void *control);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_proxy_steerable()</i> function starts the built-in 0MQ proxy in the current application thread, as <i>zmq_proxy()</i> do. Please, refer to this function for the general description and usage. We describe here only the additional control flow provided by the socket passed as the fourth argument &quot;control&quot;. </p>
<p> If the control socket is not NULL, the proxy supports control flow. If <i>PAUSE</i> is received on this socket, the proxy suspends its activities. If <i>RESUME</i> is received, it goes on. If <i>TERMINATE</i> is received, it terminates smoothly. At start, the proxy runs normally as if zmq_proxy was used. </p>
<p> If the control socket is NULL, the function behave exactly as if zmq_proxy had been called. </p>
<p> Refer to <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for a description of the available socket types. Refer to <code><a href="/docs/linux/man/3-zmq_proxy/">zmq_proxy</a></code>(3) for a description of the zmq_proxy.</p>
<h2>Example Usage</h2>
<p>cf zmq_proxy</p>
<h2>Return Value</h2>
<p>The <i>zmq_proxy_steerable()</i> function returns 0 if TERMINATE is sent to its control socket. Otherwise, it returns -1 and <i>errno</i> set to <code>ETERM</code> (the 0MQ <i>context</i> associated with either of the specified sockets was terminated).</p>
<h2>Example</h2>
<p><code>Creating a shared queue proxy</code>. void *control = zmq_socket(context, ZMQ_PUB);<br />
assert(control);<br />
assert(zmq_bind(control, &quot;tcp://*:5557&quot;) == 0);</p>
<p>// pause the proxy<br />
assert(zmq_send(control, &quot;PAUSE&quot;, 5, 0) == 0);</p>
<p>// resume the proxy<br />
assert(zmq_send(control, &quot;RESUME&quot;, 6, 0) == 0);</p>
<p>// terminate the proxy<br />
assert(zmq_send(control, &quot;TERMINATE&quot;, 9, 0) == 0);<br />
&#8212; &#8211;</p>
<p>   SEE ALSO <code>Set up a controller in another node, process or whatever</code>. </p>
<pre><code>void *control = zmq_socket(context, ZMQ_PUB);
assert(control);
assert(zmq_bind(control, &quot;tcp://*:5557&quot;) == 0);

// pause the proxy
assert(zmq_send(control, &quot;PAUSE&quot;, 5, 0) == 0);

// resume the proxy
assert(zmq_send(control, &quot;RESUME&quot;, 6, 0) == 0);

// terminate the proxy
assert(zmq_send(control, &quot;TERMINATE&quot;, 9, 0) == 0);
-- -

   SEE ALSO</code></pre>
<p> <code><a href="/docs/linux/man/3-zmq_proxy/">zmq_proxy</a></code>(3) <code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
