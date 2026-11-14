---
title: "skb_fill_page_desc(9)"
name: "skb_fill_page_desc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_fill_page_desc/"
description: "skb_fill_page_desc – initialise a paged fragment in an skb"
---

<p>skb_fill_page_desc &#8211; initialise a paged fragment in an skb</p>
<h2>Synopsis</h2>
<pre><code>void skb_fill_page_desc(struct sk_buff *skb, int i, struct page *page, int off, int size);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer containing fragment to be initialised</dl>
<p> <i>i</i></p>
<dl>
<dd>paged fragment index to initialise</dl>
<p> <i>page</i></p>
<dl>
<dd>the page to use for this fragment</dl>
<p> <i>off</i></p>
<dl>
<dd>the offset to the data with <i>page</i></dl>
<p> <i>size</i></p>
<dl>
<dd>the length of the data</dl>
<h2>Description</h2>
<p>As per <code>__skb_fill_page_desc</code> &#8212; initialises the <i>i</i>&#8216;th fragment of <i>skb</i> to point to <i>size</i> bytes at offset <i>off</i> within <i>page</i>. In addition updates <i>skb</i> such that <i>i</i> is the last fragment. </p>
<p> Does not take any additional reference on the fragment.</p>
<h2>Copyright</h2>
