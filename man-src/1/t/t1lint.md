---
title: "t1lint(1)"
name: "t1lint"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1lint/"
description: "t1lint – check a PostScript Type 1 font for correctness"
---

<h2 class="name">NAME</h2>
<p> t1lint &#8211; check a PostScript Type 1 font for correctness </p>
<h2>SYNOPSIS</h2>
<p> <code>t1lint</code> <i>font</i> [<i>font</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>T1lint</code> checks PostScript Type 1 font programs for correctness. Any errors or variances from the specification are reported to standard error. If there are no errors, the command prints nothing. It exits with status 0 if all fonts were OK, and status 1 otherwise. If no input files are supplied, t1lint reads a font from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not generate any error messages. The only output will be the exit status. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i></p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
