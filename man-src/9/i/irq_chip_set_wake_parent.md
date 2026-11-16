---
title: "irq_chip_set_wake_parent(9)"
name: "irq_chip_set_wake_parent"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_set_wake_parent/"
description: "irq_chip_set_wake_parent – Set/reset wake-up on the parent interrupt"
---

<p>irq_chip_set_wake_parent &#8211; Set/reset wake-up on the parent interrupt</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_set_wake_parent(struct irq_data *data, unsigned int on);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
</dd><dd>Pointer to interrupt specific data</dd></dl>
<p> <i>on</i></p>
<dl>
<dd>Whether to set or reset the wake-up capability of this irq</dd></dl>
<h2>Description</h2>
<p>Conditional, as the underlying parent chip might not implement it.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
