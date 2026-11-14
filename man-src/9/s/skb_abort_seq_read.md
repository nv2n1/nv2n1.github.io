---
title: "skb_abort_seq_read(9)"
name: "skb_abort_seq_read"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_abort_seq_read/"
description: "skb_abort_seq_read – Abort a sequential read of skb data"
---

<p>skb_abort_seq_read &#8211; Abort a sequential read of skb data</p>
<h2>Synopsis</h2>
<pre><code>void skb_abort_seq_read(struct skb_seq_state *st);</code></pre>
<h2>Arguments</h2>
<p><i>st</i></p>
<dl>
<dd>
<dd>state variable</dl>
<h2>Description</h2>
<p>Must be called if <code>skb_seq_read</code> was not called until it returned 0.</p>
<h2>Copyright</h2>
