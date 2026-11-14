---
title: "zmq_tipc(7)"
name: "zmq_tipc"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq_tipc/"
description: "zmq_tipc – 0MQ unicast transport using TIPC"
---

<p>zmq_tipc &#8211; 0MQ unicast transport using TIPC</p>
<h2>Synopsis</h2>
<p>TIPC is a cluster IPC protocol with a location transparent addressing scheme.</p>
<h2>Addressing</h2>
<p>A 0MQ endpoint is a string consisting of a <i>transport</i>:// followed by an <i>address</i>. The <i>transport</i> specifies the underlying protocol to use. The <i>address</i> specifies the transport-specific address to connect to. </p>
<p> For the TIPC transport, the transport is tipc, and the meaning of the <i>address</i> part is defined below. </p>
<p> Assigning a port name to a socket </p>
<dl>
<dd>
<pre>When assigning a port name to a socket using _zmq_bind()_ with the 'tipc'
transport, the 'endpoint' is defined in the form:
{type, lower, upper}
* Type is the numerical (u32) ID of your service.
* Lower and Upper specify a range for your service.
Publishing the same service with overlapping lower/upper ID's will
cause connection requests to be distributed over these in a round-robin
manner.
Connecting a socket</pre>
</dl>
<p> When connecting a socket to a peer address using <i>zmq_connect()</i> with the <i>tipc</i> transport, the <i>endpoint</i> shall be interpreted as a service ID, followed by a comma and the instance ID. </p>
<p> The instance ID must be within the lower/upper range of a published port name for the endpoint to be valid.</p>
<h2>Examples</h2>
<p><code>Assigning a local address to a socket</code>. </p>
<pre><code>//  Publish TIPC service ID 5555
rc = zmq_bind(socket, &quot;tipc://{5555,0,0}&quot;);
assert (rc == 0);
//  Publish TIPC service ID 5555 with a service range of 0-100
rc = zmq_bind(socket, &quot;tipc://{5555,0,100}&quot;);
assert (rc == 0);</code></pre>
<p> <code>Connecting a socket</code>. </p>
<pre><code>//  Connect to service 5555 instance id 50
rc = zmq_connect(socket, &quot;tipc://{5555,50}&quot;);
assert (rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7) <code><a href="/docs/linux/man/7-zmq_pgm/">zmq_pgm</a></code>(7) <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7) <code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
