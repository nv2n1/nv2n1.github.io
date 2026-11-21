---
title: "vcd2vzt(1)"
name: "vcd2vzt"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcd2vzt/"
description: "vcd2vzt – Converts VCD files to VZT files"
---

<h2>NAME</h2>
<p> vcd2vzt &#8211; Converts VCD files to VZT files</p>
<h2>SYNTAX</h2>
<p> vcd2vzt [<i>option</i>]&#8230; [<i>VCDFILE</i>] [<i>VZTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts VCD files to VZT files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v,&#8211;vcdname</code> &lt;<i>filename</i>&gt;</dt>
<dd> Specify VCD input filename.</dd>
<dt><code>-l,&#8211;vztname</code> &lt;<i>filename</i>&gt;</dt>
<dd> Specify VZT output filename.</dd>
<dt><code>-d,&#8211;depth</code> &lt;<i>value</i>&gt;</dt>
<dd> Specify 0..9 gzip compression depth, default is 4.</dd>
<dt><code>-m,&#8211;maxgranule</code> &lt;<i>value</i>&gt;</dt>
<dd> Specify number of granules per section, default is 8. One granule is equal to 32 timesteps.</dd>
<dt><code>-b,&#8211;break</code> &lt;<i>value</i>&gt;</dt>
<dd> Specify break size (default = 0 = off). When the break size is exceeded, the VZT dumper will dump all state information at the next convenient granule plus dictionary boundary.</dd>
<dt><code>-z,&#8211;ziptype</code> &lt;<i>value</i>&gt;</dt>
<dd> Specify zip type (default = 0 gzip, 1 = bzip2, 2 = lzma). This allows you to override the default compression algorithm to use a more effective one at the expense of greater runtime. Note that bzip2 does not decompress as fast as gzip so the viewer will be about two times slower when decompressing blocks.</dd>
<dt><code>-t,&#8211;twostate</code></dt>
<dd> Forces MVL2 twostate mode (default is MVL4). When enabled, the trace will only store 0/1 values for binary facilities. This is useful for functional simulation and will speed up dumping as well as make traces somewhat smaller.</dd>
<dt><code>-r, &#8211;rle</code></dt>
<dd> Uses an bitwise RLE compression on the value table. Default is off. When enabled, this causes the trace data table to be stored using an alternate representation which can improve compression in many cases.</dd>
<dt><code>-h,&#8211;help</code></dt>
<dd> Show help screen.</dd>
</dl>
<h2>EXAMPLES</h2>
<p> Note that you should specify dumpfile.vcd directly or use &quot;-&quot; for stdin.</p>
<dl>
<dt>vcd2vzt dumpfile.vcd dumpfile.lxt &#8211;depth 9 &#8211;break 1073741824</dt>
<dd> This sets the compression level to 9 and sets the break size to 1GB.</dd>
<dt>vcd2vzt dumpfile.vcd dumpfile.lxt &#8211;depth 9 &#8211;maxgranule 512</dt>
<dd> Allows more granules per section which allows for greater compression at the expense of memory usage.</dd></dl>
<h2>LIMITATIONS</h2>
<p> <i>vcd2vzt</i> does not store glitches as these are coalesced together into one value change during the writing of the VZT file. </p>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vzt2vcd/">vzt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
