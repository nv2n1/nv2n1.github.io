---
title: "skb_copy_and_csum_datagram_msg(9)"
name: "skb_copy_and_csum_datagram_msg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy_and_csum_datagram_msg/"
---

skb_copy_and_csum_datagram_msg - Copy and checksum skb to user iovec.

<h2>Synopsis</h2>

<pre><code>int skb_copy_and_csum_datagram_msg(struct sk_buff *skb, int hlen, struct msghdr *msg);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>skbuff</dl>
 

 <i>hlen</i>
<dl><dd>hardware length</dl>
 

 <i>msg</i>
<dl><dd>destination</dl>

<h2>Description</h2>

Caller _must_ check that skb will fit to this iovec.

<h2>Return</h2>

0 - success. -EINVAL - checksum failure. -EFAULT - fault during copy.

<h2>Copyright</h2>


