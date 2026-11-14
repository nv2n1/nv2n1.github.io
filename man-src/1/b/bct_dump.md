---
title: "bct_dump(1)"
name: "bct_dump"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bct_dump/"
description: "bct_dump – tegra BCT disassembly tool"
---

<h2 class="name">NAME</h2>
<p> bct_dump &#8211; tegra BCT disassembly tool </p>
<h2>SYNOPSIS</h2>
<p> <code>bct_dump</code> <i>bctfile</i></p>
<h2>DESCRIPTION</h2>
<p> This program is used to take a binary Tegra Boot Configuration Table (BCT) and disassemble it into a text format suitable to be compiled with <a href="/docs/linux/man/1-cbootimage/">cbootimage</a>(1). </p>
<h3>Platforms supported</h3>
<dl>
<dt>&bull;</p>
<dd> <code>Tegra20</code></p>
<dt>&bull;</p>
<dd> <code>Tegra30</code></p>
<dt>&bull;</p>
<dd> <code>Tegra114</code></p>
<dt>&bull;</p>
<dd> <code>Tegra124</code></p>
<dt>&bull;</p>
<dd> <code>Tegra132</code></p>
<dt>&bull;</p>
<dd> <code>Tegra210</code> </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>bctfile</i></p>
<dd> Specify the BCT file to disassemble </p>
</dl>
<h2>EXAMPLES</h2>
<p> To disassemble the BCT file for a Tegra124 Jetson-TK1: </p>
<pre><code>
$ bct_dump PM375_Hynix_2GB_H5TC4G63AFR_RDA_924MHz.bct
    Version = 0x00400001;
BlockSize = 0x00004000;
PageSize = 0x00000200;
PartitionSize = 0x01000000;
OdmData = 0x800d8000;
JtagCtrl = 0x00000000;
ChipUid = 0x00000000000000000000000000000000;
#Bootloader used = 0;
#Bootloaders max = 4;
#BCT size = 8192;
...
</code></pre>
<h2>RETURN VALUE</h2>
<p> If any error occurs a non zero exit status is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tegrarcm/">tegrarcm</a>(1),</code><a href="/docs/linux/man/1-cbootimage/">cbootimage</a>(1) </p>
<h2>Index</h2>
