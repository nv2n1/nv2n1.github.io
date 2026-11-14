---
title: "djpeg(1)"
name: "djpeg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djpeg/"
description: "djpeg – decompress a JPEG file to an image file"
---

<h2 class="name">NAME</h2>
<p> djpeg &#8211; decompress a JPEG file to an image file </p>
<h2>SYNOPSIS</h2>
<p> <code>djpeg</code> [ <i>options</i> ] [ <i>filename</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>djpeg</code> decompresses the named JPEG file, or the standard input if no file is named, and produces an image file on the standard output. PBMPLUS (PPM/PGM), BMP, GIF, Targa, or RLE (Utah Raster Toolkit) output format can be selected. (RLE is supported only if the URT library is available.)</p>
<h2>OPTIONS</h2>
<p> All switch names may be abbreviated; for example, <code>-grayscale</code> may be written <code>-gray</code> or <code>-gr</code>. Most of the &quot;basic&quot; switches can be abbreviated to as little as one letter. Upper and lower case are equivalent (thus <code>-BMP</code> is the same as <code>-bmp</code>). British spellings are also accepted (e.g., <code>-greyscale</code>), though for brevity these are not mentioned below. </p>
<p> The basic switches are:</p>
<dl>
<dt><code>-colors</code><i> N</i></p>
<dd> Reduce image to at most N colors. This reduces the number of colors used in the output image, so that it can be displayed on a colormapped display or stored in a colormapped file format. For example, if you have an 8-bit display, you&#8217;d need to reduce to 256 or fewer colors.</p>
<dt><code>-quantize</code><i> N</i></p>
<dd> Same as <code>-colors</code>. <code>-colors</code> is the recommended name, <code>-quantize</code> is provided only for backwards compatibility.</p>
<dt><code>-fast</code></p>
<dd> Select recommended processing options for fast, low quality output. (The default options are chosen for highest quality output.) Currently, this is equivalent to <code>-dct fast -nosmooth -onepass -dither ordered</code>.</p>
<dt><code>-grayscale</code></p>
<dd> Force grayscale output even if JPEG file is color. Useful for viewing on monochrome displays; also, <code>djpeg</code> runs noticeably faster in this mode.</p>
<dt><code>-rgb</code></p>
<dd> Force RGB output even if JPEG file is grayscale.</p>
<dt><code>-scale</code><i> M/N</i></p>
<dd> Scale the output image by a factor M/N. Currently the scale factor must be M/8, where M is an integer between 1 and 16 inclusive, or any reduced fraction thereof (such as 1/2, 3/4, etc.) Scaling is handy if the image is larger than your screen; also, <code>djpeg</code> runs much faster when scaling down the output.</p>
<dt><code>-bmp</code></p>
<dd> Select BMP output format (Windows flavor). 8-bit colormapped format is emitted if <code>-colors</code> or <code>-grayscale</code> is specified, or if the JPEG file is grayscale; otherwise, 24-bit full-color format is emitted.</p>
<dt><code>-gif</code></p>
<dd> Select GIF output format. Since GIF does not support more than 256 colors, <code>-colors 256</code> is assumed (unless you specify a smaller number of colors).</p>
<dt><code>-os2</code></p>
<dd> Select BMP output format (OS/2 1.x flavor). 8-bit colormapped format is emitted if <code>-colors</code> or <code>-grayscale</code> is specified, or if the JPEG file is grayscale; otherwise, 24-bit full-color format is emitted.</p>
<dt><code>-pnm</code></p>
<dd> Select PBMPLUS (PPM/PGM) output format (this is the default format). PGM is emitted if the JPEG file is grayscale or if <code>-grayscale</code> is specified; otherwise PPM is emitted.</p>
<dt><code>-rle</code></p>
<dd> Select RLE output format. (Requires URT library.)</p>
<dt><code>-targa</code></p>
<dd> Select Targa output format. Grayscale format is emitted if the JPEG file is grayscale or if <code>-grayscale</code> is specified; otherwise, colormapped format is emitted if <code>-colors</code> is specified; otherwise, 24-bit full-color format is emitted.</dl>
<p> Switches for advanced users:</p>
<dl>
<dt><code>-dct int</code></p>
<dd> Use integer DCT method (default).</p>
<dt><code>-dct fast</code></p>
<dd> Use fast integer DCT (less accurate). In libjpeg-turbo, the fast method is generally about 5-15% faster than the int method when using the x86/x86-64 SIMD extensions (results may vary with other SIMD implementations, or when using libjpeg-turbo without SIMD extensions.) If the JPEG image was compressed using a quality level of 85 or below, then there should be little or no perceptible difference between the two algorithms. When decompressing images that were compressed using quality levels above 85, however, the difference between the fast and int methods becomes more pronounced. With images compressed using quality=97, for instance, the fast method incurs generally about a 4-6 dB loss (in PSNR) relative to the int method, but this can be larger for some images. If you can avoid it, do not use the fast method when decompressing images that were compressed using quality levels above 97. The algorithm often degenerates for such images and can actually produce a more lossy output image than if the JPEG image had been compressed using lower quality levels.</p>
<dt><code>-dct float</code></p>
<dd> Use floating-point DCT method. The float method is mainly a legacy feature. It does not produce significantly more accurate results than the int method, and it is much slower. The float method may also give different results on different machines due to varying roundoff behavior, whereas the integer methods should give the same results on all machines.</p>
<dt><code>-dither fs</code></p>
<dd> Use Floyd-Steinberg dithering in color quantization.</p>
<dt><code>-dither ordered</code></p>
<dd> Use ordered dithering in color quantization.</p>
<dt><code>-dither none</code></p>
<dd> Do not use dithering in color quantization. By default, Floyd-Steinberg dithering is applied when quantizing colors; this is slow but usually produces the best results. Ordered dither is a compromise between speed and quality; no dithering is fast but usually looks awful. Note that these switches have no effect unless color quantization is being done. Ordered dither is only available in <code>-onepass</code> mode.</p>
<dt><code>-icc</code><i> file</i></p>
<dd> Extract ICC color management profile to the specified file.</p>
<dt><code>-map</code><i> file</i></p>
<dd> Quantize to the colors used in the specified image file. This is useful for producing multiple files with identical color maps, or for forcing a predefined set of colors to be used. The <i>file</i> must be a GIF or PPM file. This option overrides <code>-colors</code> and <code>-onepass</code>.</p>
<dt><code>-nosmooth</code></p>
<dd> Use a faster, lower-quality upsampling routine.</p>
<dt><code>-onepass</code></p>
<dd> Use one-pass instead of two-pass color quantization. The one-pass method is faster and needs less memory, but it produces a lower-quality image. <code>-onepass</code> is ignored unless you also say <code>-colors</code> <i>N</i>. Also, the one-pass method is always used for grayscale output (the two-pass method is no improvement then).</p>
<dt><code>-maxmemory</code><i> N</i></p>
<dd> Set limit for amount of memory to use in processing large images. Value is in thousands of bytes, or millions of bytes if &quot;M&quot; is attached to the number. For example, <code>-max 4m</code> selects 4000000 bytes. If more space is needed, an error will occur.</p>
<dt><code>-outfile</code><i> name</i></p>
<dd> Send output image to the named file, not to standard output.</p>
<dt><code>-memsrc</code></p>
<dd> Load input file into memory before decompressing. This feature was implemented mainly as a way of testing the in-memory source manager (jpeg_mem_src().)</p>
<dt><code>-skip</code><i> Y0,Y1</i></p>
<dd> Decompress all rows of the JPEG image except those between Y0 and Y1 (inclusive.) Note that if decompression scaling is being used, then Y0 and Y1 are relative to the scaled image dimensions.</p>
<dt><code>-crop</code><i> WxH+X+Y</i></p>
<dd> Decompress only a rectangular subregion of the image, starting at point X,Y with width W and height H. If necessary, X will be shifted left to the nearest iMCU boundary, and the width will be increased accordingly. Note that if decompression scaling is being used, then X, Y, W, and H are relative to the scaled image dimensions. Currently this option only works with the PBMPLUS (PPM/PGM), GIF, and Targa output formats.</p>
<dt><code>-verbose</code></p>
<dd> Enable debug printout. More <code>-v</code>&#8216;s give more output. Also, version information is printed at startup.</p>
<dt><code>-debug</code></p>
<dd> Same as <code>-verbose</code>.</p>
<dt><code>-version</code></p>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> This example decompresses the JPEG file foo.jpg, quantizes it to 256 colors, and saves the output in 8-bit BMP format in foo.bmp:</p>
<dl>
<dt>
<dd> <code>djpeg -colors 256 -bmp</code> <i>foo.jpg</i> <code>&gt;</code> <i>foo.bmp</i></dl>
<h2>HINTS</h2>
<p> To get a quick preview of an image, use the <code>-grayscale</code> and/or <code>-scale</code> switches. <code>-grayscale -scale 1/8</code> is the fastest case. </p>
<p> Several options are available that trade off image quality to gain speed. <code>-fast</code> turns on the recommended settings. </p>
<p> <code>-dct fast</code> and/or <code>-nosmooth</code> gain speed at a small sacrifice in quality. When producing a color-quantized image, <code>-onepass -dither ordered</code> is fast but much lower quality than the default behavior. <code>-dither none</code> may give acceptable results in two-pass mode, but is seldom tolerable in one-pass mode. </p>
<p> If you are fortunate enough to have very fast floating point hardware, <code>-dct float</code> may be even faster than <code>-dct fast</code>. But on most machines <code>-dct float</code> is slower than <code>-dct int</code>; in this case it is not worth using, because its theoretical accuracy advantage is too small to be significant in practice.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JPEGMEM</code></p>
<dd> If this environment variable is set, its value is the default memory limit. The value is specified as described for the <code>-maxmemory</code> switch. <code>JPEGMEM</code> overrides the default value specified when the program was compiled, and itself is overridden by an explicit <code>-maxmemory</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1)<br />
 <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5)<br />
 Wallace, Gregory K. &quot;The JPEG Still Picture Compression Standard&quot;, Communications of the ACM, April 1991 (vol. 34, no. 4), pp. 30-44.</p>
<h2>AUTHOR</h2>
<p> Independent JPEG Group </p>
<p> This file was modified by The libjpeg-turbo Project to include only information relevant to libjpeg-turbo, to wordsmith certain sections, and to describe features not present in libjpeg.</p>
<h2>ISSUES</h2>
<p> Support for compressed GIF output files was removed in djpeg v6b due to concerns over the Unisys LZW patent. Although this patent expired in 2006, djpeg still lacks compressed GIF support, for these historical reasons. (Conversion of JPEG files to GIF is usually a bad idea anyway, since GIF is a 256-color format.) The uncompressed GIF files that djpeg generates are larger than they should be, but they are readable by standard GIF decoders. </p>
<h2>Index</h2>
