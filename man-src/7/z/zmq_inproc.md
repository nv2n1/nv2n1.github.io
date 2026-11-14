---
title: "zmq_inproc(7)"
name: "zmq_inproc"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq_inproc/"
description: "zmq_inproc – 0MQ local in-process (inter-thread) communication transport"
---

<p>zmq_inproc &#8211; 0MQ local in-process (inter-thread) communication transport</p>
<h2>Synopsis</h2>
<p>The in-process transport passes messages via memory directly between threads sharing a single 0MQ <i>context</i>.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 No I/O threads are involved in passing messages using the <i>inproc</i> transport. Therefore, if you are using a 0MQ <i>context</i> for in-process messaging only you can initialise the <i>context</i> with zero I/O threads. See <code><a href="/docs/linux/man/3-zmq_init/">zmq_init</a></code>(3) for details. </p>
<h2>Addressing</h2>
<p>A 0MQ endpoint is a string consisting of a <i>transport</i>:// followed by an <i>address</i>. The <i>transport</i> specifies the underlying protocol to use. The <i>address</i> specifies the transport-specific address to connect to. </p>
<p> For the in-process transport, the transport is inproc, and the meaning of the <i>address</i> part is defined below.</p>
<h3>Assigning a local address to a socket</h3>
<p>When assigning a local address to a <i>socket</i> using <i>zmq_bind()</i> with the <i>inproc</i> transport, the <i>endpoint</i> shall be interpreted as an arbitrary string identifying the <i>name</i> to create. The <i>name</i> must be unique within the 0MQ <i>context</i> associated with the <i>socket</i> and may be up to 256 characters in length. No other restrictions are placed on the format of the <i>name</i>.</p>
<h3>Connecting a socket</h3>
<p>When connecting a <i>socket</i> to a peer address using <i>zmq_connect()</i> with the <i>inproc</i> transport, the <i>endpoint</i> shall be interpreted as an arbitrary string identifying the <i>name</i> to connect to. The <i>name</i> must have been previously created by assigning it to at least one <i>socket</i> within the same 0MQ <i>context</i> as the <i>socket</i> being connected.</p>
<h2>Examples</h2>
<p><code>Assigning a local address to a socket</code>. </p>
<pre><code>//  Connect to the in-process name &quot;#1&quot;
rc = zmq_connect(socket, &quot;inproc://#1&quot;);
assert (rc == 0);
//  Connect to the in-process name &quot;my-endpoint&quot;
rc = zmq_connect(socket, &quot;inproc://my-endpoint&quot;);
assert (rc == 0);
</code></pre>
<p> <code>Connecting a socket</code>. </p>
<pre><code>//  Connect to the in-process name &quot;#1&quot;
rc = zmq_connect(socket, &quot;inproc://#1&quot;);
assert (rc == 0);
//  Connect to the in-process name &quot;my-endpoint&quot;
rc = zmq_connect(socket, &quot;inproc://my-endpoint&quot;);
assert (rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7) <code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7) <code><a href="/docs/linux/man/7-zmq_pgm/">zmq_pgm</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
