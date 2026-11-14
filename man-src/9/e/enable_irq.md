---
title: "enable_irq(9)"
name: "enable_irq"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enable_irq/"
description: "enable_irq – enable handling of an irq"
---

<p>enable_irq &#8211; enable handling of an irq</p>
<h2>Synopsis</h2>
<pre><code>void enable_irq(unsigned int irq);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt to enable</dl>
<h2>Description</h2>
<p>Undoes the effect of one call to <code>disable_irq</code>. If this matches the last disable, processing of interrupts on this IRQ line is re-enabled. </p>
<p> This function may be called from IRQ context only when desc-&gt;irq_data.chip-&gt;bus_lock and desc-&gt;chip-&gt;bus_sync_unlock are NULL !</p>
<h2>Copyright</h2>
