---
title: "struct_irq_data(9)"
name: "struct_irq_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_data/"
description: "struct_irq_data – per irq chip data passed down to chip functions"
---

<p>struct_irq_data &#8211; per irq chip data passed down to chip functions</p>
<h2>Synopsis</h2>
<pre><code>struct irq_data {
    u32 mask;
    unsigned int irq;
    unsigned long hwirq;
    struct irq_common_data *common;
    struct irq_chip *chip;
    struct irq_domain *domain;
#ifdef CONFIG_IRQ_DOMAIN_HIERARCHY
    struct irq_data *parent_data;
#endif
    void *chip_data;
};</code></pre>
<h2>Members</h2>
<p>mask</p>
<dl>
<dd>precomputed bitmask for accessing the chip registers</dd></dl>
<p> irq</p>
<dl>
<dd>interrupt number</dd></dl>
<p> hwirq</p>
<dl>
<dd>hardware interrupt number, local to the interrupt domain</dd></dl>
<p> common</p>
<dl>
<dd>point to data shared by all irqchips</dd></dl>
<p> chip</p>
<dl>
<dd>low level interrupt hardware access</dd></dl>
<p> domain</p>
<dl>
<dd>Interrupt translation domain; responsible for mapping between hwirq number and linux irq number.</dd></dl>
<p> parent_data</p>
<dl>
<dd>pointer to parent struct irq_data to support hierarchy irq_domain</dd></dl>
<p> chip_data</p>
<dl>
<dd>platform-specific per-chip private data for the chip methods, to allow shared chip implementations</dd></dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
