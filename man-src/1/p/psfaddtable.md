---
title: "psfaddtable(1)"
name: "psfaddtable"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psfaddtable/"
description: "psfaddtable – add a Unicode character table to a console font"
---

<h2 class="name">NAME</h2>
<p> psfaddtable &#8211; add a Unicode character table to a console font </p>
<h2>SYNOPSIS</h2>
<p> <code>psfaddtable</code> <i>fontfile tablefile outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>psfaddtable</code> takes a console font in .psf format given by <i>fontfile</i> and merges it with the Unicode character table given by <i>tablefile</i> to produce a font file with an embedded character table, which is written to <i>outfile</i>. An input file name of &quot;-&quot; denotes standard input, and an output file name of &quot;-&quot; denotes standard output. If the <i>fontfile</i> already contains an embedded character table, it is ignored.</p>
<h2>TABLE FILE FORMAT</h2>
<p> Each line in the <i>tablefile</i> should be either blank, contain a comment (preceded by <i>#</i>), or contain a sequence of numbers in either decimal (default), octal (preceded by <i>0</i>), or hexadecimal (preceded by <i>0x</i>) format, separated by spaces or tabs. The first number on each line indicates the glyph slot in the font that is being referred to, this is between 0 and 0xff for a 256-character font and 0 and 0x1ff for a 512-character font. Any subsequent numbers on the same line are Unicodes matched by this specific glyph slot. Instead of a single Unicode one may have a sequence of Unicodes separates by commas, to denote that the glyph depicts the corresponding composed symbol. It is permissible to have multiple lines for the same glyph.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/1-psfgettable/">psfgettable</a></code>(1), <code><a href="/docs/linux/man/1-psfstriptable/">psfstriptable</a></code>(1), <code><a href="/docs/linux/man/1-psfxtable/">psfxtable</a></code>(1) </p>
<h2>Index</h2>
