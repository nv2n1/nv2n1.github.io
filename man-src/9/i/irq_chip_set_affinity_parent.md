---
title: "irq_chip_set_affinity_parent(9)"
name: "irq_chip_set_affinity_parent"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_set_affinity_parent/"
description: "irq_chip_set_affinity_parent – Set affinity on the parent interrupt"
---

<p>irq_chip_set_affinity_parent &#8211; Set affinity on the parent interrupt</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_set_affinity_parent(struct irq_data *data, const struct cpumask *dest, bool force);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<p> <i>dest</i></p>
<dl>
<dd>The affinity mask to set</dl>
<p> <i>force</i></p>
<dl>
<dd>Flag to enforce setting (disable online checks)</dl>
<h2>Description</h2>
<p>Conditinal, as the underlying parent chip might not implement it.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
