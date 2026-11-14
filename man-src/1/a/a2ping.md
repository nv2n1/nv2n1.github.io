---
title: "a2ping(1)"
name: "a2ping"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a2ping/"
description: "a2ping.pl — convert between PS, EPS and PDF and other page description formats"
---

<h2 class="name">NAME</h2>
<p> a2ping.pl &#8212; convert between PS, EPS and PDF and other page description formats </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<code>a2ping.pl</code>&nbsp;[<code>&#8212;</code>]<code>help</code><br />
&nbsp;<code>a2ping.pl</code>&nbsp;[<code>&#8212;</code>]<code>doc</code><br />
&nbsp;<code>a2ping.pl</code>&nbsp;[<i>options</i>]&nbsp;&lt;<i>inputfile</i>&gt;&nbsp;[[<i>outformat</i>:]&nbsp;<i>outputfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>a2ping</code> is a <font SIZE="-1">UNIX</font> command line utility written in Perl that converts many raster image and vector graphics formats to <font SIZE="-1">EPS</font> or <font SIZE="-1">PDF</font> and other page description formats. Accepted input file formats are: <font SIZE="-1">PS</font> (PostScript), <font SIZE="-1">EPS, PDF, PNG, JPEG, TIFF, PNM, BMP, GIF, LBM, XPM, PCX, TGA.</font> Accepted output formats are: <font SIZE="-1">EPS, PCL5, PDF, PDF1, PBM, PGM, PPM, PS,</font> markedEPS, markedPS, <font SIZE="-1">PNG, XWD, BMP, TIFF, JPEG, GIF, XPM.</font> <code>a2ping</code> delegates the low-level work to Ghostscript (<font SIZE="-1">GS</font>), <code>pdftops</code> and <code>sam2p</code>. <code>a2ping</code> fixes many glitches during the <font SIZE="-1">EPS</font> to <font SIZE="-1">EPS</font> conversion, so its output is often more compatible and better embeddable than its input. </p>
<p> Without the <tt>&quot;--below&quot;</tt> option, it is guarenteed to start at the 0,0 coordinate. <tt>&quot;--below&quot;</tt>, <tt>&quot;--hires&quot;</tt> and <tt>&quot;-v&quot;</tt> are recommended options. </p>
<p> The page size is set exactly corresponding to the BoundingBox. This means that when Ghostscript renders it, the result needs no cropping, and the <font SIZE="-1">PDF</font> MediaBox is correct. </p>
<p> If the bounding box is not right, of course, you have problems. If you feed crap in, you get crap. But you can supply the <code>&#8211;bboxfrom=compute-gs</code> option to make <font SIZE="-1">GS</font> recompute the bounding box. </p>
<p> The name of the input file doesn&#8217;t matter &#8212; <code>a2ping</code> detects the file format based on the first few bytes of the file. The name of the output file matters if <i>outformat</i> is missing from the command line: then the extension of the output file determines the FileFormat (<i>outformat</i>).</p>
<h2>EXTERNAL PROGRAMS</h2>
<p> The internal file format of <code>a2ping.pl</code> is <font SIZE="-1">PS/EPS.</font> Everything read is first converted to <font SIZE="-1">PS</font> or <font SIZE="-1">EPS,</font> then processed by <code>a2ping.pl</code>, then converted to the output format. </p>
<p> To analyse the bounding box and other properties of non-EPS <font SIZE="-1">PS</font> files (and <font SIZE="-1">EPS</font> files with option <code>&#8211;bboxfrom</code> other than <code>=guess</code>), <font SIZE="-1">GS</font> is used. Converting <font SIZE="-1">PS</font> to <font SIZE="-1">EPS</font> involves this analysis. </p>
<p> To write <font SIZE="-1">PDF</font> files, <font SIZE="-1">GS</font> is used. </p>
<p> To read <font SIZE="-1">PDF</font> files, <code>pdftops</code> from the <code>xpdf</code> package is used. </p>
<p> Sampled input formats are <font SIZE="-1">PNG, JPEG, TIFF, PNM, BMP, GIF, LBM, XPM, PCX</font> and <font SIZE="-1">TGA.</font> To read sampled input formats, <code>sam2p</code> is used. <code>sam2p</code> is a raster image converter written in C<font SIZE="-2">++</font> by the author of <code>a2ping.pl</code>. </p>
<p> Extra output formats are <font SIZE="-1">PNG, XWD, BMP, TIFF, JPEG, GIF</font> and <font SIZE="-1">XPM.</font> To write extra output formats, <code>sam2p</code> and <font SIZE="-1">GS</font> are used. </p>
<p> <font SIZE="-1">PNM</font> output formats are <font SIZE="-1">PGM, PGM</font> and <font SIZE="-1">PPM.</font> To write <font SIZE="-1">PNM</font> output formats, <font SIZE="-1">GS</font> is used.</p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a summary of the usage</p>
<dt><code>&#8211;doc</code></p>
<dd> Show the man page</p>
<dt><code>-v</code>, <code>&#8211;(no)verbose</code></p>
<dd> Show progress and debug messages (default: no)</dl>
<h3>Options for the Bounding box</h3>
<dl>
<dt><code>&#8211;(no)hires</code></p>
<dd> Use HiResBoundingBox in the input file, if present (default: yes)</p>
<dt><code>&#8211;(no)exact</code></p>
<dd> Use ExactBoundingBox in the input file, if present (default: no)</p>
<dt><code>&#8211;(no)keepoldmediabox</code></p>
<dd> keep only old, [0 0]-based MediaBox in <font SIZE="-1">PDF</font> (default: no)</p>
<dt><code>&#8211;bboxfrom=</code><i>adsc|compute-gs|guess|pagesize</i></p>
<dd> Method for determining the BoundingBox (default: guess)</p>
<dt><code>&#8211;(no)below</code></p>
<dd> Allow page content below and left of the origin (default: no)</dl>
<h3>Options for graphics and fonts</h3>
<dl>
<dt><code>&#8211;(no)compress</code></p>
<dd> use compression (default: best)</p>
<dt><code>&#8211;(no)antialias</code></p>
<dd> render shades at outlines. Possible values: (=<i>scale3yes</i> =<i>no</i> =<i>yes</i>) (default: scale3no)</p>
<dt><code>&#8211;(no)lossy</code></p>
<dd> allow lossy image filters (<font SIZE="-1">EPS-</font>&gt;<font SIZE="-1">PDF</font>) (default: yes)</p>
<dt><code>&#8211;papersize=</code><i>unchanged|force-unknown|600bpx5cm</i></p>
<dd> (default: default) (bp)</p>
<dt><code>&#8211;threshold=</code></p>
<dd> min color for 1 in 8-&gt;1 bit conv (default: 128)</dl>
<h3>Options for debugging and changing internals</h3>
<dl>
<dt><code>&#8211;(no)tmpunlink</code></p>
<dd> Unlink temporary files (default: yes). Use <code>&#8211;notmpunklink</code> if you want to inspect intermediate files.</p>
<dt><code>&#8211;gs-cmd=</code><i>path</i></p>
<dd> path to Ghostscript program (default: gs or gswin32c)</p>
<dt><code>&#8211;gs-ccmd=</code><i>path</i></p>
<dd> path to Ghostscript for BoundingBox calculation (default: gs or gswin32c)</p>
<dt><code>&#8211;gsextra=</code><i></i><font SIZE="-1"><i>GS_ARGS</i></font><i></i></p>
<dd> Pass extra arguments to gs</p>
<dt><code>&#8211;extra=</code></p>
<dd> Pass extra arguments to external program (i.e pdftops)</dl>
<h2>TIPS AND TRICKS</h2>
<dl>
<dt>&bull;</p>
<dd> If your <font SIZE="-1">EPS</font> contains a wrong bounding box, you can fix it by running <tt>&quot;a2ping.pl -v --bboxfrom=compute-gs thefile.eps --&quot;</tt></p>
<dt>&bull;</p>
<dd> You can specify <code>&#8211;</code> as <i>inputfile</i> to get stdin and as <i>outputfile</i> to get stdout. This works even for <font SIZE="-1">PDF</font> files (which must be seekable), because <code>a2ping</code> copies them to a temporary file automatically.</p>
<dt>&bull;</p>
<dd> If <i>inputfile</i> and <i>outputfile</i> are the same, <code>a2ping</code> copies the <i>inputfile</i> to a temporary location first. However, this usage is recommended only if there is a backup of the file to be restored in case <code>a2ping</code> doesn&#8217;t produce the desired result.</p>
<dt>&bull;</p>
<dd> If you specify <code>&#8212;</code> as <i>outputfile</i>, it will be the same as <i>inputfile</i>.</p>
<dt>&bull;</p>
<dd> <code>a2ping</code> respects <code>&#8211;Duplex</code> for FileFormat <font SIZE="-1">PCL5,</font> even though <font SIZE="-1">GS</font> doesn&#8217;t.</p>
<dt>&bull;</p>
<dd> If you have an incompatible <font SIZE="-1">PS</font> that <font SIZE="-1">GS</font> can read but your printer cannot print, just run <tt>&quot;a2ping.pl foo.ps PDF: - | a2ping.pl - PS: foo.ps&quot;</tt></p>
<dt>&bull;</p>
<dd> If you have a <font SIZE="-1">PS</font> coming from Win32 (often with extension <tt>&quot;.prn&quot;</tt>), run it through <code>a2ping</code>. It will remove the resolution changes and the progress text printed to the terminal (which confuses <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1) and makes some filters in the print queue emit incorrect output).</p>
<dt>&bull;</p>
<dd> <code>a2ping</code> does antialiasing (<code>&#8211;antialias=scale3no</code>) of glyphs and curves when emitting a sampled image (FileFormats such as <font SIZE="-1">PGM</font> and <font SIZE="-1">PPM</font>). This improves readability of the glyphs. <code>=yes</code> instructs <font SIZE="-1">GS</font> to do internal antialiasing, but it usually doesn&#8217;t improve much. <code>=scale3no</code> turns off <font SIZE="-1">GS</font> internal antialiasing, but makes it render everything 3&#215;3 as big, and then scales it back down. <code>=scale3no</code> turns on both 3&#215;3 scaling and <font SIZE="-1">GS</font> internal antialiasing, which results in thicker lines and worse quality in general.</p>
<dt>&bull;</p>
<dd> When creating a <font SIZE="-1">PBM</font> file, antialiasing usually doesn&#8217;t improve the quality, so it is switched off by default. But if you set <code>&#8211;antialias=scale3no</code> or <code>&#8211;antialias=scale3yes</code>, <font SIZE="-1">GS</font> will render a <font SIZE="-1">PGM</font> file, and the value of <code>&#8211;threshold</code> determines the minimum intensity for white in the final <font SIZE="-1">PBM.</font></p>
<dt>&bull;</p>
<dd> If you need a bigger sampled output file, specify a larger <code>&#8211;Resolution</code>. The default is <code>&#8211;Resolution=72</code>. If your sampled output file is going to be really big, you should specify <code>&#8211;AntiAlias=yes</code> instead of the default <code>&#8211;AntiAlias=scale3no</code> to speed up conversion.</p>
<dt>&bull;</p>
<dd> To make sure fonts are included in a <font SIZE="-1">PDF</font> file generated from eps, use <code>&#8211;gsextra=&#8217;-dEmbedAllFonts=true -dPDFSETTINGS=/printer&#8217;</code>.</dl>
<h2>MISC</h2>
<dl>
<dt>&bull;</p>
<dd> Doesn&#8217;t depend on the filename or extension of the input file.</p>
<dt>&bull;</p>
<dd> Conversion from <font SIZE="-1">EPS</font> to <font SIZE="-1">PDF:</font> fixes glitches etc., calls gs -sDEVICE=pdfwrite</p>
<dt>&bull;</p>
<dd> Conversion from <font SIZE="-1">EPS</font> to <font SIZE="-1">EPS:</font> fixes various glitches, moves (llx,lly) to (0,0), removes binary junk from the beginning of the <font SIZE="-1">EPS</font> etc.</p>
<dt>&bull;</p>
<dd> Conversion from <font SIZE="-1">PDF</font> to <font SIZE="-1">PDF:</font> keeps the file intact</p>
<dt>&bull;</p>
<dd> Conversion from <font SIZE="-1">PDF</font> to <font SIZE="-1">EPS:</font> calls pdftops -eps (of the xpdf package)</p>
<dt>&bull;</p>
<dd> Conversion from <font SIZE="-1">PS</font> to <font SIZE="-1">EPS:</font> keeps 1st page only, removes setpagedevice etc.</dl>
<h2>AUTHORS</h2>
<p> The author of <code>a2ping</code> is Peter Szabo &lt;<i>pts [at] fazekas.hu</i>&gt;. </p>
<p> <code>a2ping</code> is inspired by and historically based on the <code>epstopdf</code> Perl script modified by Thomas Esser, Sept. 1998, but his modifications have been removed from <code>a2ping</code>, and also <code>a2ping</code> and <code>epstopdf</code> do not share common code anymore. <code>epstopdf</code> is written by Sebastian Rahtz, for Elsevier Science. <code>epstopdf</code> contained extra tricks from Hans Hagen&#8217;s texutil. </p>
<p> <code>a2ping</code> contains contributions from several people, see the file <i></i><font SIZE="-1"><i>HISTORY</i></font><i>.txt</i> for details. Thank you all for contributing! </p>
<h2>Index</h2>
