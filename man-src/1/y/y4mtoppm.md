---
title: "y4mtoppm(1)"
name: "y4mtoppm"
section: "1"
letter: "y"
url: "/docs/linux/man/1-y4mtoppm/"
description: "y4mtoppm – Convert YUV4MPEG2 stream to PPM images"
---

<h2>NAME</h2>
<p> y4mtoppm &#8211; Convert YUV4MPEG2 stream to PPM images </p>
<h2>SYNOPSIS</h2>
<p> <code>y4mtoppm</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>y4mtoppm</code> converts a YUV4MPEG2 stream into a sequence of raw PPM images. </p>
<p> Output is to stdout (but feel free to have the shell redirect to a file). </p>
<p> Input is read from stdin, like all other YUV4MPEG2 filters and tools. YUV4MPEG2 streams contain frames using the Y&#8217;CbCr colorspace (ITU-R BT.601). <code>y4mtoppm</code> will convert each pixel to the usual R&#8217;G&#8217;B&#8217; colorspace used for computer graphics. </p>
<p> YUV4MPEG2 streams may (often!) have subsampled chroma planes. <code>y4mtoppm</code> can upsample &quot;4:2:0 JPEG&quot; streams using a simple, lousy algorithm. Better results will be obtained using a filters such as <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1) which are capable of general-purpose subsampling operations. <code>y4mtoppm</code> will fail on streams which have chroma subsampling modes other than 4:4:4 or 4:2:0-JPEG. </p>
<p> For interlaced streams, these operations are performed on each field individually. Fields can be output as separate PPM images in time-order (default), or interleaved into full-frame images. </p>
<p> If multiple PPM images are generated, they are simply output one after another. If you want to turn such a &quot;multi-image&quot; PPM stream/file into individual files, use <code>pnmsplit</code>. (Some PNM filters can process multi-image files/streams; however, many written before June 2000 will only process the first image.) </p>
<p> <code>y4mtoppm</code> and <code>ppmtoy4m</code> are inverses of each other; you can pipe the output of one into the other, and vice-versa. Note that the colorspace (and subsampling) operations are lossy in both directions. And, when converting to PPM, information on interlacing and sample aspect ratio is lost (but can be reconstructed by supplying command-line arguments to <code>ppmtoy4m</code>). </p>
<h2>OPTIONS</h2>
<p> <code>y4mtoppm</code> accepts the following options: </p>
<dl>
<dt><code>-L</code></p>
<dd> For interlaced streams, output a single PPM image for each frame, containing two interleaved fields. (Otherwise, two PPM images will be generated for each frame; one per field.)</p>
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
<dd> lav2yuv -f 15 your-video.avi | y4mtoppm | pnmsplit &#8211; &quot;your-video-%d.ppm&quot;</dl>
<h2>AUTHOR</h2>
<p> This man page was written by Matt Marjanovic.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-ppmtoy4m/">ppmtoy4m</a></code>(1), <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-pnmsplit/">pnmsplit</a></code>(1), <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1) </p>
<h2>Index</h2>
