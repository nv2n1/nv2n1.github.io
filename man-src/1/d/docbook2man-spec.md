---
title: "docbook2man-spec(1)"
name: "docbook2man-spec"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docbook2man-spec/"
description: "docbook2man-spec.pl – convert DocBook RefEntries to man pages"
---

<h2 class="name">NAME</h2>
<p> docbook2man-spec.pl &#8211; convert DocBook RefEntries to man pages </p>
<h2>SYNOPSIS</h2>
<p> <code>sgmlspl</code> <code>docbook2man-spec.pl</code> </p>
<p> <code>nsgmls</code> [ <i>sgml document</i> ]<code>| sgmlspl</code> <code>docbook2man-spec.pl</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>docbook2man</code> is a sgmlspl spec file that produced man pages (using the -man macros) from DocBook RefEntry markup. </p>
<p> The program reads ESIS produced by nsgmls (or other SGML parsers) from standard input. Markup not found in RefEntry is discarded. </p>
<p> Its output, the converted man pages, are written to the current directory. If RefMeta information is not specified in a RefEntry, then the man page will be written to standard output. </p>
<p> The file <i>manpage.links</i> will also be created, which contains any aliases of the manpages generated. This file is in the format: </p>
<pre>
<i>&lt;man page&gt;</i> <i>&lt;alias
manpage&gt;</i>
</pre>
<p> The <i>manpage.refs</i> file keeps track of XRef references. Note that if the input document has any forward references, then <code>docbook2man</code> may have to be invoked twice (the first time updating <i>manpage.refs</i>) to resolve them.</p>
<h2>REQUIREMENTS</h2>
<p> The SGMLSpm package from CPAN. This package includes the sgmlspl script that is also needed.</p>
<h2>LIMITATIONS</h2>
<p> Trying <code>docbook2man</code> on non-DocBook or non-conformant SGML results in undefined behavior. :-) </p>
<p> This program is a slow, dodgy Perl script. </p>
<p> This program does not come close to supporting all the possible markup in DocBook, and may produce wrong output in some cases with supported markup.</p>
<h2>TO DO</h2>
<p> Obvious stuff:</p>
<dl>
<dt>*</p>
<dd> Fix <code>docbook2man</code> breakages found in the test documents, especially <i>weird.sgml</i>.</p>
<dt>*</p>
<dd> Add new element handling and fix existing handling. Be robust.</p>
<dt>*</p>
<dd> Produce cleanest, readable man output as possible (unlike some other converters). Follow Linux <code><a href="/docs/linux/man/7-man/">man</a></code>(7) convention. As conversion to man pages is usually not done very often, it is better to be slower/more complicated than to produce wrong output. Also if someone wants to give up using DocBook for whatever reason, the last-converted man pages can then be maintained manually.</p>
<dt>*</p>
<dd> Make it faster. I think most of the speed problems so far is with parsing ESIS. Rewrite <i>SGMLS.pm</i> with C and/or get input directly from <code>SP</code>.</p>
<dt>*</p>
<dd> Support other (human) languages. But what to do with non-ASCII charsets? SGMLSpm doesn&#8217;t report them and <code>roff</code> does not grok them. [Comment: text after enclosed lists (and SS blocks) will break docbook2man] If we do this, more people can use DocBook.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-1999 Steve Cheng &lt;steve [at] ggi-project.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> You should have received a copy of the GNU General Public License along with this program; see the file <i>COPYING</i>. If not, please write to the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
