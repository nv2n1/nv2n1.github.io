---
title: "setup_irq(9)"
name: "setup_irq"
section: "9"
letter: "s"
url: "/docs/linux/man/9-setup_irq/"
---

setup_irq - setup an interrupt

<h2>Synopsis</h2>

<pre><code>int setup_irq(unsigned int irq, struct irqaction *act);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line to setup</dl>
 

 <i>act</i>
<dl><dd>irqaction for the interrupt</dl>

<h2>Description</h2>

Used to statically setup interrupts in the early boot process.

<h2>Copyright</h2>


