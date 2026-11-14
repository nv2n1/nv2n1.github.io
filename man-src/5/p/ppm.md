---
title: "ppm(5)"
name: "ppm"
section: "5"
letter: "p"
url: "/docs/linux/man/5-ppm/"
description: "ppm – portable pixmap file format"
---

<p>ppm &#8211; portable pixmap file format</p>
<h2>Description</h2>
<p>The portable pixmap format is a lowest common denominator color image file format. It should be noted that this format is egregiously inefficient. It is highly redundant, while containing a lot of information that the human eye can&#8217;t even discern. Furthermore, the format allows very little information about the image besides basic color, which means you may have to couple a file in this format with other independent information to get any decent use out of it. However, it is very easy to write and analyze programs to process this format, and that is the point. It should also be noted that files often conform to this format in every respect except the precise semantics of the sample values. These files are useful because of the way PPM is used as an intermediary format. They are informally called PPM files, but to be absolutely precise, you should indicate the variation from true PPM. For example, &quot;PPM using the red, green, and blue colors that the scanner in question uses.&quot; The format definition is as follows. A PPM file consists of a sequence of one or more PPM images. There are no data, delimiters, or padding before, after, or between images. Each PPM image consists of the following:</p>
<dl>
<dt>&#8211;</p>
<dd>A &quot;magic number&quot; for identifying the file type. A ppm image&#8217;s magic number is the two characters &quot;P6&quot;.</p>
<dt>&#8211;</p>
<dd>Whitespace (blanks, TABs, CRs, LFs).</p>
<dt>&#8211;</p>
<dd>A width, formatted as ASCII characters in decimal.</p>
<dt>&#8211;</p>
<dd>Whitespace.</p>
<dt>&#8211;</p>
<dd>A height, again in ASCII decimal.</p>
<dt>&#8211;</p>
<dd>Whitespace.</p>
<dt>&#8211;</p>
<dd>The maximum color value (Maxval), again in ASCII decimal. Must be less than 65536.</p>
<dt>&#8211;</p>
<dd>Newline or other single whitespace character.</p>
<dt>&#8211;</p>
<dd>A raster of Width * Height pixels, proceeding through the image in normal English reading order. Each pixel is a triplet of red, green, and blue samples, in that order. Each sample is represented in pure binary by either 1 or 2 bytes. If the Maxval is less than 256, it is 1 byte. Otherwise, it is 2 bytes. The most significant byte is first.</p>
<dt>&#8211;</p>
<dd>In the raster, the sample values are &quot;nonlinear.&quot; They are proportional to the intensity of the CIE Rec. 709 red, green, and blue in the pixel, adjusted by the CIE Rec. 709 gamma transfer function. (That transfer function specifies a gamma number of 2.2 and has a linear section for small intensities). A value of Maxval for all three samples represents CIE D65 white and the most intense color in the color universe of which the image is part (the color universe is all the colors in all images to which this image might be compared).</p>
<dt>&#8211;</p>
<dd>Note that a common variation on the PPM format is to have the sample values be &quot;linear,&quot; i.e. as specified above except without the gamma adjustment. <code>pnmgamma</code> takes such a PPM variant as input and produces a true PPM as output.</p>
<dt>&#8211;</p>
<dd>Characters from a &quot;#&quot; to the next end-of-line, before the maxval line, are comments and are ignored.</dl>
<p> Note that you can use <code>pnmdepth</code> to convert between a the format with 1 byte per sample and the one with 2 bytes per sample. There is actually another version of the PPM format that is fairly rare: &quot;plain&quot; PPM format. The format above, which generally considered the normal one, is known as the &quot;raw&quot; PPM format. See <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) for some commentary on how plain and raw formats relate to one another. The difference in the plain format is:</p>
<dl>
<dt>&#8211;</p>
<dd>There is exactly one image in a file.</p>
<dt>&#8211;</p>
<dd>The magic number is P3 instead of P6.</p>
<dt>&#8211;</p>
<dd>Each sample in the raster is represented as an ASCII decimal number (of arbitrary size).</p>
<dt>&#8211;</p>
<dd>Each sample in the raster has white space before and after it. There must be at least one character of white space between any two samples, but there is no maximum. There is no particular separation of one pixel from another &#8212; just the required separation between the blue sample of one pixel from the red sample of the next pixel.</p>
<dt>&#8211;</p>
<dd>No line should be longer than 70 characters.</dl>
<p> Here is an example of a small pixmap in this format: </p>
<pre>P3
# feep.ppm
4 4
15
 0 0 0 0 0 0 0 0 0 15 0 15
 0 0 0 0 15 7 0 0 0 0 0 0
 0 0 0 0 0 0 0 15 7 0 0 0
