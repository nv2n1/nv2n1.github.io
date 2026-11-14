---
title: "enum_irq_gc_flags(9)"
name: "enum_irq_gc_flags"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_irq_gc_flags/"
description: "enum_irq_gc_flags – Initialization flags for generic irq chips"
---

<p>enum_irq_gc_flags &#8211; Initialization flags for generic irq chips</p>
<h2>Synopsis</h2>
<pre>enum irq_gc_flags {
 IRQ_GC_INIT_MASK_CACHE,
 IRQ_GC_INIT_NESTED_LOCK,
 IRQ_GC_MASK_CACHE_PER_TYPE,
 IRQ_GC_NO_MASK,
 IRQ_GC_BE_IO
}; </pre>
<h2>Constants</h2>
<p>IRQ_GC_INIT_MASK_CACHE</p>
<dl>
<dd>Initialize the mask_cache by reading mask reg</dl>
<p> IRQ_GC_INIT_NESTED_LOCK</p>
<dl>
<dd>Set the lock class of the irqs to nested for irq chips which need to call <code>irq_set_wake</code> on the parent irq. Usually GPIO implementations</dl>
<p> IRQ_GC_MASK_CACHE_PER_TYPE</p>
<dl>
<dd>Mask cache is chip type private</dl>
<p> IRQ_GC_NO_MASK</p>
<dl>
<dd>Do not calculate irq_data-&gt;mask</dl>
<p> IRQ_GC_BE_IO</p>
<dl>
<dd>Use big-endian register accesses (default: LE)</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
