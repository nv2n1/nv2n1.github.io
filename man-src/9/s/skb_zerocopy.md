---
title: "skb_zerocopy(9)"
name: "skb_zerocopy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_zerocopy/"
description: "skb_zerocopy – Zero copy skb to skb"
---

<p>skb_zerocopy &#8211; Zero copy skb to skb</p>
<h2>Synopsis</h2>
<pre><code>int skb_zerocopy(struct sk_buff *to, struct sk_buff *from, int len, int hlen);</code></pre>
<h2>Arguments</h2>
<p><i>to</i></p>
<dl>
<dd>
<dd>destination buffer</dl>
<p> <i>from</i></p>
<dl>
<dd>source buffer</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to copy from source buffer</dl>
<p> <i>hlen</i></p>
<dl>
<dd>size of linear headroom in destination buffer</dl>
<h2>Description</h2>
<p>Copies up to `len` bytes from `from` to `to` by creating references to the frags in the source buffer. </p>
<p> The `hlen` as calculated by <code>skb_zerocopy_headlen</code> specifies the headroom in the `to` buffer. </p>
<p> Return value: 0: everything is OK -ENOMEM: couldn&#8217;t orphan frags of <i>from</i> due to lack of memory -EFAULT: <code>skb_copy_bits</code> found some problem with skb geometry</p>
<h2>Copyright</h2>
