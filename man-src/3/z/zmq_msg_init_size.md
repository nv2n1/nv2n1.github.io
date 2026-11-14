---
title: "zmq_msg_init_size(3)"
name: "zmq_msg_init_size"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_init_size/"
description: "zmq_msg_init_size – initialise 0MQ message of a specified size"
---

<p>zmq_msg_init_size &#8211; initialise 0MQ message of a specified size</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_init_size(zmq_msg_t *msg, size_t size);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_init_size()</i> function shall allocate any resources required to store a message <i>size</i> bytes long and initialise the message object referenced by <i>msg</i> to represent the newly allocated message. The implementation shall choose whether to store message content on the stack (small messages) or on the heap (large messages). For performance reasons <i>zmq_msg_init_size()</i> shall not clear the message data.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The functions <i>zmq_msg_init()</i>, <i>zmq_msg_init_data()</i> and <i>zmq_msg_init_size()</i> are mutually exclusive. Never initialize the same <i>zmq_msg_t</i> twice. </p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_init_size()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>ENOMEM</code></p>
<dl>
<dd>Insufficient storage space is available.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_data/">zmq_msg_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_size/">zmq_msg_size</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
