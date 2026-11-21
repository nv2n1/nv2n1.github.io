---

title: "ttf2afm(1)"
name: "ttf2afm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttf2afm/"
description: "ttf2afm – utility to generate AFM files for TrueType fonts"
---

<p> ttf2afm &#8211; utility to generate AFM files for TrueType fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>ttf2afm</code> [<i>OPTIONS</i>] <i>FONTFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ttf2afm</code> is used to generate Adobe Font Metrics (AFM) files for TrueType (TTF) fonts to allow them to be used with TeX. </p>
<p> <code>ttf2afm</code> takes the name of a TrueType font file as a required argument. It may also take one or more options from the list below (<code>-i</code> and <code>-u</code> are mutually exclusive). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></dt>
<dd> force printing glyph names in form `index&#8217;<i>decnum</i></dd>
<dt><code>-u</code></dt>
<dd> force printing glyph names in form `uni&#8217;<i>hexnum</i></dd>
<dt><code>-c</code> <i>name</i></dt>
<dd> write encoding tables to file <i>name.eMN</i>, where <i>M</i> is the platform ID and <i>N</i> is the encoding ID</dd>
<dt><code>-v</code></dt>
<dd> print program version</dd>
<dt><code>-e</code> <i>enc</i></dt>
<dd> encode AFM output using encoding vector from <i>enc</i></dd>
<dt><code>-o</code> <i>outfile</i></dt>
<dd> output to file <i>outfile</i> instead of standard output</dd>
<dt><code>-m</code> <i>num</i></dt>
<dd> use Unicode mapping <i>num</i> in the font</dd></dl>
<p> Platform numbers can be one of</p>
<dl>
<dt>0</dt>
<dd> Apple Unicode</dd>
<dt>1</dt>
<dd> Macintosh</dd>
<dt>2</dt>
<dd> ISO</dd>
<dt>3</dt>
<dd> Microsoft</dd></dl>
<p> Encodings can be</p>
<dl>
<dt>0</dt>
<dd> Roman (if platform is Macintosh)</dd>
<dt>0</dt>
<dd> Symbol (if platform is Microsoft)</dd>
<dt>1</dt>
<dd> Unicode (if platform is Microsoft)</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-afm2tfm/">afm2tfm</a>(1), <a href="/docs/linux/man/1-afm2pl/">afm2pl</a>(1). FontForge (<a rel="nofollow" href="http://fontforge.sf.net">http://fontforge.sf.net</a>). LCDF TypeTools (<a rel="nofollow" href="http://lcdf.org">http://lcdf.org</a>). A closer look at TrueType fonts and pdfTeX, Han The Thanh (<a rel="nofollow" href="http://tug.org/TUGboat/tb30-1/tb94thanh.pdf">http://tug.org/TUGboat/tb30-1/tb94thanh.pdf</a>). </p>
<h2>BUGS</h2>
<p> Send bug reports to &lt;pdftex [at] tug.org&gt; (public mailing list). </p>
<h2>AUTHOR</h2>
<p> <code>ttf2afm</code> is part of pdfTeX and was written by Han The Thanh. </p>
<p> This manual page was originally written by C.M. Connelly, for the Debian GNU/Linux system, and updated by Karl Berry and others. </p>
