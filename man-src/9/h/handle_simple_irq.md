---
title: "handle_simple_irq(9)"
name: "handle_simple_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_simple_irq/"
description: "handle_simple_irq – Simple and software-decoded IRQs."
---

<p>handle_simple_irq &#8211; Simple and software-decoded IRQs.</p>
<h2>Synopsis</h2>
<pre><code>void handle_simple_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Simple interrupts are either sent from a demultiplexing interrupt handler or come from hardware, where no interrupt hardware control is necessary.</p>
<h2>Note</h2>
<p>The caller is expected to handle the ack, clear, mask and unmask issues if necessary.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
