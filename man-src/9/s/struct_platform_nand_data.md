---
title: "struct_platform_nand_data(9)"
name: "struct_platform_nand_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_platform_nand_data/"
description: "struct_platform_nand_data – container structure for platform-specific data"
---

<p>struct_platform_nand_data &#8211; container structure for platform-specific data</p>
<h2>Synopsis</h2>
<pre><code>struct platform_nand_data {
    struct platform_nand_chip chip;
    struct platform_nand_ctrl ctrl;
};</code></pre>
<h2>Members</h2>
<p>chip</p>
<dl>
<dd>chip level chip structure</dl>
<p> ctrl</p>
<dl>
<dd>controller level device structure</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
