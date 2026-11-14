---
title: "hp2ps(1)"
name: "hp2ps"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp2ps/"
description: "hp2ps – convert a heap profile to a POSTSCRIPT graph"
---

<h2 class="name">NAME</h2>
<p> hp2ps &#8211; convert a heap profile to a P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> graph </p>
<h2>SYNOPSIS</h2>
<p> <code>hp2ps</code> [flags] [file][.hp]</p>
<h2>DESCRIPTION</h2>
<p> The program <code>hp2ps</code> converts a heap profile stored in <i>file</i> into a P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> graph, sending the result to <i>file.ps.</i> By convention, files to be processed by <code>hp2ps</code> have a <i>.hp</i> extension. However, for compatibility with older versions of <code>hp2ps, </code> this extension can be omitted. If <i>file</i> is omitted entirely, then the program behaves as a filter.</p>
<h2>OPTIONS</h2>
<p> The flags are:</p>
<dl>
<dt><code>-d</code></p>
<dd> In order to make graphs more readable, <code>hp2ps</code> sorts the shaded bands for each identifier. The default sort ordering is for the bands with the largest area to be stacked on top of the smaller ones. The <code>-d</code> option causes rougher bands (those reprsenting series of values with the largest standard deviations) to be stacked on top of smoother ones.</p>
<dt><code>-b</code></p>
<dd> Normally, <code>hp2ps</code> puts the title of the graph in a small box at the top of the page. However, if the JOB string is too long to fit in a small box (more than 35 characters), then <code>hp2ps</code> will choose to use a big box instead. The <code>-b</code> option forces <code>hp2ps</code> to use a big box.</p>
<dt><code>-e</code> <i>float</i>[in|mm|pt]</p>
<dd> Generate encapsulated P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> suitable for inclusion in LaTeX documents. Usually, the P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> graph is drawn in landscape mode in an area 9 inches wide by 6 inches high, and <code>hp2ps</code> arranges for this area to be approximately centered on a sheet of a4 paper. This format is convenient of studying the graph in detail, but it is unsuitable for inclusion in LaTeX documents. The <code>-e </code> option causes the graph to be drawn in portrait mode, with <i>float</i> specifying the width in inches, millimetres or points (the default). The resulting P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> file conforms to the <i>Encapsulated Post Script</i> (EPS) convention, and it can be included in a LaTeX document using Rokicki&#8217;s dvi-to-P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> converter <code>dvips.</code> <code>hp2ps</code> requires the width to exceed 2 inches.</p>
<dt><code>-g</code></p>
<dd> Create output suitable for the <code>gs</code> P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> previewer (or similar). In this case the graph is printed in portrait mode without scaling. The output is unsuitable for a laser printer.</p>
<dt><code>-p</code></p>
<dd> Use previous parameters. By default, the P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> graph is automatically scaled both horizontally and vertically so that it fills the page. However, when preparing a seires of graphs for use in a presentation, it is often useful to draw a new graph using the same scale, shading and ordering as a previous one. The <code>-p</code> flag causes the graph to be drawn using the parameters determined by a previous run of <code>hp2ps</code> on <i>file.</i></p>
<dt><code>-s</code></p>
<dd> Use a small box for the title.</p>
<dt><code>-y</code></p>
<dd> Draw the graph in the traditional York style, ignoring marks.</p>
<dt><code>-?</code></p>
<dd> Print out usage information.</dl>
<h2>INPUT FORMAT</h2>
<p> The format of a heap profile is best described by example: </p>
<dl>
<dt>
<dd>
<pre>
JOB &quot;a.out -p&quot;
DATE &quot;Fri Apr 17 11:43:45 1992&quot;
SAMPLE_UNIT &quot;seconds&quot;
VALUE_UNIT &quot;bytes&quot;
BEGIN_SAMPLE 0.00
  SYSTEM 24
END_SAMPLE 0.00
BEGIN_SAMPLE 1.00
  elim 180
  insert 24
  intersect 12
  disin 60
  main 12
  reduce 20
  SYSTEM 12
END_SAMPLE 1.00
MARK 1.50
MARK 1.75
MARK 1.80
BEGIN_SAMPLE 2.00
  elim 192
  insert 24
  intersect 12
  disin 84
  main 12
  SYSTEM 24
END_SAMPLE 2.00
BEGIN_SAMPLE 2.82 
END_SAMPLE 2.82 
</dl>
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dvips/">dvips</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), hbchp (1), <a href="/docs/linux/man/1-lmlchp/">lmlchp</a>(1)<br />
 C. Runciman and D. Wakeling, <i>Heap Profiling for Lazy Functional Languages, YCS-172, University of York, 1992</i></p>
<h2>NOTES</h2>
<p> P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> is a registered trademark of Adobe Systems Incorporated.</p>
<h2>AUTHOR</h2>
<p> David Wakeling of the University of York. </p>
<h2>Index</h2>
