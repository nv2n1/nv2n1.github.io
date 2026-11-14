---
title: "gencmn(8)"
name: "gencmn"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gencmn/"
description: "gencmn – generate an ICU memory-mappable data file"
---

<p><code>gencmn</code> &#8211; generate an ICU memory-mappable data file</p>
<h2>Synopsis</h2>
<p><code>gencmn</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> | <code>-C</code>, <code>&#8211;comment</code><i> comment</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-n</code>, <code>&#8211;name</code><i> name</i> ] [ <code>-t</code>, <code>&#8211;type</code><i> fileext</i> ] [ <code>-S</code>, <code>&#8211;source</code> ] [ <code>-e</code>, <code>&#8211;entrypoint</code><i> name</i> ] <i>maxsize</i> [ <i>listfilename</i> ]</p>
<h2>Description</h2>
<p><code>gencmn</code> takes a set of files and packages them as an ICU memory-mappable data file. The resulting data file can then be used directly by ICU. </p>
<p> <code>gencmn</code> reads a list of files to be packaged from either the supplied <i>listfilename</i> file, or from its standard output. It packages all the files from the list that are not bigger than <i>maxsize</i> bytes, except if <i>maxsize</i> is 0, which indicates that there is no size limit on files.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display extra informative messages during execution.</p>
<dt><code>-c</code>,<code>&#8211;copyright</code></p>
<dd>Include the ICU copyright notice in the resulting data.</p>
<dt><code>-C</code>, <code>&#8211;comment</code><i> comment</i></p>
<dd>Include the specified <i>comment</i> in the resulting data instead of the ICU copyright notice.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd>Set the destination directory to <i>destination</i>. The default destination directory is specified by the environment variable <code>ICU_DATA</code>.</p>
<dt><code>-n</code>, <code>&#8211;name</code><i> name</i></p>
<dd>Set the data name to <i>name</i> instead of the default. This name is also used as the base name of the output. The default name is made of the <i>icudt</i> prefix, followed by a two-digit version number corresponding to the current version of the ICU release, and a single letter indicating the endianness of the data (the letter <i>b</i> indicated big endian data, and the letter <i>l</i> indicates little endian ones).</p>
<dt><code>-t</code>, <code>&#8211;type</code><i> type</i></p>
<dd>Use <i>type</i> as the type of the data. This type is also used as the extension of the generated data file. The default type ie <i>dat</i>.</p>
<dt><code>-S</code>, <code>&#8211;source</code></p>
<dd>Write a C source file with the table of contents of the data.</p>
<dt><code>-e</code>, <code>&#8211;entrypoint</code><i> name</i></p>
<dd>Set the data entry point (used for linking against the data in a shared library form) to <i>name</i>. The default entry point name is made of the data (set by the <code>-n</code>, <code>&#8211;name</code> option) followed by an underscore and the type of the data (set by the <code>-t</code>, <code>&#8211;type</code> option).</dl>
<h2>Environment</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd>Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>Version</h2>
<p>70.1</p>
<h2>Copyright</h2>
<p>Copyright (C) 2000-2001 IBM, Inc. and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-decmn/">decmn</a></code>(8) </p>
