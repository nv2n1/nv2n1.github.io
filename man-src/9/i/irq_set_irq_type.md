---
title: "irq_set_irq_type(9)"
name: "irq_set_irq_type"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_irq_type/"
description: "irq_set_irq_type – set the irq trigger type for an irq"
---

<p>irq_set_irq_type &#8211; set the irq trigger type for an irq</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_irq_type(unsigned int irq, unsigned int type);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>irq number</dl>
<p> <i>type</i></p>
<dl>
<dd>IRQ_TYPE_{LEVEL,EDGE}_* value &#8211; see include/linux/irq.h</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
