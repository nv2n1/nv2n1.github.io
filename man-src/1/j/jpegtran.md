---
title: "jpegtran(1)"
name: "jpegtran"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpegtran/"
description: "jpegtran – lossless transformation of JPEG files"
---

<h2 class="name">NAME</h2>
<p> jpegtran &#8211; lossless transformation of JPEG files </p>
<h2>SYNOPSIS</h2>
<p> <code>jpegtran</code> [ <i>options</i> ] [ <i>filename</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>jpegtran</code> performs various useful transformations of JPEG files. It can translate the coded representation from one variant of JPEG to another, for example from baseline JPEG to progressive JPEG or vice versa. It can also perform some rearrangements of the image data, for example turning an image from landscape to portrait format by rotation. </p>
<p> For EXIF files and JPEG files containing Exif data, you may prefer to use <code>exiftran</code> instead. </p>
<p> <code>jpegtran</code> works by rearranging the compressed data (DCT coefficients), without ever fully decoding the image. Therefore, its transformations are lossless: there is no image degradation at all, which would not be true if you used <code>djpeg</code> followed by <code>cjpeg</code> to accomplish the same conversion. But by the same token, <code>jpegtran</code> cannot perform lossy operations such as changing the image quality. However, while the image data is losslessly transformed, metadata can be removed. See the <code>-copy</code> option for specifics. </p>
<p> <code>jpegtran</code> reads the named JPEG/JFIF file, or the standard input if no file is named, and produces a JPEG/JFIF file on the standard output.</p>
<h2>OPTIONS</h2>
<p> All switch names may be abbreviated; for example, <code>-optimize</code> may be written <code>-opt</code> or <code>-o</code>. Upper and lower case are equivalent. British spellings are also accepted (e.g., <code>-optimise</code>), though for brevity these are not mentioned below. </p>
<p> To specify the coded JPEG representation used in the output file, <code>jpegtran</code> accepts a subset of the switches recognized by <code>cjpeg</code>:</p>
<dl>
<dt><code>-optimize</code></p>
<dd> Perform optimization of entropy encoding parameters.</p>
<dt><code>-progressive</code></p>
<dd> Create progressive JPEG file.</p>
<dt><code>-restart</code><i> N</i></p>
<dd> Emit a JPEG restart marker every N MCU rows, or every N MCU blocks if &quot;B&quot; is attached to the number.</p>
<dt><code>-arithmetic</code></p>
<dd> Use arithmetic coding.</p>
<dt><code>-scans</code><i> file</i></p>
<dd> Use the scan script given in the specified text file.</dl>
<p> See <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1) for more details about these switches. If you specify none of these switches, you get a plain baseline-JPEG output file. The quality setting and so forth are determined by the input file. </p>
<p> The image can be losslessly transformed by giving one of these switches:</p>
<dl>
<dt><code>-flip horizontal</code></p>
<dd> Mirror image horizontally (left-right).</p>
<dt><code>-flip vertical</code></p>
<dd> Mirror image vertically (top-bottom).</p>
<dt><code>-rotate 90</code></p>
<dd> Rotate image 90 degrees clockwise.</p>
<dt><code>-rotate 180</code></p>
<dd> Rotate image 180 degrees.</p>
<dt><code>-rotate 270</code></p>
<dd> Rotate image 270 degrees clockwise (or 90 ccw).</p>
<dt><code>-transpose</code></p>
<dd> Transpose image (across UL-to-LR axis).</p>
<dt><code>-transverse</code></p>
<dd> Transverse transpose (across UR-to-LL axis).</dl>
<p> The transpose transformation has no restrictions regarding image dimensions. The other transformations operate rather oddly if the image dimensions are not a multiple of the iMCU size (usually 8 or 16 pixels), because they can only transform complete blocks of DCT coefficient data in the desired way. </p>
<p> <code>jpegtran</code>&#8216;s default behavior when transforming an odd-size image is designed to preserve exact reversibility and mathematical consistency of the transformation set. As stated, transpose is able to flip the entire image area. Horizontal mirroring leaves any partial iMCU column at the right edge untouched, but is able to flip all rows of the image. Similarly, vertical mirroring leaves any partial iMCU row at the bottom edge untouched, but is able to flip all columns. The other transforms can be built up as sequences of transpose and flip operations; for consistency, their actions on edge pixels are defined to be the same as the end result of the corresponding transpose-and-flip sequence. </p>
<p> For practical use, you may prefer to discard any untransformable edge pixels rather than having a strange-looking strip along the right and/or bottom edges of a transformed image. To do this, add the <code>-trim</code> switch:</p>
<dl>
<dt><code>-trim</code></p>
<dd> Drop non-transformable edge blocks.</p>
<dt>
<dd> Obviously, a transformation with <code>-trim</code> is not reversible, so strictly speaking <code>jpegtran</code> with this switch is not lossless. Also, the expected mathematical equivalences between the transformations no longer hold. For example, <code>-rot 270 -trim</code> trims only the bottom edge, but <code>-rot 90 -trim</code> followed by <code>-rot 180 -trim</code> trims both edges.</p>
<dt><code>-perfect</code></p>
<dd> If you are only interested in perfect transformations, add the <code>-perfect</code> switch. This causes <code>jpegtran</code> to fail with an error if the transformation is not perfect.</p>
<dt>
<dd> For example, you may want to do</p>
<dt>
<dd> <code>(jpegtran -rot 90 -perfect</code> <i>foo.jpg</i> <code>|| djpeg</code> <i>foo.jpg</i> <code>| pnmflip -r90 | cjpeg)</code></p>
<dt>
<dd> to do a perfect rotation, if available, or an approximated one if not.</dl>
<p> This version of <code>jpegtran</code> also offers a lossless crop option, which discards data outside of a given image region but losslessly preserves what is inside. Like the rotate and flip transforms, lossless crop is restricted by the current JPEG format; the upper left corner of the selected region must fall on an iMCU boundary. If it doesn&#8217;t, then it is silently moved up and/or left to the nearest iMCU boundary (the lower right corner is unchanged.) Thus, the output image covers at least the requested region, but it may cover more. The adjustment of the region dimensions may be optionally disabled by attaching an &#8216;f&#8217; character (&quot;force&quot;) to the width or height number. </p>
<p> The image can be losslessly cropped by giving the switch:</p>
<dl>
<dt><code>-crop WxH+X+Y</code></p>
<dd> Crop the image to a rectangular region of width W and height H, starting at point X,Y. The lossless crop feature discards data outside of a given image region but losslessly preserves what is inside. Like the rotate and flip transforms, lossless crop is restricted by the current JPEG format; the upper left corner of the selected region must fall on an iMCU boundary. If it doesn&#8217;t, then it is silently moved up and/or left to the nearest iMCU boundary (the lower right corner is unchanged.)</dl>
<p> Other not-strictly-lossless transformation switches are:</p>
<dl>
<dt><code>-grayscale</code></p>
<dd> Force grayscale output.</p>
<dt>
<dd> This option discards the chrominance channels if the input image is YCbCr (ie, a standard color JPEG), resulting in a grayscale JPEG file. The luminance channel is preserved exactly, so this is a better method of reducing to grayscale than decompression, conversion, and recompression. This switch is particularly handy for fixing a monochrome picture that was mistakenly encoded as a color JPEG. (In such a case, the space savings from getting rid of the near-empty chroma channels won&#8217;t be large; but the decoding time for a grayscale JPEG is substantially less than that for a color JPEG.)</dl>
<p> <code>jpegtran</code> also recognizes these switches that control what to do with &quot;extra&quot; markers, such as comment blocks:</p>
<dl>
<dt><code>-copy none</code></p>
<dd> Copy no extra markers from source file. This setting suppresses all comments and other metadata in the source file.</p>
<dt><code>-copy comments</code></p>
<dd> Copy only comment markers. This setting copies comments from the source file but discards any other metadata.</p>
<dt><code>-copy all</code></p>
<dd> Copy all extra markers. This setting preserves miscellaneous markers found in the source file, such as JFIF thumbnails, Exif data, and Photoshop settings. In some files, these extra markers can be sizable. Note that this option will copy thumbnails as-is; they will not be transformed.</dl>
<p> The default behavior is <code>-copy comments</code>. (Note: in IJG releases v6 and v6a, <code>jpegtran</code> always did the equivalent of <code>-copy none</code>.) </p>
<p> Additional switches recognized by jpegtran are:</p>
<dl>
<dt><code>-icc</code><i> file</i></p>
<dd> Embed ICC color management profile contained in the specified file. Note that this will cause <code>jpegtran</code> to ignore any APP2 markers in the input file, even if <code>-copy all</code> is specified.</p>
<dt><code>-maxmemory</code><i> N</i></p>
<dd> Set limit for amount of memory to use in processing large images. Value is in thousands of bytes, or millions of bytes if &quot;M&quot; is attached to the number. For example, <code>-max 4m</code> selects 4000000 bytes. If more space is needed, an error will occur.</p>
<dt><code>-outfile</code><i> name</i></p>
<dd> Send output image to the named file, not to standard output.</p>
<dt><code>-verbose</code></p>
<dd> Enable debug printout. More <code>-v</code>&#8216;s give more output. Also, version information is printed at startup.</p>
<dt><code>-debug</code></p>
<dd> Same as <code>-verbose</code>.</p>
<dt><code>-version</code></p>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> This example converts a baseline JPEG file to progressive form:</p>
<dl>
<dt>
<dd> <code>jpegtran -progressive</code> <i>foo.jpg</i> <code>&gt;</code> <i>fooprog.jpg</i></dl>
<p> This example rotates an image 90 degrees clockwise, discarding any unrotatable edge pixels:</p>
<dl>
<dt>
<dd> <code>jpegtran -rot 90 -trim</code> <i>foo.jpg</i> <code>&gt;</code> <i>foo90.jpg</i></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JPEGMEM</code></p>
<dd> If this environment variable is set, its value is the default memory limit. The value is specified as described for the <code>-maxmemory</code> switch. <code>JPEGMEM</code> overrides the default value specified when the program was compiled, and itself is overridden by an explicit <code>-maxmemory</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1)<br />
 Wallace, Gregory K. &quot;The JPEG Still Picture Compression Standard&quot;, Communications of the ACM, April 1991 (vol. 34, no. 4), pp. 30-44.</p>
<h2>AUTHOR</h2>
<p> Independent JPEG Group </p>
<p> This file was modified by The libjpeg-turbo Project to include only information relevant to libjpeg-turbo and to wordsmith certain sections.</p>
<h2>BUGS</h2>
<p> The transform options can&#8217;t transform odd-size images perfectly. Use <code>-trim</code> or <code>-perfect</code> if you don&#8217;t like the results. </p>
<p> The entire image is read into memory and then written out again, even in cases where this isn&#8217;t really necessary. Expect swapping on large images, especially when using the more complex transform options. </p>
<h2>Index</h2>
