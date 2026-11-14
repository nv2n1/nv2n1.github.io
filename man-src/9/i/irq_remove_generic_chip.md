---
title: "irq_remove_generic_chip(9)"
name: "irq_remove_generic_chip"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_remove_generic_chip/"
description: "irq_remove_generic_chip – Remove a chip"
---

<p>irq_remove_generic_chip &#8211; Remove a chip</p>
<h2>Synopsis</h2>
<pre><code>void irq_remove_generic_chip(struct irq_chip_generic *gc, u32 msk, unsigned int clr, unsigned int set);</code></pre>
<h2>Arguments</h2>
<p><i>gc</i></p>
<dl>
<dd>
<dd>Generic irq chip holding all data</dl>
<p> <i>msk</i></p>
<dl>
<dd>Bitmask holding the irqs to initialize relative to gc-&gt;irq_base</dl>
<p> <i>clr</i></p>
<dl>
<dd>IRQ_* bits to clear</dl>
<p> <i>set</i></p>
<dl>
<dd>IRQ_* bits to set</dl>
<h2>Description</h2>
<p>Remove up to 32 interrupts starting from gc-&gt;irq_base.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
