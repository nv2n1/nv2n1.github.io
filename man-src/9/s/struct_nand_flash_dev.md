---
title: "struct_nand_flash_dev(9)"
name: "struct_nand_flash_dev"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_flash_dev/"
description: "struct_nand_flash_dev – NAND Flash Device ID Structure"
---

<p>struct_nand_flash_dev &#8211; NAND Flash Device ID Structure</p>
<h2>Synopsis</h2>
<pre><code>struct nand_flash_dev {
    char *name;
    union ecc;
    int onfi_timing_mode_default;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>a human-readable name of the NAND chip</dl>
<p> ecc</p>
<dl>
<dd>The ECC step required by the <i>ecc</i>.strength_ds, same as the <i>ecc_step_ds</i> in nand_chip{}, also from the datasheet. For example, the &#8220;4bit ECC for each 512Byte&#8221; can be set with NAND_ECC_INFO(4, 512).</dl>
<p> onfi_timing_mode_default</p>
<dl>
<dd>the default ONFI timing mode entered after a NAND reset. Should be deduced from timings described in the datasheet.</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
