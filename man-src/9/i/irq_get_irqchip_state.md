---
title: "irq_get_irqchip_state(9)"
name: "irq_get_irqchip_state"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_get_irqchip_state/"
---

irq_get_irqchip_state - returns the irqchip state of a interrupt.

<h2>Synopsis</h2>

<pre><code>int irq_get_irqchip_state(unsigned int irq, enum irqchip_irq_state which, bool *state);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line that is forwarded to a VM</dl>
 

 <i>which</i>
<dl><dd>One of IRQCHIP_STATE_* the caller wants to know about</dl>
 

 <i>state</i>
<dl><dd>a pointer to a boolean where the state is to be storeed</dl>

<h2>Description</h2>

This call snapshots the internal irqchip state of an interrupt, returning into <i>state</i> the bit corresponding to stage <i>which</i> 

 This function should be called with preemption disabled if the interrupt controller has per-cpu registers.

<h2>Copyright</h2>


