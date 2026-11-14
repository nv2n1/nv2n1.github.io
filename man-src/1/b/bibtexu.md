---
title: "bibtexu(1)"
name: "bibtexu"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtexu/"
description: "bibtexu – UTF-8 Big BibTeX"
---

<h2 class="name">NAME</h2>
<p> bibtexu &#8211; UTF-8 Big BibTeX </p>
<h2>SYNOPSIS</h2>
<p> <code>bibtexu</code> [<i>options</i>] <i>aux-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>BibTeXu</code> is the Unicode-compliant version of BibTeX. It is largely based on Niel Kempson&#8217;s BibTeX8, and it provides a better support for UTF-8 by integrating ICU library. Therefore, <code>BibTeXu</code> no longer requires the Codepage and Sort order (&quot;CS&quot;) file; instead, the method of sorting and case-changing can be controled via command-line options.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> <code>&#8211;help</code></p>
<dd> display some brief help text.</p>
<dt><code>-d</code> <code>&#8211;debug</code> TYPE</p>
<dd> report debugging information. TYPE is one or more of all, csf, io, mem, misc, search.</p>
<dt><code>-s</code> <code>&#8211;statistics</code></p>
<dd> report internal statistics.</p>
<dt><code>-t</code> <code>&#8211;trace</code></p>
<dd> report execution tracing.</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> report BibTeX version.</p>
<dt><code>-l</code> <code>&#8211;language</code> LANG</p>
<dd> use language LANG to convert strings to low case. This argument is passed to ICU library.</p>
<dt><code>-o</code> <code>&#8211;location</code> LANG</p>
<dd> use language LANG for sorting. This argument is passed to ICU library.</p>
<dt><code>-B</code> <code>&#8211;big</code></p>
<dd> set large BibTeX capacity.</p>
<dt><code>-H</code> <code>&#8211;huge</code></p>
<dd> set huge BibTeX capacity.</p>
<dt><code>-W</code> <code>&#8211;wolfgang</code></p>
<dd> set really huge BibTeX capacity for Wolfgang.</p>
<dt><code>-M</code> <code>&#8211;min_crossrefs</code> ##</p>
<dd> set min_crossrefs to ##.</p>
<dt><code>&#8211;mstrings</code> ##</p>
<dd> allow ## unique strings.</dl>
<h2>SEE ALSO</h2>
<p> More detailed description of <code>BibTeXu</code> is available at $TEXMFDIST/doc/bibtexu/README.</p>
<h2>AUTHORS</h2>
<p> <code>BibTeXu </code> was written by Yannis Haralambous and his students. This manpage was written for TeX Live. </p>
<h2>Index</h2>
