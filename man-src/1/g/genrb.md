---
title: "genrb(1)"
name: "genrb"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genrb/"
description: "genrb – compile a resource bundle"
---

<h2 class="name">NAME</h2>
<p> <code>genrb</code> &#8211; compile a resource bundle </p>
<h2>SYNOPSIS</h2>
<p> <code>genrb</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-e</code>, <code>&#8211;encoding</code><i> encoding</i> ] [ <code>-j</code>, <code>&#8211;write-java</code><i> </i>[ encoding ] ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] <i>bundle</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>genrb</code> converts the resource <i>bundle</i> source files passed on the command line to their binary form or to a Java source file for use with ICU4J. The resulting binary files have a <code>.res</code> extension while resource bundle source files typically have a <code>.txt</code> extension. Java source files have a <code>java</code> extension and follow the ICU4J naming conventions. </p>
<p> It is customary to name the resource bundles by their locale name, i.e. to use a local identifier for the <i>bundle</i> filename, e.g. <code>ja_JP.txt</code> for Japanese (Japan) data, or <code>root.txt</code> for the root bundle. In any case, <code>genrb</code> will produce a file whose base name is the name of the locale found in the resource file, not the base name of the resource file itself. </p>
<p> The binary files can be read directly by ICU, or used by <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) for incorporation into a larger archive or library.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>genrb</code> and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-e</code>, <code>&#8211;encoding</code><i> encoding</i></p>
<dd> Set the encoding used to read input files to <i>encoding</i>. The default encoding is the invariant (subset of ASCII or EBCDIC) codepage for the system (see section <code>INVARIANT CHARACTERS</code>). The encodings UTF-8, UTF-16BE, and UTF-16LE are automatically detected if a byte order mark (BOM) is present.</p>
<dt><code>-j</code>, <code>&#8211;write-java</code><i> </i>[ encoding ]</p>
<dd> Generate a Java source code for use with ICU4J. An optional <i>encoding</i> for the Java file can be given.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source</i></p>
<dd> Set the source directory to <i>source</i>. The default source directory is specified by the environment variable <code>ICU_DATA</code>, or the location set when ICU was built if <code>ICU_DATA</code> is not set.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd> Set the destination directory to <i>destination</i>. The default destination directory is specified by the environment variable <code>ICU_DATA</code> or is the location set when ICU was built if <code>ICU_DATA</code> is not set.</p>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></p>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, when processing collation overrides, the file <code>ucadata.dat</code> must be located. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>.</dl>
<h2>INVARIANT CHARACTERS</h2>
<p> The <code>invariant character set</code> consists of the following set of characters, expressed as a standard POSIX regular expression: <code>[a-z]|[A-Z]|[0-9]|_| |+|-|*|/</code>. This is the set which is guaranteed to be available regardless of code page.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd> Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>VERSION</h2>
<p> 70.1</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2002 IBM, Inc. and others.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-derb/">derb</a></code>(1)<br />
 <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) </p>
<h2>Index</h2>
