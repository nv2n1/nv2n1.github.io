---
title: "pstopnm(1)"
name: "pstopnm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstopnm/"
description: "pstopnm – convert a PostScript file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pstopnm &#8211; convert a PostScript file into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pstopnm</code> [<code>-stdout</code>] [<code>-forceplain</code>] [<code>-help</code>] [<code>-llx</code> <i>s</i>] [<code>-lly</code> <i>s</i>] [<code>-landscape</code>] [<code>-portrait</code>] [<code>-nocrop</code>] [<code>-pbm</code> |<code>-pgm</code> |<code>-ppm</code>] [<code>-urx</code> <i>s</i>] [<code>-ury</code> <i>s</i>] [<code>-verbose</code>] [<code>-xborder</code> <i>n</i>] [<code>-xmax</code> <i>n</i>] [<code>-xsize</code> <i>f</i>] [<code>-yborder</code> <i>f</i>] [<code>-ymax</code> <i>n</i>] [<code>-ysize</code> <i>n</i>] <i>psfile</i>[<i></i><code>.ps</code>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a PostScript file as input. Produces PBM, PGM, or PPM files as output. This program simply uses <code>GhostScript</code> to render a PostScript file with its PNM device drivers. If you don&#8217;t have <code>GhostScript</code> installed (invoked by a <code>gs</code> command), or the version you have installed was not built with the relevant PNM device drivers, <code>pstopnm</code> will fail. You can see if you have the proper environment by issuing the command <code>gs &#8211;help </code>. If it responds and lists under &quot;Available Devices&quot; <code>pbm</code>, <code>pbmraw</code>, <code>pgm</code>, <code>pgmraw</code>, <code>pnm</code>, <code>pnmraw</code>, <code>ppm</code>, or <code>ppmraw</code>, you&#8217;re in business. </p>
<p> <code>pstopnm</code> does not use the Netpbm libraries to generate the output files, so may not be entirely consistent with most Netpbm programs. </p>
<p> <i>psfile</i>[<i></i><code>.ps</code>] is the name of the input file. <code>.pstopnm</code> will add the <code>ps</code> to the end of the name you specify if no file exists by the exact name you specify, but one with added does. Use <code>&#8211;</code> to indicate Standard Input. </p>
<p> If you use the <code>-stdout </code> option, <code>pstopnm</code> outputs images of all the pages as a multi-image file to Standard Output. Otherwise, <code>pstopnm</code> creates one file for each page in the Postscript document. The files are named as follows: If the input file is named <code>psfile.ps</code>, the name of the files will be <code>psfile001.ppm</code>, <code>psfile002.ppm</code>, etc. The filetype suffix is <code>.ppm</code>, <code>.pgm</code>, or <code>.pbm</code>, depending on which kind of output you choose with your invocation options. If the input file name does not end in <code>.ps</code>, the whole file name is used in the output file name. For example, if the input file is named <code>psfile.old</code>, the output file name is <code>psfile.old001.ppm</code>, etc. </p>
<p> Note that the output file selection is inconsistent with most Netpbm programs, because it does not default to Standard Output. This is for historical reasons, based on the fact that the Netpbm formats did not always provide for a sequence of images in a single file. </p>
<p> Each output file contains the image of a rectangular part of the page to which it pertains. The selected area will always be centered in the output file, and may have borders around it. The image area to be extracted from the PostScript file and rendered into a portable anymap is defined by four numbers, the lower left corner and the upper right corner x and y coordinates. These coordinates are usually specified by the BoundingBox comment in the PostScript file header, but they can be overridden by the user by specifying one or more of the following options: <code>-llx</code>, <code>-lly</code>, <code>-urx</code>, and <code>-ury</code>. The presence and thickness of a border to be left around the image area is controlled by the use of the options <code>-xborder</code> and <code>-yborder</code>. If <code>pstopnm </code> does not find BoundingBox parameters in the input, and you don&#8217;t specify image area coordinates on the command line, <code>pstopnm</code> uses default values. If your input is from Standard Input, <code>pstopnm</code> does not use the BoundingBox parameters (due to the technical difficulty of extracting that information and still feeding the file to Ghostscript), so you either have to specify the image area coordinates or take the default. </p>
<p> Unless you specify both output file width and height, via the <code>-xsize </code> and <code>-ysize </code> options, <code>pstopnm </code> maps the document into the output image by preserving its aspect ratio. </p>
<p> It has been reported that on some Postscript Version 1 input, Ghostscript, and therefore <code>pstopnm</code>, produces no output. To solve this problem, you can convert the file to Postscript Version 3 with the program <code>ps2ps</code>. It is reported that the program <code>pstops</code> does not work. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-forceplain</code></p>
<dd> forces the output file to be in plain (text) format. Otherwise, it is in raw (binary) format. See <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1), etc.</p>
<dt><code>-llx </code><i>bx</i></p>
<dd> selects <i>bx</i> as the lower left corner x coordinate (in inches).</p>
<dt><code>-lly </code><i>by</i></p>
<dd> selects <i>by</i> as the lower left corner y coordinate (in inches).</p>
<dt><code>-landscape</code></p>
<dd> renders the image in landscape mode.</p>
<dt><code>-portrait</code></p>
<dd> renders the image in portrait mode.</p>
<dt><code>-nocrop</code></p>
<dd> does not crop the output image dimensions to match the PostScript image area dimensions.</p>
<dt><code>-pbm -pgm -ppm</code></p>
<dd> selects the format of the output file. By default, all files are rendered as portable pixmaps (ppm format).</p>
<dt><code>-stdout</code></p>
<dd> causes output to go to Standard Output instead of to regular files, one per page (see description of output files above). Use <code>pnmsplit</code> to extract individual pages from Standard Output.</p>
<dt><code>-urx </code><i>tx</i></p>
<dd> selects <i>tx</i> as the upper right corner x coordinate (in inches).</p>
<dt><code>-ury </code><i>ty</i></p>
<dd> selects <i>ty</i> as the upper right corner y coordinate (in inches).</p>
<dt><code>-verbose</code></p>
<dd> prints processing information to stdout.</p>
<dt><code>-xborder </code><i>frac</i></p>
<dd> specifies that the border width along the Y axis should be <i>frac</i> times the document width as specified by the bounding box comment in the PostScript file header. The default value is 0.1.</p>
<dt><code>-xmax </code><i>xs</i></p>
<dd> specifies that the maximum output image width should have a size less or equal to <i>xs</i> pixels (default: 612).</p>
<dt><code>-xsize </code><i>xsize</i></p>
<dd> specifies that the output image width must be exactly <i>xs</i> pixels.</p>
<dt><code>-yborder </code><i>frac</i></p>
<dd> specifies that the border width along the X axis should be <i>frac</i> times the document width as specified by the bounding box comment in the PostScript file header. The default value is 0.1.</p>
<dt><code>-ymax </code><i>ys</i></p>
<dd> specifies that the maximum output image height should have a size less or equal to <i>ys</i> pixels (default: 792).</p>
<dt><code>-ysize </code><i>ys</i></p>
<dd> specifies that the output image height must be exactly <i>ys</i> pixels. </p>
</dl>
<h2>BUGS</h2>
<p> The program will produce incorrect results with PostScript files that initialize the current transformation matrix. In these cases, page translation and rotation will not have any effect. To render these files, probably the best bet is to use the following options: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;pstopnm -xborder 0 -yborder 0 -portrait -nocrop file.ps </p>
<p> Additional options may be needed if the document is supposed to be rendered on a medium different from letter-size paper.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-pstofits/">pstofits</a></code>(1), <code><a href="/docs/linux/man/1-pnmtops/">pnmtops</a></code>(1), <code><a href="/docs/linux/man/1-psidtopgm/">psidtopgm</a></code>(1), <code><a href="/docs/linux/man/1-pbmtolps/">pbmtolps</a></code>(1), <code><a href="/docs/linux/man/1-pbmtoepsi/">pbmtoepsi</a></code>(1), <code><a href="/docs/linux/man/1-pnmsplit/">pnmsplit</a></code>(1) </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1992 Smithsonian Astrophysical Observatory<br />
 PostScript is a Trademark of Adobe Systems Incorporated.</p>
<h2>AUTHOR</h2>
<p> Alberto Accomazzi, WIPL, Center for Astrophysics. </p>
<h2>Index</h2>
