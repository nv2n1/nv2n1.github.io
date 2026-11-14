---
title: "airq_iv_free(9)"
name: "airq_iv_free"
section: "9"
letter: "a"
url: "/docs/linux/man/9-airq_iv_free/"
description: "airq_iv_free – free irq bits of an interrupt vector"
---

<p>airq_iv_free &#8211; free irq bits of an interrupt vector</p>
<h2>Synopsis</h2>
<pre><code>void airq_iv_free(struct airq_iv *iv, unsigned long bit, unsigned long num);</code></pre>
<h2>Arguments</h2>
<p><i>iv</i></p>
<dl>
<dd>
<dd>pointer to interrupt vector structure</dl>
<p> <i>bit</i></p>
<dl>
<dd>number of the first irq bit to free</dl>
<p> <i>num</i></p>
<dl>
<dd>number of consecutive irq bits to free</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
