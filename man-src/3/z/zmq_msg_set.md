---
title: "zmq_msg_set(3)"
name: "zmq_msg_set"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_set/"
description: "zmq_msg_set – set message property"
---

<p>zmq_msg_set &#8211; set message property</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_set(zmq_msg_t *message, int property, int value);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_set()</i> function shall set the property specified by the <i>property</i> argument to the value of the <i>value</i> argument for the 0MQ message fragment pointed to by the <i>message</i> argument. </p>
<p> Currently the <i>zmq_msg_set()</i> function does not support any property names.</p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_set()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The requested property <i>property</i> is unknown.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_get/">zmq_msg_get</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
