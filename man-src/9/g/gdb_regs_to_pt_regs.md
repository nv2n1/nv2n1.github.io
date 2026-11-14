---
title: "gdb_regs_to_pt_regs(9)"
name: "gdb_regs_to_pt_regs"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gdb_regs_to_pt_regs/"
description: "gdb_regs_to_pt_regs – Convert GDB regs to ptrace regs."
---

<p>gdb_regs_to_pt_regs &#8211; Convert GDB regs to ptrace regs.</p>
<h2>Synopsis</h2>
<pre><code>void gdb_regs_to_pt_regs(unsigned long *gdb_regs, struct pt_regs *regs);</code></pre>
<h2>Arguments</h2>
<p><i>gdb_regs</i></p>
<dl>
<dd>
<dd>A pointer to hold the registers we&#8217;ve received from GDB.</dl>
<p> <i>regs</i></p>
<dl>
<dd>A pointer to a struct pt_regs to hold these values in.</dl>
<h2>Description</h2>
<p>Convert the GDB regs in <i>gdb_regs</i> into the pt_regs, and store them in <i>regs</i>.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
