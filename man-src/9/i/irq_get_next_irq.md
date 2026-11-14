---
title: "irq_get_next_irq(9)"
name: "irq_get_next_irq"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_get_next_irq/"
description: "irq_get_next_irq – get next allocated irq number"
---

<p>irq_get_next_irq &#8211; get next allocated irq number</p>
<h2>Synopsis</h2>
<pre><code>unsigned int irq_get_next_irq(unsigned int offset);</code></pre>
<h2>Arguments</h2>
<p><i>offset</i></p>
<dl>
<dd>
<dd>where to start the search</dl>
<h2>Description</h2>
<p>Returns next irq number after offset or nr_irqs if none is found.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
