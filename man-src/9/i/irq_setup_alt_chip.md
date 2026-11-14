---
title: "irq_setup_alt_chip(9)"
name: "irq_setup_alt_chip"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_setup_alt_chip/"
description: "irq_setup_alt_chip – Switch to alternative chip"
---

<p>irq_setup_alt_chip &#8211; Switch to alternative chip</p>
<h2>Synopsis</h2>
<pre><code>int irq_setup_alt_chip(struct irq_data *d, unsigned int type);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>irq_data for this interrupt</dl>
<p> <i>type</i></p>
<dl>
<dd>Flow type to be initialized</dl>
<h2>Description</h2>
<p>Only to be called from chip-&gt;<code>irq_set_type</code> callbacks.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
