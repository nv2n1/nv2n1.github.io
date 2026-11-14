---
title: "wimax_msg_alloc(9)"
name: "wimax_msg_alloc"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_msg_alloc/"
description: "wimax_msg_alloc – Create a new skb for sending a message to userspace"
---

<p>wimax_msg_alloc &#8211; Create a new skb for sending a message to userspace</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *wimax_msg_alloc(struct wimax_dev *wimax_dev, const char *pipe_name, const void *msg, size_t size, gfp_t gfp_flags);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<p> <i>pipe_name</i></p>
<dl>
<dd>&quot;named pipe&quot; the message will be sent to</dl>
<p> <i>msg</i></p>
<dl>
<dd>pointer to the message data to send</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the message to send (in bytes), including the header.</dl>
<p> <i>gfp_flags</i></p>
<dl>
<dd>flags for memory allocation.</dl>
<h2>Return</h2>
<p><code>0</code> if ok, negative errno code on error</p>
<h2>Description</h2>
<p>Allocates an skb that will contain the message to send to user space over the messaging pipe and initializes it, copying the payload. </p>
<p> Once this call is done, you can deliver it with <code>wimax_msg_send</code>. </p>
<p> IMPORTANT: </p>
<p> Don&#8217;t use <code>skb_push</code>/<code>skb_pull</code>/<code>skb_reserve</code> on the skb, as <code>wimax_msg_send</code> depends on skb-&gt;data being placed at the beginning of the user message. </p>
<p> Unlike other WiMAX stack calls, this call can be used way early, even before <code>wimax_dev_add</code> is called, as long as the wimax_dev-&gt;net_dev pointer is set to point to a proper net_dev. This is so that drivers can use it early in case they need to send stuff around or communicate with user space.</p>
<h2>Copyright</h2>
