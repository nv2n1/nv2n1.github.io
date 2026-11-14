---
title: "fst2vcd(1)"
name: "fst2vcd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fst2vcd/"
description: "fst2vcd – Converts FST files to VCD"
---

<h2>NAME</h2>
<p> fst2vcd &#8211; Converts FST files to VCD</p>
<h2>SYNTAX</h2>
<p> fst2vcd [<i>option</i>]&#8230; [<i>FSTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts FST files to VCD files. If an output filename is not specified, the VCD is emitted to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f,&#8211;fstname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify FST input filename.</p>
<dt><code>-o,&#8211;output</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify optional VCD output filename.</p>
<dt><code>-e,&#8211;extensionsFr</p>
<dd> Emit FST extensions to VCD. Enabling this may create VCD files unreadable by other tools. This is generally intended to be used as a debugging tool when developing FST writer interfaces to simulators.</p>
<dt>-h,&#8211;help</code></p>
<dd> Display help then exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type:</p>
<dl>
<dt>fst2vcd filename.fst</p>
<dd> The VCD conversion is emitted to stdout.</dl>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vcd2fst/">vcd2fst</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
