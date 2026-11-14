---
title: "irq_gc_mask_set_bit(9)"
name: "irq_gc_mask_set_bit"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_gc_mask_set_bit/"
description: "irq_gc_mask_set_bit – Mask chip via setting bit in mask register"
---

<p>irq_gc_mask_set_bit &#8211; Mask chip via setting bit in mask register</p>
<h2>Synopsis</h2>
<pre><code>void irq_gc_mask_set_bit(struct irq_data *d);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>irq_data</dl>
<h2>Description</h2>
<p>Chip has a single mask register. Values of this register are cached and protected by gc-&gt;lock</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
