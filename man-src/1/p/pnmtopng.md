---
title: "pnmtopng(1)"
name: "pnmtopng"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtopng/"
description: "pnmtopng – convert a portable anymap into a Portable Network Graphics file"
---

<h2 class="name">NAME</h2>
<p> pnmtopng &#8211; convert a portable anymap into a Portable Network Graphics file </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtopng</code> [-verbose] [-downscale] [-interlace] [-alpha file]<br />
 [-transparent [=]color] [-background color] [-gamma value]<br />
 [-hist] [-chroma wx wy rx ry gx gy bx by] [-phys x y unit]<br />
 [-text file] [-ztxt file] [-time [yy]yy-mm-dd hh:mm:ss]<br />
 [-filter type] [-compression level] [-force] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a Portable Network Graphics file as output. </p>
<p> Color values in PNG files are either eight or sixteen bits wide, so <i>pnmtopng</i> will automatically scale colors to have a maxval of 255 or 65535. Grayscale files will be produced with bit depths 1, 2, 4, 8 or 16. An extra <i>pnmdepth</i> step is not necessary.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display the format of the output file.</p>
<dt><code>-downscale</code></p>
<dd> Enables scaling of maxvalues of more then 65535 to 16 bit. Since this means loss of image data, the step is not performed by default.</p>
<dt><code>-interlace</code></p>
<dd> Creates an interlaced PNG file (Adam7).</p>
<dt><code>-alpha file</code></p>
<dd> The alpha channel of pixel (or image) specifies the transparency of a pixel. To create this fourth pixel value a separate <i>.pbm-</i> or <i>.pgm-file</i> is needed. In this file black (0) stands for fully transparant and white (1) will become opaque. The sizes of both pbm/pgm/ppm-files must be the same. If the information contained in the alpha mask can also be represented as a transparency index, it will be used, since this should result in a smaller image file.</p>
<dt><code>-transparent color</code></p>
<dd> <code>ppmtogif</code> marks the specified color as transparent in the PNG image. </p>
<p> You specify the color as in <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1).<code>E.g.</code> <code>red</code> or <code>rgb:ff/00/0d</code>. If the color you specify is not present in the image, <code>pnmtopnm</code> selects instead the color in the image that is closest to the one you specify. Closeness is measured as a cartesian distance between colors in RGB space. If multiple colors are equidistant, <code>pnmtopnm</code> chooses one of them arbitrarily. </p>
<p> However, if you prefix your color specification with &quot;=&quot;, e.g. </p>
<p> <code>-transparent =red</code> </p>
<p> Only the exact color you specify will be transparent. If that color does not appear in the image, there will be no transparency. <code>pnmtopng</code> issues an information message when this is the case. </p>
<dt><code>-background color</code></p>
<dd> To create a background color chunck in the <i>png-file,</i> which can be used for subsequent alpha-channel or transparent-color conversions. See -transparent for format of color.</p>
<dt><code>-gamma value</code></p>
<dd> Creates an gAMA chunk. By providing the gamma-value of the <i>pnm-file</i> the software that lateron will display the <i>png-file</i> will be able to do the necessary gamma-corrections. A good rule-of-thumb is that when the file is created by a software program (like a CAD-program or a ray-tracer) the value is probably 1.0. When the <i>pnm-file</i> looks good on a non-gamma corrected PC display (which has itself a gamma-value of 2.2 &#8211; 2.8), a value of 0.45 should be given.</p>
<dt><code>-hist</code></p>
<dd> Use this parameter to create a chunk that specifies the frequency (or histogram) of the colors in the image.</p>
<dt><code>-chroma white point X and Y, red X and Y, green X and Y, and blue X and Y</code></p>
<dd> To specify the white point and rgb values following the CIE-1931 spec.</p>
<dt><code>-phys x y unit</code></p>
<dd> When your image should not be displayed with square but with rectangular pixels this option should be used to create a pHYS chunk. When the unit-value is 0 the x and y only gives the ratio of pixel width and height. When it is 1 the x and y specify the number of pixels per meter.</p>
<dt><code>-text file</code></p>
<dd> Allows to include comments in the text-chunk of the <i>png-file.</i> The format of the text-file is as follows: when the first column does not contain a blank or a tab, the first word is considered to be the keyword. For keywords to contain spaces, enclose them in double-quotes.<br />
 When the first character on a line is a blank or tab, the rest of the line is a new line of the current comment. Note that the initial spaces are not considered to be part of the comment line. </p>
<p> Here is an example:<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
 Title PNG-file<br />
 Author your name<br />
 Description how to include a text-chunk<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;into a PNG file<br />
 &quot;Creation date&quot; 3-feb-1987<br />
 Software pnmtopng<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</p>
<dt><code>-ztxt file</code></p>
<dd> The same as -text, but now the text will be compressed.</p>
<dt><code>-time yy-mm-dd hh:mm:ss or -time yyyy-mm-dd hh:mm:ss</code></p>
<dd> This option allows you to specify the (modification)time. The year parameter can be given as a two- or a four-digit value.</p>
<dt><code>-filter type</code></p>
<dd> When the types of filters must be restricted you can specify here which filter you want to use. Allowed values are: 0 (none), 1 (sub), 2 (up), 3 (avg) and 4 (paeth).</p>
<dt><code>-compression level</code></p>
<dd> To explicitly set the compression level of zlib use this parameter. Select a level between 0 for no compression (max speed) and 9 for maximum compression.</p>
<dt><code>-force</code></p>
<dd> When set, -force limits the optimizations of pnmtopng. A png-file similar to the pnm-input is as much as possible enforced. For example no paletted files will be created and alpha-channel images will not be converted to images with a transparency chunck.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pngtopnm/">pngtopnm</a>(1), <a href="/docs/linux/man/1-gif2png/">gif2png</a>(1), <a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>NOTE</h2>
<p> Instead of xxxtopnm|pnmtopng, a specific converter should be used, if available. E.g. <i>gif2png</i> (GIF conversion), etc.</p>
<h2>BUGS</h2>
<p> There could be an option to read the comment text from pnm comments instead of a separate file. </p>
<p> The program could be much faster, with a bit of code optimizing.</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1995-1997 by Alexander Lehmann </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and Willem van Schaik. </p>
<h2>Index</h2>
