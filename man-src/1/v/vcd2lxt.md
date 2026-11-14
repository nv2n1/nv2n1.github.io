---
title: "vcd2lxt(1)"
name: "vcd2lxt"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcd2lxt/"
description: "vcd2lxt – Converts VCD files to interlaced or linear LXT files"
---

<h2>NAME</h2>
<p> vcd2lxt &#8211; Converts VCD files to interlaced or linear LXT files</p>
<h2>SYNTAX</h2>
<p> vcd2lxt [<i>VCDFILE</i>] [<i>LXTFILE</i>] [<i>option</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Converts VCD files to interlaced or linear LXT files. Noncompressed interlaced files will provide the fastest access, linear files will provide the slowest yet have the greatest compression ratios.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-stats</code></p>
<dd> Prints out statistics on all nets in VCD file in addition to performing the conversion.</p>
<dt><code>-clockpack</code></p>
<dd> Apply two-way subtraction algorithm in order to identify nets whose value changes by a constant XOR or whose value increases/decreases by a constant amount per constant unit of time. This option can reduce dumpfile size dramatically as value changes can be represented by an equation rather than explicitly as a triple of time, net, and value.</p>
<dt><code>-chgpack</code></p>
<dd> Emit data to file after being filtered through zlib (gzip).</p>
<dt><code>-linear</code></p>
<dd> Write out LXT in &quot;linear&quot; format with no backpointers. These are re-generated during initialization in <i>gtkwave</i>. Additionally, use libbz2 (bzip2) as the compression filter.</p>
<dt><code>-dictpack</code> &lt;<i>size</i>&gt;</p>
<dd> Store value changes greater than or equal to <i>size</i> bits as an index into a dictionary. Experimentation shows that a value of 18 is optimal for most cases.</dl>
<h2>EXAMPLES</h2>
<p> Note that you should specify dumpfile.vcd directly or use &quot;-&quot; for stdin.</p>
<dl>
<dt>vcd2lxt dumpfile.vcd dumpfile.lxt -clockpack -chgpack -dictpack 18</p>
<dd> This turns on clock packing, zlib compression, and enables the dictionary encoding. Note that using no options writes out a normal LXT file.</p>
<dt>vcd2lxt dumpfile.vcd dumpfile.lxt -clockpack -linear -dictpack 18</p>
<dd> Uses linear mode for even smaller files.</dl>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
