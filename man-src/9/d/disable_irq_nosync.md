---
title: "disable_irq_nosync(9)"
name: "disable_irq_nosync"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disable_irq_nosync/"
description: "disable_irq_nosync – disable an irq without waiting"
---

<p>disable_irq_nosync &#8211; disable an irq without waiting</p>
<h2>Synopsis</h2>
<pre><code>void disable_irq_nosync(unsigned int irq);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt to disable</dl>
<h2>Description</h2>
<p>Disable the selected interrupt line. Disables and Enables are nested. Unlike <code>disable_irq</code>, this function does not ensure existing instances of the IRQ handler have completed before returning. </p>
<p> This function may be called from IRQ context.</p>
<h2>Copyright</h2>
