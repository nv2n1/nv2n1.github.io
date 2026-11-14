---
title: "irq_chip_compose_msi_msg(9)"
name: "irq_chip_compose_msi_msg"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_chip_compose_msi_msg/"
description: "irq_chip_compose_msi_msg – Componse msi message for a irq chip"
---

<p>irq_chip_compose_msi_msg &#8211; Componse msi message for a irq chip</p>
<h2>Synopsis</h2>
<pre><code>int irq_chip_compose_msi_msg(struct irq_data *data, struct msi_msg *msg);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>Pointer to interrupt specific data</dl>
<p> <i>msg</i></p>
<dl>
<dd>Pointer to the MSI message</dl>
<h2>Description</h2>
<p>For hierarchical domains we find the first chip in the hierarchy which implements the irq_compose_msi_msg callback. For non hierarchical we use the top level chip.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
