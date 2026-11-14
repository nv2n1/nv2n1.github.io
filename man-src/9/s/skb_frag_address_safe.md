---
title: "skb_frag_address_safe(9)"
name: "skb_frag_address_safe"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_frag_address_safe/"
description: "skb_frag_address_safe – gets the address of the data contained in a paged fragment"
---

<p>skb_frag_address_safe &#8211; gets the address of the data contained in a paged fragment</p>
<h2>Synopsis</h2>
<pre><code>void *skb_frag_address_safe(const skb_frag_t *frag);</code></pre>
<h2>Arguments</h2>
<p><i>frag</i></p>
<dl>
<dd>
<dd>the paged fragment buffer</dl>
<h2>Description</h2>
<p>Returns the address of the data within <i>frag</i>. Checks that the page is mapped and returns <code>NULL</code> otherwise.</p>
<h2>Copyright</h2>
