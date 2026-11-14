---
title: "gensprep(8)"
name: "gensprep"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gensprep/"
description: "gensprep – compile StringPrep data from files filtered by filterRFC3454.pl"
---

<p><code>gensprep</code> &#8211; compile StringPrep data from files filtered by filterRFC3454.pl</p>
<h2>Synopsis</h2>
<p><code>gensprep</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ]</p>
<h2>Description</h2>
<p><code>gensprep</code> reads filtered RFC 3454 files and compiles their information into a binary form. The resulting file, <code>&lt;name&gt;.icu</code>, can then be read directly by ICU, or used by <code><a href="/docs/linux/man/8-pkgdata/">pkgdata</a></code>(8) for incorporation into a larger archive or library. </p>
<p> The files read by <code>gensprep</code> are described in the <code>FILES</code> section.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
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
<dd>Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>Files</h2>
<p>The following files are read by <code>gensprep</code> and are looked for in the <i>source</i> /misc for rfc3454_*.txt files and in <i>source</i> /unidata for NormalizationCorrections.txt.</p>
<dl>
<dt><code>rfc3453_A_1.txt </code></p>
<dd>Contains the list of unassigned codepoints in Unicode version 3.2.0&#8230;.</p>
<dt><code>rfc3454_B_1.txt</code></p>
<dd>Contains the list of code points that are commonly mapped to nothing&#8230;.</p>
<dt><code>rfc3454_B_2.txt</code></p>
<dd>Contains the list of mappings for casefolding of code points when Normalization form NFKC is specified&#8230;.</p>
<dt><code>rfc3454_C_X.txt</code></p>
<dd>Contains the list of code points that are prohibited for IDNA.</p>
<dt><code>NormalizationCorrections.txt</code></p>
<dd>Contains the list of code points whose normalization has changed since Unicode Version 3.2.0.</dl>
<h2>Version</h2>
<p>70.1</p>
<h2>Copyright</h2>
<p>Copyright (C) 2000-2002 IBM, Inc. and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pkgdata/">pkgdata</a></code>(8) </p>
