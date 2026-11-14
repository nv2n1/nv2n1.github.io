---
title: "tiff2ps(1)"
name: "tiff2ps"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiff2ps/"
description: "tiff2ps – convert a TIFF image to PostScript"
---

<h2>NAME</h2>
<p> tiff2ps &#8211; convert a <font SIZE="-1">TIFF</font> image to PostScript</p>
<h2>SYNOPSIS</h2>
<p> <code>tiff2ps</code> [ <i>options</i> ] <i>input.tif &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>tiff2ps</i> reads <font SIZE="-1">TIFF</font> images and writes PostScript or Encapsulated PostScript (EPS) on the standard output. By default, <i>tiff2ps</i> writes Encapsulated PostScript for the first image in the specified <font SIZE="-1">TIFF</font> image file. </p>
<p> By default, <i>tiff2ps</i> will generate PostScript that fills a printed area specified by the <font SIZE="-1">TIFF</font> tags in the input file. If the file does not contain <i>XResolution</i> or <i>YResolution</i> tags, then the printed area is set according to the image dimensions. The <code>-w</code> and <code>-h</code> options (see below) can be used to set the dimensions of the printed area in inches; overriding any relevant <font SIZE="-1">TIFF</font> tags. </p>
<p> The PostScript generated for <font SIZE="-1">RGB,</font> palette, and <font SIZE="-1">CMYK</font> images uses the <i>colorimage</i> operator. The PostScript generated for greyscale and bilevel images uses the <i>image</i> operator. When the <i>colorimage</i> operator is used, PostScript code to emulate this operator on older PostScript printers is also generated. Note that this emulation code can be very slow. </p>
<p> Color images with associated alpha data are composited over a white background.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> Generate PostScript Level 1 (the default).</p>
<dt><code>-2</code></p>
<dd> Generate PostScript Level 2.</p>
<dt><code>-3</code></p>
<dd> Generate PostScript Level 3. It basically allows one to use the /flateDecode filter for ZIP compressed TIFF images.</p>
<dt><code>-8</code></p>
<dd> Disable use of ASCII85 encoding with PostScript Level 2/3</p>
<dt><code>-a</code></p>
<dd> Generate output for all IFDs (pages) in the input file.</p>
<dt><code>-b</code></p>
<dd> Specify the bottom margin for the output (in inches). This does not affect the height of the printed image.</p>
<dt><code>-c</code></p>
<dd> Center the image in the output. This option only shows an effect if both the <code>-w</code> and the <code>-h</code> option are given.</p>
<dt><code>-d</code></p>
<dd> Set the initial <font SIZE="-1">TIFF</font> directory to the specified directory number. (NB: Directories are numbered starting at zero.) This option is useful for selecting individual pages in a multi-page (e.g. facsimile) file.</p>
<dt><code>-D</code></p>
<dd> Enable duplex printing (two pages per sheet of paper)</p>
<dt><code>-e</code></p>
<dd> Force the generation of Encapsulated PostScript (implies <code>-z</code>).</p>
<dt><code>-h</code></p>
<dd> Specify the vertical size of the printed area (in inches).</p>
<dt><code>-H</code></p>
<dd> Specify the maximum height of image (in inches). Images with larger sizes will be split in several pages. Option <code>-L</code> may be used for specifying size of split images overlapping.</p>
<dt><code>-W</code></p>
<dd> Specify the maximum width of image (in inches). Images with larger sizes will be split in several pages. Options <code>-L</code> and <code>-W</code> are mutually exclusive.</p>
<dt><code>-i</code></p>
<dd> Enable/disable pixel interpolation. This option requires a single numeric value: zero to disable pixel interpolation and non-zero to enable. The default is enabled.</p>
<dt><code>-L</code></p>
<dd> Specify the size of overlapping for split images (in inches). Used in conjunction with <code>-H</code> option and <code>-W</code> option.</p>
<dt><code>-l</code></p>
<dd> Specify the left margin for the output (in inches). This does not affect the width of the printed image.</p>
<dt><code>-m</code></p>
<dd> Where possible render using the <i>imagemask</i> PostScript operator instead of the <i>image</i> operator. When this option is specified <i>tiff2ps</i> will use <i>imagemask</i> for rendering 1 bit deep images. If this option is not specified or if the image depth is greater than 1 then the <i>image</i> operator is used.</p>
<dt><code>-o</code></p>
<dd> Set the initial <font SIZE="-1">TIFF</font> directory to the <font SIZE="-1">IFD</font> at the specified file offset. This option is useful for selecting thumbnail images and the like which are hidden using the <i>SubIFD</i> tag.</p>
<dt><code>-O</code></p>
<dd> Write PostScript to specified file instead of standard output Set the initial</p>
<dt><code>-p</code></p>
<dd> Force the generation of (non-Encapsulated) PostScript.</p>
<dt><code>-P</code></p>
<dd> Set optional PageOrientation DSC comment to Landscape or Portrait.</p>
<dt><code>-r 90|180|270|auto</code></p>
<dd> Rotate image by 90, 180, 270 degrees or auto. Auto picks the best fit for the image on the specified paper size (eg portrait or landscape) if -h or -w is specified. Rotation is in degrees counterclockwise. Auto rotates 90 degrees ccw to produce landscape.</p>
<dt><code>-s</code></p>
<dd> Generate output for a single IFD (page) in the input file.</p>
<dt><code>-t</code></p>
<dd> Specify the document title string</p>
<dt><code>-T</code></p>
<dd> Print pages for top edge binding</p>
<dt><code>-w</code></p>
<dd> Specify the horizontal size of the printed area (in inches).</p>
<dt><code>-x</code></p>
<dd> Override resolution units specified in the TIFF as centimeters.</p>
<dt><code>-y</code></p>
<dd> Override resolution units specified in the TIFF as inches.</p>
<dt><code>-z</code></p>
<dd> When generating PostScript Level 2, data is scaled so that it does not image into the <i>deadzone</i> on a page (the outer margin that the printing device is unable to mark). This option suppresses this behavior. When PostScript Level 1 is generated, data is imaged to the entire printed page and this option has no affect.</dl>
<h2>EXAMPLES</h2>
<p> The following generates PostScript Level 2 for all pages of a facsimile:</p>
<dl>
<dt>
<dd>
<pre>
tiff2ps -a2 fax.tif | lpr
</pre>
</dl>
<p> Note also that if you have version 2.6.1 or newer of Ghostscript then you can efficiently preview facsimile generated with the above command. </p>
<p> To generate Encapsulated PostScript for a the image at directory 2 of an image use:</p>
<dl>
<dt>
<dd>
<pre>
tiff2ps -d 1 foo.tif
</pre>
</dl>
<p> (Notice that directories are numbered starting at zero.) </p>
<p> If you have a long image, it may be split in several pages:</p>
<dl>
<dt>
<dd>
<pre>
tiff2ps -h11 -w8.5 -H14 -L.5 foo.tif &gt; foo.ps
</pre>
</dl>
<p> The page size is set to 8.5&#215;11 by <code>-w</code> and <code>-h</code> options. We will accept a small amount of vertical compression, so <code>-H</code> set to 14. Any pages between 11 and 14 inches will be fit onto one page. Pages longer than 14 inches are cut off at 11 and continued on the next page. The <code>-L.5</code> option says to repeat a half inch on the next page (to improve readability).</p>
<h2>BUGS</h2>
<p> Because PostScript does not support the notion of a colormap, 8-bit palette images produce 24-bit PostScript images. This conversion results in output that is six times bigger than the original image and which takes a long time to send to a printer over a serial line. Matters are even worse for 4-, 2-, and 1-bit palette images. </p>
<p> Does not handle tiled images when generating PostScript Level I output.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffgt/">tiffgt</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/1-tiff2bw/">tiff2bw</a></code>(1), <code><a href="/docs/linux/man/1-tiffsv/">tiffsv</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
