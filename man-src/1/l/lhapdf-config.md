---
title: "lhapdf-config(1)"
name: "lhapdf-config"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lhapdf-config/"
description: "lhapdf-config – script to get version number and compiler flags of the installed LHAPDF library"
---

<h2>NAME</h2>
<p> lhapdf-config &#8211; script to get version number and compiler flags of the installed LHAPDF library</p>
<h2>SYNOPSIS</h2>
<p> <code>lhapdf-config</code> [[<i>&#8211;help|-h</i>] <i>| </i>[<i>&#8211;prefix</i>] <i>| </i>[<i>&#8211;pdfsets-path</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <i>lhapdf-config</i> is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>LHAPDF</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code> | <code>-h</code></dt>
<dd> : show this help message</dd>
<dt><code>&#8211;prefix</code></dt>
<dd> : show the installation prefix (cf. autoconf)</dd>
<dt><code>&#8211;incdir</code></dt>
<dd> : show the path to the LHAPDF header directory (for C++ interface)</dd>
<dt><code>&#8211;libdir</code></dt>
<dd> : show the path to the LHAPDF library directory</dd>
<dt><code>&#8211;datadir</code></dt>
<dd> : show the path to the LHAPDF installed data directory</dd>
<dt> <code>&#8211;pdfsets-path</code> : show the path to the directory containing the PDF set data files</dt>
<dt><code>&#8211;cppflags</code></dt>
<dd> : get compiler flags for use with the C preprocessor stage of C++ compilation</dd>
<dt><code>&#8211;ldflags</code></dt>
<dd> : get compiler flags for use with the linker stage of any compilation</dd>
<dt><code>&#8211;version</code></dt>
<dd> : returns LHAPDF release version number</dd></dl>
<h2>AUTHOR</h2>
<dd>This manual page was written by Lifeng Sun &lt;lifongsun [at] gmail.com&gt; for the Debian system (but may be used by others). </dd>
<h2>Index</h2>
