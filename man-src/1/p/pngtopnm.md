---
title: "pngtopnm(1)"
name: "pngtopnm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pngtopnm/"
description: "pngtopnm – convert a Portable Network Graphics file into portable anymap"
---

<h2 class="name">NAME</h2>
<p> pngtopnm &#8211; convert a Portable Network Graphics file into portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pngtopnm</code> [-verbose] [-alpha | -mix] [-background color]<br />
 [-gamma value] [-text file] [-time] [<i>pngfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Portable Network Graphics as input. Produces a portable anymap as output. The type of the output file depends on the input file &#8211; if it&#8217;s black &amp; white, a <i>pbm</i> file is written, else if it&#8217;s grayscale a <i>pgm</i> file, else a <i>ppm</i> file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display the format of the input file and the type of the output file. If the chunks are part of the <i>png-file,</i> the alpha, transparency and gamma-values will be indicated.</p>
<dt><code>-alpha</code></p>
<dd> Output the alpha channel or transparency mask of the image. The result is either a <i>pbm</i> file or <i>pgm</i> file, depending on whether different levels of transparency appear.</p>
<dt><code>-mix</code></p>
<dd> Compose the image with the transparency or alpha mask against a the background. When a background chunk is available that color is taken, else black will do.</p>
<dt><code>-background color</code></p>
<dd> If no background color chunck is present in the <i>png-file,</i> or when another color is required this parameter can be used to set the background color of images. This is especially useful for alpha-channel images or those with transparency chunks. The format, to specify the color in, is either (in the case of orange) &quot;1.0,0.5,0.0&quot;, where the values are floats between zero and one, or with the syntax &quot;#RGB&quot;, &quot;#RRGGBB&quot; or &quot;#RRRRGGGGBBBB&quot; where R, G and B are hexa-decimal numbers.</p>
<dt><code>-gamma value</code></p>
<dd> Converts the image to a new display-gamma value. When a gAMA chunk is present in the <i>png-file,</i> the image-gamma value will be used. When not, the image-gamma is considered to be 1.0. Based on the image-gamma and the display-gamma given with this option the colors written to the <i>pnm-file</i> will be adjusted.<br />
 Because the gamma&#8217;s of uncompensated monitors are around 2.6, which results in an image-gamma of 0.45, some typical situations are: when the image-gamma is 0.45 (use -verbose to check) and the picture is too light, your system is gamma-corrected, so convert with &quot;-gamma 1.0&quot;. When no gAMA chunk is present or the image-gamma is 1.0, use 2.2 to make the picture lighter and 0.45 to make the picture darker.</p>
<dt><code>-text file</code></p>
<dd> Writes the tEXt and zTXt chunks to a file, in a format as described in the <i>pnmtopng</i> man-page. These chunks contain text comments or annotations.</p>
<dt><code>-time</code></p>
<dd> Prints the tIME chunk to stderr.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a>(1), <a href="/docs/linux/man/1-ptot/">ptot</a>(1), <a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>NOTE</h2>
<p> Instead of pngtopnm|pnmtoxxx, a specific converter should be used, if available. E.g. <i>ptot</i> (PNG to TIFF conversion), etc.</p>
<h2>BUGS</h2>
<p> There could be an option to read the comment text from pnm comments instead of a separate file. </p>
<p> The program could be much faster, with a bit of code optimizing.</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1995-1997 by Alexander Lehmann </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and Willem van Schaik. </p>
<h2>Index</h2>
