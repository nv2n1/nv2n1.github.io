---
title: "genuca(8)"
name: "genuca"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genuca/"
description: "genuca – create the UCA data table"
---

<p><code>genuca</code> &#8211; create the UCA data table</p>
<h2>Synopsis</h2>
<p><code>genuca</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <i>file</i> ]</p>
<h2>Description</h2>
<p><code>genuca</code> compiles the Unicode Collation Algorithm (UCA) data from <i>file</i> (or from <code>FractionalUCA.txt</code> if <i>file</i> is omitted) into its binary form, the files <code>ucadata.dat</code> and <code>invuca.dat</code>. These binary files can then be read directly by ICU, or used by <code><a href="/docs/linux/man/8-pkgdata/">pkgdata</a></code>(8) for incorporation into a larger archive or library.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print the version of <code>genuca</code> and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display extra informative messages during execution.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd>Include a copyright notice into the binary data.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source</i></p>
<dd>Set the source directory to <i>source</i>. The default source directory is specified by the environment variable <code>ICU_DATA</code>.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd>Set the destination directory to <i>destination</i>. The default destination directory is specified by the environment variable <code>ICU_DATA</code>.</dl>
<h2>Environment</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd>Specifies the directory containing ICU data. Defaults to <code>/usr/share/icu/4.2.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>Files</h2>
<dl>
<dt><code>FractionalUCA.txt</code></p>
<dd>Machine-readable file containing data for the Unicode collation algorithm.</dl>
<h2>Version</h2>
<p>4.2.1</p>
<h2>Copyright</h2>
<p>Copyright (C) 2001 IBM, Inc. and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pkgdata/">pkgdata</a></code>(8) </p>
