---
title: "dvilj4l(1)"
name: "dvilj4l"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvilj4l/"
description: "dvilj4, dvilj4l, dvilj2p, dvilj – convert a TeX DVI file to PCL, for HP LaserJet printers"
---

<h2 class="name">NAME</h2>
<p> dvilj4, dvilj4l, dvilj2p, dvilj &#8211; convert a TeX DVI file to PCL, for HP LaserJet printers </p>
<h2>SYNOPSIS</h2>
<pre><code>
dvilj[--Dnumber][-ccopies][-dmode][-D][-E][-eoutputfile]
     [-ffrompage][-g][-hheaderfile][-l][-Mflag][-mmag][-ppages]
     [-q][-r][-ttopage][-spagesize][-v][-Vmode][-w][-xxoff(mm)]
     [-yyoff(mm)][-Xxoff(dots)][-Yyoff(dots)][-z][filename]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dvilj</code> and siblings convert TeX-output <tt>&quot;.dvi&quot;</tt> files into <font SIZE="-1">PCL </font>(the Hewlett-Packard Printer Control Language) commands suitable for printing on a <font SIZE="-1">HP</font> LaserJet+, <font SIZE="-1">HP</font> LaserJet <font SIZE="-1">IIP </font>(using <code>dvilj2p</code>), <font SIZE="-1">HP</font> LaserJet 4 (using <code>dvilj4</code>), and fully compatible printers. </p>
<p> <code>dvilj4</code> also provides support for the builtin Intellifont and TrueType fonts; <font SIZE="-1">TFM</font> and <font SIZE="-1">VF</font> files are provided in the distribution. Virtual fonts are not supported directly by <code>dvilj</code>, so you must run <i><a href="/docs/linux/man/1-dvicopy/">dvicopy</a></i>(1) first, or otherwise expand the virtual fonts </p>
<p> All programs are generated from one source file <i>dvi2xx.c</i>. They are usually called via a shell script or as a line printer filter. One such script, <i><a href="/docs/linux/man/1-dvihp/">dvihp</a></i>(1), is included in the distribution. It provides command-line options similar to those of <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;D</code><i>number</i></p>
<dd> Debug according to the bits of <i>number</i>; see the <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3) manual for values. Also turns on general verbosity.</p>
<dt><code>-c</code><i>number</i></p>
<dd> Print each page <i>number</i> times (including original)</p>
<dt><code>-d</code><i>number</i></p>
<dd> print in duplex mode. The option <code>-d1</code> means long edge binding, <code>-d2</code> stands for short edge binding. This option is only selectable in <code>dvilj4</code> and <code>dvilj2p</code>.</p>
<dt><code>-D</code><i>[-12]</i></p>
<dd> Double-sided printing &#8211; see below; <code>-D1</code> prints odd sides only, <code>-D2</code> is for even pages, a trailing <code>&#8211;</code> suppresses printing of empty padding pages.</p>
<dt><code>-E</code></p>
<dd> Switch printer into econo mode (<code>dvilj4</code> only).</p>
<dt><code>-e</code><i>outfile</i></p>
<dd> Send output to <i>outfile</i> instead of the basename of dvi file extended with <tt>&quot;.lj&quot;</tt>. If outfile is <code>&#8211;</code> (as in <tt>&quot;-e-&quot;</tt>) the output is directed to standard output and can be directly piped into a spooler.</p>
<dt><code>-f</code><i>pagenum</i></p>
<dd> Print pages with TeX page numbers greater than or equal to <i>pagenum</i>.</p>
<dt><code>-g</code></p>
<dd> <i>Go</i> mode: do not reset printer at start of job.</p>
<dt><code>-h</code><i>headerfile</i></p>
<dd> Copy <i>headerfile</i> to output before translation of the <font SIZE="-1">DVI</font> file. Used to send arbitrary commands to the laserprinter.</p>
<dt><code>-l</code></p>
<dd> Print output in landscape mode; supported only by <code>dvilj2p</code> and <code>dvilj4</code>.</p>
<dt><code>-M</code><i>flag</i></p>
<dd> Do (not) call <i><a href="/docs/linux/man/1-mktexpk/">mktexpk</a></i>(1) to generate fonts on demand. <code>-M1</code> and <code>-M</code> are equivalent. <code>-M0</code> enables invoking <i><a href="/docs/linux/man/1-mktexpk/">mktexpk</a></i>(1). (This is the same as in <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1).) The default behavior (i.e., if no <code>-M</code> option is given) is chosen at compile-time; as distributed, mktexpk is enabled.</p>
<dt><code>-m</code><i>magnification</i></p>
<dd> Specify the magnification to use. The following are available: </p>
<pre>
  -m#usermag e.g., #900
  -m0 equivalent to -m#1000
  -mh equivalent to -m#1095
  -m1 equivalent to -m#1200
  -mq equivalent to -m#1250
  -m2 equivalent to -m#1440
  -m3 equivalent to -m#1728
  -m4 equivalent to -m#2074
  -m5 equivalent to -m#2488
