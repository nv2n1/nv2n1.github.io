---
title: "irq_set_irqchip_state(9)"
name: "irq_set_irqchip_state"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_irqchip_state/"
---

irq_set_irqchip_state - set the state of a forwarded interrupt.

<h2>Synopsis</h2>

<pre><code>int irq_set_irqchip_state(unsigned int irq, enum irqchip_irq_state which, bool val);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd></dd><dd>Interrupt line that is forwarded to a VM</dd></dl>
 

 <i>which</i>
<dl><dd>State to be restored (one of IRQCHIP_STATE_*)</dd></dl>
 

 <i>val</i>
<dl><dd>Value corresponding to <i>which</i></dd></dl>

<h2>Description</h2>

This call sets the internal irqchip state of an interrupt, depending on the value of <i>which</i>. 

 This function should be called with preemption disabled if the interrupt controller has per-cpu registers.

<h2>Copyright</h2>


