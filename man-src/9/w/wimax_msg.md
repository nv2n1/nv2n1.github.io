---
title: "wimax_msg(9)"
name: "wimax_msg"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_msg/"
description: "wimax_msg – Send a message to user space"
---

<p>wimax_msg &#8211; Send a message to user space</p>
<h2>Synopsis</h2>
<pre><code>int wimax_msg(struct wimax_dev *wimax_dev, const char *pipe_name, const void *buf, size_t size, gfp_t gfp_flags);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor (properly referenced)</dl>
<p> <i>pipe_name</i></p>
<dl>
<dd>&quot;named pipe&quot; the message will be sent to</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to the message to send.</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the buffer pointed to by <i>buf</i> (in bytes).</dl>
<p> <i>gfp_flags</i></p>
<dl>
<dd>flags for memory allocation.</dl>
<h2>Return</h2>
<p><code>0</code> if ok, negative errno code on error.</p>
<h2>Description</h2>
<p>Sends a free-form message to user space on the device <i>wimax_dev</i>.</p>
<h2>Notes</h2>
<p>Once the <i>skb</i> is given to this function, who will own it and will release it when done (unless it returns error).</p>
<h2>Copyright</h2>
