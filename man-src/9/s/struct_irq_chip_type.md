---
title: "struct_irq_chip_type(9)"
name: "struct_irq_chip_type"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_chip_type/"
description: "struct_irq_chip_type – Generic interrupt chip instance for a flow type"
---

<p>struct_irq_chip_type &#8211; Generic interrupt chip instance for a flow type</p>
<h2>Synopsis</h2>
<pre><code>struct irq_chip_type {
    struct irq_chip chip;
    struct irq_chip_regs regs;
    irq_flow_handler_t handler;
    u32 type;
    u32 mask_cache_priv;
    u32 *mask_cache;
};</code></pre>
<h2>Members</h2>
<p>chip</p>
<dl>
<dd>The real interrupt chip which provides the callbacks</dl>
<p> regs</p>
<dl>
<dd>Register offsets for this chip</dl>
<p> handler</p>
<dl>
<dd>Flow handler associated with this chip</dl>
<p> type</p>
<dl>
<dd>Chip can handle these flow types</dl>
<p> mask_cache_priv</p>
<dl>
<dd>Cached mask register private to the chip type</dl>
<p> mask_cache</p>
<dl>
<dd>Pointer to cached mask register</dl>
<h2>Description</h2>
<p>A irq_generic_chip can have several instances of irq_chip_type when it requires different functions and register offsets for different flow types.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
