---
title: "handle_percpu_devid_irq(9)"
name: "handle_percpu_devid_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_percpu_devid_irq/"
description: "handle_percpu_devid_irq – Per CPU local irq handler with per cpu dev ids"
---

<p>handle_percpu_devid_irq &#8211; Per CPU local irq handler with per cpu dev ids</p>
<h2>Synopsis</h2>
<pre><code>void handle_percpu_devid_irq(struct irq_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>the interrupt description structure for this irq</dl>
<h2>Description</h2>
<p>Per CPU interrupts on SMP machines without locking requirements. Same as <code>handle_percpu_irq</code> above but with the following extras: </p>
<p> action-&gt;percpu_dev_id is a pointer to percpu variables which contain the real device id for the cpu on which this handler is called</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
