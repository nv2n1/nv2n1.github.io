---
title: "skb_frag_set_page(9)"
name: "skb_frag_set_page"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_frag_set_page/"
---

skb_frag_set_page - sets the page contained in a paged fragment of an skb

<h2>Synopsis</h2>

<pre><code>void skb_frag_set_page(struct sk_buff *skb, int f, struct page *page);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>the buffer</dl>
 

 <i>f</i>
<dl><dd>the fragment offset</dl>
 

 <i>page</i>
<dl><dd>the page to set</dl>

<h2>Description</h2>

Sets the <i>f</i>'th fragment of <i>skb</i> to contain <i>page</i>.

<h2>Copyright</h2>


