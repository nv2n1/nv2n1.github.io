---
title: "t1binary(1)"
name: "t1binary"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1binary/"
description: "t1binary – convert PostScript Type 1 font from ASCII to binary"
---

<h2 class="name">NAME</h2>
<p> t1binary &#8211; convert PostScript Type 1 font from ASCII to binary </p>
<h2>SYNOPSIS</h2>
<p> <code>t1binary</code> [<code>-l</code> <i>length</i>] [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>t1binary</code> converts Adobe Type 1 font programs in PFA (hexadecimal) format to PFB (binary) format. If the file <i>output</i> is not specified output goes to the standard output. If the file <i>input</i> is not specified input comes from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;block-length=</code><i>length</i>, <code>-l</code><i> length</i></p>
<dd> Set the maximum length of sections in PFB output to <i>length.</i> The default length is as large as memory allows.</dl>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i></p>
<h2>AUTHORS</h2>
<p> Lee Hetherington (ilh [at] lcs.mit.edu)<br />
 Eddie Kohler (ekohler [at] gmail.com) </p>
<p> Ported to Microsoft C/C++ Compiler and MS-DOS operating system by Kai-Uwe Herbing (herbing [at] netmbx.netmbx.de). </p>
<h2>Index</h2>
