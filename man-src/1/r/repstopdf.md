---
title: "repstopdf(1)"
name: "repstopdf"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repstopdf/"
description: "epstopdf, repstopdf – convert an EPS file to PDF"
---

<h2 class="name">NAME</h2>
<p> epstopdf, repstopdf &#8211; convert an EPS file to PDF </p>
<h2>SYNOPSIS</h2>
<p> <code>epstopdf</code> [<i>options</i>] [<i>epsfile</i> [<i>pdffile</i>.pdf]]</p>
<h2>DESCRIPTION</h2>
<p> By default, <code>epstopdf</code> converts the input PostScript file to PDF, using Ghostscript. </p>
<p> <code>Epstopdf</code> transforms the Encapsulated PostScript file <i>epsfile</i> (or standard input) so that it is guaranteed to start at the 0,0 coordinate, and it sets a page size exactly corresponding to the BoundingBox. Thus, the result needs no cropping, and the PDF MediaBox is correct. </p>
<p> By default, the output name is the input name with any extension replaced by <code>.pdf</code>. An output name ending with .pdf can also be given as a second argument on the command line, or the <code>&#8211;outfile</code> (<code>-o</code>) option can be used with any name. </p>
<p> The output is PDF 1.5 by default; use, e.g., </p>
<pre>
--gsopt=-dCompatibilityLevel=1.7
</pre>
<p> to change this. (Until epstopdf 2.28 (released September 2018), the PDF version was whatever the underlying Ghostscript or other interpreter produced by default.) </p>
<p> PJL commands at the start of a file are removed. DOS EPS binary files (TN 5002) are supported. </p>
<p> If the bounding box in the input is incorrect, of course there will be resulting problems.</p>
<h2>OPTIONS</h2>
<p> Options may start with either &quot;<code>&#8211;</code>&quot; or &quot;<code>&#8212;</code>&quot;, and may be unambiguously abbreviated. It is best to use the full option name in scripts to avoid possible collisions with new options in the future. </p>
<p> General script options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> display version information and exit</p>
<dt><code>&#8211;outfile</code>=<i>file</i></p>
<dd> write result to <i>file</i>. If this option is not given, and <code>&#8211;nogs</code> or <code>&#8211;filter</code> is specified, write to standard output; otherwise, the default is to construct the output file name by replacing any extension in the input file with `.pdf&#8217;.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>debug</code></p>
<dd> write debugging info (default: false).</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>exact</code></p>
<dd> scan ExactBoundingBox (default: false).</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>filter</code></p>
<dd> read standard input and (unless <code>&#8211;outfile</code> is given) write standard output (default: false).</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>gs</code></p>
<dd> run Ghostscript (default: true). With <code>&#8211;nogs</code>, output (to standard output by default) the PostScript that would normally be converted; that is, the input PostScript as modified by <code>epstopdf</code>.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>hires</code></p>
<dd> scan HiresBoundingBox (default: false).</p>
<dt><code>&#8211;restricted</code>=<i>val</i></p>
<dd> turn on restricted mode (default: [true for repstopdf, else false]); this forbids the use of <code>&#8211;gscmd</code> and other options and imposes restrictions on the input and output file names according to the values of openin_any and openout_any (see the Web2c manual, <a rel="nofollow" href="http://tug.org/web2c">http://tug.org/web2c</a>).</dl>
<p> Options for Ghostscript (more info below):</p>
<dl>
<dt><code>&#8211;gscmd</code>=<i>val</i></p>
<dd> pipe output to <i>val</i> (default: [<code>gswin32c</code> on Windows, else <code>gs</code>])</p>
<dt><code>&#8211;gsopt</code>=<i>val</i></p>
<dd> include <i>val</i> as one argument in the gs command (can be repeated).</p>
<dt><code>&#8211;gsopts</code>=<i>val</i></p>
<dd> split <i>val</i> at whitespace and include each resulting word as an argument in the gs command (can be repeated).</p>
<dt><code>&#8211;autorotate</code>=<i>val</i></p>
<dd> set AutoRotatePages (default: None); recognized <i>val</i> choices: None, All, PageByPage. For EPS files, PageByPage is equivalent to All.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>compress</code></p>
<dd> use compression in the output (default: true); if turned off, passes <i>-dUseFlateCompression=false</i>.</p>
<dt><code>&#8211;device</code>=<i>dev</i></p>
<dd> use -sDEVICE=<i>dev</i> (default: pdfwrite); not allowed in restricted mode.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>embed</code></p>
<dd> embed fonts (default: true); passes <i>-dMaxSubsetPct=100 -dSubsetFonts=true -dEmbedAllFonts=true.</i></p>
<dt><code>&#8212;</code>[<code>no</code>]<code>gray</code></p>
<dd> grayscale output (default: false); passes <i>-sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray.</i></p>
<dt><code>&#8211;pdfsettings</code>=<i>val</i></p>
<dd> use -dPDFSETTINGS=/<i>val</i> (default is `prepress&#8217; if <code>&#8211;embed</code>, else empty); recognized <i>val</i> choices: screen, ebook, printer, prepress, default.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>quiet</code></p>
<dd> use -q, a.k.a. -dQUIET (default: false).</p>
<dt><code>&#8211;res</code>=<i>dpi, dpi</i>x<i>dpi</i></p>
<dd> set image resolution (default: [use gs default]); ignored if <code>&#8211;debug</code> is set.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>safer</code></p>
<dd> use -d(NO)QUIET (default: true).</dl>
<p> In addition to the specific options above, additional options to be used with gs can be specified with either or both of the two cumulative options <code>&#8211;gsopts</code> and <code>&#8211;gsopt.</code> </p>
<p> <code>&#8211;gsopts</code> takes a single string of options, which is split at whitespace, each resulting word then added to the gs command line individually. </p>
<p> <code>&#8211;gsopt</code> adds its argument as a single option to the gs command line. It can be used multiple times to specify options separately, and is necessary if an option or its value contains whitespace. </p>
<p> In restricted mode, options are limited to those with names and values known to be safe. Some options taking booleans, integers or fixed names are allowed, those taking general strings are not. </p>
<h2>EXAMPLES</h2>
<p> These examples all equivalently convert `test.eps&#8217; to `test.pdf&#8217;: </p>
<pre>
epstopdf test.eps
epstopdf test.eps test.pdf
cat test.eps | epstopdf --filter &gt;test.pdf
cat test.eps | epstopdf -f -o=test.pdf
</pre>
<p> Example for using HiResBoundingBox instead of BoundingBox: </p>
<pre>
epstopdf --hires test.eps
</pre>
<p> Example for <code>epstopdf</code>&#8216;s attempt at correcting PostScript: </p>
<pre>
$program --nogs test.ps &gt;testcorr.ps
</pre>
<p> In all cases, you can add <code>&#8211;debug</code> (<code>-d</code>) to see more about what <code>epstopdf</code> is doing.</p>
<h2>BUGS</h2>
<p> The case of &quot;%%BoundingBox: (atend)&quot; when input is not seekable (e.g., from a pipe) is not supported. </p>
<p> Report bugs in the program or this man page to tex-k [at] tug.org. When reporting bugs, please include an input file and the command line options specified, so the problem can be reproduced.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-pdfcrop/">pdfcrop</a></code>(1). </p>
<p> The epstopdf LaTeX package, part of the oberdiek bundle, which automates running this script on the fly under TeX: <a rel="nofollow" href="http://ctan.org/pkg/epstopdf-pkg.">http://ctan.org/pkg/epstopdf-pkg.</a></p>
<h2>AUTHOR</h2>
<p> Originally written by Sebastian Rahtz, for Elsevier Science, with subsequent contributions from Thomas Esser, Gerben Wierda, Heiko Oberdiek, and many others. Currently maintained by Karl Berry. </p>
<p> Man page originally written by Jim Van Zandt. </p>
<p> epstopdf home page: <a rel="nofollow" href="http://tug.org/epstopdf.">http://tug.org/epstopdf.</a> </p>
<p> You may freely use, modify and/or distribute this man page. </p>
<h2>Index</h2>
