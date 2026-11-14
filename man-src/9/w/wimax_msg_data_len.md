---
title: "wimax_msg_data_len(9)"
name: "wimax_msg_data_len"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_msg_data_len/"
description: "wimax_msg_data_len – Return a pointer and size of a message’s payload"
---

<p>wimax_msg_data_len &#8211; Return a pointer and size of a message&#8217;s payload</p>
<h2>Synopsis</h2>
<pre><code>const void *wimax_msg_data_len(struct sk_buff *msg, size_t *size);</code></pre>
<h2>Arguments</h2>
<p><i>msg</i></p>
<dl>
<dd>
<dd>Pointer to a message created with <code>wimax_msg_alloc</code></dl>
<p> <i>size</i></p>
<dl>
<dd>Pointer to where to store the message&#8217;s size</dl>
<h2>Description</h2>
<p>Returns the pointer to the message data.</p>
<h2>Copyright</h2>