</pre>
<dt><code>-p</code><i>pagecount</i></p>
<dd> Print <i>pagecount</i> pages after the starting page.</p>
<dt><code>-q</code></p>
<dd> Quiet operation: omit final statistics, etc.</p>
<dt><code>-r</code></p>
<dd> Toggle page reversal.</p>
<dt><code>-s</code><i>pagesize</i></p>
<dd> Specify the page size: </p>
<pre>
  -s1: Executive (7.25&quot; x 10.5&quot;)
  -s2: Letter (8.5&quot; x 11&quot;)
  -s3: Legal (8.5&quot; x 14&quot;)
  -s6: Ledger (11&quot; x 17&quot;)
  -s25: A5 paper (148mm x 210mm)
  -s26: A4 paper (210mm x 297mm)
  -s27: A3 (297mm x 420mm)
  -s45: JIS B5 paper (182mm x 257mm)
  -s46: JIS B4 paper (250mm x 354mm)
  -s71: Hagaki postcard (100mm x 148mm)
  -s72: Oufuku-Hagaki postcard (200mm x 148mm)
  -s80: Monarch Envelope (3 7/8&quot; x 7 1/2&quot;)
  -s81: Commercial Envelope 10 (4 1/8&quot; x 9 1/2&quot;)
  -s90: International DL (110mm x 220mm)
  -s91: International C5 (162mm x 229mm)
  -s100: International B5 (176mm x 250mm)
