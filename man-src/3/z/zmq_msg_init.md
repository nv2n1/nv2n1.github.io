---
title: "zmq_msg_init(3)"
name: "zmq_msg_init"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_init/"
description: "zmq_msg_init – initialise empty 0MQ message"
---

<p>zmq_msg_init &#8211; initialise empty 0MQ message</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_init(zmq_msg_t *msg);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_init()</i> function shall initialise the message object referenced by <i>msg</i> to represent an empty message. This function is most useful when called before receiving a message with <i>zmq_recv()</i>.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The functions <i>zmq_msg_init()</i>, <i>zmq_msg_init_data()</i> and <i>zmq_msg_init_size()</i> are mutually exclusive. Never initialize the same <i>zmq_msg_t</i> twice. </p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_init()</i> function always returns zero.</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>Example</h2>
<p><code>Receiving a message from a socket</code>. </p>
<pre><code>zmq_msg_t msg;
rc = zmq_msg_init(&amp;msg);
assert(rc == 0);
int nbytes = zmq_recv(socket, &amp;msg, 0);
assert(nbytes != -1);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_data/">zmq_msg_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_size/">zmq_msg_size</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
