---
title: "e2freefrag(8)"
name: "e2freefrag"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2freefrag/"
description: "e2freefrag – report free space fragmentation information"
---

<p>e2freefrag &#8211; report free space fragmentation information</p>
<h2>Synopsis</h2>
<p><code>e2freefrag</code> [ <code>-c chunk_kb</code> ] [ <code>-h</code> ] <code>filesys</code> </p>
<h2>Description</h2>
<p><code>e2freefrag</code> is used to report free space fragmentation on ext2/3/4 file systems. <i>filesys</i> is the file system device name (e.g. <i>/dev/hdc1</i>, <i>/dev/md0</i>). The <code>e2freefrag</code> program will scan the block bitmap information to check how many free blocks are present as contiguous and aligned free space. The percentage of contiguous free blocks of size and of alignment <i>chunk_kb</i> is reported. It also displays the minimum/maximum/average free chunk size in the file system, along with a histogram of all free chunks. This information can be used to gauge the level of free space fragmentation in the file system.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> chunk_kb</i></p>
<dd>If a chunk size is specified, then <code>e2freefrag</code> will print how many free chunks of size <i>chunk_kb</i> are available in units of kilobytes (Kb). The chunk size must be a power of two and be larger than file system block size.</p>
<dt><code>-h</code></p>
<dd>Print the usage of the program.</dl>
<h2>Example</h2>
<p># e2freefrag /dev/vgroot/lvhome<br />
 Device: /dev/vgroot/lvhome<br />
 Blocksize: 4096 bytes<br />
 Total blocks: 1504085<br />
 Free blocks: 292995 (19.5%) </p>
<p> Min. free extent: 4 KB<br />
 Max. free extent: 24008 KB<br />
 Avg. free extent: 252 KB </p>
<p> HISTOGRAM OF FREE EXTENT SIZES:<br />
 Extent Size Range : Free extents Free Blocks Percent </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4K&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;704&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;704&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.2% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8K&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;16K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;810&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1979&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.7% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16K&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;32K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;843&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4467&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1.5% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;32K&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;64K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;579&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6263&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2.1% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;64K&#8230;&nbsp;<wbr>&nbsp;128K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;493&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;11067&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3.8% </p>
<p>&nbsp;<wbr>&nbsp;128K&#8230;&nbsp;<wbr>&nbsp;256K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;394&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;18097&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6.2% </p>
<p>&nbsp;<wbr>&nbsp;256K&#8230;&nbsp;<wbr>&nbsp;512K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;281&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;25477&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8.7% </p>
<p>&nbsp;<wbr>&nbsp;512K&#8230; 1024K- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;253&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;44914&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;15.3% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1M&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2M- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;143&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;51897&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;17.7% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2M&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4M- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;73&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;50683&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;17.3% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4M&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8M- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;37&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;52417&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;17.9% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8M&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;16M- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;19028&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6.5% </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16M&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;32M- :&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2.0%</p>
<h2>Author</h2>
<p>This version of e2freefrag was written by Rupesh Thakare, and modified by Andreas Dilger &lt;adilger [at] sun.com&gt;, and Kalpak Shah.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-debugfs/">debugfs</a></i>(8), <i><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></i>(8), <i><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></i>(8) </p>
