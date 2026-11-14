---
title: "vzt2vcd(1)"
name: "vzt2vcd"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vzt2vcd/"
description: "vzt2vcd – Converts VZT files to VCD"
---

<h2>NAME</h2>
<p> vzt2vcd &#8211; Converts VZT files to VCD</p>
<h2>SYNTAX</h2>
<p> vzt2vcd [<i>option</i>]&#8230; [<i>VZTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts VZT files to VCD files. If an output filename is not specified, the VCD is emitted to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v,&#8211;vztname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify VZT input filename.</p>
<dt><code>-o,&#8211;output</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify optional VCD output filename.</p>
<dt><code>-f,&#8211;flatearth</code></p>
<dd> Emit flattened hierarchies.</p>
<dt><code>-c,&#8211;coalesce</code></p>
<dd> Coalesce bitblasted vectors.</p>
<dt><code>-n,&#8211;notruncate</code></p>
<dd> Do not shorten bitvectors. This disables binary value compression as described in the IEEE-1364 specification. (i.e., all values except for &#8216;1&#8217; left propagate as a sign bit on vectors which do not fill up their entire declared width)</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Display help then exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type:</p>
<dl>
<dt>vzt2vcd filename.vzt</p>
<dd> The VCD conversion is emitted to stdout.</dl>
<h2>LIMITATIONS</h2>
<p> <i>vzt2vcd</i> does not re-create glitches as these are coalesced together into one value change during the writing of the VZT file. </p>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt/">vcd2lxt</a></i>(1) <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
