---
title: "zmq_proxy(3)"
name: "zmq_proxy"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_proxy/"
description: "zmq_proxy – start built-in 0MQ proxy"
---

<p>zmq_proxy &#8211; start built-in 0MQ proxy</p>
<h2>Synopsis</h2>
<pre><code>int zmq_proxy(const void *frontend, const void *backend, const void *capture);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_proxy()</i> function starts the built-in 0MQ proxy in the current application thread. </p>
<p> The proxy connects a frontend socket to a backend socket. Conceptually, data flows from frontend to backend. Depending on the socket types, replies may flow in the opposite direction. The direction is conceptual only; the proxy is fully symmetric and there is no technical difference between frontend and backend. </p>
<p> Before calling <i>zmq_proxy()</i> you must set any socket options, and connect or bind both frontend and backend sockets. The two conventional proxy models are: </p>
<p> <i>zmq_proxy()</i> runs in the current thread and returns only if/when the current context is closed. </p>
<p> If the capture socket is not NULL, the proxy shall send all messages, received on both frontend and backend, to the capture socket. The capture socket should be a <i>ZMQ_PUB</i>, <i>ZMQ_DEALER</i>, <i>ZMQ_PUSH</i>, or <i>ZMQ_PAIR</i> socket. </p>
<p> Refer to <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for a description of the available socket types.</p>
<h2>Example Usage</h2>
<h3>Shared Queue</h3>
<p>When the frontend is a ZMQ_ROUTER socket, and the backend is a ZMQ_DEALER socket, the proxy shall act as a shared queue that collects requests from a set of clients, and distributes these fairly among a set of services. Requests shall be fair-queued from frontend connections and distributed evenly across backend connections. Replies shall automatically return to the client that made the original request.</p>
<h3>Forwarder</h3>
<p>When the frontend is a ZMQ_XSUB socket, and the backend is a ZMQ_XPUB socket, the proxy shall act as a message forwarder that collects messages from a set of publishers and forwards these to a set of subscribers. This may be used to bridge networks transports, e.g. read on tcp:// and forward on <a href="pgm://.">pgm://.</a></p>
<h3>Streamer</h3>
<p>When the frontend is a ZMQ_PULL socket, and the backend is a ZMQ_PUSH socket, the proxy shall collect tasks from a set of clients and forwards these to a set of workers using the pipeline pattern.</p>
<h2>Return Value</h2>
<p>The <i>zmq_proxy()</i> function always returns -1 and <i>errno</i> set to <code>ETERM</code> (the 0MQ <i>context</i> associated with either of the specified sockets was terminated).</p>
<h2>Example</h2>
<p><code>Creating a shared queue proxy</code>. </p>
<pre><code>//  Create frontend and backend sockets
void *frontend = zmq_socket(context, ZMQ_ROUTER);
assert(backend);
void *backend = zmq_socket(context, ZMQ_DEALER);
assert(frontend);
//  Bind both sockets to TCP ports
assert(zmq_bind(frontend, &quot;tcp://*:5555&quot;) == 0);
assert(zmq_bind(backend, &quot;tcp://*:5556&quot;) == 0);
//  Start the queue proxy, which runs until ETERM
zmq_proxy(frontend, backend, NULL);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
