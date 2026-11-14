---
title: "irq_set_chip_data(9)"
name: "irq_set_chip_data"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_chip_data/"
description: "irq_set_chip_data – set irq chip data for an irq"
---

<p>irq_set_chip_data &#8211; set irq chip data for an irq</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_chip_data(unsigned int irq, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt number</dl>
<p> <i>data</i></p>
<dl>
<dd>Pointer to chip specific data</dl>
<h2>Description</h2>
<p>Set the hardware irq chip data for an irq</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
