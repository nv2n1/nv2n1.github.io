---
title: "skb_prepare_seq_read(9)"
name: "skb_prepare_seq_read"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_prepare_seq_read/"
description: "skb_prepare_seq_read – Prepare a sequential read of skb data"
---

<p>skb_prepare_seq_read &#8211; Prepare a sequential read of skb data</p>
<h2>Synopsis</h2>
<pre><code>void skb_prepare_seq_read(struct sk_buff *skb, unsigned int from, unsigned int to, struct skb_seq_state *st);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>the buffer to read</dl>
<p> <i>from</i></p>
<dl>
<dd>lower offset of data to be read</dl>
<p> <i>to</i></p>
<dl>
<dd>upper offset of data to be read</dl>
<p> <i>st</i></p>
<dl>
<dd>state variable</dl>
<h2>Description</h2>
<p>Initializes the specified state variable. Must be called before invoking <code>skb_seq_read</code> for the first time.</p>
<h2>Copyright</h2>
