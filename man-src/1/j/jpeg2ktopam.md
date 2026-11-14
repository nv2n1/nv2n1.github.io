---
title: "jpeg2ktopam(1)"
name: "jpeg2ktopam"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpeg2ktopam/"
description: "jpeg2ktopam – convert JPEG-2000 code stream to PAM/PNM"
---

<h2 class="name">NAME</h2>
<p> jpeg2ktopam &#8211; convert JPEG-2000 code stream to PAM/PNM</p>
<h2>SYNOPSIS</h2>
<p> <code>jpeg2ktopam</code> [<code>-verbose</code>] [<code>-debuglevel=</code><i>number</i>] <i>filename</i> </p>
<h2>OPTION USAGE</h2>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>jpeg2ktopam</code> converts the named JPEG-2000 file (JP2 or JPC), or Standard Input if no file is named, to a PBM, PGM, PPM, or PAM file on Standard Output. </p>
<p> The JPEG-2000 specification specifies two different formats: JP2 and JPEG-2000 code stream (JPC). JP2 represents a visual image quite specifically, whereas JPC is a more or less arbitrary array of codes. A JP2 image contains a JPC stream and metadata describing how that stream represents a visual image. <code>jpeg2ktopam</code> converts both. </p>
<p> If the color space identified in the image is grayscale (JAS_IMAGE_CS_GRAY), <code>jpeg2ktopam</code> generates a PGM image, unless the image contains only one bit per pixel, in which case <code>jpeg2ktopam</code> generates PBM. If the color space is RGB (JAS_IMAGE_CS_RGB), <code>jpeg2ktopam</code> generates a PPM image. If the input image is anything else, <code>jpeg2ktopam</code> generates a PAM image with no tuple type identified. </p>
<p> In the PGM and PPM cases, <code>jpeg2ktopam</code> assumes the intensity values in the input image have the same meaning as for PGM and PPM. One thing that implies is the ITU-R Recommendation BT.709 color space, which means the assumption is false for JP2 input. JP2 input uses SRGB color encoding. So if you use <code>jpeg2ktopam</code> to convert a JP2 image to PPM, it changes the visual image (slightly) &#8212; the colors in the output are not the same as in the input. </p>
<p> In the PAM image, the output samples are numerically identical to the input samples. If the input samples are signed, they are represented in two&#8217;s complement form in the output (because PAM samples are always unsigned). The PAM plane numbers are identical to the JPC component numbers. </p>
<p> A JPEG-2000 image has a &quot;precision,&quot; which is the number of bits used for each code (in Netpbm lingo, &quot;sample&quot;). Actually, each component has a separate precision. The maxval of a PGM, PPM, or PAM output is the largest number you can represent in the JPEG-2000 precision of the JPEG-2000 component with the greatest precision. The samples in all components are scaled to that maxval. So if the red component has a precision of 4 bits and the green component has a precision of 6 bits, the maxval is 63 and the red component codes from the JPEG-2000 image are multiplied by 63/15 to generate the output samples. </p>
<p> <code>jpeg2ktopam</code> interprets the JPEG-2000 input with the Jasper JPEG-2000 library . See documentation of the library for details on what <code>jpeg2ktopam</code> handles. Note that the Jasper library contains facilities for writing PNM images, but <code>jpeg2ktopam</code> does not use those. It uses the Netpbm library instead. Note that the makers of the Jasper library write it &quot;JasPer,&quot; but Netpbm documentation follows standard American English typography rules, which don&#8217;t allow that kind of capitalization. </p>
<p> Use <code>pamtojpeg2k</code> to convert in the other direction. </p>
<p> The program <code>jasper</code>, which is packaged with the Jasper JPEG-2000 library, also converts between JPEG-2000 and PNM formats. Because it&#8217;s packaged with the library, it may exploit it better, especially recently added features. However, since it does not use the Netpbm library to read and write the Netpbm formats, it doesn&#8217;t do as good a job on that side. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> This option causes <code>jpeg2ktopam</code> to issue informational messages about the conversion process. </p>
<dt><code>-debuglevel</code>=<i>number</i></p>
<dd> This option controls debug messages from the Jasper library. <code>jpeg2ktopam</code> passes <i>number</i> as the debug level to the Jasper JPEG-2000 decoder. </p>
<p>&nbsp;<wbr>&nbsp;<wbr></dl>
<h2>EXAMPLES</h2>
<pre>
  jpeg2ktopam myimg.jpc &gt;myimg.ppm
</pre>
<h2>ABOUT JPEG-2000</h2>
<p> See <code>the</code><code>pamtojpeg2k</code><code><a href="/docs/linux/man/1-manual/">manual</a></code>(1) </p>
<p> for general information on JPEG-2000 compression and the JPEG-2000 formats. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtojpeg2k/">pamtojpeg2k</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtopeg/">pnmtopeg</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>History</h2>
<p> <code>jpeg2ktopam</code> was added to Netpbm in Release 10.12 (November 2002). </p>
<p> Before Netpbm 10.49 (December 2009), <code>jpeg2ktopam</code> could not convert a JP2 file &#8212; only JPC. </p>
<h2>Index</h2>
