---
title: "evcd2vcd(1)"
name: "evcd2vcd"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evcd2vcd/"
description: "evcd2vcd – Converts EVCD files to VCD files"
---

<h2>NAME</h2>
<p> evcd2vcd &#8211; Converts EVCD files to VCD files</p>
<h2>SYNTAX</h2>
<p> evcd2vcd [<i>option</i>]&#8230; [<i>EVCDFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts EVCD files with bidirectional port definitions to VCD files with separate in and out ports.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f,&#8211;filename</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify EVCD input filename.</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Show help screen.</p>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> Note that you should specify dumpfile.vcd directly or use &quot;-&quot; for stdin.</p>
<dl>
<dt>evcd2vcd dumpfile.evcd</p>
<dd> VCD is emitted to stdout.</dl>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vcd2fst/">vcd2fst</a></i>(1) <i><a href="/docs/linux/man/1-fst2vcd/">fst2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt/">vcd2lxt</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2vzt/">vcd2vzt</a></i>(1) <i><a href="/docs/linux/man/1-vzt2vcd/">vzt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