15 0 15 0 0 0 0 0 0 0 0 0</pre>
<p>Programs that read this format should be as lenient as possible, accepting anything that looks remotely like a pixmap. </p>
<h2>Compatibility</h2>
<p>Before April 2000, a raw format PPM file could not have a maxval greater than 255. Hence, it could not have more than one byte per sample. Old programs may depend on this. </p>
<p> Before July 2000, there could be at most one image in a PPM file. As a result, most tools to process PPM files ignore (and don&#8217;t read) any data after the first image.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-giftopnm/">giftopnm</a>(1), <a href="/docs/linux/man/1-gouldtoppm/">gouldtoppm</a>(1), <a href="/docs/linux/man/1-ilbmtoppm/">ilbmtoppm</a>(1), <a href="/docs/linux/man/1-imgtoppm/">imgtoppm</a>(1), <a href="/docs/linux/man/1-mtvtoppm/">mtvtoppm</a>(1), <a href="/docs/linux/man/1-pcxtoppm/">pcxtoppm</a>(1), <a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a>(1), <a href="/docs/linux/man/1-pi1toppm/">pi1toppm</a>(1), <a href="/docs/linux/man/1-picttoppm/">picttoppm</a>(1), <a href="/docs/linux/man/1-pjtoppm/">pjtoppm</a>(1), <a href="/docs/linux/man/1-qrttoppm/">qrttoppm</a>(1), <a href="/docs/linux/man/1-rawtoppm/">rawtoppm</a>(1), <a href="/docs/linux/man/1-rgb3toppm/">rgb3toppm</a>(1), <a href="/docs/linux/man/1-sldtoppm/">sldtoppm</a>(1), <a href="/docs/linux/man/1-spctoppm/">spctoppm</a>(1), <a href="/docs/linux/man/1-sputoppm/">sputoppm</a>(1), <a href="/docs/linux/man/1-tgatoppm/">tgatoppm</a>(1), <a href="/docs/linux/man/1-ximtoppm/">ximtoppm</a>(1), <a href="/docs/linux/man/1-xpmtoppm/">xpmtoppm</a>(1), <a href="/docs/linux/man/1-yuvtoppm/">yuvtoppm</a>(1), <a href="/docs/linux/man/1-ppmtoacad/">ppmtoacad</a>(1), <a href="/docs/linux/man/1-ppmtogif/">ppmtogif</a>(1), <a href="/docs/linux/man/1-ppmtoicr/">ppmtoicr</a>(1), <a href="/docs/linux/man/1-ppmtoilbm/">ppmtoilbm</a>(1), <a href="/docs/linux/man/1-ppmtopcx/">ppmtopcx</a>(1), <a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a>(1), <a href="/docs/linux/man/1-ppmtopi1/">ppmtopi1</a>(1), <a href="/docs/linux/man/1-ppmtopict/">ppmtopict</a>(1), <a href="/docs/linux/man/1-ppmtopj/">ppmtopj</a>(1), <a href="/docs/linux/man/1-ppmtopuzz/">ppmtopuzz</a>(1), <a href="/docs/linux/man/1-ppmtorgb3/">ppmtorgb3</a>(1), <a href="/docs/linux/man/1-ppmtosixel/">ppmtosixel</a>(1), <a href="/docs/linux/man/1-ppmtotga/">ppmtotga</a>(1), <a href="/docs/linux/man/1-ppmtouil/">ppmtouil</a>(1), <a href="/docs/linux/man/1-ppmtoxpm/">ppmtoxpm</a>(1), <a href="/docs/linux/man/1-ppmtoyuv/">ppmtoyuv</a>(1), <a href="/docs/linux/man/1-ppmdither/">ppmdither</a>(1), <a href="/docs/linux/man/1-ppmforge/">ppmforge</a>(1), <a href="/docs/linux/man/1-ppmhist/">ppmhist</a>(1), <a href="/docs/linux/man/1-ppmmake/">ppmmake</a>(1), <a href="/docs/linux/man/1-ppmpat/">ppmpat</a>(1), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1), <a href="/docs/linux/man/1-ppmquantall/">ppmquantall</a>(1), <a href="/docs/linux/man/1-ppmrelief/">ppmrelief</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>Author</h2>
<p>Copyright (C) 1989, 1991 by Jef Poskanzer.</p>