</pre>
<p> These values are from the <font SIZE="-1">PCL 5</font> technical reference manual. If the <code>-s</code> commandline option is omitted, no clipping is performed at the bottom of the page. (But printing below the paper bottom should not disturb any correctly behaving <font SIZE="-1">PCL</font> printer.) Please remember that the correct paper tray must be installed for selected paper size, so use this option only if you have full control over your print destination.</p>
<dt><code>-t</code><i>pagenum</i></p>
<dd> Print pages with TeX page numbers less than or equal to <i>pagenum</i>.</p>
<dt><code>-v</code></p>
<dd> Verbose mode: list fonts used, etc.</p>
<dt><code>-V</code><i>mode</i></p>
<dd> Compatibility mode. As <i>mode</i>, use <tt>&quot;K&quot;</tt> for Kyocera, <tt>&quot;B&quot;</tt> for Brother, <tt>6</tt> for <font SIZE="-1">LJ6</font> printers.</p>
<dt><code>-w</code></p>
<dd> Omit warnings.</p>
<dt><code>-x</code><i>offset</i></p>
<dd> Global x-offset in mm on output page relative to 1 inch/1 inch origin.</p>
<dt><code>-y</code><i>offset</i></p>
<dd> Global y-offset in mm on output page relative to 1 inch/1 inch origin.</p>
<dt><code>-X</code><i>offset</i></p>
<dd> Global x-offset in dots on output page (overrides 1 inch/1 inch origin).</p>
<dt><code>-Y</code><i>offset</i></p>
<dd> Global y-offset in dots on output page (overrides 1 inch/1 inch origin).</p>
<dt><code>-z</code></p>
<dd> Print a test page with the page counter at end of job.</dl>
<h2>OPERANDS</h2>
<p> If no operands are specified a brief usage message is displayed.</p>
<dl>
<dt><i>filename</i></p>
<dd> The <font SIZE="-1">DVI</font> file name that shall be converted by <code>dvilj</code>. It must always be seekable. </p>
<p> The output file name is constructed from <i>filename</i>. Either an extension <tt>&quot;.dvi&quot;</tt> is replaced by <tt>&quot;.lj&quot;</tt>, or the extension <tt>&quot;.lj&quot;</tt> is appended. </p>
<p> If <i>filename</i> is <code>&#8211;</code>, the <font SIZE="-1">DVI</font> file is read from standard input and the resulting <font SIZE="-1">PCL</font> document is written to standard output. (Please remember that thhe <font SIZE="-1">DVI</font> file must be seekable, even if it&#8217;s stdin.)</dl>
<h2>SUPPORTED TeX \special COMMANDS</h2>
<p> <tt>&quot;\special&quot;</tt> commands supported by <code>dvilj</code> have the generic syntax </p>
<p>\special<br />
{<br />
    key1 = value key1 = &#8220;value with space&#8221;<br />
}<br />
\special<br />
{<br />
    key3 = value key4 = &#8216;note optional spaces around equal sign&#8217;<br />
}</p>
<p> I.e., specials are a sequence of key/value pairs, separated by an equal sign. Spaces around the equal sign are ignored. The value is either a space separated word, or a quoted string. Both double and single quotes can be used, alternatively. There is no support for quoting quote characters in values; if you want both double and single quotes in one value, you&#8217;re out of luck. </p>
<p> The following key/value combinations are valid:</p>
<dl>
<dt><code>hpfile</code>=<i>file</i></p>
<dd> Insert <i>file</i> at the current position. <i>file</i> is searched with <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3), see below. </p>
<p> The file content must be valid for this printer, i.e., it should contain <font SIZE="-1">PCL</font> escape sequences or <font SIZE="-1">HP-GL/2</font> commands. If the file is a graphics file, this typically means that the upper left corner of the graphics is placed at the current position. </p>
<p> <font SIZE="-1">PCL</font> absolute positioning escape sequences in <i>file</i> are rewritten to be relative positioning commands; the lowest appearing coordinate is used as reference.</p>
<dt><code>hpfile_verbatim</code>=<i>file</i></p>
<dd> Insert <i>file</i> verbatim at the current position, without any changes of the file content. <i>file</i> is searched with <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3), see below. </p>
<p> This is mostly used to keep absolute positions in <font SIZE="-1">PCL</font> files.</p>
<dt><code>psfile</code>=<i>file</i> <code>llx</code>=<i>x0</i> <code>lly</code>=<i>y0</i> <code>urx</code>=<i>x1</i> <code>ury</code>=<i>y1</i> <code>rwi</code>=<i>s</i></p>
<dd> Convert Postscript file <i>file</i> to <font SIZE="-1">HP PCL,</font> by Ghostscript with device <tt>&quot;ljetplus&quot;</tt>, and insert the resulting graphics file at the current position, rewriting absolute position escape sequences. <i>file</i> is searched with <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3), see below. </p>
<p> The accompanying key/value pairs are mandatory, they can be specified in an arbitrary order. Values <i>x0</i>, <i>x1</i>, <i>y0</i>, <i>y1</i>, and <i>s</i> are integers. (<i>x0</i>,<i>y0</i>) is the lower left corner, (<i>x1</i>,<i>y1</i>) the upper right corner of the image. </p>
<p> <code>Please note: The specific semantics of this special is not known.</code> In particular, the <code>rwi</code> parameter is some scale factor; but even looking at the source code it is not quite clear what the special&#8217;s author intended to implement here. In addition, it is unclear what dimensions are used to specify the corners, Postscript points or <font SIZE="-1">PCL</font> dots. </p>
<p> <i>If you happen to know the psfile semantics, or if you spent the work analyzing them, please inform us at tex-k [at] tug.org, so that we can update this man page with the relevant information.</i></p>
<dt><code>dvilj-psfile-syntax</code>=<i>syntax</i></p>
<dd> where <i>syntax</i> is either <tt>&quot;dvilj&quot;</tt> or <tt>&quot;ignore&quot;</tt>. This is a very crude way to tell the driver what to do with <code>psfile</code> specials. </p>
<p> If the value is <tt>&quot;ignore&quot;</tt>, all <code>psfile</code> specials that are processed afterwards are ignored, until the next <code>dvilj-psfile-syntax</code> special is processed. </p>
<p> If the value is <tt>&quot;dvilj&quot;</tt>, <code>psfiles</code> specials are processed as explained above, until the next <code>dvilj-psfile-syntax</code> special is processed. </p>
<p> An obvious, planned, extension is the value <tt>&quot;dvips&quot;</tt>, but this has not been implemented yet. </p>
<p> That special is not as simple as it sounds at first. Since its semantics is defined by processing order, it is only of use if it is placed on the same page as the <code>psfile</code> special. Having it once in a file (e.g., on the first page) does not help if you print just one page of the document &#8212; <code>dvilj</code> does not do prescanning of first-page specials like some other drivers do. (Patches would be welcome, of course.)</p>
<dt><code>comment</code>=<i>arbitrary text</i></p>
<dd>
<dt><code>comment</code> <i>arbitrary text</i></p>
<dd> This causes the rest of the special to be ignored; it may be used to add meta-information to a <font SIZE="-1">DVI</font> file. </p>
<p> With the first form, the comment may appear anywhere in the special. When it appears first, the processing of this special is terminated and all other text behind is ignored. </p>
<p> The second form is a speciality that has been introduced for compatibility with other drivers. If the first keyword of the special is <code>comment</code> and has no value, it is taken as a valid comment syntax, too; the rest of the special is ignored.</p>
<dt><code>orientation</code>=<i>po</i></p>
<dd> Position the page on the physical paper. The value <i>po</i> may be one of the following values: </p>
<pre><code>
  0  for portrait
  1  for landscape
  2  for reverse portrait
  3  for reverse landscape
