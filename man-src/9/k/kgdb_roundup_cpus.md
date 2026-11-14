---
title: "kgdb_roundup_cpus(9)"
name: "kgdb_roundup_cpus"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kgdb_roundup_cpus/"
description: "kgdb_roundup_cpus – Get other CPUs into a holding pattern"
---

<p>kgdb_roundup_cpus &#8211; Get other CPUs into a holding pattern</p>
<h2>Synopsis</h2>
<pre><code>void kgdb_roundup_cpus(unsigned long flags);</code></pre>
<h2>Arguments</h2>
<p><i>flags</i></p>
<dl>
<dd>
<dd>Current IRQ state</dl>
<h2>Description</h2>
<p>On SMP systems, we need to get the attention of the other CPUs and get them into a known state. This should do what is needed to get the other CPUs to call <code>kgdb_wait</code>. Note that on some arches, the NMI approach is not used for rounding up all the CPUs. For example, in case of MIPS, <code>smp_call_function</code> is used to roundup CPUs. In this case, we have to make sure that interrupts are enabled before calling <code>smp_call_function</code>. The argument to this function is the flags that will be used when restoring the interrupts. There is <code>local_irq_save</code> call before <code>kgdb_roundup_cpus</code>. </p>
<p> On non-SMP systems, this is not called.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
