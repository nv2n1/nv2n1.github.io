---
title: "ttftotype42(1)"
name: "ttftotype42"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttftotype42/"
description: "ttftotype42 – create PostScript Type 42 wrapper of TrueType font"
---

<h2 class="name">NAME</h2>
<p> ttftotype42 &#8211; create PostScript Type 42 wrapper of TrueType font </p>
<h2>SYNOPSIS</h2>
<p> <code>ttftotype42</code> [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ttftotype42</code> converts TrueType or TrueType-flavored OpenType font programs into PostScript Type 42 format, which is a wrapper for the TrueType outlines. This conversion preserves all outlines and hint information from the original TrueType font. The Type 42 wrapper uses glyph names identical to those expected by or so encoding files suitable for TrueType fonts and <code>pdflatex</code> will also work for the Type 42 fonts and If the file <i>output</i> is not specified output goes to the standard output. If the file <i>input</i> is not specified input comes from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i> file</i>, <code>&#8211;output</code><i> file</i></p>
<dd> Write output font to <i>file</i> instead of the standard output. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not generate any error messages. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>SEE ALSO</h2>
<p> Adobe Technical Note #5012, <i>The Type 42 Font Format Specification</i> </p>
<p> <i>OpenType Specification</i>, Version 1.4</p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<p> The latest version is available from:<br />
 <a rel="nofollow" href="http://www.lcdf.org/type/">http://www.lcdf.org/type/</a> </p>
<h2>Index</h2>
