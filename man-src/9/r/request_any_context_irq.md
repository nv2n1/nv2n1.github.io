---
title: "request_any_context_irq(9)"
name: "request_any_context_irq"
section: "9"
letter: "r"
url: "/docs/linux/man/9-request_any_context_irq/"
---

request_any_context_irq - allocate an interrupt line

<h2>Synopsis</h2>

<pre><code>int request_any_context_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char *name, void *dev_id);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line to allocate</dl>
 

 <i>handler</i>
<dl><dd>Function to be called when the IRQ occurs. Threaded handler for threaded interrupts.</dl>
 

 <i>flags</i>
<dl><dd>Interrupt type flags</dl>
 

 <i>name</i>
<dl><dd>An ascii name for the claiming device</dl>
 

 <i>dev_id</i>
<dl><dd>A cookie passed back to the handler function</dl>

<h2>Description</h2>

This call allocates interrupt resources and enables the interrupt line and IRQ handling. It selects either a hardirq or threaded handling method depending on the context. 

 On failure, it returns a negative value. On success, it returns either IRQC_IS_HARDIRQ or IRQC_IS_NESTED.

<h2>Copyright</h2>


