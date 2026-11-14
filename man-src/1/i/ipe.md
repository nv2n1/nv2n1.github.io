---
title: "ipe(1)"
name: "ipe"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipe/"
description: "ipe – drawing editor for creating figures in PDF or PS formats"
---

<h2 class="name">NAME</h2>
<p> ipe &#8211; drawing editor for creating figures in PDF or PS formats </p>
<h2>SYNOPSIS</h2>
<p> <code>ipe</code> [ <i>Qt options</i> ] [ -debug ] [ -sheet <i>stylesheet</i> ] [ -geom <i>WxH+X+Y</i> ] <i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> Ipe is a program that supports making small figures for inclusion into LaTeX documents as well as making multi-page PDF presentations. </p>
<p> This manual page only documents the command line options and environment variables. Full documentation for using Ipe can be found in HTML and PDF format; see below. </p>
<dl>
<dt><code>-sheet</code> <i>stylesheet</i></p>
<dd> add the Ipe style sheet in the indicated file to all newly created Ipe documents.</p>
<dt><code>-geom</code> <i>WxH+X+Y</i></p>
<dd> display the first Ipe window with the given position and size.</p>
<dt><code>-debug</code></p>
<dd> display debug output on stderr. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Ipe respects the following environment variables: </p>
<dl>
<dt><code>IPELATEXDIR</code></p>
<dd> the directory where Ipe runs Pdflatex. </p>
<dt><code>IPEPDFLATEX</code></p>
<dd> the name of the Pdflatex executable. If Pdflatex is on your path, the value <i>pdflatex</i> is sufficient. </p>
<dt><code>IPEBINDIR</code></p>
<dd> the directory containing the <i>ipe5toxml</i> program (it is run by Ipe to open Ipe 5 documents). </p>
<dt><code>IPEDOCDIR</code></p>
<dd> the directory containing the Ipe documentation. </p>
<dt><code>IPELANGDIR</code></p>
<dd> the directory containing user interface localization for Ipe. (No such localization exists yet.) </p>
<dt><code>IPEFONTMAP</code></p>
<dd> the complete path of the font map, describing where Ipe can find the 14 standard PDF fonts. </p>
<dt><code>IPEBROWSER</code></p>
<dd> the name of the HTML browser to be used to display the Ipe on-line manual. (If Ipe was linked with KDE, this value is not used.) </p>
<dt><code>IPELETPATH</code></p>
<dd> a list of directories where Ipe looks for ipelets. Directories are separated by &quot;:&quot; on Unix, and by &quot;;&quot; on Windows. </p>
<dt><code>TEXINPUTS</code></p>
<dd> when running Pdflatex, Ipe prepends both the current directory (where Ipe was started) as the directory containing the current document to the <code>TEXINPUTS</code> environment variable. </p>
</dl>
<h2>AUTHOR</h2>
<p> Otfried Cheong </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs using Ipe bugzilla at <i><a rel="nofollow" href="http://tclab.kaist.ac.kr/ipe/bugzilla.html">http://tclab.kaist.ac.kr/ipe/bugzilla.html</a></i> </p>
<h2>SEE ALSO</h2>
<p> Ipe is documented fully in <i>The Ipe Manual</i>, which can be found in <i>/usr/share/doc/ipe/manual.html</i> or in pdf format in <i>/usr/share/doc/ipe/manual.pdf</i>. </p>
<h2>Index</h2>
