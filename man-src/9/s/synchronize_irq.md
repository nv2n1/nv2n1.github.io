---
title: "synchronize_irq(9)"
name: "synchronize_irq"
section: "9"
letter: "s"
url: "/docs/linux/man/9-synchronize_irq/"
---

synchronize_irq - wait for pending IRQ handlers (on other CPUs)

<h2>Synopsis</h2>

<pre><code>void synchronize_irq(unsigned int irq);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>interrupt number to wait for</dl>

<h2>Description</h2>

This function waits for any pending IRQ handlers for this interrupt to complete before returning. If you use this function while holding a resource the IRQ handler may need you will deadlock. 

 This function may be called - with care - from IRQ context.

<h2>Copyright</h2>


