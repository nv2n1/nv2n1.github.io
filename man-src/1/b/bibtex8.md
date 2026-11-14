---
title: "bibtex8(1)"
name: "bibtex8"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtex8/"
description: "bibtex8 – 8-bit Big BibTeX"
---

<h2 class="name">NAME</h2>
<p> bibtex8 &#8211; 8-bit Big BibTeX </p>
<h2>SYNOPSIS</h2>
<p> <code>bibtex8</code> [<i>options</i>] <i>aux-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>BibTeX8</code> is an 8-bit implementation of BibTeX written in C. It has been enhanced by adding the following features: </p>
<p> &#8211; &quot;big&quot; (32-bit) and customisable capacity </p>
<p> &#8211; flexible support for non-English languages using 8-bit character sets </p>
<p> <code>BibTeX8</code> accepts 8-bit characters in its input files, and writes 8-bit characters to its output files. The character set is defined by an external configuration file &#8212; the Codepage and Sort order (&quot;CS&quot;) file. By default, it reads a specific CS file &quot;88591lat.csf&quot;, which defines ISO 8859-1 character set and its alphabetical sorting order including accented characters.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> <code>&#8211;help</code></p>
<dd> display some brief help text.</p>
<dt><code>-7</code> <code>&#8211;traditional</code></p>
<dd> operate in the original 7-bit mode, no CS file used. Only 7-bit ASCII characters are supported, and they are sorted by ASCII code value.</p>
<dt><code>-8</code> <code>&#8211;8bit</code></p>
<dd> force 8-bit mode, no CS file used. All 8-bit characters (code &gt; 127) are treated as letters, and they are sorted by their code value.</p>
<dt><code>-c</code> <code>&#8211;csfile</code> FILE</p>
<dd> read FILE as the BibTeX character set and sort definition file. Note that options <code>-7</code>, <code>-8</code> and <code>-c</code> are exclusive.</p>
<dt><code>-d</code> <code>&#8211;debug</code> TYPE</p>
<dd> report debugging information. TYPE is one or more of all, csf, io, mem, misc, search.</p>
<dt><code>-s</code> <code>&#8211;statistics</code></p>
<dd> report internal statistics.</p>
<dt><code>-t</code> <code>&#8211;trace</code></p>
<dd> report execution tracing.</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> report BibTeX version.</p>
<dt><code>-B</code> <code>&#8211;big</code></p>
<dd> set large BibTeX capacity.</p>
<dt><code>-H</code> <code>&#8211;huge</code></p>
<dd> set huge BibTeX capacity.</p>
<dt><code>-W</code> <code>&#8211;wolfgang</code></p>
<dd> set really huge BibTeX capacity for Wolfgang.</p>
<dt><code>-M</code> <code>&#8211;min_crossrefs</code> ##</p>
<dd> set min_crossrefs to ##.</p>
<dt><code>&#8211;mcites</code> ##</p>
<dd> allow ## 
