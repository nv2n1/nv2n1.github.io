---
title: "lambda(1)"
name: "lambda"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lambda/"
description: "omega, iniomega, viromega – extended unicode TeX"
---

<h2 class="name">NAME</h2>
<p> omega, iniomega, viromega &#8211; extended unicode TeX </p>
<h2>SYNOPSIS</h2>
<p> <code>omega</code> [<i>options</i>] [<code>&amp;</code> <i>format</i> ] [ <i>file</i> | <code>\</code> <i>commands</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Run the Omega typesetter on <i>file</i>, usually creating <i>file.dvi</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of Omega commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument Omega uses a different set of precompiled commands, contained in <i>format.fmt</i>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> Omega is a version of the TeX program modified for multilingual typesetting. It uses unicode, and has additional primitives for (among other things) bidirectional typesetting. </p>
<p> The <code>iniomega</code> and <code>viromega</code> commands are Omega&#8217;s analogues to the <code>initex</code> and <code>virtex</code> commands. In this installation, they are symlinks to the <code>omega</code> executable. </p>
<p> Omega&#8217;s command line options are similar to those of TeX. </p>
<p> Omega is experimental software.</p>
<h2>OPTIONS</h2>
<p> This version of Omega understands the following command line options.</p>
<dl>
<dt><code>&#8211;oft</code><i>&nbsp;<wbr>format</i></p>
<dd> Use <i>format</i> as the name of the format to be used, instead of the name by which Omega was called or a <i>%&amp;</i> line.</p>
<dt><code>-halt-on-error</code></p>
<dd> Exit with an error code when an error is encountered during processing.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;ini</code></p>
<dd> Be <code>iniomega</code>, for dumping formats; this is implicitly true if the program is called as <code>iniomega</code>.</p>
<dt><code>&#8211;interaction</code><i>&nbsp;<wbr>mode</i></p>
<dd> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding 
