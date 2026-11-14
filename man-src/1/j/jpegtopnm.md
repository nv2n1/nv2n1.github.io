---
title: "jpegtopnm(1)"
name: "jpegtopnm"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpegtopnm/"
description: "jpegtopnm – convert JPEG/JFIF file to portable pixmap or graymap"
---

<h2 class="name">NAME</h2>
<p> jpegtopnm &#8211; convert JPEG/JFIF file to portable pixmap or graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>jpegtopnm</code> [<code>-dct</code> {<code>int</code>|<code>fast</code>|<code>float</code>}] [<code>-nosmooth</code>] [<code>-maxmemory</code> <i>N</i>] [{<code>-adobe</code>|<code>-notadobe</code>}] [<code>-comments</code>] [<code>-dumpexif</code>] [<code>-exif=</code><i>filespec</i>] [<code>-verbose</code>] [<code>-tracelevel</code> <i>N</i>] [ <i>filename</i> ] </p>
<p> All options may be abbreviated to their shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> <code>jpegtopnm</code> converts the named JFIF file, or the standard input if no file is named to a PPM or PGM image file on the standard output. If the JFIF file is of the grayscale variety, <code>jpegtopnm</code> generates a PGM (Portable Graymap) file. Otherwise, it generates a PPM (Portable Pixmap) file. </p>
<p> <code>jpegtopnm</code> uses the Independent JPEG Group&#8217;s JPEG library to interpret the input file. See <code><a rel="nofollow" href="http://www.ijg.org">http://www.ijg.org</a> </code> for information on the library. </p>
<p> &quot;JFIF&quot; is the correct name for the image format commonly known as &quot;JPEG.&quot; Strictly speaking, JPEG is a method of compression. The image format using JPEG compression that is by far the most common is JFIF. There is also a subformat of TIFF that uses JPEG compression. </p>
<p> EXIF is an image format that is a subformat of JFIF (to wit, a JFIF file that contains an EXIF header as an APP1 marker). <code>jpegtopnm</code> handles EXIF. </p>
<p> JFIF files can have either 8 bits per sample or 12 bits per sample. The 8 bit variety is by far the most common. There are two versions of the IJG JPEG library. One reads only 8 bit files and the other reads only 12 bit files. You must link the appropriate one of these libraries with <code>jpegtopnm</code>. Ordinarily, this means the library is in your shared library search path when you run <code>jpegtopnm</code>. </p>
<p> <code>jpegtopnm</code> generates output with either one byte or two bytes per sample depending on whether the JFIF input has either 8 bits or 12 bits per sample. You can use <code>pnmdepth</code> to reduce a two-byte-per-sample file to a one-byte-per-sample file if you need to. </p>
<p> If the JFIF file uses the CMYK or YCCK color space, the input does not actually contain enough information to know what color each pixel is. To know what color a pixel is, one would have to know the properties of the inks to which the color space refers. <code>jpegtopnm</code> interprets the colors using the common transformation which assumes all the inks are simply subtractive and linear. </p>
<h2>OPTIONS</h2>
<p> The options are only for advanced users:</p>
<dl>
<dt><code>-dct int</code></p>
<dd> Use integer DCT method (default).</p>
<dt><code>-dct fast</code></p>
<dd> Use fast integer DCT (less accurate).</p>
<dt><code>-dct float</code></p>
<dd> Use floating-point DCT method. The float method is very slightly more accurate than the int method, but is much slower unless your machine has very fast floating-point hardware. Also note that results of the floating-point method may vary slightly across machines, while the integer methods should give the same results everywhere. The fast integer method is much less accurate than the other two.</p>
<dt><code>-nosmooth</code></p>
<dd> Use a faster, lower-quality upsampling routine.</p>
<dt><code>-maxmemory</code><i> N</i></p>
<dd> Set limit on the amount of memory <code>jpegtopnm</code> uses in processing large images. Value is in thousands of bytes, or millions of bytes if &quot;M&quot; is suffixed to the number. For example, <code>-maxmemory 4m</code> selects 4000000 bytes. If <code>jpegtopnm</code> needs more space, it uses temporary files.</p>
<dt><code>-adobe</code></p>
<dd>
<dt><code>-notadobe</code></p>
<dd> There are two variations on the CMYK (and likewise YCCK) color space that may be used in the JFIF input. In the normal one, a zero value for a color components indicates absence of ink. In the other, a zero value means the maximum ink coverage. The latter is used by Adobe Photoshop when it creates a bare JFIF output file (but not when it creates JFIF output as part of Encapsulated Postscript output). </p>
<p> These options tell <code>jpegtopnm</code> which version of the CMYK or YCCK color space the image uses. If you specify neither, <code>jpegtopnm</code> tries to figure it out on its own. In the present version, it doesn&#8217;t try very hard at all: It just assumes the Photoshop version, since Photoshop and its emulators seem to be the main source of CMYK and YCCK images. But with experience of use, future versions might be more sophisticated. </p>
<p> If the JFIF image does not indicate that it is CMYK or YCCK, these options have no effect. </p>
<p> If you don&#8217;t use the right one of these options, the symptom is output that looks like a negative. </p>
<dt><code>-dumpexif</code></p>
<dd> Print the interpreted contents of any Exif header in the input file to the Standard Error file. Similar to the program <code>jhead</code> (not part of the Netpbm package).</p>
<dt><code>-exif=</code><i>filespec</i></p>
<dd> Extract the contents of the EXIF header from the input image and write it to the file <i>filespec</i>. <i>filespec </i> = <code>&#8211;</code> means write it to Standard Output. In this case, <code>jpegtopnm</code> does not output the converted image at all. </p>
<p> <code>jpegtopnm</code> writes the contents of the EXIF header byte-for-byte, starting with the two byte length field (which length includes those two bytes). </p>
<p> You can use this file as input to <code>ppmtojpeg</code> to insert an identical EXIF header into a new JFIF image. </p>
<p> If there is no EXIF header, <code>jpegtopnm</code> writes two bytes of binary zero and nothing else. </p>
<p> An EXIF header takes the form of a JFIF APP1 marker. Only the first such marker within the JFIF header counts. </p>
<dt><code>-comments</code></p>
<dd> Print any comments in the input file to the Standard Error file.</p>
<dt><code>-verbose</code></p>
<dd> Print details about the conversion to the Standard Error file.</p>
<dt><code>-tracelevel</code><i> n</i></p>
<dd> Turn on the JPEG library&#8217;s trace messages to the Standard Error file. A higher value of <i>n</i> gets more trace information. <code>-verbose</code> implies a trace level of at least 1. </p>
</dl>
<h2>EXAMPLES</h2>
<p> This example converts the color JFIF file foo.jpg to a PPM file named foo.ppm:</p>
<dl>
<dt>
<dd> <code>jpegtopnm foo.jpg &gt;foo.ppm</code> </p>
</dl>
<h2>HINTS</h2>
<p> You can use <code>ppmquant</code> to color quantize the result, i.e. to reduce the number of distinct colors in the image. In fact, you may have to if you want to convert the PPM file to certain other formats. <code>ppmdither</code> Does a more sophisticated quantization. </p>
<p> Use <code>pnmscale</code> to change the dimensions of the resulting image. </p>
<p> Use <code>ppmtopgm </code> to convert a color JFIF file to a grayscale PGM file. </p>
<p> You can easily use these converters together. E.g.:</p>
<dl>
<dt>
<dd> <code>jpegtopnm foo.jpg | ppmtopgm | pnmscale .25 </code><br />
 <code>&gt;foo.pgm</code></dl>
