---
title: "zerocopy_sg_from_iter(9)"
name: "zerocopy_sg_from_iter"
section: "9"
letter: "z"
url: "/docs/linux/man/9-zerocopy_sg_from_iter/"
description: "zerocopy_sg_from_iter – Build a zerocopy datagram from an iov_iter"
---

<p>zerocopy_sg_from_iter &#8211; Build a zerocopy datagram from an iov_iter</p>
<h2>Synopsis</h2>
<pre><code>int zerocopy_sg_from_iter(struct sk_buff *skb, struct iov_iter *from);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to copy</dl>
<p> <i>from</i></p>
<dl>
<dd>the source to copy from</dl>
<h2>Description</h2>
<p>The function will first copy up to headlen, and then pin the userspace pages and build frags through them. </p>
<p> Returns 0, -EFAULT or -EMSGSIZE.</p>
<h2>Copyright</h2>


