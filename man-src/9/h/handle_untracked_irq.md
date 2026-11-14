---
title: "handle_untracked_irq(9)"
name: "handle_untracked_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_untracked_irq/"
description: "handle_untracked_irq – Simple and software-decoded IRQs."
---

<p>handle_untracked_irq &#8211; Simple and software-decoded IRQs.</p>
<h2>Synopsis</h2>
<pre><code>void handle_untracked_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Untracked interrupts are sent from a demultiplexing interrupt handler when the demultiplexer does not know which device it its multiplexed irq domain generated the interrupt. IRQ&#8217;s handled through here are not subjected to stats tracking, randomness, or spurious interrupt detection.</p>
<h2>Note</h2>
<p>Like handle_simple_irq, the caller is expected to handle the ack, clear, mask and unmask issues if necessary.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
