---
title: "free_percpu_irq(9)"
name: "free_percpu_irq"
section: "9"
letter: "f"
url: "/docs/linux/man/9-free_percpu_irq/"
---

free_percpu_irq - free an interrupt allocated with request_percpu_irq

<h2>Synopsis</h2>

<pre><code>void free_percpu_irq(unsigned int irq, void __percpu *dev_id);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line to free</dl>
 

 <i>dev_id</i>
<dl><dd>Device identity to free</dl>

<h2>Description</h2>

Remove a percpu interrupt handler. The handler is removed, but the interrupt line is not disabled. This must be done on each CPU before calling this function. The function does not return until any executing interrupts for this IRQ have completed. 

 This function must not be called from interrupt context.

<h2>Copyright</h2>


