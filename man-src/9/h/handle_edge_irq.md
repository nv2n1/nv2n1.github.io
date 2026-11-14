---
title: "handle_edge_irq(9)"
name: "handle_edge_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_edge_irq/"
description: "handle_edge_irq – edge type IRQ handler"
---

<p>handle_edge_irq &#8211; edge type IRQ handler</p>
<h2>Synopsis</h2>
<pre><code>void handle_edge_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Interrupt occures on the falling and/or rising edge of a hardware signal. The occurrence is latched into the irq controller hardware and must be acked in order to be reenabled. After the ack another interrupt can happen on the same source even before the first one is handled by the associated event handler. If this happens it might be necessary to disable (mask) the interrupt depending on the controller hardware. This requires to reenable the interrupt inside of the loop which handles the interrupts which have arrived while the handler was running. If all pending interrupts are handled, the loop is left.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
