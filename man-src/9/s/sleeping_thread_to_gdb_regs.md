---
title: "sleeping_thread_to_gdb_regs(9)"
name: "sleeping_thread_to_gdb_regs"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sleeping_thread_to_gdb_regs/"
description: "sleeping_thread_to_gdb_regs – Convert ptrace regs to GDB regs"
---

<p>sleeping_thread_to_gdb_regs &#8211; Convert ptrace regs to GDB regs</p>
<h2>Synopsis</h2>
<pre><code>void sleeping_thread_to_gdb_regs(unsigned long *gdb_regs, struct task_struct *p);</code></pre>
<h2>Arguments</h2>
<p><i>gdb_regs</i></p>
<dl>
<dd>
<dd>A pointer to hold the registers in the order GDB wants.</dl>
<p> <i>p</i></p>
<dl>
<dd>The struct task_struct of the desired process.</dl>
<h2>Description</h2>
<p>Convert the register values of the sleeping process in <i>p</i> to the format that GDB expects. This function is called when kgdb does not have access to the struct pt_regs and therefore it should fill the gdb registers <i>gdb_regs</i> with what has been saved in struct thread_struct thread field during switch_to.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
