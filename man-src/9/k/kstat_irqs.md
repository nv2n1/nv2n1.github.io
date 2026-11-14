---
title: "kstat_irqs(9)"
name: "kstat_irqs"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kstat_irqs/"
description: "kstat_irqs – Get the statistics for an interrupt"
---

<p>kstat_irqs &#8211; Get the statistics for an interrupt</p>
<h2>Synopsis</h2>
<pre><code>unsigned int kstat_irqs(unsigned int irq);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>The interrupt number</dl>
<h2>Description</h2>
<p>Returns the sum of interrupt counts on all cpus since boot for <i>irq</i>. The caller must ensure that the interrupt is not removed concurrently.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