<p> <code>-dct fast</code> and/or <code>-nosmooth</code> gain speed at a small sacrifice in quality. </p>
<p> If you are fortunate enough to have very fast floating point hardware, <code>-dct float</code> may be even faster than <code>-dct fast</code>. But on most machines <code>-dct float</code> is slower than <code>-dct int</code>; in this case it is not worth using, because its theoretical accuracy advantage is too small to be significant in practice. </p>
<p> Another program, <code>djpeg</code>, is similar. <code>djpeg</code> is maintained by the Independent JPEG Group and packaged with the JPEG library which <code>jpegtopnm</code> uses for all its JPEG work. Because of that, you may expect it to exploit more current JPEG features. Also, since you have to have the library to run <code>jpegtopnm</code>, but not vice versa, <code>cjpeg</code> may be more commonly available. </p>
<p> On the other hand, <code>djpeg</code> does not use the NetPBM libraries to generate its output, as all the NetPBM tools such as <code>jpegtopnm</code> do. This means it is less likely to be consistent with all the other programs that deal with the NetPBM formats. Also, the command syntax of <code>jpegtopnm</code> is consistent with that of the other Netpbm tools, unlike <code>djpeg</code>. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JPEGMEM</code></p>
<dd> If this environment variable is set, its value is the default memory limit. The value is specified as described for the <code>-maxmemory</code> option. An explicit <code>-maxmemory </code> option overrides any <code>JPEGMEM</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/1-ppmtojpeg/">ppmtojpeg</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1), <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1), <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1),<br />
 <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1), <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-jhead/">jhead</a></code>(1)<br />
 Wallace, Gregory K. &quot;The JPEG Still Picture Compression Standard&quot;, Communications of the ACM, April 1991 (vol. 34, no. 4), pp. 30-44. </p>
<h2>LIMITATIONS</h2>
<p> Arithmetic coding is not supported for legal reasons. </p>
<p> The program could be much faster. </p>
<h2>AUTHOR</h2>
<p> <code>jpegtopnm</code> and this man page were derived in large part from <code>djpeg</code>, by the Independent JPEG Group. The program is otherwise by Bryan Henderson on March 19, 2000. </p>
<h2>Index</h2>