</code></pre>
<dt><code>defpoint</code>=<i>n(x,y)</i></p>
<dd> Define the point number <i>n</i>. This point can be referred to later in other special commands to specify areas that shall be filled with some pattern. <i>n</i> must be between 0 and 79. </p>
<p> <i>x</i> and <i>y</i> are the position of that point and have the form <tt>&quot;?pt&quot;</tt> where <tt>&quot;?&quot;</tt> is a floating point number. The positions are relative to the <font SIZE="-1">DVI</font> page origin; i.e., coordinates increase moving right and down, the point of origin is (1in,1in) in the upper left corner, altered by options <code>-x</code>, <code>-y</code>, <code>-X</code>, and <code>-Y</code>, but not by \hoffset and offset. </p>
<p> <i>x</i> and <i>y</i> can be omitted, i.e., the values <tt>3</tt> or <tt>&quot;4(,)&quot;</tt> are valid. Then the current page position is used as position for point <i>n</i>.</p>
<dt><code>resetpoints</code>=&quot;all&quot;</p>
<dd> This undefines all points again.</p>
<dt><code>gray</code>=<i>gray_scale</i></p>
<dd>
<dt><code>grey</code>=<i>gray_scale</i></p>
<dd> This sets the fill mode for the next <code>fill</code> special, the area will be filled with gray color. (<code>grey</code> is an alias for <code>gray</code>.) Any pattern specification is reset. </p>
<p> <i>gray_scale</i> is the percentage of gray that shall be used here; with <tt>0</tt> meaning white and <tt>100</tt> meaning black. </p>
<p> Caveat: That special is actually a misnomer. <font SIZE="-1">PCL</font> names these gray scales <i>shading patterns</i> and they are created by placing dots in the area. The gray scale selects how far spread the dots are. In the lower ranges, this doesn&#8217;t look very gray on close sight, but more like a dotted background. Furthermore, the gray scales are not as fine-grained as the value range 0..100 might make you believe. In reality, there are only 8 different gray patterns available: </p>
<pre>
   1 -  2%
   3 - 10%
  11 - 20%
  21 - 35%
  36 - 55%
  56 - 80%
  81 - 99%
  100%
