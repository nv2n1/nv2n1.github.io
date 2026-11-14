---
title: "irq_set_irq_wake(9)"
name: "irq_set_irq_wake"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_irq_wake/"
---

irq_set_irq_wake - control irq power management wakeup

<h2>Synopsis</h2>

<pre><code>int irq_set_irq_wake(unsigned int irq, unsigned int on);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>interrupt to control</dl>
 

 <i>on</i>
<dl><dd>enable/disable power management wakeup</dl>

<h2>Description</h2>

Enable/disable power management wakeup mode, which is disabled by default. Enables and disables must match, just as they match for non-wakeup mode support. 

 Wakeup mode lets this IRQ wake the system from sleep states like "suspend to RAM".

<h2>Copyright</h2>


