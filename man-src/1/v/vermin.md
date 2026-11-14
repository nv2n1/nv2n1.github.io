---
title: "vermin(1)"
name: "vermin"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vermin/"
description: "vermin – Parses and processes Verilog HDL files"
---

<h2>NAME</h2>
<p> vermin &#8211; Parses and processes Verilog HDL files</p>
<h2>SYNTAX</h2>
<p> vermin [<i>VERILOGFILE</i>]&#8230; [<i>option</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Parses Verilog HDL files for use by other tools. The Verilog grammar used is 1364-1995.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h[elp]</code></p>
<dd> Prints out help screen.</p>
<dt><code>-emitmono </code><i>fname</i></p>
<dd> Emit monolithic (parser view of) file to <i>fname</i>.</p>
<dt><code>-emitstems</code></p>
<dd> Emit source code stems to stdout.</p>
<dt><code>-emitvars</code></p>
<dd> Emit source code variables to stdout.</p>
<dt><code>-D</code><i>x</i>=<i>y</i></p>
<dd> Equivalent to `define <i>X Y</i> in source.</p>
<dt><code>+define+</code><i>x</i>=<i>y</i></p>
<dd> Equivalent to `define <i>X Y</i> in source.</p>
<dt><code>+incdir+</code><i>dirname</i></p>
<dd> Add <i>dirname</i> to include search path.</p>
<dt><code>+libext+</code><i>ext</i></p>
<dd> Add <i>ext</i> to filename when searching for files.</p>
<dt><code>-pragma </code><i>name</i></p>
<dd> Add <i>name</i> (synopsys, verilint, vertex) to accepted pragmas. Note that &quot;vertex&quot; is for legacy reasons; the executable name has since changed to avoid name clashes with an existing 3D modeling program.</p>
<dt><code>-y </code><i>dirname</i></p>
<dd> Add directory <i>dirname</i> to source input path.</p>
<dt><code>-yi </code><i>dirname</i></p>
<dd> Add directory <i>dirname</i> to source input path (case insensitive search).</p>
<dt><code>-f </code><i>filename</i></p>
<dd> Insert args from filename. Does not work recursively.</dl>
<h2>EXAMPLES</h2>
<p> The following indicates that the library extension is .v and that the include directory is the current working directory and that the library directory is also the current working directory. Stems generation is enabled to generate a stems file for use with other tools. Various compile-time defines are also defined on the command line.</p>
<dl>
<dt>vermin XYZ450AC6V1.v -emitstems -y . +incdir+. +libext+.v -DUTLB_OutputData=0 -D__PORTALS_VERILOG__</p>
<dd></dl>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rtlbrowse/">rtlbrowse</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
