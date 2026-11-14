---
title: "struct_nand_data_interface(9)"
name: "struct_nand_data_interface"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_data_interface/"
description: "struct_nand_data_interface – NAND interface timing"
---

<p>struct_nand_data_interface &#8211; NAND interface timing</p>
<h2>Synopsis</h2>
<pre><code>struct nand_data_interface {
    enum nand_data_interface_type type;
    union timings;
};</code></pre>
<h2>Members</h2>
<p>type</p>
<dl>
<dd>type of the timing</dl>
<p> timings</p>
<dl>
<dd>The timing, type according to <i>type</i></dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
