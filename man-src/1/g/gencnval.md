---
title: "gencnval(1)"
name: "gencnval"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gencnval/"
description: "gencnval – compile the converters aliases file"
---

<h2 class="name">NAME</h2>
<p> <code>gencnval</code> &#8211; compile the converters aliases file </p>
<h2>SYNOPSIS</h2>
<p> <code>gencnval</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <i>converterfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gencnval</code> converts the ICU aliases file <i>converterfile</i> into the binary file <code>cnvalias.icu</code>. This binary file can then be read directly by ICU, or used by <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) for incorporation into a larger archive or library. </p>
<p> If <i>converterfile</i> is not provided, the default ICU <code>convrtrs.txt</code> file is used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display verbose output. This information can include information about conflicting aliases and the converters the aliases resolve to.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Include a copyright notice in the binary data.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source</i></p>
<dd> Set the source directory to <i>source</i>. The default source directory is specified by the environment variable <code>ICU_DATA</code>.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd> Set the destination directory to <i>destination</i>. The default destination directory is specified by the environment variable <code>ICU_DATA</code>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd> Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>FILES</h2>
<dl>
<dt><code>icu/source/data/mappings/convrtrs.txt</code></p>
<dd> Description of ICU&#8217;s converters and their aliases. This data file is not normally installed, and it is available as a part of ICU source code.</dl>
<h2>VERSION</h2>
<p> 70.1</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2004 IBM, Inc. and others.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) </p>
<h2>Index</h2>
