---
title: "skb_copy_datagram_from_iter(9)"
name: "skb_copy_datagram_from_iter"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy_datagram_from_iter/"
---

skb_copy_datagram_from_iter - Copy a datagram from an iov_iter.

<h2>Synopsis</h2>

<pre><code>int skb_copy_datagram_from_iter(struct sk_buff *skb, int offset, struct iov_iter *from, int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to copy</dl>
 

 <i>offset</i>
<dl><dd>offset in the buffer to start copying to</dl>
 

 <i>from</i>
<dl><dd>the copy source</dl>
 

 <i>len</i>
<dl><dd>amount of data to copy to buffer from iovec</dl>

<h2>Description</h2>

Returns 0 or -EFAULT.

<h2>Copyright</h2>


