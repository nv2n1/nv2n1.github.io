---
title: "irq_set_affinity(9)"
name: "irq_set_affinity"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_affinity/"
description: "irq_set_affinity – Set the irq affinity of a given irq"
---

<p>irq_set_affinity &#8211; Set the irq affinity of a given irq</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_affinity(unsigned int irq, const struct cpumask *cpumask);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt to set affinity</dl>
<p> <i>cpumask</i></p>
<dl>
<dd>cpumask</dl>
<h2>Description</h2>
<p>Fails if cpumask does not contain an online CPU</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
