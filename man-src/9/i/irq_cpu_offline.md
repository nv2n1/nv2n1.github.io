---
title: "irq_cpu_offline(9)"
name: "irq_cpu_offline"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_cpu_offline/"
description: "irq_cpu_offline – Invoke all irq_cpu_offline functions."
---

<p>irq_cpu_offline &#8211; Invoke all irq_cpu_offline functions.</p>
<h2>Synopsis</h2>
<pre><code>void irq_cpu_offline(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>Iterate through all irqs and invoke the chip.<code>irq_cpu_offline</code> for each.</p>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
