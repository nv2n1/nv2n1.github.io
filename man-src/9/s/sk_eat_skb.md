---
title: "sk_eat_skb(9)"
name: "sk_eat_skb"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_eat_skb/"
---

sk_eat_skb - Release a skb if it is no longer needed

<h2>Synopsis</h2>

<pre><code>void sk_eat_skb(struct sock *sk, struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>socket to eat this skb from</dl>
 

 <i>skb</i>
<dl><dd>socket buffer to eat</dl>

<h2>Description</h2>

This routine must be called with interrupts disabled or with the socket locked so that the sk_buff queue operation is ok.

<h2>Copyright</h2>


