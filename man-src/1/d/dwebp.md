---
title: "dwebp(1)"
name: "dwebp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dwebp/"
description: "dwebp – decompress a WebP file to an image file"
---

<h2>NAME</h2>
<p> dwebp &#8211; decompress a WebP file to an image file</p>
<h2>SYNOPSIS</h2>
<p> <code>dwebp</code> [<i>options</i>]<i> input_file.webp</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>dwebp</code> command. </p>
<p> <code>dwebp</code> decompresses WebP files into PNG, PAM, PPM or PGM images.</p>
<h2>OPTIONS</h2>
<p> The basic options are:</p>
<dl>
<dt><code>-h</code></p>
<dd> Print usage summary.</p>
<dt><code>-version</code></p>
<dd> Print the version number (as major.minor.revision) and exit.</p>
<dt><code>-o</code><i> string</i></p>
<dd> Specify the name of the output file (as PNG format by default).</p>
<dt><code>-pam</code></p>
<dd> Change the output format to PAM (retains alpha).</p>
<dt><code>-ppm</code></p>
<dd> Change the output format to PPM (discards alpha).</p>
<dt><code>-pgm</code></p>
<dd> Change the output format to PGM. The output consists of luma/chroma samples instead of RGB, using the ICM4 layout. This option is mainly for verification and debugging purposes.</p>
<dt><code>-yuv</code></p>
<dd> Change the output format to raw YUV. The output consists of luma/chroma-U/chroma-V samples instead of RGB, saved sequentially as individual planes. This option is mainly for verification and debugging purposes.</p>
<dt><code>-nofancy</code></p>
<dd> Don&#8217;t use the fancy upscaler for YUV420. This may lead to jaggy edges (especially the red ones), but should be faster.</p>
<dt><code>-nofilter</code></p>
<dd> Don&#8217;t use the in-loop filtering process even if it is required by the bitstream. This may produce visible blocks on the non-compliant output, but will make the decoding faster.</p>
<dt><code>-mt</code></p>
<dd> Use multi-threading for decoding, if possible.</p>
<dt><code>-crop</code><i> x_position y_position width height</i></p>
<dd> Crop the decoded picture to a rectangle with top-left corner at coordinates (<code>x_position</code>, <code>y_position</code>) and size <code>width</code> x <code>height</code>. This cropping area must be fully contained within the source rectangle. The top-left corner will be snapped to even coordinates if needed. This option is meant to reduce the memory needed for cropping large images. Note: the cropping is applied <i>before</i> any scaling.</p>
<dt><code>-scale</code><i> width height</i></p>
<dd> Rescale the decoded picture to dimension <code>width</code> x <code>height</code>. This option is mostly intended to reducing the memory needed to decode large images, when only a small version is needed (thumbnail, preview, etc.). Note: scaling is applied <i>after</i> cropping.</p>
<dt><code>-v</code></p>
<dd> Print extra information (decoding time in particular).</p>
<dt><code>-noasm</code></p>
<dd> Disable all assembly optimizations. </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to our issue tracker: <a rel="nofollow" href="http://code.google.com/p/webp/issues">http://code.google.com/p/webp/issues</a><br />
 Patches welcome! See this page to get started: <a rel="nofollow" href="http://www.webmproject.org/code/contribute/submitting-patches/">http://www.webmproject.org/code/contribute/submitting-patches/</a> </p>
<h2>EXAMPLES</h2>
<p> dwebp picture.webp -o output.png<br />
 dwebp picture.webp -ppm -o output.ppm </p>
<h2>AUTHORS</h2>
<p> <code>dwebp</code> was written by the WebP team.<br />
 The latest source tree is available at <a rel="nofollow" href="http://www.webmproject.org/code">http://www.webmproject.org/code</a> </p>
<p> This manual page was written by Pascal Massimino &lt;pascal.massimino [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cwebp/">cwebp</a></code>(1), <code><a href="/docs/linux/man/1-webpmux/">webpmux</a></code>(1), <code><a href="/docs/linux/man/1-gif2webp/">gif2webp</a></code>(1).<br />
 Please refer to <a rel="nofollow" href="http://developers.google.com/speed/webp/">http://developers.google.com/speed/webp/</a> for additional information.</p>
<h3>Output file format details</h3>
<p> PAM: <a rel="nofollow" href="http://netpbm.sourceforge.net/doc/pam.html">http://netpbm.sourceforge.net/doc/pam.html</a><br />
 PGM: <a rel="nofollow" href="http://netpbm.sourceforge.net/doc/pgm.html">http://netpbm.sourceforge.net/doc/pgm.html</a><br />
 PPM: <a rel="nofollow" href="http://netpbm.sourceforge.net/doc/ppm.html">http://netpbm.sourceforge.net/doc/ppm.html</a><br />
 PNG: <a rel="nofollow" href="http://www.libpng.org/pub/png/png-sitemap.html#info">http://www.libpng.org/pub/png/png-sitemap.html#info</a> </p>
<h2>Index</h2>
