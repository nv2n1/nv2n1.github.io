---
title: "irq_cpu_online(9)"
name: "irq_cpu_online"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_cpu_online/"
description: "irq_cpu_online – Invoke all irq_cpu_online functions."
---

<p>irq_cpu_online &#8211; Invoke all irq_cpu_online functions.</p>
<h2>Synopsis</h2>
<pre><code>void irq_cpu_online(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>Iterate through all irqs and invoke the chip.<code>irq_cpu_online</code> for each.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
