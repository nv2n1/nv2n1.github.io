---
title: "kgdb_arch_set_pc(9)"
name: "kgdb_arch_set_pc"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kgdb_arch_set_pc/"
description: "kgdb_arch_set_pc – Generic call back to the program counter"
---

<p>kgdb_arch_set_pc &#8211; Generic call back to the program counter</p>
<h2>Synopsis</h2>
<pre><code>void kgdb_arch_set_pc(struct pt_regs *regs, unsigned long pc);</code></pre>
<h2>Arguments</h2>
<p><i>regs</i></p>
<dl>
<dd>
<dd>Current struct pt_regs.</dl>
<p> <i>pc</i></p>
<dl>
<dd>The new value for the program counter</dl>
<h2>Description</h2>
<p>This function handles updating the program counter and requires an architecture specific implementation.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
