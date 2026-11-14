---
title: "irq_set_msi_desc(9)"
name: "irq_set_msi_desc"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_msi_desc/"
description: "irq_set_msi_desc – set MSI descriptor data for an irq"
---

<p>irq_set_msi_desc &#8211; set MSI descriptor data for an irq</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_msi_desc(unsigned int irq, struct msi_desc *entry);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt number</dl>
<p> <i>entry</i></p>
<dl>
<dd>Pointer to MSI descriptor data</dl>
<h2>Description</h2>
<p>Set the MSI descriptor entry for an irq</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
