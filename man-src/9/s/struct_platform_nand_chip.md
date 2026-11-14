---
title: "struct_platform_nand_chip(9)"
name: "struct_platform_nand_chip"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_platform_nand_chip/"
description: "struct_platform_nand_chip – chip level device structure"
---

<p>struct_platform_nand_chip &#8211; chip level device structure</p>
<h2>Synopsis</h2>
<pre><code>struct platform_nand_chip {
    int nr_chips;
    int chip_offset;
    int nr_partitions;
    struct mtd_partition *partitions;
    int chip_delay;
    unsigned int options;
    unsigned int bbt_options;
    const char **part_probe_types;
};</code></pre>
<h2>Members</h2>
<p>nr_chips</p>
<dl>
<dd>max. number of chips to scan for</dl>
<p> chip_offset</p>
<dl>
<dd>chip number offset</dl>
<p> nr_partitions</p>
<dl>
<dd>number of partitions pointed to by partitions (or zero)</dl>
<p> partitions</p>
<dl>
<dd>mtd partition list</dl>
<p> chip_delay</p>
<dl>
<dd>R/B delay value in us</dl>
<p> options</p>
<dl>
<dd>Option flags, e.g. 16bit buswidth</dl>
<p> bbt_options</p>
<dl>
<dd>BBT option flags, e.g. NAND_BBT_USE_FLASH</dl>
<p> part_probe_types</p>
<dl>
<dd>NULL-terminated array of probe types</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
