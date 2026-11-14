---
title: "skb_copy_datagram_iter(9)"
name: "skb_copy_datagram_iter"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy_datagram_iter/"
---

skb_copy_datagram_iter - Copy a datagram to an iovec iterator.

<h2>Synopsis</h2>

<pre><code>int skb_copy_datagram_iter(const struct sk_buff *skb, int offset, struct iov_iter *to, int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to copy</dl>
 

 <i>offset</i>
<dl><dd>offset in the buffer to start copying from</dl>
 

 <i>to</i>
<dl><dd>iovec iterator to copy to</dl>
 

 <i>len</i>
<dl><dd>amount of data to copy from buffer to iovec</dl>

<h2>Copyright</h2>


