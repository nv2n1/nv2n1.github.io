---
title: "wimax_msg_send(9)"
name: "wimax_msg_send"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_msg_send/"
description: "wimax_msg_send – Send a pre-allocated message to user space"
---

<p>wimax_msg_send &#8211; Send a pre-allocated message to user space</p>
<h2>Synopsis</h2>
<pre><code>int wimax_msg_send(struct wimax_dev *wimax_dev, struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<p> <i>skb</i></p>
<dl>
<dd>struct sk_buff returned by <code>wimax_msg_alloc</code>. Note the ownership of <i>skb</i> is transferred to this function.</dl>
<h2>Return</h2>
<p>0 if ok, &lt; 0 errno code on error</p>
<h2>Description</h2>
<p>Sends a free-form message that was preallocated with <code>wimax_msg_alloc</code> and filled up. </p>
<p> Assumes that once you pass an skb to this function for sending, it owns it and will release it when done (on success). </p>
<p> IMPORTANT: </p>
<p> Don&#8217;t use <code>skb_push</code>/<code>skb_pull</code>/<code>skb_reserve</code> on the skb, as <code>wimax_msg_send</code> depends on skb-&gt;data being placed at the beginning of the user message. </p>
<p> Unlike other WiMAX stack calls, this call can be used way early, even before <code>wimax_dev_add</code> is called, as long as the wimax_dev-&gt;net_dev pointer is set to point to a proper net_dev. This is so that drivers can use it early in case they need to send stuff around or communicate with user space.</p>
<h2>Copyright</h2>
