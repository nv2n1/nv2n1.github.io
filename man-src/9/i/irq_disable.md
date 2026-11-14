---
title: "irq_disable(9)"
name: "irq_disable"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_disable/"
description: "irq_disable – Mark interrupt disabled"
---

<p>irq_disable &#8211; Mark interrupt disabled</p>
<h2>Synopsis</h2>
<pre><code>void irq_disable(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>irq descriptor which should be disabled</dl>
<h2>Description</h2>
<p>If the chip does not implement the irq_disable callback, we use a lazy disable approach. That means we mark the interrupt disabled, but leave the hardware unmasked. That&#8217;s an optimization because we avoid the hardware access for the common case where no interrupt happens after we marked it disabled. If an interrupt happens, then the interrupt flow handler masks the line at the hardware level and marks it pending. </p>
<p> If the interrupt chip does not implement the irq_disable callback, a driver can disable the lazy approach for a particular irq line by calling &#8216;irq_set_status_flags(irq, IRQ_DISABLE_UNLAZY)&#8217;. This can be used for devices which cannot disable the interrupt at the device level under certain circumstances and have to use disable_irq[_nosync] instead.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
