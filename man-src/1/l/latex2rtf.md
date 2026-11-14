---
title: "latex2rtf(1)"
name: "latex2rtf"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2rtf/"
description: "latex2rtf – Convert a LaTeX file to an RTF file"
---

<h2>NAME</h2>
<p> latex2rtf &#8211; Convert a LaTeX file to an RTF file</p>
<h2>SYNTAX</h2>
<p> latex2rtf [-hlpFSVW] [ -d# ] [ -D# ] [ -M# ] [ -se#] [ -sf#] [ -t# ] [ -Z# ] [ -a <i>auxfile</i> ] [ -b <i>bblfile</i> ] [ -C <i>codepage</i> ] [ -i <i>language</i> ] [ -o <i>outputfile</i> ] [ -P <i>/path/to/cfg</i> ] [ -T <i>/path/to/tmp</i> ] [ <i>inputfile</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The <i>latex2rtf</i> command converts a LaTeX file into RTF text format. The text and much of the formatting information is translated to RTF.</p>
<dl>
<dt><code>-a auxfile</code></p>
<dd> Used to specify a particular cross-referencing file. When this option is omitted, the <i>auxfile </i> is assumed to be the same as <i>inputfile</i> with the .tex suffix replaced by .aux.</p>
<dt><code>-b bblfile</code></p>
<dd> Used to specify a particular bibliography file When this option is omitted, the <i>bblfile </i> is assumed to be the same as <i>inputfile</i> with the .tex suffix replaced by .bbl.</p>
<dt><code>-C codepage</code></p>
<dd> used to specify the character set (code page) used in the LaTeX document for non-ansi characters. <i>codepage</i> may be one of the following: ansinew, applemac, cp437, cp437de, cp850, cp852, cp855, cp865, cp866, decmulti, cp1250, cp1252, koi8-r, koi8-u, latin1, latin2, latin3, latin4, latin5, latin9, maccyr, macukr, next, raw, raw437, raw852, raw1250, raw1251, and raw1253. The default behavior is to use ansinew (same as cp1252). For convenience, just the numbers 437, 437de, 850, 852, 855, 866, 1250 or 1252 may be specified. </p>
<p> The raw character set encoding prevents any 8-bit character translation. The RTF file is marked to use the same encoding as the default encoding for the program interpreting the RTF file. This is particularly useful when translating a file written in a language (e.g., czech) that maps poorly into the ansinew (western european) character set. </p>
<dt><code>-d#</code></p>
<dd> Write extra debugging output to stderr. Higher numbers cause more debugging output and range from 0 (only errors) to 6 (absurdly many messages). The default is 1 (Warnings and Errors only).</p>
<dt><code>-D dots_per_inch</code></p>
<dd> Used to specify the number of dots per inch in equations that are converted to bitmaps and for graphics that must be converted. Default is 300 dpi.</p>
<dt><code>-E# </code></p>
<dd> where # selects the type of figure handling desired. RTF does not support insertion of PS, PDF, or EPS file types. These figures must be converted to a bitmap format and then inserted. One trick is to insert the filenames into the RTF file and then in post-processing, insert the file. These options can be added together.<br />
 -E3 insert all figures (DEFAULT)<br />
 -E0 no figures in the RTF<br />
 -E1 insert figures having RTF-supported formats<br />
 -E2 convert and insert unsupported figure formats<br />
 -E4 insert only filenames for supported file formats<br />
 -E8 insert only filenames for unsupported file formats</p>
<dt><code>-f use fields</code></p>
<dd> -f0 do not use fields in RTF. This is handy when primitive RTF editors are being used to view the RTF output.<br />
 -f1 use fields for equations but not ef and 
