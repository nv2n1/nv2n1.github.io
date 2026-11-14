---
title: "sldtoppm(1)"
name: "sldtoppm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sldtoppm/"
description: "sldtoppm – convert an AutoCAD slide file into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> sldtoppm &#8211; convert an AutoCAD slide file into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>sldtoppm</code> [<code>-adjust</code>] [<code>-dir</code>] [<code>-height</code>|<code>-ysize</code> <i>s</i>] [<code>-info</code>] [<code>-lib</code>|<code>-Lib</code> <i>name</i>] [<code>-scale</code> <i>s</i>] [<code>-verbose</code>] [<code>-width</code>|<code>-xsize</code> <i>s</i>] [<i>slidefile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads an AutoCAD&#174; slide file and outputs a portable pixmap. If no <i>slidefile</i> is specified, input is read from standard input. The ppmdraw library is used to convert the vector and polygon information in the slide file to a pixmap; see the file ppmdraw.h for details on this package.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-adjust</code></p>
<dd> If the display on which the slide file was created had non-square pixels, when the slide is processed with <code>sldtoppm</code> and the <code>-adjust</code> option is not present, the following warning will appear: Warning &#8211; pixels on source screen were non-square.<br />
 Specifying <code>-adjust</code> will correct image width to compensate. Specifying the <code>-adjust</code> option causes <code>sldtoppm</code> to scale the width of the image so that pixels in the resulting portable pixmap are square (and hence circles appear as true circles, not ellipses). The scaling is performed in the vector domain, before scan converting the objects. The results are, therefore, superior in appearance to what you&#8217;d obtain were you to perform the equivalent scaling with <code>pnmscale</code> after the bitmap had been created.</p>
<dt><code>-dir</code></p>
<dd> The input is assumed to be an AutoCAD slide library file. A directory listing each slide in the library is printed on standard error.</p>
<dt><code>-height</code><i> size</i></p>
<dd> Scales the image in the vector domain so it is <i>size</i> pixels in height. If no <code>-width</code> or <code>-xsize</code> option is specified, the width will be adjusted to preserve the pixel aspect ratio.</p>
<dt><code>-info</code></p>
<dd> Dump the slide file header on standard error, displaying the original screen size and aspect ratio among other information.</p>
<dt><code>-lib</code><i> name</i></p>
<dd> Extracts the slide with the given <i>name</i> from the slide library given as input. The specified <i>name</i> is converted to upper case.</p>
<dt><code>-Lib</code><i> name</i></p>
<dd> Extracts the slide with the given <i>name</i> from the slide library given as input. The <i>name</i> is used exactly as specified; it is not converted to upper case.</p>
<dt><code>-scale</code><i> s</i></p>
<dd> Scales the image by factor <i>s</i>, which may be any floating point value greater than zero. Scaling is done after aspect ratio adjustment, if any. Since scaling is performed in the vector domain, before rasterisation, the results look much better than running the output of <code>sldtoppm</code> through <code>pnmscale</code>.</p>
<dt><code>-verbose</code></p>
<dd> Dumps the slide file header and lists every vector and polygon in the file on standard error.</p>
<dt><code>-width</code><i> size</i></p>
<dd> Scales the image in the vector domain so it is <i>size</i> pixels wide. If no <code>-height</code> or <code>-ysize</code> option is specified, the height will be adjusted to preserve the pixel aspect ratio.</p>
<dt><code>-xsize</code><i> size</i></p>
<dd> Scales the image in the vector domain so it is <i>size</i> pixels wide. If no <code>-height</code> or <code>-ysize</code> option is specified, the height will be adjusted to preserve the pixel aspect ratio.</p>
<dt><code>-ysize</code><i> size</i></p>
<dd> Scales the image in the vector domain so it is <i>size</i> pixels in height. If no <code>-width</code> or <code>-xsize</code> option is specified, the width will be adjusted to preserve the pixel aspect ratio.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>BUGS</h2>
<p> Only Level 2 slides are converted. Level 1 format has been obsolete since the advent of AutoCAD Release 9 in 1987, and was not portable across machine architectures. </p>
<p> Slide library items with names containing 8 bit (such as ISO) or 16 bit (Kanji, for example) characters may not be found when chosen with the <code>-lib</code> option unless <code>sldtoppm</code> has been built with character set conversion functions appropriate to the locale. You can always retrieve slides from libraries regardless of the character set by using the <code>-Lib</code> option and specifying the precise name of library member. Use the <code>-dir</code> option to list the slides in a library if you&#8217;re unsure of the exact name.</p>
<h2>SEE ALSO</h2>
<p> AutoCAD Reference Manual: <i>Slide File Format</i>, <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)</p>
<h2>AUTHOR</h2>
<dl>
<dt>
<dd>
<pre>
John Walker
Autodesk SA
Avenue des Champs-Montants 14b
CH-2074 MARIN
Suisse/Schweiz/Svizzera/Svizra/Switzerland
<dl>
<dt>Usenet:<dd>kelvin [at] Autodesk.com
<dt>Fax:<dd>038/33 88 15
<dt>Voice:<dd>038/33 76 33
</pre>
</dl>
</dl>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. This software is provided &#8220;as is&#8221; without express or implied warranty. </p>
<p> AutoCAD and Autodesk are registered trademarks of Autodesk, Inc. </p>
<h2>Index</h2>
