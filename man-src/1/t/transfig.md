---
title: "transfig(1)"
name: "transfig"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transfig/"
description: "transfig – creates a makefile for portable LaTeX figures"
---

<h2 class="name">NAME</h2>
<p> transfig &#8211; creates a makefile for portable LaTeX figures </p>
<h2>SYNOPSIS</h2>
<p> <code>transfig</code> [ -L <i>language</i> ] [ -M <i>makefile</i> ] [ -T <i>texfile</i> ] [ -I <i>macrofile</i> ] [ -V ] [ <i>control_specs</i> figfile &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Transfig</i> creates a makefile to translate figures described in Fig code or PIC into a specified LaTeX graphics <i>language</i>. PIC files are identified by the suffix &quot;.pic&quot;; Fig files can be specified either with or without the suffix &quot;.fig&quot; . Transfig also creates a TeX macro file appropriate to the target language.</p>
<h2>OPTIONS</h2>
<p> The <i>language</i> specifier must be one of <code>box,</code> <code>cgm,</code> <code>eepic,</code> <code>eepicemu,</code> <code>emf,</code> <code>epic,</code> <code>eps,</code> <code>ge,</code> <code>gif,</code> <code>ibmgl,</code> <code>jpeg,</code> <code>latex,</code> <code>map,</code> <code>mf,</code> <code>mmp,</code> <code>mp,</code> <code>pcx,</code> <code>pdf,</code> <code>pdftex,</code> <code>pdftex_t,</code> <code>pic,</code> <code>pictex,</code> <code>png,</code> <code>ppm,</code> <code>ps,</code> <code>psfig,</code> <code>pstex,</code> <code>pstex_t,</code> <code>ptk,</code> <code>sld,</code> <code>textyl,</code> <code>tiff,</code> <code>tk,</code> <code>tpic,</code> <code>xbm,</code> <code>xpm</code> or <code>null</code>. The specifier <code>psfig</code> is like the <code>ps</code> specifier, except that it make use of the psfig macro package. The specifier <code>pstex</code> is like <code>psfig,</code> except that it uses LaTeX to process formatted (special) text. The specifier <code>null</code> results in the figures being replaced by empty boxes of the appropriate size. If no language is specified, <code>epic</code> is the default. </p>
<p> The names of the makefile and TeX macro file can be set with the -M and -T options. The default names are &quot;Makefile&quot; and &quot;transfig.tex&quot;, respectively. If there is already an existing <i>makefile</i> in the directory, transfig first renames it to <i>makefile~</i>. The same holds for any existing TeX macro file. If the -I option is specified, then a command to read in <i>macrofile</i> is <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>inserted into the TeX macro file.<br />
 If the -V option is specified, the program version number is printed only. </p>
<p> Control specifiers are</p>
<dl>
<dt><code>-m</code><i> mag</i></p>
<dd> set the magnification at which the figure is rendered (default 1.0).</p>
<dt><code>-f</code><i> font</i></p>
<dd> set the default font family used for text objects (default &quot;<code>rm</code>&quot;).</p>
<dt><code>-s </code><i>fontsize</i></p>
<dd> set the default font size (in points) for text objects (default 11*<i>mag</i>).</p>
<dt><code>-o </code><i>option</i></p>
<dd> pass the specified option string through to fig2dev.</dl>
<p> If there is no scaling, the default font is an eleven point roman font. Language and control specifiers may occur more than once; they affect the translation of files which appear to their right in the argument list. If no files are specified, then &quot;*.fig&quot; is assumed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/l-fig/">fig</a>(l), <a href="/docs/linux/man/l-fig2dev/">fig2dev</a>(l), <a href="/docs/linux/man/l-pic/">pic</a>(l), <a href="/docs/linux/man/l-pic2fig/">pic2fig</a>(l), <a href="/docs/linux/man/l-xfig/">xfig</a>(l)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1985 Supoj Sutantavibul<br />
 Copyright (C) 1991 Micah Beck<br />
 Parts Copyright (C) 1991-2002 Brian Smith </p>
<p> THE AUTHORS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. </p>
<p> Any party obtaining a copy of these files is granted, free of charge, a full and unrestricted irrevocable, world-wide, paid up, royalty-free, nonexclusive right and license to deal in this software and documentation files (the &quot;Software&quot;), including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons who receive copies from any such party to do so, with the only requirement being that this copyright notice remain intact. </p>
<h2>AUTHOR</h2>
<p> Micah Beck </p>
<h2>Index</h2>
