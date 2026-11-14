---
title: "irq_force_affinity(9)"
name: "irq_force_affinity"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_force_affinity/"
description: "irq_force_affinity – Force the irq affinity of a given irq"
---

<p>irq_force_affinity &#8211; Force the irq affinity of a given irq</p>
<h2>Synopsis</h2>
<pre><code>int irq_force_affinity(unsigned int irq, const struct cpumask *cpumask);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt to set affinity</dl>
<p> <i>cpumask</i></p>
<dl>
<dd>cpumask</dl>
<h2>Description</h2>
<p>Same as irq_set_affinity, but without checking the mask against online cpus. </p>
<p> Solely for low level cpu hotplug code, where we need to make per cpu interrupts affine before the cpu becomes online.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
