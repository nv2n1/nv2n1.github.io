---
title: "disable_irq(9)"
name: "disable_irq"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disable_irq/"
---

disable_irq - disable an irq and wait for completion

<h2>Synopsis</h2>

<pre><code>void disable_irq(unsigned int irq);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt to disable</dl>

<h2>Description</h2>

Disable the selected interrupt line. Enables and Disables are nested. This function waits for any pending IRQ handlers for this interrupt to complete before returning. If you use this function while holding a resource the IRQ handler may need you will deadlock. 

 This function may be called - with care - from IRQ context.

<h2>Copyright</h2>


