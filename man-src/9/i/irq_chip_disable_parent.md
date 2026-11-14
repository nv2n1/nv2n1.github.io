---
title: "irq_chip_disable_parent(9)"
name: "irq_chip_disable_parent"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_disable_parent/"
description: "irq_chip_disable_parent – Disable the parent interrupt (defaults to mask if NULL)"
---

<p>irq_chip_disable_parent &#8211; Disable the parent interrupt (defaults to mask if NULL)</p>
<h2>Synopsis</h2>
<pre><code>void irq_chip_disable_parent(struct irq_data *data);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
