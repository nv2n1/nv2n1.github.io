---
title: "debugfs_print_regs32(9)"
name: "debugfs_print_regs32"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_print_regs32/"
---

debugfs_print_regs32 - use seq_print to describe a set of registers

<h2>Synopsis</h2>

<pre><code>void debugfs_print_regs32(struct seq_file *s, const struct debugfs_reg32 *regs, int nregs, void __iomem *base, char *prefix);</code></pre>

<h2>Arguments</h2>

<i>s</i>
<dl><dd><dd>the seq_file structure being used to generate output</dl>
 

 <i>regs</i>
<dl><dd>an array if struct debugfs_reg32 structures</dl>
 

 <i>nregs</i>
<dl><dd>the length of the above array</dl>
 

 <i>base</i>
<dl><dd>the base address to be used in reading the registers</dl>
 

 <i>prefix</i>
<dl><dd>a string to be prefixed to every output line</dl>

<h2>Description</h2>

This function outputs a text block describing the current values of some 32-bit hardware registers. It is meant to be used within debugfs files based on seq_file that need to show registers, intermixed with other information. The prefix argument may be used to specify a leading string, because some peripherals have several blocks of identical registers, for example configuration of dma channels

<h2>Copyright</h2>


