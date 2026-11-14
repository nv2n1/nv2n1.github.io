---
title: "airq_iv_alloc(9)"
name: "airq_iv_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-airq_iv_alloc/"
description: "airq_iv_alloc – allocate irq bits from an interrupt vector"
---

<p>airq_iv_alloc &#8211; allocate irq bits from an interrupt vector</p>
<h2>Synopsis</h2>
<pre><code>unsigned long airq_iv_alloc(struct airq_iv *iv, unsigned long num);</code></pre>
<h2>Arguments</h2>
<p><i>iv</i></p>
<dl>
<dd>
<dd>pointer to an interrupt vector structure</dl>
<p> <i>num</i></p>
<dl>
<dd>number of consecutive irq bits to allocate</dl>
<h2>Description</h2>
<p>Returns the bit number of the first irq in the allocated block of irqs, or -1UL if no bit is available or the AIRQ_IV_ALLOC flag has not been specified</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
