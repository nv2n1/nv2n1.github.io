---
title: "raw2tiff(1)"
name: "raw2tiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-raw2tiff/"
description: "raw2tiff – create a TIFF file from a raw data"
---

<h2>NAME</h2>
<p> raw2tiff &#8211; create a <font SIZE="-1">TIFF</font> file from a raw data</p>
<h2>SYNOPSIS</h2>
<p> <code>raw2tiff</code> [ <i>options</i> ] <i>input.raw</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>raw2tiff</i> converts a raw byte sequence into <font SIZE="-1">TIFF.</font> By default, the <font SIZE="-1">TIFF</font> image is created with data samples packed (<i>PlanarConfiguration</i>=1), compressed with the PackBits algorithm (<i>Compression</i>=32773), and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code><i> number</i></p>
<dd> size of input image file header in bytes (0 by default). This amount of data just will be skipped from the start of file while reading.</p>
<dt><code>-w</code><i> number</i></p>
<dd> width of input image in pixels (can be guessed, see <font SIZE="-1"><code>GUESSING THE IMAGE GEOMETRY</code> </font> below).</p>
<dt><code>-l</code><i> number</i></p>
<dd> length of input image in lines (can be guessed, see <font SIZE="-1"><code>GUESSING THE IMAGE GEOMETRY</code> </font> below).</p>
<dt><code>-b</code><i> number</i></p>
<dd> number of bands in input image (1 by default).</p>
<dt><code>-d</code><i> data_type</i></p>
<dd> type of samples in input image, where <i>data_type</i> may be:<br />
 <code>byte </code> 8-bit unsigned integer (default),<br />
 <code>short </code> 16-bit unsigned integer,<br />
 <code>long </code> 32-bit unsigned integer,<br />
 <code>sbyte </code> 8-bit signed integer,<br />
 <code>sshort </code> 16-bit signed integer,<br />
 <code>slong </code> 32-bit signed integer,<br />
 <code>float </code> 32-bit IEEE floating point,<br />
 <code>double </code> 64-bit IEEE floating point.</p>
<dt><code>-i</code><i> config</i></p>
<dd> type of samples interleaving in input image, where <i>config</i> may be:<br />
 <code>pixel </code> pixel interleaved data (default),<br />
 <code>band </code> band interleaved data.</p>
<dt><code>-p</code><i> photo</i></p>
<dd> photometric interpretation (color space) of the input image, where <i>photo</i> may be:<br />
 <code>miniswhite </code> white color represented with 0 value,<br />
 <code>minisblack </code> black color represented with 0 value (default),<br />
 <code>rgb </code> image has RGB color model,<br />
 <code>cmyk </code> image has CMYK (separated) color model,<br />
 <code>ycbcr </code> image has YCbCr color model,<br />
 <code>cielab </code> image has CIE L*a*b color model,<br />
 <code>icclab </code> image has ICC L*a*b color model,<br />
 <code>itulab </code> image has ITU L*a*b color model.</p>
<dt><code>-s</code></p>
<dd> swap bytes fetched from the input file.</p>
<dt><code>-L</code></p>
<dd> input data has LSB2MSB bit order (default).</p>
<dt><code>-M</code></p>
<dd> input data has MSB2LSB bit order.</p>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression, <code>-c packbits</code> for the PackBits compression algorithm (the default), <code>-c jpeg</code> for the baseline JPEG compression algorithm, <code>-c zip</code> for the Deflate compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch.</p>
<dt><code>-r</code><i> number</i></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</dl>
<h2>GUESSING THE IMAGE GEOMETRY</h2>
<p> <i>raw2tiff</i> can guess image width and height in case one or both of these parameters are not specified. If you omit one of those parameters, the complementary one will be calculated based on the file size (taking into account header size, number of bands and data type). If you omit both parameters, the statistical approach will be used. Utility will compute correlation coefficient between two lines at the image center using several appropriate line sizes and the highest absolute value of the coefficient will indicate the right line size. That is why you should be cautious with the very large images, because guessing process may take a while (depending on your system performance). Of course, the utility can&#8217;t guess the header size, number of bands and data type, so it should be specified manually. If you don&#8217;t know anything about your image, just try with the several combinations of those options. </p>
<p> There is no magic, it is just a mathematical statistics, so it can be wrong in some cases. But for most ordinary images guessing method will work fine.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
