---
title: "gif2webp(1)"
name: "gif2webp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gif2webp/"
description: "gif2webp – Convert a GIF image to WebP"
---

<h2>NAME</h2>
<p> gif2webp &#8211; Convert a GIF image to WebP</p>
<h2>SYNOPSIS</h2>
<p> <code>gif2webp</code> [<i>options</i>]<i> input_file.gif -o output_file.webp</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>gif2webp</code> command. </p>
<p> <code>gif2webp</code> converts a GIF image to a WebP image.</p>
<h2>OPTIONS</h2>
<p> The basic options are:</p>
<dl>
<dt><code>-o</code><i> string</i></p>
<dd> Specify the name of the output WebP file. If omitted, <code>gif2webp</code> will perform conversion but only report statistics.</p>
<dt><code>-h, -help</code></p>
<dd> Usage information.</p>
<dt><code>-version</code></p>
<dd> Print the version number (as major.minor.revision) and exit.</p>
<dt><code>-lossy</code></p>
<dd> Encode the image using lossy compression.</p>
<dt><code>-q</code><i> float</i></p>
<dd> Specify the compression factor for RGB channels between 0 and 100. The default is 75.<br />
 In case of lossless compression (default), a small factor enables faster compression speed, but produces a larger file. Maximum compression is achieved by using a value of 100.<br />
 In case of lossy compression (specified by the -lossy option), a small factor produces a smaller file with lower quality. Best quality is achieved by using a value of 100.</p>
<dt><code>-m</code><i> int</i></p>
<dd> Specify the compression method to use. This parameter controls the trade off between encoding speed and the compressed file size and quality. Possible values range from 0 to 6. Default value is 4. When higher values are used, the encoder will spend more time inspecting additional encoding possibilities and decide on the quality gain. Lower value can result is faster processing time at the expense of larger file size and lower compression quality.</p>
<dt><code>-f</code><i> int</i></p>
<dd> For lossy encoding only (specified by the -lossy option). Specify the strength of the deblocking filter, between 0 (no filtering) and 100 (maximum filtering). A value of 0 will turn off any filtering. Higher value will increase the strength of the filtering process applied after decoding the picture. The higher the value the smoother the picture will appear. Typical values are usually in the range of 20 to 50.</p>
<dt><code>-v</code></p>
<dd> Print extra information.</p>
<dt><code>-quiet</code></p>
<dd> Do not print anything. </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to our issue tracker: <a rel="nofollow" href="http://code.google.com/p/webp/issues">http://code.google.com/p/webp/issues</a><br />
 Patches welcome! See this page to get started: <a rel="nofollow" href="http://www.webmproject.org/code/contribute/submitting-patches/">http://www.webmproject.org/code/contribute/submitting-patches/</a> </p>
<h2>EXAMPLES</h2>
<p> gif2webp picture.gif -o picture.webp<br />
 gif2webp -q 70 picture.gif -o picture.webp<br />
 gif2webp -lossy -m 3 picture.gif -o picture_lossy.webp<br />
 gif2webp -lossy -f 50 picture.gif -o picture.webp </p>
<h2>AUTHORS</h2>
<p> <code>gif2webp</code> was written by the WebP team.<br />
 The latest source tree is available at <a rel="nofollow" href="http://www.webmproject.org/code">http://www.webmproject.org/code</a> </p>
<p> This manual page was written by Urvang Joshi &lt;urvang [at] google.com&gt;, for the Debian project (and may be used by others). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dwebp/">dwebp</a></code>(1), <code><a href="/docs/linux/man/1-cwebp/">cwebp</a></code>(1), <code><a href="/docs/linux/man/1-webpmux/">webpmux</a></code>(1).<br />
 Please refer to <a rel="nofollow" href="http://developers.google.com/speed/webp/">http://developers.google.com/speed/webp/</a> for additional information. </p>
<h2>Index</h2>
