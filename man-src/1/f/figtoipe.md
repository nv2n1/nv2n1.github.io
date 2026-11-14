---
title: "figtoipe(1)"
name: "figtoipe"
section: "1"
letter: "f"
url: "/docs/linux/man/1-figtoipe/"
description: "figtoipe – Convert FIG figures into Ipe format"
---

<h2 class="name">NAME</h2>
<p> figtoipe &#8211; Convert FIG figures into Ipe format </p>
<h2>SYNOPSIS</h2>
<p> <code>figtoipe </code> [-g] [-p <i>preamble</i>] <i>FIGfile</i> <i>XMLfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>figtoipe</code> converts files in FIG format (as created, e.g., by <code>xfig</code>) to Ipe&#8217;s XML format. </p>
<p> <code>figtoipe</code> is not complete. The main lacking feature is the conversion of splines. Arc-boxes are replaced by rectangles. Feel free to improve this version! </p>
<p> The drawing models of FIG and Ipe are somewhat different. Ipe does not support depth ordering independent of grouping, pattern fill, and Postscript fonts. </p>
<p> <code>figtoipe</code> tries to include images specified in the XFIG file. For JPEG pictures, it tries include the compressed image data into the XML file. For files not recognized as JPEG, <code>anytopnm</code> is called; its output is compressed and included in the XML file. Some output of <code>anytopnm</code> might be rejected (e.g. images larger than 5000&#215;5000 pixels or B&amp;W bitmaps), or misunderstood. </p>
<h2>OPTIONS</h2>
<p> <code>-g</code> group the figure in the output XML</p>
<dl>
<dt><code>-p </code><i>latex</i></p>
<dd> add <i>latex</i> as a preamble to the generated XML file, e.g. </p>
<pre>
'
