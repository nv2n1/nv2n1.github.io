---
title: "irq_chip_ack_parent(9)"
name: "irq_chip_ack_parent"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_ack_parent/"
description: "irq_chip_ack_parent – Acknowledge the parent interrupt"
---

<p>irq_chip_ack_parent &#8211; Acknowledge the parent interrupt</p>
<h2>Synopsis</h2>
<pre><code>void irq_chip_ack_parent(struct irq_data *data);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
