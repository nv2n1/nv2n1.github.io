---
title: "rubibtex(1)"
name: "rubibtex"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rubibtex/"
description: "rubibtex – make a bibliography for (La)TeX using Russian letters as item names"
---

<h2>NAME</h2>
<p> rubibtex &#8211; make a bibliography for (La)TeX using Russian letters as item names </p>
<h2>SYNOPSIS</h2>
<p> <code>rubibtex</code> <i>BASENAME</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rubibtex</code> is used to run <code><a href="/docs/linux/man/1-bibtex/">bibtex</a></code>(1) on auxiliary files with Russian characters in item names (citation keys). It is part of the T2 package. </p>
<p> <code>rubibtex</code> copies the auxiliary file to <i>/tmp</i>, uses <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) to convert Cyrillic character commands to their 8-bit ASCII equivalents; runs <code><a href="/docs/linux/man/1-bibtex/">bibtex</a></code>(1) on the modified file; and finally moves the original auxiliary file back (overwriting the modified file). </p>
<p> <code>rubibtex</code> assumes that the <code><a href="/docs/linux/man/1-bibtex/">bibtex</a></code>(1) database (<tt>bib</tt>) files are encoded with the KOI8-R encoding. </p>
<h2>FILES</h2>
<dl>
<dt>
<dd>
<dt><i>basename.aux</i></p>
<dd> LaTeX auxiliary file</p>
<dt>
<dd></dl>
<h2>BUGS</h2>
<p> None known, but report any bugs found to the authors. </p>
<h2>COPYRIGHT</h2>
<p> The T2 package is Copyright 1997-1999 Werner Lemberg, Vladimir Volovich and any individual authors listed elsewhere in package files. </p>
<p> It may be distributed under the conditions of the LaTeX Project Public License, either version 1.1 of this license or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bibtex/">bibtex</a></code>(1), <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1), &lt;<a href="ftp://ftp.vsu.ru/pub/tex/T2/README">ftp://ftp.vsu.ru/pub/tex/T2/README</a>&gt;. </p>
<h2>AUTHOR</h2>
<p> Werner Lemberg &lt;wl [at] gnu.org&gt;, Vladimir Volovich &lt;TeX [at] vvv.vsu.ru&gt;. </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
