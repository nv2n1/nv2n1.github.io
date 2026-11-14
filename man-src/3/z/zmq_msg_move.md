---
title: "zmq_msg_move(3)"
name: "zmq_msg_move"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_move/"
description: "zmq_msg_move – move content of a message to another message"
---

<p>zmq_msg_move &#8211; move content of a message to another message</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_move(zmq_msg_t *dest, zmq_msg_t *src);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_move()</i> function shall move the content of the message object referenced by <i>src</i> to the message object referenced by <i>dest</i>. No actual copying of message content is performed, <i>dest</i> is simply updated to reference the new content. <i>src</i> becomes an empty message after calling <i>zmq_msg_move()</i>. The original content of <i>dest</i>, if any, shall be released.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. </p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_move()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EFAULT</code></p>
<dl>
<dd>Invalid message.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_copy/">zmq_msg_copy</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
