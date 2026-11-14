---
title: "zmq_msg_close(3)"
name: "zmq_msg_close"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_close/"
description: "zmq_msg_close – release 0MQ message"
---

<p>zmq_msg_close &#8211; release 0MQ message</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_close(zmq_msg_t *msg);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_close()</i> function shall inform the 0MQ infrastructure that any resources associated with the message object referenced by <i>msg</i> are no longer required and may be released. Actual release of resources associated with the message object shall be postponed by 0MQ until all users of the message or underlying data buffer have indicated it is no longer required. Applications should ensure that <i>zmq_msg_close()</i> is called once a message is no longer required, otherwise memory leaks may occur. Note that this is NOT necessary after a successful <i>zmq_msg_send()</i>.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. </p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_close()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EFAULT</code></p>
<dl>
<dd>Invalid message.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_data/">zmq_msg_data</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_size/">zmq_msg_size</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
