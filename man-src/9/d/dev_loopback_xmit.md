---
title: "dev_loopback_xmit(9)"
name: "dev_loopback_xmit"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_loopback_xmit/"
---

dev_loopback_xmit - loop back <i>skb</i>

<h2>Synopsis</h2>

<pre><code>int dev_loopback_xmit(struct net *net, struct sock *sk, struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>net</i>
<dl><dd><dd>network namespace this loopback is happening in</dl>
 

 <i>sk</i>
<dl><dd>sk needed to be a netfilter okfn</dl>
 

 <i>skb</i>
<dl><dd>buffer to transmit</dl>

<h2>Copyright</h2>


