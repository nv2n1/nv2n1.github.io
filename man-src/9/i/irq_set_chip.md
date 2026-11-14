---
title: "irq_set_chip(9)"
name: "irq_set_chip"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_chip/"
description: "irq_set_chip – set the irq chip for an irq"
---

<p>irq_set_chip &#8211; set the irq chip for an irq</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_chip(unsigned int irq, struct irq_chip *chip);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>irq number</dl>
<p> <i>chip</i></p>
<dl>
<dd>pointer to irq chip description structure</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
