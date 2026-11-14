---
title: "irq_chip_pm_put(9)"
name: "irq_chip_pm_put"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_pm_put/"
description: "irq_chip_pm_put – Disable power for an IRQ chip"
---

<p>irq_chip_pm_put &#8211; Disable power for an IRQ chip</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_pm_put(struct irq_data *data);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<h2>Description</h2>
<p>Disable the power to the IRQ chip referenced by the interrupt data structure, belongs. Note that power will only be disabled, once this function has been called for all IRQs that have called <code>irq_chip_pm_get</code>.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
