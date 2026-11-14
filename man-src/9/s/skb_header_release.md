---
title: "skb_header_release(9)"
name: "skb_header_release"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_header_release/"
description: "skb_header_release – release reference to header"
---

<p>skb_header_release &#8211; release reference to header</p>
<h2>Synopsis</h2>
<pre><code>void skb_header_release(struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to operate on</dl>
<h2>Description</h2>
<p>Drop a reference to the header part of the buffer. This is done by acquiring a payload reference. You must not read from the header part of skb-&gt;data after this.</p>
<h2>Note</h2>
<p>Check if you can use <code>__skb_header_release</code> instead.</p>
<h2>Copyright</h2>
