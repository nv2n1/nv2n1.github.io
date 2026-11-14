---
title: "ttf2afm(1)"
name: "ttf2afm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttf2afm/"
description: "ttf2afm – utility to generate AFM files for TrueType fonts"
---

<h2>NAME</h2>
<p> ttf2afm &#8211; utility to generate AFM files for TrueType fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>ttf2afm</code> [<i>OPTIONS</i>] <i>FONTFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ttf2afm</code> is used to generate Adobe Font Metrics (AFM) files for TrueType (TTF) fonts to allow them to be used with TeX. </p>
<p> <code>ttf2afm</code> takes the name of a TrueType font file as a required argument. It may also take one or more options from the list below (<code>-i</code> and <code>-u</code> are mutually exclusive). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> force printing glyph names in form `index&#8217;<i>decnum</i></p>
<dt><code>-u</code></p>
<dd> force printing glyph names in form `uni&#8217;<i>hexnum</i></p>
<dt><code>-c</code> <i>name</i></p>
<dd> write encoding tables to file <i>name.eMN</i>, where <i>M</i> is the platform ID and <i>N</i> is the encoding ID</p>
<dt><code>-v</code></p>
<dd> print program version</p>
<dt><code>-e</code> <i>enc</i></p>
<dd> encode AFM output using encoding vector from <i>enc</i></p>
<dt><code>-o</code> <i>outfile</i></p>
<dd> output to file <i>outfile</i> instead of standard output</p>
<dt><code>-m</code> <i>num</i></p>
<dd> use Unicode mapping <i>num</i> in the font</dl>
<p> Platform numbers can be one of</p>
<dl>
<dt>0</p>
<dd> Apple Unicode</p>
<dt>1</p>
<dd> Macintosh</p>
<dt>2</p>
<dd> ISO</p>
<dt>3</p>
<dd> Microsoft</dl>
<p> Encodings can be</p>
<dl>
<dt>0</p>
<dd> Roman (if platform is Macintosh)</p>
<dt>0</p>
<dd> Symbol (if platform is Microsoft)</p>
<dt>1</p>
<dd> Unicode (if platform is Microsoft)</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-afm2tfm/">afm2tfm</a>(1), <a href="/docs/linux/man/1-afm2pl/">afm2pl</a>(1). FontForge (<a rel="nofollow" href="http://fontforge.sf.net">http://fontforge.sf.net</a>). LCDF TypeTools (<a rel="nofollow" href="http://lcdf.org">http://lcdf.org</a>). A closer look at TrueType fonts and pdfTeX, Han The Thanh (<a rel="nofollow" href="http://tug.org/TUGboat/tb30-1/tb94thanh.pdf">http://tug.org/TUGboat/tb30-1/tb94thanh.pdf</a>). </p>
<h2>BUGS</h2>
<p> Send bug reports to &lt;pdftex [at] tug.org&gt; (public mailing list). </p>
<h2>AUTHOR</h2>
<p> <code>ttf2afm</code> is part of pdfTeX and was written by Han The Thanh. </p>
<p> This manual page was originally written by C.M. Connelly, for the Debian GNU/Linux system, and updated by Karl Berry and others. </p>
<h2>Index</h2>
