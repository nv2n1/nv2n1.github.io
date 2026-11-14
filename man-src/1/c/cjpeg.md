---
title: "cjpeg(1)"
name: "cjpeg"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cjpeg/"
description: "cjpeg – compress an image file to a JPEG file"
---

<h2 class="name">NAME</h2>
<p> cjpeg &#8211; compress an image file to a JPEG file </p>
<h2>SYNOPSIS</h2>
<p> <code>cjpeg</code> [ <i>options</i> ] [ <i>filename</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>cjpeg</code> compresses the named image file, or the standard input if no file is named, and produces a JPEG/JFIF file on the standard output. The currently supported input file formats are: PPM (PBMPLUS color format), PGM (PBMPLUS grayscale format), BMP, Targa, and RLE (Utah Raster Toolkit format). (RLE is supported only if the URT library is available.)</p>
<h2>OPTIONS</h2>
<p> All switch names may be abbreviated; for example, <code>-grayscale</code> may be written <code>-gray</code> or <code>-gr</code>. Most of the &quot;basic&quot; switches can be abbreviated to as little as one letter. Upper and lower case are equivalent (thus <code>-BMP</code> is the same as <code>-bmp</code>). British spellings are also accepted (e.g., <code>-greyscale</code>), though for brevity these are not mentioned below. </p>
<p> The basic switches are:</p>
<dl>
<dt><code>-quality</code><i> N[,&#8230;]</i></p>
<dd> Scale quantization tables to adjust image quality. Quality is 0 (worst) to 100 (best); default is 75. (See below for more info.)</p>
<dt><code>-grayscale</code></p>
<dd> Create monochrome JPEG file from color input. Be sure to use this switch when compressing a grayscale BMP file, because <code>cjpeg</code> isn&#8217;t bright enough to notice whether a BMP file uses only shades of gray. By saying <code>-grayscale,</code> you&#8217;ll get a smaller JPEG file that takes less time to process.</p>
<dt><code>-rgb</code></p>
<dd> Create RGB JPEG file. Using this switch suppresses the conversion from RGB colorspace input to the default YCbCr JPEG colorspace.</p>
<dt><code>-optimize</code></p>
<dd> Perform optimization of entropy encoding parameters. Without this, default encoding parameters are used. <code>-optimize</code> usually makes the JPEG file a little smaller, but <code>cjpeg</code> runs somewhat slower and needs much more memory. Image quality and speed of decompression are unaffected by <code>-optimize</code>.</p>
<dt><code>-progressive</code></p>
<dd> Create progressive JPEG file (see below).</p>
<dt><code>-targa</code></p>
<dd> Input file is Targa format. Targa files that contain an &quot;identification&quot; field will not be automatically recognized by <code>cjpeg</code>; for such files you must specify <code>-targa</code> to make <code>cjpeg</code> treat the input as Targa format. For most Targa files, you won&#8217;t need this switch.</dl>
<p> The <code>-quality</code> switch lets you trade off compressed file size against quality of the reconstructed image: the higher the quality setting, the larger the JPEG file, and the closer the output image will be to the original input. Normally you want to use the lowest quality setting (smallest file) that decompresses into something visually indistinguishable from the original image. For this purpose the quality setting should generally be between 50 and 95 (the default is 75) for photographic images. If you see defects at <code>-quality</code> 75, then go up 5 or 10 counts at a time until you are happy with the output image. (The optimal setting will vary from one image to another.) </p>
<p> <code>-quality</code> 100 will generate a quantization table of all 1&#8217;s, minimizing loss in the quantization step (but there is still information loss in subsampling, as well as roundoff error.) For most images, specifying a quality value above about 95 will increase the size of the compressed file dramatically, and while the quality gain from these higher quality values is measurable (using metrics such as PSNR or SSIM), it is rarely perceivable by human vision. </p>
<p> In the other direction, quality values below 50 will produce very small files of low image quality. Settings around 5 to 10 might be useful in preparing an index of a large image library, for example. Try <code>-quality</code> 2 (or so) for some amusing Cubist effects. (Note: quality values below about 25 generate 2-byte quantization tables, which are considered optional in the JPEG standard. <code>cjpeg</code> emits a warning message when you give such a quality value, because some other JPEG programs may be unable to decode the resulting file. Use <code>-baseline</code> if you need to ensure compatibility at low quality values.) </p>
<p> The <code>-quality</code> option has been extended in this version of <code>cjpeg</code> to support separate quality settings for luminance and chrominance (or, in general, separate settings for every quantization table slot.) The principle is the same as chrominance subsampling: since the human eye is more sensitive to spatial changes in brightness than spatial changes in color, the chrominance components can be quantized more than the luminance components without incurring any visible image quality loss. However, unlike subsampling, this feature reduces data in the frequency domain instead of the spatial domain, which allows for more fine-grained control. This option is useful in quality-sensitive applications, for which the artifacts generated by subsampling may be unacceptable. </p>
<p> The <code>-quality</code> option accepts a comma-separated list of parameters, which respectively refer to the quality levels that should be assigned to the quantization table slots. If there are more q-table slots than parameters, then the last parameter is replicated. Thus, if only one quality parameter is given, this is used for both luminance and chrominance (slots 0 and 1, respectively), preserving the legacy behavior of cjpeg v6b and prior. More (or customized) quantization tables can be set with the <code>-qtables</code> option and assigned to components with the <code>-qslots</code> option (see the &quot;wizard&quot; switches below.) </p>
<p> JPEG files generated with separate luminance and chrominance quality are fully compliant with standard JPEG decoders. </p>
<p> <code>CAUTION:</code> For this setting to be useful, be sure to pass an argument of <code>-sample 1&#215;1</code> to <code>cjpeg</code> to disable chrominance subsampling. Otherwise, the default subsampling level (2&#215;2, AKA &quot;4:2:0&quot;) will be used. </p>
<p> The <code>-progressive</code> switch creates a &quot;progressive JPEG&quot; file. In this type of JPEG file, the data is stored in multiple scans of increasing quality. If the file is being transmitted over a slow communications link, the decoder can use the first scan to display a low-quality image very quickly, and can then improve the display with each subsequent scan. The final image is exactly equivalent to a standard JPEG file of the same quality setting, and the total file size is about the same &#8212; often a little smaller. </p>
<p> Switches for advanced users:</p>
<dl>
<dt><code>-arithmetic</code></p>
<dd> Use arithmetic coding. <code>Caution:</code> arithmetic coded JPEG is not yet widely implemented, so many decoders will be unable to view an arithmetic coded JPEG file at all.</p>
<dt><code>-dct int</code></p>
<dd> Use integer DCT method (default).</p>
<dt><code>-dct fast</code></p>
<dd> Use fast integer DCT (less accurate). In libjpeg-turbo, the fast method is generally about 5-15% faster than the int method when using the x86/x86-64 SIMD extensions (results may vary with other SIMD implementations, or when using libjpeg-turbo without SIMD extensions.) For quality levels of 90 and below, there should be little or no perceptible difference between the two algorithms. For quality levels above 90, however, the difference between the fast and the int methods becomes more pronounced. With quality=97, for instance, the fast method incurs generally about a 1-3 dB loss (in PSNR) relative to the int method, but this can be larger for some images. Do not use the fast method with quality levels above 97. The algorithm often degenerates at quality=98 and above and can actually produce a more lossy image than if lower quality levels had been used. Also, in libjpeg-turbo, the fast method is not fully accelerated for quality levels above 97, so it will be slower than the int method.</p>
<dt><code>-dct float</code></p>
<dd> Use floating-point DCT method. The float method is mainly a legacy feature. It does not produce significantly more accurate results than the int method, and it is much slower. The float method may also give different results on different machines due to varying roundoff behavior, whereas the integer methods should give the same results on all machines.</p>
<dt><code>-icc</code><i> file</i></p>
<dd> Embed ICC color management profile contained in the specified file.</p>
<dt><code>-restart</code><i> N</i></p>
<dd> Emit a JPEG restart marker every N MCU rows, or every N MCU blocks if &quot;B&quot; is attached to the number. <code>-restart 0</code> (the default) means no restart markers.</p>
<dt><code>-smooth</code><i> N</i></p>
<dd> Smooth the input image to eliminate dithering noise. N, ranging from 1 to 100, indicates the strength of smoothing. 0 (the default) means no smoothing.</p>
<dt><code>-maxmemory</code><i> N</i></p>
<dd> Set limit for amount of memory to use in processing large images. Value is in thousands of bytes, or millions of bytes if &quot;M&quot; is attached to the number. For example, <code>-max 4m</code> selects 4000000 bytes. If more space is needed, an error will occur.</p>
<dt><code>-outfile</code><i> name</i></p>
<dd> Send output image to the named file, not to standard output.</p>
<dt><code>-memdst</code></p>
<dd> Compress to memory instead of a file. This feature was implemented mainly as a way of testing the in-memory destination manager (jpeg_mem_dest()), but it is also useful for benchmarking, since it reduces the I/O overhead.</p>
<dt><code>-verbose</code></p>
<dd> Enable debug printout. More <code>-v</code>&#8216;s give more output. Also, version information is printed at startup.</p>
<dt><code>-debug</code></p>
<dd> Same as <code>-verbose</code>.</p>
<dt><code>-version</code></p>
<dd> Print version information and exit.</dl>
<p> The <code>-restart</code> option inserts extra markers that allow a JPEG decoder to resynchronize after a transmission error. Without restart markers, any damage to a compressed file will usually ruin the image from the point of the error to the end of the image; with restart markers, the damage is usually confined to the portion of the image up to the next restart marker. Of course, the restart markers occupy extra space. We recommend <code>-restart 1</code> for images that will be transmitted across unreliable networks such as Usenet. </p>
<p> The <code>-smooth</code> option filters the input to eliminate fine-scale noise. This is often useful when converting dithered images to JPEG: a moderate smoothing factor of 10 to 50 gets rid of dithering patterns in the input file, resulting in a smaller JPEG file and a better-looking image. Too large a smoothing factor will visibly blur the image, however. </p>
<p> Switches for wizards:</p>
<dl>
<dt><code>-baseline</code></p>
<dd> Force baseline-compatible quantization tables to be generated. This clamps quantization values to 8 bits even at low quality settings. (This switch is poorly named, since it does not ensure that the output is actually baseline JPEG. For example, you can use <code>-baseline</code> and <code>-progressive</code> together.)</p>
<dt><code>-qtables</code><i> file</i></p>
<dd> Use the quantization tables given in the specified text file.</p>
<dt><code>-qslots</code><i> N[,&#8230;]</i></p>
<dd> Select which quantization table to use for each color component.</p>
<dt><code>-sample</code><i> HxV[,&#8230;]</i></p>
<dd> Set JPEG sampling factors for each color component.</p>
<dt><code>-scans</code><i> file</i></p>
<dd> Use the scan script given in the specified text file.</dl>
<p> The &quot;wizard&quot; switches are intended for experimentation with JPEG. If you don&#8217;t know what you are doing, <code>don&#8217;t use them</code>. These switches are documented further in the file wizard.txt.</p>
<h2>EXAMPLES</h2>
<p> This example compresses the PPM file foo.ppm with a quality factor of 60 and saves the output as foo.jpg:</p>
<dl>
<dt>
<dd> <code>cjpeg -quality</code> <i>60 foo.ppm</i> <code>&gt;</code> <i>foo.jpg</i></dl>
<h2>HINTS</h2>
<p> Color GIF files are not the ideal input for JPEG; JPEG is really intended for compressing full-color (24-bit) images. In particular, don&#8217;t try to convert cartoons, line drawings, and other images that have only a few distinct colors. GIF works great on these, JPEG does not. If you want to convert a GIF to JPEG, you should experiment with <code>cjpeg</code>&#8216;s <code>-quality</code> and <code>-smooth</code> options to get a satisfactory conversion. <code>-smooth 10</code> or so is often helpful. </p>
<p> Avoid running an image through a series of JPEG compression/decompression cycles. Image quality loss will accumulate; after ten or so cycles the image may be noticeably worse than it was after one cycle. It&#8217;s best to use a lossless format while manipulating an image, then convert to JPEG format when you are ready to file the image away. </p>
<p> The <code>-optimize</code> option to <code>cjpeg</code> is worth using when you are making a &quot;final&quot; version for posting or archiving. It&#8217;s also a win when you are using low quality settings to make very small JPEG files; the percentage improvement is often a lot more than it is on larger files. (At present, <code>-optimize</code> mode is always selected when generating progressive JPEG files.)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JPEGMEM</code></p>
<dd> If this environment variable is set, its value is the default memory limit. The value is specified as described for the <code>-maxmemory</code> switch. <code>JPEGMEM</code> overrides the default value specified when the program was compiled, and itself is overridden by an explicit <code>-maxmemory</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1)<br />
 <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5)<br />
 Wallace, Gregory K. &quot;The JPEG Still Picture Compression Standard&quot;, Communications of the ACM, April 1991 (vol. 34, no. 4), pp. 30-44.</p>
<h2>AUTHOR</h2>
<p> Independent JPEG Group </p>
<p> This file was modified by The libjpeg-turbo Project to include only information relevant to libjpeg-turbo, to wordsmith certain sections, and to describe features not present in libjpeg.</p>
<h2>ISSUES</h2>
<p> Support for GIF input files was removed in cjpeg v6b due to concerns over the Unisys LZW patent. Although this patent expired in 2006, cjpeg still lacks GIF support, for these historical reasons. (Conversion of GIF files to JPEG is usually a bad idea anyway, since GIF is a 256-color format.) </p>
<p> Not all variants of BMP and Targa file formats are supported. </p>
<p> The <code>-targa</code> switch is not a bug, it&#8217;s a feature. (It would be a bug if the Targa format designers had not been clueless.) </p>
<h2>Index</h2>
