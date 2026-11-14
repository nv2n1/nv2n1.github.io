---
title: "rtlbrowse(1)"
name: "rtlbrowse"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rtlbrowse/"
description: "rtlbrowse – Allows hierarchical browsing of Verilog HDL source code and library design files."
---

<h2>NAME</h2>
<p> rtlbrowse &#8211; Allows hierarchical browsing of Verilog HDL source code and library design files.</p>
<h2>SYNTAX</h2>
<p> rtlbrowse &lt;<i>stemsfilename</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> Allows hierarchical browsing of Verilog HDL source code and library design files. Navigation through the hierarchy may be done by clicking open areas of the tree widget and clicking on the individual levels of hierarchy. Inside the source code, selecting the module instantiation name by double clicking or selecting part of the name through drag-clicking will descend deeper into the RTL hierarchy. Note that it performs optional source code annotation when called as a helper application by <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) and when the primary marker is set. Source code annotation is not available for all supported dumpfile types. It is directly available for LXT2, VZT, FST, and AET2. For VCD, use the <code>-o</code>,<code>&#8211;optimize</code> option of <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) in order to optimize the VCD file into FST. All other dumpfile types (LXT, GHW) are unsupported at this time.</p>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type:</p>
<dl>
<dt>rtlbrowse stemsfile</p>
<dd> The RTL is then brought up in a GTK tree viewer. Stems must have been previously generated with <i><a href="/docs/linux/man/1-vermin/">vermin</a></i>(1) or some other tool capable of generating compatible stemsfiles. Note that <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) will bring up this program as a client application for source code annotation. It does that by bringing up the viewer with the shared memory ID of a segment of memory in the viewer rather than using a stems filename.</dl>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vermin/">vermin</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
