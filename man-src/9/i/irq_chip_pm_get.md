---
title: "irq_chip_pm_get(9)"
name: "irq_chip_pm_get"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_pm_get/"
description: "irq_chip_pm_get – Enable power for an IRQ chip"
---

<p>irq_chip_pm_get &#8211; Enable power for an IRQ chip</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_pm_get(struct irq_data *data);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<h2>Description</h2>
<p>Enable the power to the IRQ chip referenced by the interrupt data structure.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
