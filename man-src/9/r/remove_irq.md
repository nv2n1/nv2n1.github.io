---
title: "remove_irq(9)"
name: "remove_irq"
section: "9"
letter: "r"
url: "/docs/linux/man/9-remove_irq/"
---

remove_irq - free an interrupt

<h2>Synopsis</h2>

<pre><code>void remove_irq(unsigned int irq, struct irqaction *act);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line to free</dl>
 

 <i>act</i>
<dl><dd>irqaction for the interrupt</dl>

<h2>Description</h2>

Used to remove interrupts statically setup by the early boot process.

<h2>Copyright</h2>


