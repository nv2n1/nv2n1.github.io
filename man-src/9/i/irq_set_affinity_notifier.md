---
title: "irq_set_affinity_notifier(9)"
name: "irq_set_affinity_notifier"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_affinity_notifier/"
description: "irq_set_affinity_notifier – control notification of IRQ affinity changes"
---

<p>irq_set_affinity_notifier &#8211; control notification of IRQ affinity changes</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_affinity_notifier(unsigned int irq, struct irq_affinity_notify *notify);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt for which to enable/disable notification</dl>
<p> <i>notify</i></p>
<dl>
<dd>Context for notification, or <code>NULL</code> to disable notification. Function pointers must be initialised; the other fields will be initialised by this function.</dl>
<h2>Description</h2>
<p>Must be called in process context. Notification may only be enabled after the IRQ is allocated and must be disabled before the IRQ is freed using <code>free_irq</code>.</p>
<h2>Copyright</h2>
