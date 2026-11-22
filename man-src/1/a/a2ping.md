---

title: "a2ping(1)"
name: "a2ping"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a2ping/"
description: "a2ping.pl — convert between PS, EPS and PDF and other page description formats"
---

<p> a2ping.pl &#8212; convert between PS, EPS and PDF and other page description formats </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<code>a2ping.pl</code>&nbsp;[<code>&#8212;</code>]<code>help</code><br/>
&nbsp;<code>a2ping.pl</code>&nbsp;[<code>&#8212;</code>]<code>doc</code><br/>
&nbsp;<code>a2ping.pl</code>&nbsp;[<i>options</i>]&nbsp;&lt;<i>inputfile</i>&gt;&nbsp;[[<i>outformat</i>:]&nbsp;<i>outputfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>a2ping</code> is a UNIX command line utility written in Perl that converts many raster image and vector graphics formats to EPS or PDF and other page description formats. Accepted input file formats are: PS (PostScript), EPS, PDF, PNG, JPEG, TIFF, PNM, BMP, GIF, LBM, XPM, PCX, TGA. Accepted output formats are: EPS, PCL5, PDF, PDF1, PBM, PGM, PPM, PS, markedEPS, markedPS, PNG, XWD, BMP, TIFF, JPEG, GIF, XPM. <code>a2ping</code> delegates the low-level work to Ghostscript (GS), <code>pdftops</code> and <code>sam2p</code>. <code>a2ping</code> fixes many glitches during the EPS to EPS conversion, so its output is often more compatible and better embeddable than its input. </p>
<p> Without the <tt>&quot;--below&quot;</tt> option, it is guarenteed to start at the 0,0 coordinate. <tt>&quot;--below&quot;</tt>, <tt>&quot;--hires&quot;</tt> and <tt>&quot;-v&quot;</tt> are recommended options. </p>
<p> The page size is set exactly corresponding to the BoundingBox. This means that when Ghostscript renders it, the result needs no cropping, and the PDF MediaBox is correct. </p>
<p> If the bounding box is not right, of course, you have problems. If you feed crap in, you get crap. But you can supply the <code>&#8211;bboxfrom=compute-gs</code> option to make GS recompute the bounding box. </p>
<p> The name of the input file doesn&#8217;t matter &#8212; <code>a2ping</code> detects the file format based on the first few bytes of the file. The name of the output file matters if <i>outformat</i> is missing from the command line: then the extension of the output file determines the FileFormat (<i>outformat</i>).</p>
<h2>EXTERNAL PROGRAMS</h2>
<p> The internal file format of <code>a2ping.pl</code> is PS/EPS. Everything read is first converted to PS or EPS, then processed by <code>a2ping.pl</code>, then converted to the output format. </p>
<p> To analyse the bounding box and other properties of non-EPS PS files (and EPS files with option <code>&#8211;bboxfrom</code> other than <code>=guess</code>), GS is used. Converting PS to EPS involves this analysis. </p>
<p> To write PDF files, GS is used. </p>
<p> To read PDF files, <code>pdftops</code> from the <code>xpdf</code> package is used. </p>
<p> Sampled input formats are PNG, JPEG, TIFF, PNM, BMP, GIF, LBM, XPM, PCX and TGA. To read sampled input formats, <code>sam2p</code> is used. <code>sam2p</code> is a raster image converter written in C++ by the author of <code>a2ping.pl</code>. </p>
<p> Extra output formats are PNG, XWD, BMP, TIFF, JPEG, GIF and XPM. To write extra output formats, <code>sam2p</code> and GS are used. </p>
<p> PNM output formats are PGM, PGM and PPM. To write PNM output formats, GS is used.</p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show a summary of the usage</dd>
<dt><code>&#8211;doc</code></dt>
<dd> Show the man page</dd>
<dt><code>-v</code>, <code>&#8211;(no)verbose</code></dt>
<dd> Show progress and debug messages (default: no)</dd></dl>
<h3>Options for the Bounding box</h3>
<dl>
<dt><code>&#8211;(no)hires</code></dt>
<dd> Use HiResBoundingBox in the input file, if present (default: yes)</dd>
<dt><code>&#8211;(no)exact</code></dt>
<dd> Use ExactBoundingBox in the input file, if present (default: no)</dd>
<dt><code>&#8211;(no)keepoldmediabox</code></dt>
<dd> keep only old, [0 0]-based MediaBox in PDF (default: no)</dd>
<dt><code>&#8211;bboxfrom=</code><i>adsc|compute-gs|guess|pagesize</i></dt>
<dd> Method for determining the BoundingBox (default: guess)</dd>
<dt><code>&#8211;(no)below</code></dt>
<dd> Allow page content below and left of the origin (default: no)</dd></dl>
<h3>Options for graphics and fonts</h3>
<dl>
<dt><code>&#8211;(no)compress</code></dt>
<dd> use compression (default: best)</dd>
<dt><code>&#8211;(no)antialias</code></dt>
<dd> render shades at outlines. Possible values: (=<i>scale3yes</i> =<i>no</i> =<i>yes</i>) (default: scale3no)</dd>
<dt><code>&#8211;(no)lossy</code></dt>
<dd> allow lossy image filters (EPS-&gt;PDF) (default: yes)</dd>
<dt><code>&#8211;papersize=</code><i>unchanged|force-unknown|600bpx5cm</i></dt>
<dd> (default: default) (bp)</dd>
<dt><code>&#8211;threshold=</code></dt>
<dd> min color for 1 in 8-&gt;1 bit conv (default: 128)</dd></dl>
<h3>Options for debugging and changing internals</h3>
<dl>
<dt><code>&#8211;(no)tmpunlink</code></dt>
<dd> Unlink temporary files (default: yes). Use <code>&#8211;notmpunklink</code> if you want to inspect intermediate files.</dd>
<dt><code>&#8211;gs-cmd=</code><i>path</i></dt>
<dd> path to Ghostscript program (default: gs or gswin32c)</dd>
<dt><code>&#8211;gs-ccmd=</code><i>path</i></dt>
<dd> path to Ghostscript for BoundingBox calculation (default: gs or gswin32c)</dd>
<dt><code>&#8211;gsextra=</code><i></i><i>GS_ARGS</i><i></i></dt>
<dd> Pass extra arguments to gs</dd>
<dt><code>&#8211;extra=</code></dt>
<dd> Pass extra arguments to external program (i.e pdftops)</dd></dl>
<h2>TIPS AND TRICKS</h2>
<dl>
<dt>&bull;</dt>
<dd> If your EPS contains a wrong bounding box, you can fix it by running <tt>&quot;a2ping.pl -v --bboxfrom=compute-gs thefile.eps --&quot;</tt></dd>
<dt>&bull;</dt>
<dd> You can specify <code>&#8211;</code> as <i>inputfile</i> to get stdin and as <i>outputfile</i> to get stdout. This works even for PDF files (which must be seekable), because <code>a2ping</code> copies them to a temporary file automatically.</dd>
<dt>&bull;</dt>
<dd> If <i>inputfile</i> and <i>outputfile</i> are the same, <code>a2ping</code> copies the <i>inputfile</i> to a temporary location first. However, this usage is recommended only if there is a backup of the file to be restored in case <code>a2ping</code> doesn&#8217;t produce the desired result.</dd>
<dt>&bull;</dt>
<dd> If you specify <code>&#8212;</code> as <i>outputfile</i>, it will be the same as <i>inputfile</i>.</dd>
<dt>&bull;</dt>
<dd> <code>a2ping</code> respects <code>&#8211;Duplex</code> for FileFormat PCL5, even though GS doesn&#8217;t.</dd>
<dt>&bull;</dt>
<dd> If you have an incompatible PS that GS can read but your printer cannot print, just run <tt>&quot;a2ping.pl foo.ps PDF: - | a2ping.pl - PS: foo.ps&quot;</tt></dd>
<dt>&bull;</dt>
<dd> If you have a PS coming from Win32 (often with extension <tt>&quot;.prn&quot;</tt>), run it through <code>a2ping</code>. It will remove the resolution changes and the progress text printed to the terminal (which confuses <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1) and makes some filters in the print queue emit incorrect output).</dd>
<dt>&bull;</dt>
<dd> <code>a2ping</code> does antialiasing (<code>&#8211;antialias=scale3no</code>) of glyphs and curves when emitting a sampled image (FileFormats such as PGM and PPM). This improves readability of the glyphs. <code>=yes</code> instructs GS to do internal antialiasing, but it usually doesn&#8217;t improve much. <code>=scale3no</code> turns off GS internal antialiasing, but makes it render everything 3&#215;3 as big, and then scales it back down. <code>=scale3no</code> turns on both 3&#215;3 scaling and GS internal antialiasing, which results in thicker lines and worse quality in general.</dd>
<dt>&bull;</dt>
<dd> When creating a PBM file, antialiasing usually doesn&#8217;t improve the quality, so it is switched off by default. But if you set <code>&#8211;antialias=scale3no</code> or <code>&#8211;antialias=scale3yes</code>, GS will render a PGM file, and the value of <code>&#8211;threshold</code> determines the minimum intensity for white in the final PBM.</dd>
<dt>&bull;</dt>
<dd> If you need a bigger sampled output file, specify a larger <code>&#8211;Resolution</code>. The default is <code>&#8211;Resolution=72</code>. If your sampled output file is going to be really big, you should specify <code>&#8211;AntiAlias=yes</code> instead of the default <code>&#8211;AntiAlias=scale3no</code> to speed up conversion.</dd>
<dt>&bull;</dt>
<dd> To make sure fonts are included in a PDF file generated from eps, use <code>&#8211;gsextra=&#8217;-dEmbedAllFonts=true -dPDFSETTINGS=/printer&#8217;</code>.</dd></dl>
<h2>MISC</h2>
<dl>
<dt>&bull;</dt>
<dd> Doesn&#8217;t depend on the filename or extension of the input file.</dd>
<dt>&bull;</dt>
<dd> Conversion from EPS to PDF: fixes glitches etc., calls gs -sDEVICE=pdfwrite</dd>
<dt>&bull;</dt>
<dd> Conversion from EPS to EPS: fixes various glitches, moves (llx,lly) to (0,0), removes binary junk from the beginning of the EPS etc.</dd>
<dt>&bull;</dt>
<dd> Conversion from PDF to PDF: keeps the file intact</dd>
<dt>&bull;</dt>
<dd> Conversion from PDF to EPS: calls pdftops -eps (of the xpdf package)</dd>
<dt>&bull;</dt>
<dd> Conversion from PS to EPS: keeps 1st page only, removes setpagedevice etc.</dd></dl>
<h2>AUTHORS</h2>
<p> The author of <code>a2ping</code> is Peter Szabo &lt;<i>pts [at] fazekas.hu</i>&gt;. </p>
<p> <code>a2ping</code> is inspired by and historically based on the <code>epstopdf</code> Perl script modified by Thomas Esser, Sept. 1998, but his modifications have been removed from <code>a2ping</code>, and also <code>a2ping</code> and <code>epstopdf</code> do not share common code anymore. <code>epstopdf</code> is written by Sebastian Rahtz, for Elsevier Science. <code>epstopdf</code> contained extra tricks from Hans Hagen&#8217;s texutil. </p>
<p> <code>a2ping</code> contains contributions from several people, see the file <i></i><i>HISTORY</i><i>.txt</i> for details. Thank you all for contributing! </p>
