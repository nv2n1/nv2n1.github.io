---
title: "tiffcp(1)"
name: "tiffcp"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffcp/"
description: "tiffcp – copy (and possibly convert) a TIFF file"
---

<h2>NAME</h2>
<p> tiffcp &#8211; copy (and possibly convert) a <font SIZE="-1">TIFF</font> file</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffcp</code> [ <i>options</i> ] <i>src1.tif &#8230; srcN.tif dst.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>tiffcp</i> combines one or more files created according to the Tag Image File Format, Revision 6.0 into a single <font SIZE="-1">TIFF</font> file. Because the output file may be compressed using a different algorithm than the input files, <i>tiffcp</i> is most often used to convert between different compression schemes. </p>
<p> By default, <i>tiffcp</i> will copy all the understood tags in a <font SIZE="-1">TIFF</font> directory of an input file to the associated directory in the output file. </p>
<p> <i>tiffcp</i> can be used to reorganize the storage characteristics of data in a file, but it is explicitly intended to not alter or convert the image data content in any way.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Append to an existing output file instead of overwriting it</p>
<dt><code>-b</code><i> image</i></p>
<dd> subtract the following monochrome image from all others processed. This can be used to remove a noise bias from a set of images. This bias image is typically an image of noise the camera saw with its shutter closed.</p>
<dt><code>-B</code></p>
<dd> Force output to be written with Big-Endian byte order. This option only has an effect when the output file is created or overwritten and not when it is appended to.</p>
<dt><code>-C</code></p>
<dd> Suppress the use of &#8220;strip chopping&#8221; when reading images that have a single strip/tile of uncompressed data.</p>
<dt><code>-c</code></p>
<dd> Specify the compression to use for data written to the output file: <code>none </code> for no compression, <code>packbits</code> for PackBits compression, <code>lzw</code> for Lempel-Ziv &amp; Welch compression, <code>zip</code> for Deflate compression, <code>lzma</code> for LZMA2 compression, <code>jpeg</code> for baseline JPEG compression, <code>g3</code> for CCITT Group 3 (T.4) compression, and <code>g4</code> for CCITT Group 4 (T.6) compression. By default <i>tiffcp</i> will compress data according to the value of the <i>Compression</i> tag found in the source file.</p>
<dt>
<dd> The <font SIZE="-1">CCITT</font> Group 3 and Group 4 compression algorithms can only be used with bilevel data.</p>
<dt>
<dd> Group 3 compression can be specified together with several T.4-specific options: <code>1d</code> for 1-dimensional encoding, <code>2d</code> for 2-dimensional encoding, and <code>fill</code> to force each encoded scanline to be zero-filled so that the terminating EOL code lies on a byte boundary. Group 3-specific options are specified by appending a &#8220;:&#8221;-separated list to the &#8220;g3&#8221; option; e.g. <code>-c g3:2d:fill</code> to get 2D-encoded data with byte-aligned EOL codes.</p>
<dt>
<dd> <font SIZE="-1">LZW, Deflate</font> and <font SIZE="-1">LZMA2</font> compression can be specified together with a <i>predictor</i> value. A predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. A value 3 is for floating point predictor which you can use if the encoded data are in floating point format. LZW-specific options are specified by appending a &#8220;:&#8221;-separated list to the &#8220;lzw&#8221; option; e.g. <code>-c lzw:2</code> for <font SIZE="-1">LZW</font> compression with horizontal differencing.</p>
<dt>
<dd> <font SIZE="-1">Deflate</font> and <font SIZE="-1">LZMA2</font> encoders support various compression levels (or encoder presets) set as character &#8220;p&#8221; and a preset number. &#8220;p1&#8221; is the fastest one with the worst compression ratio and &#8220;p9&#8221; is the slowest but with the best possible ratio; e.g. <code>-c zip:3:p9</code> for <font SIZE="-1">Deflate</font> encoding with maximum compression level and floating point predictor.</p>
<dt><code>-f</code></p>
<dd> Specify the bit fill order to use in writing output data. By default, <i>tiffcp</i> will create a new file with the same fill order as the original. Specifying <code>-f lsb2msb</code> will force data to be written with the FillOrder tag set to <font SIZE="-1">LSB2MSB,</font> while <code>-f msb2lsb</code> will force data to be written with the FillOrder tag set to <font SIZE="-1">MSB2LSB.</font></p>
<dt><code>-i</code></p>
<dd> Ignore non-fatal read errors and continue processing of the input file.</p>
<dt><code>-l</code></p>
<dd> Specify the length of a tile (in pixels). <i>tiffcp</i> attempts to set the tile dimensions so that no more than 8 kilobytes of data appear in a tile.</p>
<dt><code>-L</code></p>
<dd> Force output to be written with Little-Endian byte order. This option only has an effect when the output file is created or overwritten and not when it is appended to.</p>
<dt><code>-M</code></p>
<dd> Suppress the use of memory-mapped files when reading images.</p>
<dt><code>-o</code><i> offset</i></p>
<dd> Set initial directory offset</p>
<dt><code>-p</code></p>
<dd> Specify the planar configuration to use in writing image data that has one 8-bit sample per pixel. By default, <i>tiffcp</i> will create a new file with the same planar configuration as the original. Specifying <code>-p contig</code> will force data to be written with multi-sample data packed together, while <code>-p separate</code> will force samples to be written in separate planes.</p>
<dt><code>-r</code></p>
<dd> Specify the number of rows (scanlines) in each strip of data written to the output file. By default (or when value <code>0</code> is specified), <i>tiffcp</i> attempts to set the rows/strip that no more than 8 kilobytes of data appear in a strip. If you specify special value <code>-1</code> it will results in infinite number of the rows per strip. The entire image will be the one strip in that case.</p>
<dt><code>-s</code></p>
<dd> Force the output file to be written with data organized in strips (rather than tiles).</p>
<dt><code>-t</code></p>
<dd> Force the output file to be written with data organized in tiles (rather than strips). options can be used to force the resultant image to be written as strips or tiles of data, respectively.</p>
<dt><code>-w</code></p>
<dd> Specify the width of a tile (in pixels). <i>tiffcp</i> attempts to set the tile dimensions so that no more than 8 kilobytes of data appear in a tile. <i>tiffcp</i> attempts to set the tile dimensions so that no more than 8 kilobytes of data appear in a tile.</p>
<dt><code>-x</code></p>
<dd> Force the output file to be written with PAGENUMBER value in sequence.</p>
<dt><code>-8</code></p>
<dd> Write BigTIFF instead of classic TIFF format.</p>
<dt><code>-,=</code><i>character</i></p>
<dd> substitute <i>character</i> for `,&#8217; in parsing image directory indices in files. This is necessary if filenames contain commas. Note that <code>-,=</code> with whitespace immediately following will disable the special meaning of the `,&#8217; entirely. See examples.</dl>
<h2>EXAMPLES</h2>
<p> The following concatenates two files and writes the result using <font SIZE="-1">LZW</font> encoding:</p>
<dl>
<dt>
<dd>
<pre>
tiffcp -c lzw a.tif b.tif result.tif
</pre>
</dl>
<p> To convert a G3 1d-encoded <font SIZE="-1">TIFF</font> to a single strip of G4-encoded data the following might be used:</p>
<dl>
<dt>
<dd>
<pre>
tiffcp -c g4 -r 10000 g3.tif g4.tif
</pre>
</dl>
<p> (1000 is just a number that is larger than the number of rows in the source file.) </p>
<p> To extract a selected set of images from a multi-image TIFF file, the file name may be immediately followed by a `,&#8217; separated list of image directory indices. The first image is always in directory 0. Thus, to copy the 1st and 3rd images of image file &#8220;album.tif&#8221; to &#8220;result.tif&#8221;:</p>
<dl>
<dt>
<dd>
<pre>
tiffcp album.tif,0,2 result.tif
</pre>
</dl>
<p> A trailing comma denotes remaining images in sequence. The following command will copy all image with except the first one:</p>
<dl>
<dt>
<dd>
<pre>
tiffcp album.tif,1, result.tif
</pre>
</dl>
<p> Given file &#8220;CCD.tif&#8221; whose first image is a noise bias followed by images which include that bias, subtract the noise from all those images following it (while decompressing) with the command:</p>
<dl>
<dt>
<dd>
<pre>
tiffcp -c none -b CCD.tif CCD.tif,1, result.tif
</pre>
</dl>
<p> If the file above were named &#8220;CCD,X.tif&#8221;, the <code>-,=</code> option would be required to correctly parse this filename with image numbers, as follows:</p>
<dl>
<dt>
<dd>
<pre>
tiffcp -c none -,=% -b CCD,X.tif CCD,X%1%.tif result.tif
</dl>
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcmp/">tiffcmp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/1-tiffsplit/">tiffsplit</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
