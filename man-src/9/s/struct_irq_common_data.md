---
title: "struct_irq_common_data(9)"
name: "struct_irq_common_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_common_data/"
description: "struct_irq_common_data – per irq data shared by all irqchips"
---

<p>struct_irq_common_data &#8211; per irq data shared by all irqchips</p>
<h2>Synopsis</h2>
<pre><code>struct irq_common_data {
    unsigned int __private state_use_accessors;
#ifdef CONFIG_NUMA
    unsigned int node;
#endif
    void *handler_data;
    struct msi_desc *msi_desc;
    cpumask_var_t affinity;
#ifdef CONFIG_GENERIC_IRQ_IPI
    unsigned int ipi_offset;
#endif
};</code></pre>
<h2>Members</h2>
<p>state_use_accessors</p>
<dl>
<dd>status information for irq chip functions. Use accessor functions to deal with it</dl>
<p> node</p>
<dl>
<dd>node index useful for balancing</dl>
<p> handler_data</p>
<dl>
<dd>per-IRQ data for the irq_chip methods</dl>
<p> msi_desc</p>
<dl>
<dd>MSI descriptor</dl>
<p> affinity</p>
<dl>
<dd>IRQ affinity on SMP. If this is an IPI related irq, then this is the mask of the CPUs to which an IPI can be sent.</dl>
<p> ipi_offset</p>
<dl>
<dd>Offset of first IPI target cpu in <i>affinity</i>. Optional.</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
