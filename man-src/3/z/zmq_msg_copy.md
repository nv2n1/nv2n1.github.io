---
title: "zmq_msg_copy(3)"
name: "zmq_msg_copy"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_copy/"
description: "zmq_msg_copy – copy content of a message to another message"
---

<p>zmq_msg_copy &#8211; copy content of a message to another message</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_copy(zmq_msg_t *dest, zmq_msg_t *src);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_copy()</i> function shall copy the message object referenced by <i>src</i> to the message object referenced by <i>dest</i>. The original content of <i>dest</i>, if any, shall be released. You must initialize <i>dest</i> before copying to it.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The implementation may choose not to physically copy the message content, rather to share the underlying buffer between <i>src</i> and <i>dest</i>. Avoid modifying message content after a message has been copied with <i>zmq_msg_copy()</i>, doing so can result in undefined behaviour. If what you need is an actual hard copy, allocate a new message using <i>zmq_msg_init_size()</i> and copy the message content using <i>memcpy()</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. </p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_copy()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EFAULT</code></p>
<dl>
<dd>Invalid message.</dl>
<h2>Example</h2>
<p><code>Copying a message</code>.</p>
<dl>
<dd>
<pre>zmq_msg_t msg;
zmq_msg_init_size (&amp;msg, 255);
memcpy (zmq_msg_data (&amp;msg, &quot;Hello, World&quot;, 12);
zmq_msg_t copy;
zmq_msg_init (&amp;copy);
zmq_msg_copy (&amp;copy, &amp;msg);
...
zmq_msg_close (&amp;copy);
zmq_msg_close (&amp;msg);</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_move/">zmq_msg_move</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
