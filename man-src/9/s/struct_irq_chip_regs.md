---
title: "struct_irq_chip_regs(9)"
name: "struct_irq_chip_regs"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_chip_regs/"
description: "struct_irq_chip_regs – register offsets for struct irq_gci"
---

<p>struct_irq_chip_regs &#8211; register offsets for struct irq_gci</p>
<h2>Synopsis</h2>
<pre><code>struct irq_chip_regs {
    unsigned long enable;
    unsigned long disable;
    unsigned long mask;
    unsigned long ack;
    unsigned long eoi;
    unsigned long type;
    unsigned long polarity;
};</code></pre>
<h2>Members</h2>
<p>enable</p>
<dl>
<dd>Enable register offset to reg_base</dd></dl>
<p> disable</p>
<dl>
<dd>Disable register offset to reg_base</dd></dl>
<p> mask</p>
<dl>
<dd>Mask register offset to reg_base</dd></dl>
<p> ack</p>
<dl>
<dd>Ack register offset to reg_base</dd></dl>
<p> eoi</p>
<dl>
<dd>Eoi register offset to reg_base</dd></dl>
<p> type</p>
<dl>
<dd>Type configuration register offset to reg_base</dd></dl>
<p> polarity</p>
<dl>
<dd>Polarity configuration register offset to reg_base</dd></dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
