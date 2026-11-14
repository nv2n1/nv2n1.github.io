---
title: "handle_level_irq(9)"
name: "handle_level_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_level_irq/"
description: "handle_level_irq – Level type irq handler"
---

<p>handle_level_irq &#8211; Level type irq handler</p>
<h2>Synopsis</h2>
<pre><code>void handle_level_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Level type interrupts are active as long as the hardware line has the active level. This may require to mask the interrupt and unmask it after the associated handler has acknowledged the device, so the interrupt line is back to inactive.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
