---
title: "handle_edge_eoi_irq(9)"
name: "handle_edge_eoi_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_edge_eoi_irq/"
description: "handle_edge_eoi_irq – edge eoi type IRQ handler"
---

<p>handle_edge_eoi_irq &#8211; edge eoi type IRQ handler</p>
<h2>Synopsis</h2>
<pre><code>void handle_edge_eoi_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Similar as the above handle_edge_irq, but using eoi and w/o the mask/unmask logic.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
