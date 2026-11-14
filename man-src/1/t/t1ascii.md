---
title: "t1ascii(1)"
name: "t1ascii"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1ascii/"
description: "t1ascii – convert PostScript Type 1 font from binary to ASCII"
---

<h2 class="name">NAME</h2>
<p> t1ascii &#8211; convert PostScript Type 1 font from binary to ASCII </p>
<h2>SYNOPSIS</h2>
<p> <code>t1ascii</code> [<code>-l</code> <i>length</i>] [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>t1ascii</code> converts Adobe Type 1 font programs in PFB (binary) format to PFA (hexadecimal) format. If the file <i>output</i> is not specified output goes to the standard output. If the file <i>input</i> is not specified input comes from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;line-length=</code><i>num</i>, <code>-l</code><i> num</i></p>
<dd> Set the maximum length of encrypted lines in the output to <i>num.</i> (These are the lines consisting wholly of hexadecimal digits.) The default is 64.</p>
<dt><code>&#8211;warnings</code>, <code>-w</code></p>
<dd> Warn when the input font contains lines longer than 255 characters. Long lines don&#8217;t strictly conform to Adobe&#8217;s Document Structuring Conventions, and may cause problems with older software.</dl>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i></p>
<h2>AUTHORS</h2>
<p> Lee Hetherington (ilh [at] lcs.mit.edu)<br />
 Eddie Kohler (ekohler [at] gmail.com) </p>
<p> Ported to Microsoft C/C++ Compiler and MS-DOS operating system by Kai-Uwe Herbing (herbing [at] netmbx.netmbx.de). </p>
<h2>Index</h2>
