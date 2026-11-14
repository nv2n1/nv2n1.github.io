---
title: "y4mtopnm(1)"
name: "y4mtopnm"
section: "1"
letter: "y"
url: "/docs/linux/man/1-y4mtopnm/"
description: "y4mtopnm – Convert a YUV4MPEG2 stream to PNM images"
---

<h2>NAME</h2>
<p> y4mtopnm &#8211; Convert a YUV4MPEG2 stream to PNM images </p>
<h2>SYNOPSIS</h2>
<p> <code>y4mtopnm</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>y4mtopnm</code> converts a YUV4MPEG2 stream into a sequence of raw PPM, PGM, or PAM images. (Technically, &quot;pnm&quot; comprises the PPM, PGM and PBM formats. PAM is a fourth format, which can effectively contain any of the other three, and more.) </p>
<p> Output is to stdout (but feel free to have the shell redirect to a file). </p>
<p> Input is read from stdin, like all other YUV4MPEG2 filters and tools. YUV4MPEG2 streams contain frames using the Y&#8217;CbCr colorspace (ITU-R BT.601). For 4:4:4 (color) streams, <code>y4mtopnm</code> will convert each pixel to the usual R&#8217;G&#8217;B&#8217; colorspace used for computer graphics, and produce PPM images. &quot;MONO&quot; (luma-only) streams will be converted to full-range [0,255] grayscale and output as PGM images. </p>
<p> YUV4MPEG2 streams may (often!) have subsampled chroma planes, but <code>y4mtopnm</code> will not process them (except in the special &#8216;flatten&#8217; mode; see below). Subsampled streams will need to be converted to 4:4:4 using a tool such as <code>y4mscaler</code>. </p>
<p> If <code>y4mtopnm</code> is given a &quot;444ALPHA&quot; stream (4:4:4 video with an 8-bit alpha channel), the results depend on whether or not the &quot;-P&quot; option is specified. With &quot;-P&quot;, it will produce PAM images with a TUPLTYPE of RGB_ALPHA, containing both color and alpha channel data. Without &quot;-P&quot;, it will produce pairs of PPM and PGM images: a PPM for the color pixels followed by a PGM for the alpha channel data. (Such a sequence of interspersed PPM and PGM images cannot be later re-processed by <code>pnmtoy4m</code>. This feature is mostly for quick and easy stream debugging.) </p>
<p> If multiple output images are generated, they are simply output one after another. If you want to turn such a &quot;multi-image&quot; stream/file into individual files, use <code>pnmsplit</code>. (Some PNM filters can process multi-image files/streams; however, many written before June 2000 will only process the first image.) </p>
<p> <code>y4mtopnm</code> and <code>pnmtoy4m</code> are inverses of each other; you can typically pipe the output of one into the other, and vice-versa (except for the &quot;444ALPHA&quot; case noted above and the &quot;mixed-mode&quot; case noted below). Note that the colorspace operations can be lossy in both directions (due to range-compression and/or quantization). And, when converting to PNM, information on interlacing and sample aspect ratio of a stream is lost (but can be reconstructed by supplying command-line arguments to <code>pnmtoy4m</code>). </p>
<h2>OPTIONS</h2>
<p> <code>y4mtopnm</code> accepts the following options: </p>
<dl>
<dt><code>-P</code></p>
<dd> Produce PAM format output, instead of PPM and/or PGM. PAM can encode a superset of PNM, but is not yet understood by as many graphics programs. (Indeed, surprisingly few of the NetPBM tools seem to understand it.)</p>
<dt><code>-D</code></p>
<dd> Produce a separate output image for each field of each frame. (Otherwise, a single image per frame, containing two interleaved fields, is created.) </p>
<p> If the input stream is interlaced, the field-images are output in temporal order, i.e. the first image of a bottom-field-first stream will be the bottom-field. If the stream is progressive or has &quot;mixed-mode&quot; interlacing, then the temporal order is ambiguous, and the top-field will always be output first. </p>
<p> Note that it will <i>not</i> be possible to later use <code>pnmtoy4m</code> to reconstruct a &quot;mixed-mode&quot; stream from a sequence of PNM/PAM images.</p>
<dt><code>-f</code></p>
<dd> Produce a special &#8216;flattened&#8217; output, most useful for analyzing and debugging streams. All the planes of a frame/field are tiled together into an enlarged PGM (or grayscale PAM) output image as follows: </p>
<pre><code>
+ -- -- -+ +-- -- -+
    4:
    4:4 | Y |
    4:4
     :4 w /
          alpha |
      Y |
      +-- -- -+ +-- -- -+ | Cb | | Cb |
      +-- -- -+ +-- -- -+ | Cr | | Cr |
      +-- -- -+ +-- -- -+ | A |
      +-- -- -+ +-- -- -+
    4:2
     :2,
      | Y |
    4:2
     :0 + --+--+ +-- -- -+--+--+ |
      Cb | Cr |
    4:1
     :1 |
      Y | Cb | Cr |
      +--+--+ +-- -- -+--+--+ +-- -- -+MONO | Y |
      +-- -- -+
</code></pre>
<p> In this mode, any YUV4MPEG2 chroma format is accepted, but no upsampling or colorspace conversion is performed. This is essentially just a reformatting/permutation of the original data from the input stream into a PGM image container. All the other command-line flags continue to have the same effect on output.</p>
<dt><code>-v</code><i> [0,1,2]</i></p>
<dd> Set verbosity level.<br />
&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>warnings and errors only.<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>add informative messages, too.<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>add chatty debugging message, too. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To turn the first 15 frames of an (MJPEG or DV) AVI file into individual PPM files: </p>
<dl>
<dt>
<dd> lav2yuv -f 15 your-video.avi | y4mscaler -O chromass=444 | y4mtopnm | pnmsplit &#8211; &quot;your-video-%d.ppm&quot;</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Matt Marjanovic.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-pnmtoy4m/">pnmtoy4m</a></code>(1), <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-pnmsplit/">pnmsplit</a></code>(1), <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1) </p>
<h2>Index</h2>
