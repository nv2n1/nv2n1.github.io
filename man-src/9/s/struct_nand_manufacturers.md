---
title: "struct_nand_manufacturers(9)"
name: "struct_nand_manufacturers"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_manufacturers/"
description: "struct_nand_manufacturers – NAND Flash Manufacturer ID Structure"
---

<p>struct_nand_manufacturers &#8211; NAND Flash Manufacturer ID Structure</p>
<h2>Synopsis</h2>
<pre><code>struct nand_manufacturers {
    int id;
    char *name;
};</code></pre>
<h2>Members</h2>
<p>id</p>
<dl>
<dd>manufacturer ID code of device.</dd></dl>
<p> name</p>
<dl>
<dd>Manufacturer name</dd></dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