</pre>
<p> One of these patterns is selected according to the <i>gray_scale</i> value.</p>
<dt><code>pattern</code>=<i>pat</i></p>
<dd> This sets the fill mode for the next <code>fill</code> special, the area will be filled with a pattern. Any gray color specification is reset. </p>
<p> <i>pat</i> is one of the following values: </p>
<pre>
  1  horizontal lines
  2  vertical lines
  3  diagonal lines, from lower left corner to upper right corner
  4  diagonal lines, from upper right corner to lower left corner
  5  crossed lines, vertically
  6  crossed lines, diagonally
</pre>
<dt><code>fill</code>=<i>a/b</i></p>
<dd> Fill the area between the points <i>a</i> and <i>b</i>, according to the current fill mode. </p>
<p> Point <i>a</i> <code>must</code> be the upper left corner and point <i>b</i> <code>must</code> be the lower left corner of the rectangle. Otherwise the result is garbage. </p>
<p> The default fill mode is 10% gray color filling.</p>
<dt><i>filename</i></p>
<dd> This is a legacy special, its use is depreciated. If the special is just one word that names an existing file, that file is verbatim included. Contrary to other file inclusion means, the file is not searched with <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3). <i>You are not supposed to use this special and we won&#8217;t fix any problems with it.</i></dl>
<p> It should be noted that the special parser does sometimes accept constructs that are not valid as in the documentation above. Then, the output is most often damaged in some way.</p>
<h3>Searching for Included Files</h3>
<p> Proper file include specials search the file with <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3). The search path is configured by variable <tt>&quot;DVILJINPUTS&quot;</tt> and, if the file is not found in that search path, by variable <tt>&quot;TEXINPUTS&quot;</tt>. </p>
<p> Search via <tt>&quot;DVILJINPUTS&quot;</tt> covers the use case that one has common site-wide graphics that shall be included in documents, e.g., scanned signatures. Search via <tt>&quot;TEXINPUTS&quot;</tt> covers the use case that one has graphics as part of ones current document. </p>
<p> <tt>&quot;dvilj&quot;</tt> is used as the <tt>&quot;.PROGRAM&quot;</tt> name in <i>texmf.cnf</i>, for all driver variants, independent of the actual program name.</p>
<h3>Unknown Specials and TEX_HUSH configuration</h3>
<p> <i><a href="/docs/linux/man/3-kpathsea/">Kpathsea</a></i>(3) has the concept of warning suppression with the configuration variable <tt>&quot;TEX_HUSH&quot;</tt>, please refer to its Info node <i>TeX support / Suppressing warnings</i>. That variable holds a colon-separated identifiers that specifies the to-be-suppressed warnings. </p>
<p> If <tt>&quot;special&quot;</tt> is among the listed values, <code>dvilj</code> does not output warnings any more about specials that it doesn&#8217;t know about. But if there is a recognized special and if that special has an invalid parameter, then a warning is output nevertheless, independent of the content of <tt>&quot;TEX_HUSH&quot;</tt>.</p>
<h2>DOUBLE PAGE PRINTING</h2>
<p> If the printer has a duplex unit installed, duplex printing can be demanded with the <code>-d</code> option. </p>
<p> Otherwise, the command line option <code>-D</code> causes the printer to print in doublepage mode, that is, roughly speaking, printing first the even pages and then the odd pages of a document. If <code>-D</code> is used to print both even and odd pages (<code>-D</code> is used without the optional 1 or 2) the following will happen after half of the pages is printed: <font SIZE="-1">LJ:</font> the printer stops, shows message &#8220;<font SIZE="-1">FEED&#8221;</font> and switches on manual feed led. The printer continues when either the printed pages are fed into the manual page feeder, or the operator pushes the continue button (after placing first the printed pages into the paper tray). </p>
<p> If <code>-D1</code> was specified only odd pages will be printed, <code>-D2</code> can be used for even pages. A trailing <tt>&quot;-&quot;</tt> (as in <code>-D-</code>, <code>-D1-</code> or <code>-D2-</code>) supresses printing of empty pages which are generated for padding otherwise. </p>
<p> The driver allows the <code>-D</code> option for both print-directions (front-to-back or back-to-front printing). It tries to be clever in certain cases: when a document has an odd number of pages it inserts in the right place an empty page when a document starts with page 0 the driver inserts an empty page after the 0-page when a piece of a document is printed that starts with an even page-number it prints this page at the backside of the first page to ensure that the odd sides are always on the frontside. The 0-page is treated like an odd page. </p>
<p> The doubleside option works for all LJs, not only for the new D model with does doubleside-printing (actually, I don&#8217;t know whether it makes much sense on the new <font SIZE="-1">LJ II D</font> at all). </p>
<p> Caveat on the doubleside-option: When it is used frequently or on very large files, it might become necessary to clean the printer much more frequently. </p>
<p> The command line option <code>-p</code><i>X</i> can be used to abort printing after the output of <i>X</i> pages (can lead to strange results together with <code>-D</code>). I personally dislike this option. The secure way of printing a part of a document is using <code>-f</code> (from) and <code>-t</code> (to).</p>
<h2>ENVIRONMENT</h2>
<p> <code>dvilj</code> uses the same environment variables and algorithms for finding font files as TeX and its friends do. See the documentation for the <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3) library for details. (Repeating it here is too cumbersome.)</p>
<dl>
<dt>&quot;DVILJFONTS&quot;</p>
<dd> If set, overrides all other font paths.</p>
<dt>&quot;DVILJMAKEPK&quot;</p>
<dd> If set, overrides <i><a href="/docs/linux/man/1-mktexpk/">mktexpk</a></i>(1) as the name of the command to execute to create a <font SIZE="-1">PK</font> file if one isn&#8217;t found.</p>
<dt>&quot;DVILJSIZES&quot;</p>
<dd> May be set to indicate which sizes of fonts are available. It should consist of a list of numbers separated by colons. If the list begins with a colon, the system default sizes are used, as well. Sizes are expressed in dots per inch; decimals may be used for <tt>&quot;pxl&quot;</tt> files: for example, a 300 dots per inch file magnified by half a step comes out to 1643 dots per five inches, which should be encoded as 328.6. <code>dvilj</code> tries the actual size of the font before trying any of the given sizes.</p>
<dt>&quot;DVILJINPUTS&quot;</p>
<dd> Primary search path for include files.</p>
<dt>&quot;TEXINPUTS&quot;</p>
<dd> Secondary search path for include files.</p>
<dt>&quot;TEX_HUSH&quot;</p>
<dd> Colon separated list of identifiers that name situations where no warning shall be output. The following identifiers are used: </p>
<pre>
  checksum  suppress mismatched font checksum warnings
  readable  suppress warnings about unreadable files
  special   suppress warnings about unknown specials
  all       suppress all warning classes above
  none      suppress no warnings
