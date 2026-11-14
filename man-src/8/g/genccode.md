---
title: "genccode(8)"
name: "genccode"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genccode/"
description: "genccode – generate C or platform specific assembly code from an ICU data file."
---

<p><code>genccode</code> &#8211; generate C or platform specific assembly code from an ICU data file.</p>
<h2>Synopsis</h2>
<p><code>genccode</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-a</code>, <code>&#8211;assembly</code><i> name</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-n</code>, <code>&#8211;name</code><i> name</i> ] [ <code>-e</code>, <code>&#8211;entrypoint</code><i> name</i> ] [ <code>-f</code>, <code>&#8211;filename</code><i> name</i> ] [ <i>filename</i> &#8230; ]</p>
<h2>Description</h2>
<p><code>genccode</code> reads each of the supplied <i>filename</i> and writes out a C file containing a compilable definition of the data in the data file. The C file name is made by taking the base name of the data <i>filename</i>, replacing dots by underscores, and adding a <i>.c</i> file extension. </p>
<p> If the <code>-a</code> option is used, platform specific assembly code is generated instead of C code. Most C compilers will accept both C and assembly files. Instead of writing a filename with a <i>.c</i> file extension, a filename with a <i>.s</i> will be written instead. </p>
<p> If <code>genccode</code> is called with no <i>filename</i> it terminates gracefully.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>-a</code>, <code>&#8211;assembly</code><i> name</i></p>
<dd>Output assembly code instead of C code. Use <code>-h</code> to see the list of available types of assembly to generate and to specify for this option.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd>Set the destination directory to <i>destination</i>. The default destination directory is the current directory.</p>
<dt><code>-n</code>, <code>&#8211;name</code><i> name</i></p>
<dd>Set the data name to <i>name</i> instead of the default. This name is also used as the base name of the output. The default name is made of the <i>icudt</i> prefix, followed by a two-digit version number corresponding to the current version of the ICU release, and a single letter indicating the endianness of the data (the letter <i>b</i> indicated big endian data, and the letter <i>l</i> indicates little endian ones).</p>
<dt><code>-f</code>, <code>&#8211;filename</code><i> name</i></p>
<dd>Normally, an ICU data file such as mydata.icu will be turned into mydata_icu.c and mydata_icu.o. However, if this parameter was set to &quot;somedata&quot;, the output files will be somedata.o and somedata.c, respectively.</p>
<dt><code>-e</code>, <code>&#8211;entrypoint</code><i> name</i></p>
<dd>Set the data entry point (used for linking against the data in a shared library form) to <i>name</i>. The default entry point name is made of the data (set by the <code>-n</code>, <code>&#8211;name</code> option) followed by an underscore and the type of the data (set by the <code>-t</code>, <code>&#8211;type</code> option).</dl>
<h2>Version</h2>
<p>70.1</p>
<h2>Copyright</h2>
<p>Copyright (C) 2000-2004 IBM, Inc. and others.</p>
