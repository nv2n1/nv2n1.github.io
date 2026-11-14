---
title: "handle_fasteoi_irq(9)"
name: "handle_fasteoi_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_fasteoi_irq/"
description: "handle_fasteoi_irq – irq handler for transparent controllers"
---

<p>handle_fasteoi_irq &#8211; irq handler for transparent controllers</p>
<h2>Synopsis</h2>
<pre><code>void handle_fasteoi_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Only a single callback will be issued to the chip: an -&gt;<code>eoi</code> call when the interrupt has been serviced. This enables support for modern forms of interrupt handlers, which handle the flow details in hardware, transparently.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
