---
title: "zmq_has(3)"
name: "zmq_has"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_has/"
description: "zmq_has – check a ZMQ capability"
---

<p>zmq_has &#8211; check a ZMQ capability</p>
<h2>Synopsis</h2>
<pre><code>int zmq_has(const char *capability);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_has()</i> function shall report whether a specified capability is available in the library. This allows bindings and applications to probe a library directly, for transport and security options. </p>
<p> Capabilities shall be lowercase strings. The following capabilities are defined: </p>
<dl>
<dd>&bull; ipc &#8211; the library supports the ipc:// protocol</dl>
<dl>
<dd>&bull; pgm &#8211; the library supports the pgm:// protocol</dl>
<dl>
<dd>&bull; tipc &#8211; the library supports the tipc:// protocol</dl>
<dl>
<dd>&bull; norm &#8211; the library supports the norm:// protocol</dl>
<dl>
<dd>&bull; curve &#8211; the library supports the CURVE security mechanism</dl>
<dl>
<dd>&bull; gssapi &#8211; the library supports the GSSAPI security mechanism</dl>
<p> When this method is provided, the zmq.h header file will define ZMQ_HAS_CAPABILITIES.</p>
<h2>Return Value</h2>
<p>The <i>zmq_has()</i> function shall return 1 if the specified capability is provided. Otherwise it shall return 0.</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
