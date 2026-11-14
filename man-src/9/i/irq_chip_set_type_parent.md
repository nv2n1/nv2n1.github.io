---
title: "irq_chip_set_type_parent(9)"
name: "irq_chip_set_type_parent"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_set_type_parent/"
description: "irq_chip_set_type_parent – Set IRQ type on the parent interrupt"
---

<p>irq_chip_set_type_parent &#8211; Set IRQ type on the parent interrupt</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_set_type_parent(struct irq_data *data, unsigned int type);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<p> <i>type</i></p>
<dl>
<dd>IRQ_TYPE_{LEVEL,EDGE}_* value &#8211; see include/linux/irq.h</dl>
<h2>Description</h2>
<p>Conditional, as the underlying parent chip might not implement it.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
