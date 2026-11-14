---
title: "struct_irq_chip_generic(9)"
name: "struct_irq_chip_generic"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_chip_generic/"
description: "struct_irq_chip_generic – Generic irq chip data structure"
---

<p>struct_irq_chip_generic &#8211; Generic irq chip data structure</p>
<h2>Synopsis</h2>
<pre><code>struct irq_chip_generic {
    raw_spinlock_t lock;
    void __iomem *reg_base;
    u32 (*reg_readl)(void __iomem *addr);
    void (*reg_writel)(u32 val, void __iomem *addr);
    void (*suspend)(struct irq_chip_generic *gc);
    void (*resume)(struct irq_chip_generic *gc);
    unsigned int irq_base;
    unsigned int irq_cnt;
    u32 mask_cache;
    u32 type_cache;
    u32 polarity_cache;
    u32 wake_enabled;
    u32 wake_active;
    unsigned int num_ct;
    void *private;
    unsigned long installed;
    unsigned long unused;
    struct irq_domain *domain;
    struct list_head list;
    struct irq_chip_type chip_types[0];
};</code></pre>
<h2>Members</h2>
<p>lock</p>
<dl>
<dd>Lock to protect register and cache data access</dl>
<p> reg_base</p>
<dl>
<dd>Register base address (virtual)</dl>
<p> reg_readl</p>
<dl>
<dd>Alternate I/O accessor (defaults to readl if NULL)</dl>
<p> reg_writel</p>
<dl>
<dd>Alternate I/O accessor (defaults to writel if NULL)</dl>
<p> suspend</p>
<dl>
<dd>Function called from core code on suspend once per chip; can be useful instead of irq_chip::suspend to handle chip details even when no interrupts are in use</dl>
<p> resume</p>
<dl>
<dd>Function called from core code on resume once per chip; can be useful instead of irq_chip::suspend to handle chip details even when no interrupts are in use</dl>
<p> irq_base</p>
<dl>
<dd>Interrupt base nr for this chip</dl>
<p> irq_cnt</p>
<dl>
<dd>Number of interrupts handled by this chip</dl>
<p> mask_cache</p>
<dl>
<dd>Cached mask register shared between all chip types</dl>
<p> type_cache</p>
<dl>
<dd>Cached type register</dl>
<p> polarity_cache</p>
<dl>
<dd>Cached polarity register</dl>
<p> wake_enabled</p>
<dl>
<dd>Interrupt can wakeup from suspend</dl>
<p> wake_active</p>
<dl>
<dd>Interrupt is marked as an wakeup from suspend source</dl>
<p> num_ct</p>
<dl>
<dd>Number of available irq_chip_type instances (usually 1)</dl>
<p> private</p>
<dl>
<dd>Private data for non generic chip callbacks</dl>
<p> installed</p>
<dl>
<dd>bitfield to denote installed interrupts</dl>
<p> unused</p>
<dl>
<dd>bitfield to denote unused interrupts</dl>
<p> domain</p>
<dl>
<dd>irq domain pointer</dl>
<p> list</p>
<dl>
<dd>List head for keeping track of instances</dl>
<p> chip_types[0]</p>
<dl>
<dd>Array of interrupt irq_chip_types</dl>
<h2>Description</h2>
<p>Note, that irq_chip_generic can have multiple irq_chip_type implementations which can be associated to a particular irq line of an irq_chip_generic instance. That allows to share and protect state in an irq_chip_generic instance when we need to implement different flow mechanisms (level/edge) for it.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
