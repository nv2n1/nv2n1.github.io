---

title: "bibtexu(1)"
name: "bibtexu"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtexu/"
description: "bibtexu – UTF-8 Big BibTeX"
---

<p> bibtexu &#8211; UTF-8 Big BibTeX </p>
<h2>SYNOPSIS</h2>
<p> <code>bibtexu</code> [<i>options</i>] <i>aux-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>BibTeXu</code> is the Unicode-compliant version of BibTeX. It is largely based on Niel Kempson&#8217;s BibTeX8, and it provides a better support for UTF-8 by integrating ICU library. Therefore, <code>BibTeXu</code> no longer requires the Codepage and Sort order (&quot;CS&quot;) file; instead, the method of sorting and case-changing can be controled via command-line options.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> <code>&#8211;help</code></dt>
<dd> display some brief help text.</dd>
<dt><code>-d</code> <code>&#8211;debug</code> TYPE</dt>
<dd> report debugging information. TYPE is one or more of all, csf, io, mem, misc, search.</dd>
<dt><code>-s</code> <code>&#8211;statistics</code></dt>
<dd> report internal statistics.</dd>
<dt><code>-t</code> <code>&#8211;trace</code></dt>
<dd> report execution tracing.</dd>
<dt><code>-v</code> <code>&#8211;version</code></dt>
<dd> report BibTeX version.</dd>
<dt><code>-l</code> <code>&#8211;language</code> LANG</dt>
<dd> use language LANG to convert strings to low case. This argument is passed to ICU library.</dd>
<dt><code>-o</code> <code>&#8211;location</code> LANG</dt>
<dd> use language LANG for sorting. This argument is passed to ICU library.</dd>
<dt><code>-B</code> <code>&#8211;big</code></dt>
<dd> set large BibTeX capacity.</dd>
<dt><code>-H</code> <code>&#8211;huge</code></dt>
<dd> set huge BibTeX capacity.</dd>
<dt><code>-W</code> <code>&#8211;wolfgang</code></dt>
<dd> set really huge BibTeX capacity for Wolfgang.</dd>
<dt><code>-M</code> <code>&#8211;min_crossrefs</code> ##</dt>
<dd> set min_crossrefs to ##.</dd>
<dt><code>&#8211;mstrings</code> ##</dt>
<dd> allow ## unique strings.</dd></dl>
<h2>SEE ALSO</h2>
<p> More detailed description of <code>BibTeXu</code> is available at $TEXMFDIST/doc/bibtexu/README.</p>
<h2>AUTHORS</h2>
<p> <code>BibTeXu </code> was written by Yannis Haralambous and his students. This manpage was written for TeX Live. </p>
