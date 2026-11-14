---
title: "zmq_msg_size(3)"
name: "zmq_msg_size"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_size/"
description: "zmq_msg_size – retrieve message content size in bytes"
---

<p>zmq_msg_size &#8211; retrieve message content size in bytes</p>
<h2>Synopsis</h2>
<pre><code>size_t zmq_msg_size (zmq_msg_t *msg);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_size()</i> function shall return the size in bytes of the content of the message object referenced by <i>msg</i>.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. </p>
<h2>Return Value</h2>
<p>Upon successful completion, <i>zmq_msg_size()</i> shall return the size of the message content in bytes.</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_data/">zmq_msg_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
