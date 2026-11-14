---
title: "irq_gc_ack_set_bit(9)"
name: "irq_gc_ack_set_bit"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_gc_ack_set_bit/"
description: "irq_gc_ack_set_bit – Ack pending interrupt via setting bit"
---

<p>irq_gc_ack_set_bit &#8211; Ack pending interrupt via setting bit</p>
<h2>Synopsis</h2>
<pre><code>void irq_gc_ack_set_bit(struct irq_data *d);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>irq_data</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
