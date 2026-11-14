---
title: "vcd2fst(1)"
name: "vcd2fst"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcd2fst/"
description: "vcd2fst – Converts VCD files to FST files"
---

<h2>NAME</h2>
<p> vcd2fst &#8211; Converts VCD files to FST files</p>
<h2>SYNTAX</h2>
<p> vcd2fst [<i>option</i>]&#8230; [<i>VCDFILE</i>] [<i>FSTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts VCD files to FST files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v,&#8211;vcdname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify VCD/FSDB/VPD/WLF input filename. Processing of filetypes other than VCD requires that the appropriate 2vcd converter was found during ./configure.</p>
<dt><code>-f,&#8211;fstname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify FST output filename.</p>
<dt><code>-4,&#8211;fourpack</code></p>
<dd> Indicates that LZ4 should be used for value change data (default).</p>
<dt><code>-F,&#8211;fastpack</code></p>
<dd> Indicates that fastlz should be used instead of LZ4 for value change data.</p>
<dt><code>-4,&#8211;zlibpack</code></p>
<dd> Indicates that zlib should be used instead of LZ4 for value change data.</p>
<dt><code>-c,&#8211;compress</code></p>
<dd> Indicates that the entire file should be run through gzip on close. This results in much smaller files at the expense of a one-time decompression penalty on file open during reads.</p>
<dt><code>-p,&#8211;parallel</code></p>
<dd> Indicates that parallel mode should be enabled. This spawns a worker thread to continue with FST block processing while conversion continues on the main thread for new FST block data.</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Show help screen.</p>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> Note that you should specify dumpfile.vcd directly or use &quot;-&quot; for stdin.</p>
<dl>
<dt>vcd2fst dumpfile.vcd dumpfile.fst &#8211;compress</p>
<dd> This indicates that the FST file should be post-compressed on close.</dl>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fst2vcd/">fst2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt/">vcd2lxt</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2vzt/">vcd2vzt</a></i>(1) <i><a href="/docs/linux/man/1-vzt2vcd/">vzt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
