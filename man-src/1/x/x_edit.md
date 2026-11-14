---
title: "x_edit(1)"
name: "x_edit"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_edit/"
description: "x_edit – convert between binary and ASCII crossover correction tables."
---

<h2>NAME</h2>
<p> <code>x_edit</code> &#8211; convert between binary and ASCII crossover correction tables.</p>
<h2>SYNOPSIS</h2>
<p> <code>x_edit</code> <code>-A</code>|<code>X</code>[<i>name</i>] <code>-O</code>[<i>outname</i>]</p>
<h2>DESCRIPTION</h2>
<p> The purpose of <code>x_edit</code> is to convert between ASCII and binary versions of the crossover correction tables.</p>
<dl>
<dt><code>-A</code></p>
<dd> Name of ASCII correction table [stdin], write binary table to file given by <code>-O</code> [stdout].</p>
<dt><code>-X</code></p>
<dd> Name of binary correction table [stdin], write ASCII table to file given by <code>-O</code> [stdout].</p>
<dt><code>-O</code></p>
<dd> Name of output correction table [stdout].</dl>
<h2>EXAMPLES</h2>
<p> To convert the binary file crossover_corr.b to ASCII and write to stdout, run </p>
<p> <code>x_edit -X</code>crossover_corr.b &gt; corrections.d </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
