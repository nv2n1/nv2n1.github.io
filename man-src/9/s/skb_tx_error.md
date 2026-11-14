---
title: "skb_tx_error(9)"
name: "skb_tx_error"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_tx_error/"
---

skb_tx_error - report an sk_buff xmit error

<h2>Synopsis</h2>

<pre><code>void skb_tx_error(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer that triggered an error</dl>

<h2>Description</h2>

Report xmit error if a device callback is tracking this skb. skb must be freed afterwards.

<h2>Copyright</h2>