</pre>
<dt>&quot;KPATHSEA_DEBUG&quot;</p>
<dd> Trace <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3) lookups; set to -1 for complete tracing.</p>
<dt>&quot;GS_PATH&quot;</p>
<dd> On Windows, this may be the path to Ghostscript; there the default is <i>gswin32c.exe</i>. </p>
<p> On Unix, this environment variable is not used. Ghostscript is called as <i><a href="/docs/linux/man/1-gs/">gs</a></i>(1) and must be found over <tt>$PATH</tt>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dvihp/">dvihp</a></i>(1), <i><a href="/docs/linux/man/1-dvicopy/">dvicopy</a></i>(1), <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1), <i><a href="/docs/linux/man/1-xdvi/">xdvi</a></i>(1), <i><a href="/docs/linux/man/1-mktexpk/">mktexpk</a></i>(1), <i><a href="/docs/linux/man/1-gs/">gs</a></i>(1), <i><a href="/docs/linux/man/3-kpathsea/">kpathsea</a></i>(3) </p>
<p> Email bug reports to tex-k [at] tug.org. </p>
<p> Source is at &lt;<a rel="nofollow" href="http://mirror.ctan.org/dviware/dviljk/">http://mirror.ctan.org/dviware/dviljk/</a>&gt;; but for compilation the texk build environment is needed, from &lt;<a href="svn://tug.org/texlive/*/Build/source">svn://tug.org/texlive/*/Build/source</a>&gt;. </p>
<p> As of July 2007, <font SIZE="-1">PCL</font> reference documentation is found at <font SIZE="-1">HP</font>&#8216;s Web site at &lt;<a rel="nofollow" href="http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=bpl04568">http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=bpl04568</a>&gt;. At the end of that page are links to reference manuals for <font SIZE="-1">PCL</font> and <font SIZE="-1">PJL.</font> </p>
<p> In case that page is changed, here are the URLs of these documents. All have the form &lt;<a rel="nofollow" href="http://h20000.www2.hp.com/bc/docs/support/SupportManual/bpl">http://h20000.www2.hp.com/bc/docs/support/SupportManual/bpl</a>&lt;<font SIZE="-1">ID</font>&gt;/bpl&lt;<font SIZE="-1">ID</font>&gt;.pdf&gt;, where <tt>&quot;&lt;ID&gt;&quot;</tt> is the following document <font SIZE="-1">ID:</font></p>
<dl>
<dt><code>13205</code></p>
<dd> <font SIZE="-1">PCL 5</font> Technical Quick Reference Guide. This is the 1st thing to look up if you have questions about <font SIZE="-1">PCL</font> escape sequences.</p>
<dt><code>13210</code> and <code>13211</code></p>
<dd> <font SIZE="-1">PCL 5</font> Technical Reference Manual (part I and <font SIZE="-1">II</font>). This is the full-detailled explanation that you need to look up if you don&#8217;t understand how the printer works. Part I is the actual manual, part <font SIZE="-1">II</font> explains <font SIZE="-1">HP-GL/2</font> and has overall tips.</p>
<dt><code>13208</code> and <code>13207</code></p>
<dd> <font SIZE="-1">PJL</font> Technical Reference Manual (and addendum)</p>
<dt><code>13212</code></p>
<dd> <font SIZE="-1">PCL 5</font> Color Manual. This explains color specials for the newer <font SIZE="-1">HP</font> printers. (Not of much use today; for practical purposes we would need to add color specials to <code>dvilj</code> first.)</p>
<dt><code>13206</code> and <code>13209</code></p>
<dd> Comparison Guide (and addendum) that documents which <font SIZE="-1">PCL</font> escape sequences are supported on which <font SIZE="-1">HP</font> printers.</dl>
<h2>AUTHOR</h2>
<p> dvi2xx by Gustaf Neumann, Wirtschaftsuniversitaet Wien. </p>
<p> dviljk fork by Karl Berry. </p>
<p> Joachim Schrod &lt;jschrod [at] acm.org&gt; supplied security fixes and updated this man page.</p>
<h2>LICENSE</h2>
<p> dvi2xx is public domain software. dviljk changes are covered by the <font SIZE="-1">GNU</font> General Public License. </p>
<h2>Index</h2>
