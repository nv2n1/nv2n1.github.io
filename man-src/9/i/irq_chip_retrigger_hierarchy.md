---
title: "irq_chip_retrigger_hierarchy(9)"
name: "irq_chip_retrigger_hierarchy"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_retrigger_hierarchy/"
description: "irq_chip_retrigger_hierarchy – Retrigger an interrupt in hardware"
---

<p>irq_chip_retrigger_hierarchy &#8211; Retrigger an interrupt in hardware</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_retrigger_hierarchy(struct irq_data *data);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<h2>Description</h2>
<p>Iterate through the domain hierarchy of the interrupt and check whether a hw retrigger function exists. If yes, invoke it.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
