---
title: "vcd2lxt2(1)"
name: "vcd2lxt2"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcd2lxt2/"
description: "vcd2lxt2 – Converts VCD files to LXT2 files"
---

<h2>NAME</h2>
<p> vcd2lxt2 &#8211; Converts VCD files to LXT2 files</p>
<h2>SYNTAX</h2>
<p> vcd2lxt2 [<i>option</i>]&#8230; [<i>VCDFILE</i>] [<i>LXTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts VCD files to LXT2 files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v,&#8211;vcdname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify VCD input filename.</p>
<dt><code>-l,&#8211;lxtname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify LXT2 output filename.</p>
<dt><code>-d,&#8211;depth</code> &lt;<i>value</i>&gt;</p>
<dd> Specify 0..9 gzip compression depth, default is 4.</p>
<dt><code>-m,&#8211;maxgranule</code> &lt;<i>value</i>&gt;</p>
<dd> Specify number of granules per section, default is 8. One granule is equal to 32 timsteps.</p>
<dt><code>-b,&#8211;break</code> &lt;<i>value</i>&gt;</p>
<dd> Specify break size (default = 0 = off). When the break size is exceeded, the LXT2 dumper will dump all state information at the next convenient granule plus dictionary boundary.</p>
<dt><code>-p,&#8211;partialmode</code> &lt;<i>mode</i>&gt;</p>
<dd> Specify partial zip mode 0 = monolithic, 1 = separation. Using a value of 1 expands LXT2 filesize but provides fast access for very large traces. Note that the default mode is neither monolithic nor separation: partial zip is disabled.</p>
<dt><code>-c,&#8211;checkpoint</code> &lt;<i>mode</i>&gt;</p>
<dd> Specify checkpoint mode. 0 is on which is default, and 1 is off. This is disabled when the break size is active.</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Show help screen.</p>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> Note that you should specify dumpfile.vcd directly or use &quot;-&quot; for stdin.</p>
<dl>
<dt>vcd2lxt dumpfile.vcd dumpfile.lxt &#8211;depth 9 &#8211;break 1073741824</p>
<dd> This sets the compression level to 9 and sets the break size to 1GB.</p>
<dt>vcd2lxt dumpfile.vcd dumpfile.lxt &#8211;depth 9 &#8211;maxgranule 256</p>
<dd> Allows more granules per section which allows for greater compression.</dl>
<h2>LIMITATIONS</h2>
<p> <i>vcd2lxt2</i> does not store glitches as these are coalesced together into one value change during the writing of the LXT2 file. </p>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
