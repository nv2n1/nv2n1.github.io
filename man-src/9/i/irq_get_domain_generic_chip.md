---
title: "irq_get_domain_generic_chip(9)"
name: "irq_get_domain_generic_chip"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_get_domain_generic_chip/"
description: "irq_get_domain_generic_chip – Get a pointer to the generic chip of a hw_irq"
---

<p>irq_get_domain_generic_chip &#8211; Get a pointer to the generic chip of a hw_irq</p>
<h2>Synopsis</h2>
<pre><code>struct irq_chip_generic *irq_get_domain_generic_chip(struct irq_domain *d, unsigned int hw_irq);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>irq domain pointer</dl>
<p> <i>hw_irq</i></p>
<dl>
<dd>Hardware interrupt number</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
