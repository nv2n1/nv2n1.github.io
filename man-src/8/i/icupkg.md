---
title: "icupkg(8)"
name: "icupkg"
section: "8"
letter: "i"
url: "/docs/linux/man/8-icupkg/"
description: "icupkg – extract or modify an ICU .dat archive"
---

<p><code>icupkg</code> &#8211; extract or modify an ICU <code>.dat</code> archive</p>
<h2>Synopsis</h2>
<p><code>icupkg</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-tl</code>, <code>&#8211;type</code> l | <code>-tb</code>, <code>&#8211;type</code> b | <code>-te</code>, <code>&#8211;type</code> e ] [ <code>-c</code>, <code>&#8211;copyright</code> | <code>-C</code>, <code>&#8211;comment</code><i> comment</i> ] [ <code>-a</code>, <code>&#8211;add</code><i> list</i> ] [ <code>-r</code>, <code>&#8211;remove</code><i> list</i> ] [ <code>-x</code>, <code>&#8211;extract</code><i> list</i> ] [ <code>-l</code>, <code>&#8211;list</code> ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-w</code>, <code>&#8211;writepkg</code> ] [ <code>-m</code>, <code>&#8211;matchmode</code><i> mode</i> ] <i>infilename</i> [ <code>outfilename</code> ]</p>
<h2>Description</h2>
<p><code>icupkg</code> reads the input ICU <code>.dat</code> package file, modify it according to the options, swap it to the desired platform properties (charset &amp; endianness), and optionally write the resulting ICU <code>.dat</code> package to the output file. Items are removed, then added, then extracted and listed. An ICU <code>.dat</code> package is written if items are removed or added, or if the input and output filenames differ, or if the <code>-w</code>, <code>&#8211;writepkg</code> option is set. </p>
<p> If the input filename is &quot;new&quot; then an empty package is created. If the output filename is missing, then it is automatically generated from the input filename. If the input filename ends with an l, b, or e matching its platform properties, then the output filename will contain the letter from the <code>-t</code>, <code>&#8211;type</code> option. </p>
<p> This tool can also be used to just swap a single ICU data file, replacing the former icuswap tool. For this mode, provide the infilename (and optional outfilename) for a non-package ICU data file. Allowed options include <code>-t</code>, <code>-w</code>, <code>-s</code> and <code>-d</code> The filenames can be absolute, or relative to the source/dest dir paths. Other options are not allowed in this mode.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>-tl</code>, <code>&#8211;type</code><i> l</i></p>
<dd>Output for little-endian/ASCII charset family. The output type defaults to the input type.</p>
<dt><code>-tb</code>, <code>&#8211;type</code><i> b</i></p>
<dd>Output for big-endian/ASCII charset family. The output type defaults to the input type.</p>
<dt><code>-te</code>, <code>&#8211;type</code><i> e</i></p>
<dd>Output for big-endian/EBCDIC charset family. The output type defaults to the input type.</p>
<dt><code>-c</code>,<code>&#8211;copyright</code></p>
<dd>Include the ICU copyright notice in the resulting data.</p>
<dt><code>-C</code>, <code>&#8211;comment</code><i> comment</i></p>
<dd>Include the specified <i>comment</i> in the resulting data instead of the ICU copyright notice.</p>
<dt><code>-a</code>, <code>&#8211;add</code><i> list</i></p>
<dd>Add items from the <i>list</i> to the package. The list can be a single filename with a <code>.txt</code> file extension containing a list of item filenames, or an ICU <code>.dat</code> package filename.</p>
<dt><code>-r</code>, <code>&#8211;remove</code><i> list</i></p>
<dd>Remove items from the <i>list</i> from the package. The list can be a single filename with a <code>.txt</code> file extension containing a list of item filenames, or an ICU <code>.dat</code> package filename.</p>
<dt><code>-x</code>, <code>&#8211;extract</code><i> list</i></p>
<dd>Extract items from the <i>list</i> from the package. The list can be a single filename with a <code>.txt</code> file extension containing a list of item filenames, or an ICU <code>.dat</code> package filename.</p>
<dt><code>-m</code>, <code>&#8211;matchmode</code><i> mode</i></p>
<dd>Set the matching mode for item names with wildcards.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source</i></p>
<dd>Set the source directory to <i>source</i>. The default source directory is the current directory.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd>Set the destination directory to <i>destination</i>. The default destination directory is the current directory.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>List the package items to stdout (after modifying the package).</dl>
<h2>List File Syntax</h2>
<p>Items are listed on one or more lines and separated by whitespace (space+tab). Comments begin with <code>#</code> and are ignored. Empty lines are ignored. Lines where the first non-whitespace character is one of &quot;%&amp;'()*+,-./:;&lt;=&gt;?_ are also ignored to reserve for future syntax. </p>
<p> Items for removal or extraction may contain a single <code>*</code> wildcard character. The <code>*</code> matches zero or more characters. If <code>-m</code>, <code>&#8211;matchmode</code><i> noslash</i> is set, then the <code>*</code> character does not match the <code>/</code> character. </p>
<p> Items must be listed relative to the package, and the <code>&#8211;sourcedir</code> or the <code>&#8211;destdir</code> path will be prepended. The paths are only prepended to item filenames while adding or extracting items, not to ICU .dat package or list filenames. </p>
<p> Paths may contain <code>/</code> instead of the platform&#8217;s file separator character and are converted as appropriate.</p>
<h2>Authors</h2>
<p>Markus Scherer<br />
 George Rhoten</p>
<h2>Version</h2>
<p>1.0</p>
<h2>Copyright</h2>
<p>Copyright (C) 2006 IBM, Inc. and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) <code><a href="/docs/linux/man/1-genrb/">genrb</a></code>(1) </p>
