---
title: "pngtopam(1)"
name: "pngtopam"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pngtopam/"
description: "pngtopam – convert a PNG image into a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> pngtopam &#8211; convert a PNG image into a Netpbm image</p>
<h2>SYNOPSIS</h2>
<p> <code>pngtopam</code> [<code>-verbose</code>] [<code>-alphapam</code> | <code>-alpha</code> | <code>-mix</code>] [<code>-background</code>=<i>color</i>] [<code>-gamma</code>=<i>value</i>] [<code>-text</code>=<i>filename</i>] [<code>-time</code>] [<code>-byrow</code>] [<i>pngfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pngtopam</code> reads a PNG image (Portable Network Graphics) as input and produces a Netpbm image as output. The type of the output file depends on the input file &#8211; if it&#8217;s black &amp; white, <code>pngtopam</code> creates a PBM file. If it&#8217;s grayscale, <code>pngtopam</code> creates a PGM file. Otherwise, it creates a PPM file. Except that with the <code>-alphapam</code> option, it always creates a PAM file. That file has tuple type GRAYSCALE_ALPHA or RGB_ALPHA depending on whether the input has color or not. </p>
<p> To convert in the other direction, use <code>pnmtopng</code> or <code>pamrgbatopng</code>. The former is more powerful in almost every way, except that only the latter can recognize transparency information in a PAM file, as you might generate with <code>pngtopam -alphapam</code>. To use <code>pnmtopng</code> with a PAM file with transparency, you can separate out the transparency channel with <code>pamchannel</code> and feed it to <code>pnmtopng</code> separately. But you may want to use <code>pngtopam -alpha</code> instead of <code>pngtopam -alphapam</code> if you&#8217;re going to be converting back. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display various information about the input PNG image and the conversion process. </p>
<p> If you want even more information about the PNG image, use <code>pngcheck</code> (not part of Netpbm).<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-alphapam</code></p>
<dd> Produce a single output image containing the main image (foreground) and the alpha channel or transparency mask. This image is in the PAM format with tuple type of either GRAYSCALE_ALPHA (which has a depth of 2 channels) or RGB_ALPHA (which has a depth of 4 channels). </p>
<p> You can specify only one of <code>-alphapam</code>, <code>-alpha</code>, and <code>-mix</code>. With none of them, <code>pngtopam</code> produces an image of the foreground of the input image and discards transparency information. </p>
<p> Note that converting in the other direction, the <code>pamtopng</code> converter won&#8217;t recognize the transparency information you generate with <code>-alphapam</code>, but <code>pamrgbatopng</code> will. </p>
<p> This option was new in Netpbm 10.44 (September 2008). </p>
<dt><code>-alpha</code></p>
<dd> Output the alpha channel or transparency mask of the image. The result is either a PBM file or a PGM file, depending on whether different levels of transparency appear. </p>
<p> <code>pngtopam</code> discards the main image (the foreground). </p>
<p> You can specify only one of <code>-alphapam</code>, <code>-alpha</code>, and <code>-mix</code>. With none of them, <code>pngtopam</code> produces an image of the foreground of the input image and discards transparency information. </p>
<dt><code>-mix</code></p>
<dd> Compose the image with the transparency or alpha mask against a background. The background color is determined by the bKGD chunk in the PNG, except that you can override it with <code>-background</code>. If the PNG has no bKGD chunk and you don&#8217;t specify <code>-background</code>, the background color is white. </p>
<p> You can specify only one of <code>-alphapam</code>, <code>-alpha</code>, and <code>-mix</code>. With none of them, <code>pngtopam</code> produces an image of the foreground of the input image and discards transparency information. </p>
<dt><code>-background=</code><i>color</i></p>
<dd> This option specifies the background color with which to mix the image when you specify <code>-mix</code>. </p>
<p> <i>color</i> is as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<p> Examples: </p>
<dt>&bull;</p>
<dd> <tt>-background=rgb:01/ff/80</tt></p>
<dt>&bull;</p>
<dd> <tt>-background=rgbi:1/255/128</tt> </p>
<p> If you don&#8217;t specify <code>-background</code>, the background color is what is specified in the PNG image, and if the PNG doesn&#8217;t specify anything, white. </p>
<p> You cannot specify <code>-background</code> unless you also specify <code>-mix</code>. Before Netpbm 10.27 (March 2005), you could specify <code>-background</code> without <code>-mix</code> and it was just ignored. (This caused a usability problem). </p>
<dt><code>-gamma=</code><i>value</i></p>
<dd> Converts the image to a new display-gamma value. If a gAMA chunk is present in the <i>png-file</i>, <code>pngtopam</code> uses the specified image-gamma value. If not, <code>pngtopam</code> considers the image-gamma to be 1.0. Based on the image-gamma and the display-gamma given with this option, <code>pngtopam</code> adjusts the colors written to the <i>pnm-file</i>. </p>
<p> Because the gammas of uncompensated monitors are around 2.6, which results in an image-gamma of 0.45, some typical situations are: when the image-gamma is 0.45 (use -verbose to check) and the picture is too light, your system is gamma-corrected, so convert with &#8216;-gamma 1.0&#8217;. When no gAMA chunk is present or the image-gamma is 1.0, use 2.2 to make the picture lighter and 0.45 to make the picture darker. </p>
<p> One oddity to be aware of when using <code>-gamma</code> on an image with transparency: The PNG image specifies that a certain color is transparent, i.e. every pixel in the image of that color is transparent. But <code>pngtopam</code> interprets this as applying to the gamma-corrected space, and there may be less precision in that space than in the original, which means multiple uncorrected colors map to the same corrected color. So imagine that the image contains 3 shades of white and specifies that one of them is transparent. After gamma correction, those three shades are indistinguishable, so <code>pngtopam</code> considers pixels of all three shades to be transparent. </p>
<p> If this is not what you want, don&#8217;t use <code>gamma</code>. Instead, use <code>pnmgamma</code> on the output. </p>
<dt><code>-text=</code><i>file</i></p>
<dd> Writes the tEXt and zTXt chunks to a file, in a format as described in the <code>pnmtopng</code> user manual. These chunks contain text comments or annotations. </p>
<dt><code>-time</code></p>
<dd> Prints the tIME chunk to stderr. </p>
<dt><code>-byrow</code></p>
<dd> This option can make <code>pngtopam</code> run faster or in environments where it would otherwise fail. </p>
<p> <code>pngtopam</code> has two ways to do the conversion from PNG to PAM, using respectively two facilities of the PNG library: </p>
<dt>Whole Image</p>
<dd> Decode the entire image into memory at once, using <code>png_read_image()</code>, then convert to PAM and output row by row. </p>
<dt>Row By Row</p>
<dd> Read, convert, and output one row at a time using <code>png_read_row()</code>. </p>
<p> Whole Image is generally preferable because the PNG library does more of the work, which means it understands more of the PNG format possibilities now and in the future. Also, if the PNG is interlaced, <code>pngtopam</code> does not know how to assemble the rows in the right order. </p>
<p> Row By Row uses far less memory, which means with large images, it can run in environments where Whole Image cannot and may also run faster. And because Netpbm code does more of the work, it&#8217;s possible that it can be more flexible or at least give better diagnostic information if there&#8217;s something wrong with the PNG. </p>
<p> The Netpbm native code may do something correctly that the PNG library does incorrectly, or vice versa. </p>
<p> In Netpbm, we stress function over performance, so by default <code>pngtopam</code> uses Whole Image. You can select Row By Row with <code>-byrow</code> if you want the speed or resource requirement improvement. </p>
<p> <code>-byrow</code> was new in Netpbm 10.54 (March 2010). </p>
<dt><code>-orientraw</code></p>
<dd> A TIFF stream contains raster data which can be arranged in the stream various ways. Most commonly, it is arranged by rows, with the top row first, and the pixels left to right within each row, but many other orientations are possible. </p>
<p> The common orientation is the same on the Netpbm formats use, so <code>tifftopnm</code> can do its jobs quite efficiently when the TIFF raster is oriented that way. </p>
<p> But if the TIFF raster is oriented any other way, it can take a considerable amount of processing for <code>tifftopnm</code> to convert it to Netpbm format. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1) , <code>ptot</code>, <code><a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<p> For information on the PNG format, see <a rel="nofollow" href="http://schaik.com/png">http://schaik.com/png</a> . </p>
<h2>NOTE</h2>
<p> A PNG image contains a lot of information that can&#8217;t be represented in Netpbm formats. Therefore, you lose information when you convert to another format with &quot;pngtopam | pnmtoxxx&quot;. If there is a specialized converter that converts directly to the other format, e.g. <code>ptot</code> to convert from PNG to TIFF, you&#8217;ll get better results using that. </p>
<h2>LIMITATIONS</h2>
<p> There could be an option to include PNG comment chunks in the output image as PNM comments instead of putting them in a separate file. </p>
<p> The program could be much faster, with a bit of code optimizing. As with any Netpbm program, speed always takes a back seat to quick present and future development. </p>
<h2>HISTORY</h2>
<p> <code>pngtopam</code> was new in Netpbm 10.44, as a replacement for <code>pngtopnm</code>. The main improvement over <code>pngtopnm</code> was that it could generate a PAM image with a transparency channel, whereas with <code>pngtopnm</code>, you would have to extract the transparency channel as a separate file, in a separate run. </p>
<p> <code>pngtopnm</code> was new in Netpbm 8.1 (March 2000), the first big change to the package in Netpbm&#8217;s renaissance. It and <code>pnmtopng</code> were simply copied from the <code>pnmtopng</code> package (1)<br />
&nbsp;<wbr>by Greg Roelofs.&nbsp;<wbr>&nbsp;<wbr>Those were based on simpler reference applications by Alexander Lehmann &lt;alex [at] hal.rhein-main.de&gt; and Willem van Schaik &lt;willem [at] schaik.com&gt; and distributed with their PNG library. </p>
<p> Nearly all of the code has changed since it was copied from the <code>pnmtopng</code> package, most of it just to improve maintainability. </p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1995-1997 by Alexander Lehmann and Willem van Schaik. </p>
<h2>Index</h2>
