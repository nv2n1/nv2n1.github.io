---
title: "spans_boundary(9)"
name: "spans_boundary"
section: "9"
letter: "s"
url: "/docs/linux/man/9-spans_boundary/"
description: "spans_boundary – Check a packet can be ISA DMA’d"
---

<p>spans_boundary &#8211; Check a packet can be ISA DMA&#8217;d</p>
<h2>Synopsis</h2>
<pre><code>int spans_boundary(struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>The buffer to check</dl>
<h2>Description</h2>
<p>Returns true if the buffer cross a DMA boundary on a PC. The poor thing can only DMA within a 64K block not across the edges of it.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
