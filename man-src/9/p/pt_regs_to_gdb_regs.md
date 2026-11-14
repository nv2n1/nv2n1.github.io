---
title: "pt_regs_to_gdb_regs(9)"
name: "pt_regs_to_gdb_regs"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pt_regs_to_gdb_regs/"
description: "pt_regs_to_gdb_regs – Convert ptrace regs to GDB regs"
---

<p>pt_regs_to_gdb_regs &#8211; Convert ptrace regs to GDB regs</p>
<h2>Synopsis</h2>
<pre><code>void pt_regs_to_gdb_regs(unsigned long *gdb_regs, struct pt_regs *regs);</code></pre>
<h2>Arguments</h2>
<p><i>gdb_regs</i></p>
<dl>
<dd>
<dd>A pointer to hold the registers in the order GDB wants.</dl>
<p> <i>regs</i></p>
<dl>
<dd>The struct pt_regs of the current process.</dl>
<h2>Description</h2>
<p>Convert the pt_regs in <i>regs</i> into the format for registers that GDB expects, stored in <i>gdb_regs</i>.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
