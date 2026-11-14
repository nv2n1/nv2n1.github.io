---
title: "irq_alloc_generic_chip(9)"
name: "irq_alloc_generic_chip"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_alloc_generic_chip/"
description: "irq_alloc_generic_chip – Allocate a generic chip and initialize it"
---

<p>irq_alloc_generic_chip &#8211; Allocate a generic chip and initialize it</p>
<h2>Synopsis</h2>
<pre><code>struct irq_chip_generic *irq_alloc_generic_chip(const char *name, int num_ct, unsigned int irq_base, void __iomem *reg_base, irq_flow_handler_t handler);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>Name of the irq chip</dl>
<p> <i>num_ct</i></p>
<dl>
<dd>Number of irq_chip_type instances associated with this</dl>
<p> <i>irq_base</i></p>
<dl>
<dd>Interrupt base nr for this chip</dl>
<p> <i>reg_base</i></p>
<dl>
<dd>Register base address (virtual)</dl>
<p> <i>handler</i></p>
<dl>
<dd>Default flow handler associated with this chip</dl>
<h2>Description</h2>
<p>Returns an initialized irq_chip_generic structure. The chip defaults to the primary (index 0) irq_chip_type and <i>handler</i></p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
