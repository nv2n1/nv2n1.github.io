---
title: "t1unmac(1)"
name: "t1unmac"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1unmac/"
description: "t1unmac – translate a Mac PostScript Type 1 font into PFA or PFB format"
---

<h2 class="name">NAME</h2>
<p> t1unmac &#8211; translate a Mac PostScript Type 1 font into PFA or PFB format </p>
<h2>SYNOPSIS</h2>
<p> <code>t1unmac</code> [<code>-a</code>|<code>-b</code>] [<code>-r</code>] [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>t1unmac</code> extracts POST resources from a Macintosh PostScript font file and creates a PFA (hexadecimal) or PFB (binary) font file. The file <i>input</i> should be in MacBinary I or II, AppleSingle, AppleDouble, or BinHex format, or it can be a raw resource fork. If the file is a raw resource fork, you need to give the `&#8211;raw&#8217; option; otherwise <code>t1unmac</code> should automatically figure out what kind of file you have. If the file <i>output</i> is not specified output goes to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;pfa</code>, <code>-a</code></p>
<dd> Output in PFA (ASCII) format.</p>
<dt><code>&#8211;pfb</code>, <code>-b</code></p>
<dd> Output in PFB (binary) format. This is the default.</p>
<dt><code>&#8211;raw</code>, <code>-r</code></p>
<dd> Indicates that the input is a raw resource fork.</p>
<dt><code>&#8211;macbinary</code></p>
<dd> Indicates that the input is in MacBinary I or II format.</p>
<dt><code>&#8211;applesingle</code></p>
<dd> Indicates that the input is in AppleSingle format.</p>
<dt><code>&#8211;appledouble</code></p>
<dd> Indicates that the input is in AppleDouble format.</p>
<dt><code>&#8211;binhex</code></p>
<dd> Indicates that the input is in BinHex 4.0 format.</p>
<dt><code>&#8211;block-length=</code><i>num</i>, <code>-l</code><i> num</i></p>
<dd> PFB only: Set the maximum output block length to <i>num.</i> The default length is as large as memory allows.</p>
<dt><code>&#8211;line-length=</code><i>num</i>, <code>-l</code><i> num</i></p>
<dd> PFA only: Set the maximum length of encrypted lines in the output to <i>num.</i> (These are the lines consisting wholly of hexadecimal digits.) The default is 64.</dl>
<h2>EXAMPLES</h2>
<p> On Mac OS X, you can use <code>t1unmac</code> to translate a font into PFA or PFB format as follows: </p>
<pre>
% <code>t1unmac</code> --raw FONTFILENAME/..namedfork/rsrc &gt; OUTPUT
</pre>
<h2>SEE ALSO</h2>
<h2>AUTHORS</h2>
<p> Lee Hetherington (ilh [at] lcs.mit.edu)<br />
 Eddie Kohler (ekohler [at] gmail.com) </p>
<p> Ported to Microsoft C/C++ Compiler and MS-DOS operating system by Kai-Uwe Herbing (herbing [at] netmbx.netmbx.de). </p>
<h2>Index</h2>
