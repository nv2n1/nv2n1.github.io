---
title: "airq_iv_create(9)"
name: "airq_iv_create"
section: "9"
letter: "a"
url: "/docs/linux/man/9-airq_iv_create/"
description: "airq_iv_create – create an interrupt vector"
---

<p>airq_iv_create &#8211; create an interrupt vector</p>
<h2>Synopsis</h2>
<pre><code>struct airq_iv *airq_iv_create(unsigned long bits, unsigned long flags);</code></pre>
<h2>Arguments</h2>
<p><i>bits</i></p>
<dl>
<dd>
<dd>number of bits in the interrupt vector</dl>
<p> <i>flags</i></p>
<dl>
<dd>allocation flags</dl>
<h2>Description</h2>
<p>Returns a pointer to an interrupt vector structure</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
