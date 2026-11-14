---
title: "t1rawafm(1)"
name: "t1rawafm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1rawafm/"
description: "t1rawafm – produce raw AFM metrics from a PostScript Type 1 font"
---

<h2 class="name">NAME</h2>
<p> t1rawafm &#8211; produce raw AFM metrics from a PostScript Type 1 font </p>
<h2>SYNOPSIS</h2>
<p> <code>t1rawafm</code> [OPTIONS&#8230;] [<i>font</i> [<i>outputfile</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>T1rawafm</code> generates an AFM file with the information available in a PostScript Type~1 font. The AFM file will lack kerns, ligature information, and composite characters, but is otherwise usable. The AFM file is written to the standard output (but see the <code>&#8211;output</code> option). If no input font file is supplied, <code>t1rawafm</code> reads a PFA or PFB font from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;output</code>=<i>file</i>, <code>-o</code> <i>file</i></p>
<dd> Send output to <i>file</i> instead of standard output. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>RETURN VALUES</h2>
<p> <code>T1rawafm</code> exits with value 0 if an AFM metrics file was successfully generated, and 1 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i>, <i>Adobe Font Metrics File Format Specification v4.1</i></p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
