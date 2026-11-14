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
<dt><code>&#8211;help</code> | <code>-h</code></p>
<dd> : show this help message</p>
<dt><code>&#8211;prefix</code></p>
<dd> : show the installation prefix (cf. autoconf)</p>
<dt><code>&#8211;incdir</code></p>
<dd> : show the path to the LHAPDF header directory (for C++ interface)</p>
<dt><code>&#8211;libdir</code></p>
<dd> : show the path to the LHAPDF library directory</p>
<dt><code>&#8211;datadir</code></p>
<dd> : show the path to the LHAPDF installed data directory</p>
<dt> <code>&#8211;pdfsets-path</code> : show the path to the directory containing the PDF set data files</p>
<dt><code>&#8211;cppflags</code></p>
<dd> : get compiler flags for use with the C preprocessor stage of C++ compilation</p>
<dt><code>&#8211;ldflags</code></p>
<dd> : get compiler flags for use with the linker stage of any compilation</p>
<dt><code>&#8211;version</code></p>
<dd> : returns LHAPDF release version number</dl>
<h2>AUTHOR</h2>
<dd>This manual page was written by Lifeng Sun &lt;lifongsun [at] gmail.com&gt; for the Debian system (but may be used by others). </p>
<h2>Index</h2>
