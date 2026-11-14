---
title: "rumakeindex(1)"
name: "rumakeindex"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rumakeindex/"
description: "rumakeindex – process a LaTeX index using Russian Cyrillic characters"
---

<h2>NAME</h2>
<p> rumakeindex &#8211; process a LaTeX index using Russian Cyrillic characters </p>
<h2>SYNOPSIS</h2>
<p> <code>rumakeindex</code> <i>basename</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rumakeindex</code> is used to run <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1) on <tt>idx</tt> files that use Russian characters. It is part of the T2 package. </p>
<p> <code>rumakeindex</code> runs <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) on the <tt>idx</tt> file to convert Cyrillic character commands to 8-bit ASCII characters; pipes the results through <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1); and then through <code><a href="/docs/linux/man/1-tr/">tr</a></code>(1) to do some final conversions. The results are placed in a KOI8-R encoded <tt>ind</tt> file. </p>
<h2>FILES</h2>
<dl>
<dt>
<dd>
<dt><i>basename.idx</i></p>
<dd> LaTeX index entry file</p>
<dt><i>basename.ilg</i></p>
<dd> LaTeX index log file</p>
<dt><i>basename.ind</i></p>
<dd> LaTeX processed index file</p>
<dt>
<dd></dl>
<h2>BUGS</h2>
<p> None known, but report any bugs found to the authors. </p>
<h2>COPYRIGHT</h2>
<p> The T2 package is Copyright 1997-1999 Werner Lemberg, Vladimir Volovich and any individual authors listed elsewhere in package files. </p>
<p> It may be distributed under the conditions of the LaTeX Project Public License, either version 1.1 of this license or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1), <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1), <code><a href="/docs/linux/man/1-tr/">tr</a></code>(1), &lt;<a href="ftp://ftp.vsu.ru/pub/tex/T2/README">ftp://ftp.vsu.ru/pub/tex/T2/README</a>&gt;. </p>
<h2>AUTHOR</h2>
<p> Werner Lemberg &lt;wl [at] gnu.org&gt;, Vladimir Volovich &lt;TeX [at] vvv.vsu.ru&gt;. </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
