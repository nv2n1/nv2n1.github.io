---
title: "free_irq(9)"
name: "free_irq"
section: "9"
letter: "f"
url: "/docs/linux/man/9-free_irq/"
---

free_irq - free an interrupt allocated with request_irq

<h2>Synopsis</h2>

<pre><code>void free_irq(unsigned int irq, void *dev_id);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line to free</dl>
 

 <i>dev_id</i>
<dl><dd>Device identity to free</dl>

<h2>Description</h2>

Remove an interrupt handler. The handler is removed and if the interrupt line is no longer in use by any driver it is disabled. On a shared IRQ the caller must ensure the interrupt is disabled on the card it drives before calling this function. The function does not return until any executing interrupts for this IRQ have completed. 

 This function must not be called from interrupt context.

<h2>Copyright</h2>


