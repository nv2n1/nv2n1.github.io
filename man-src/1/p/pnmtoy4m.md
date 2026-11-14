---
title: "pnmtoy4m(1)"
name: "pnmtoy4m"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtoy4m/"
description: "pnmtoy4m – Convert PNM/PAM images to YUV4MPEG2 stream"
---

<h2>NAME</h2>
<p> pnmtoy4m &#8211; Convert PNM/PAM images to YUV4MPEG2 stream </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtoy4m</code> [<i>options</i>] <i>[ filename ]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmtoy4m</code> converts one or more raw PPM, PGM, PBM, or PAM images into a YUV4MPEG2 stream ready for further processing by other video tools. These three (or four) image formats are collectively referred to as &quot;PNM images&quot;. </p>
<p> Output is to stdout to facilitate piping to other MJPEG tools. The size of the output frame(s) is determined from the (first) input image. </p>
<p> Input is a &#8216;raw&#8217; format PNM image, read from stdin or from the optional filename. The input may contain multiple PNM images concatenated together; <code>pnmtoy4m</code> will read and process them sequentially. All images must have identical size and format. Input images can be interpreted as whole progressive frames, pairs of interleaved fields, or as sequential fields (read in pairs of images) to be output as either interlaced or progressive frames. PPM and PGM images must have 8 bits per channel (i.e. &#8216;maxval&#8217; must be 255). </p>
<p> PPM input images should be in the usual R&#8217;G&#8217;B&#8217; colorspace. They are converted to the Y&#8217;CbCr colorspace (ITU-R BT.601) before being output to a &quot;4:4:4&quot; (non-subsampled) YUV4MPEG2 stream. If chroma subsampling is required (e.g. to 4:2:0 for MPEG), the output should be further piped through a program such as <code>y4mscaler</code>. </p>
<p> PGM images should be in the standard full-range ([0,255]) grayscale colorspace. PGM and PBM images will be converted to BT.601 luma and output as &quot;MONO&quot; (luma-only) YUV4MPEG2 streams. </p>
<p> The PAM format is a newer superset of the PNM formats; the precise contents of a PAM image is defined by the TUPLTYPE header tag. <code>pnmtoy4m</code> handles TUPLTYPE &quot;GRAYSCALE&quot; as PGM, &quot;RGB&quot; as PPM, and &quot;RGB_ALPHA&quot; as PPM with an 8-bit alpha channel. (The alpha channel is converted to BT.601 luma as is appropriate for YUV4MPEG2 streams.) </p>
<p> <code>pnmtoy4m</code> and <code>y4mtopnm</code> are inverses of each other; you can pipe the output of one into the other, and vice-versa. Note that the colorspace operations are lossy in both directions. And, when converting to PNM, information on interlacing and sample aspect ratio is lost (but can be reconstructed by supplying command-line arguments to <code>pnmtoy4m</code>). </p>
<h2>OPTIONS</h2>
<p> <code>pnmtoy4m</code> accepts the following options: </p>
<dl>
<dt><code>-o</code><i> num</i></p>
<dd> Frame offset: skip output of the first &#8216;num&#8217; frames. (default: 0)</p>
<dt><code>-n</code><i> num</i></p>
<dd> Output a total of &#8216;num&#8217; output frames. Use &#8216;0&#8217; to specify all frames. (default: 0)</p>
<dt><code>-B</code></p>
<dd> Interpret data as being BGR rather than RGB.</p>
<dt><code>-r</code></p>
<dd> Repeat last input frame until output is complete. If &#8216;-n 0&#8217; is also specified, last input frame will be repeated forever.</p>
<dt><code>-D</code><i> x</i></p>
<dd> Treat each PNM image as a single (de-interleaved) field instead of a full frame. The argument specifies the interpretation:<br />
&nbsp;<wbr>t &#8211; the first image is a top-field<br />
&nbsp;<wbr>b &#8211; the first image is a bottom-field </p>
<p> With this option, two input images will be required per output frame. Be careful: mismatched &quot;-I&quot; and &quot;-D&quot; options can invert the temporal or spatial order of the fields (or both).</p>
<dt><code>-F</code><i> n:d</i></p>
<dd> Set framerate encoded in output stream, as an exact integer ratio. (default: 30000:1001) Common rates are:<br />
&nbsp;<wbr>24000:1001 &#8211; NTSC 3:2 pulldown converted film<br />
&nbsp;<wbr>24:1 &#8211; native film<br />
&nbsp;<wbr>25:1 &#8211; PAL/SECAM<br />
&nbsp;<wbr>30000:1001 &#8211; NTSC video<br />
&nbsp;<wbr>50:1 &#8211; PAL field rate<br />
&nbsp;<wbr>60000:1001 &#8211; NTSC field rate</p>
<dt><code>-A</code><i> n:d</i></p>
<dd> Set pixel aspect ratio encoded in output stream, as an exact integer ratio. (default: 1:1) Common ratios are:<br />
&nbsp;<wbr>&nbsp;<wbr>1:1&nbsp;<wbr>&nbsp;<wbr>&#8211; square pixels&nbsp;<wbr>(computer graphics)<br />
&nbsp;<wbr>10:11 &#8211; CCIR-601 NTSC<br />
&nbsp;<wbr>59:54 &#8211; CCIR-601 PAL</p>
<dt><code>-I</code><i> x</i></p>
<dd> Set the output interlacing mode, encoded in the output stream. (Default is to match &quot;-D&quot; if given, or &#8216;p&#8217; if not.)<br />
&nbsp;<wbr>p &#8211; progressive, non-interlaced<br />
&nbsp;<wbr>t &#8211; top/upper-field-first interlaced<br />
&nbsp;<wbr>b &#8211; bottom/lower-field-first interlaced</p>
<dt><code>-v</code><i> [0,1,2]</i></p>
<dd> Set verbosity level.<br />
&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>warnings and errors only.<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>add informative messages, too.<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>add chatty debugging message, too. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To convert a file containing a single PPM file into a stream of 15 (identical) frames: </p>
<dl>
<dt>
<dd> pnmtoy4m -n 15 -r some-image.ppm</dl>
<p> To convert a series of Targa format images (in the current directory) to a YUV4MPEG2 stream displayed by yuvplay: </p>
<dl>
<dt>
<dd> ls *.tga | xargs -n1 tgatoppm | pnmtoy4m | yuvplay</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Matt Marjanovic.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-y4mtopnm/">y4mtopnm</a></code>(1), <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvplay/">yuvplay</a></code>(1) </p>
<h2>Index</h2>
