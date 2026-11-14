---
title: "aleph(1)"
name: "aleph"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aleph/"
description: "aleph – extended Unicode TeX"
---

<h2 class="name">NAME</h2>
<p> aleph &#8211; extended Unicode TeX </p>
<h2>SYNOPSIS</h2>
<p> <code>aleph</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]</p>
<h2>DESCRIPTION</h2>
<p> Run the Aleph typesetter on <i>file</i>, usually creating <i>file.dvi</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of Aleph commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument Aleph uses a different set of precompiled commands, contained in <i>format</i><code>.fmt</code>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> Aleph is a version of the TeX program modified for multilingual typesetting. It uses Unicode, and has additional primitives for (among other things) bidirectional typesetting. </p>
<p> Aleph&#8217;s command line options are similar to those of TeX. </p>
<p> Aleph is no longer being actively developed; see LuaTeX for current activity.</p>
<h2>OPTIONS</h2>
<p> Run aleph &#8211;help to see the complete list of options; this is not exhaustive.</p>
<dl>
<dt><code>-cnf-line</code><i>&nbsp;string</i></p>
<dd> Parse <i>string</i> as a <i>texmf.cnf</i> configuration line. See the Kpathsea manual.</p>
<dt><code>&#8211;fmt</code><i>&nbsp;format</i></p>
<dd> Use <i>format</i> as the name of the format to be used, instead of the name by which Aleph was called or a <i>%&amp;</i> line.</p>
<dt><code>&#8211;halt-on-error</code></p>
<dd> Exit with an error code when an error is encountered during processing.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;ini</code></p>
<dd> Be `initial&#8217; Aleph for dumping formats; this is implicitly true if the program is called as <code>inialeph</code>.</p>
<dt><code>&#8211;interaction</code><i>&nbsp;mode</i></p>
<dd> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding 
