---
title: "ppmtoy4m(1)"
name: "ppmtoy4m"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoy4m/"
description: "ppmtoy4m – Convert PPM images to YUV4MPEG2 stream"
---

<h2>NAME</h2>
<p> ppmtoy4m &#8211; Convert PPM images to YUV4MPEG2 stream </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoy4m</code> [<i>options</i>] <i>[ filename ]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ppmtoy4m</code> converts one or more raw PPM images into a YUV4MPEG2 stream ready for further processing by other video tools. </p>
<p> Output is to stdout to facilitate piping to other MJPEG tools. The size of the output frame(s) is determined from the (first) input image. </p>
<p> Input is a &#8216;raw&#8217; format PPM image, read from stdin or from the optional filename. The input may contain multiple PPM images concatenated together; <code>ppmtoy4m</code> will read and process them sequentially. All images must have identical size and format. Input images can be interpreted as whole progressive frames, interleaved fields, or (in pairs) as sequential fields. The input images must have 8 bits per channel (i.e. &#8216;maxval&#8217; must be 255). </p>
<p> Input images should be in the usual R&#8217;G&#8217;B&#8217; colorspace. They are converted to the Y&#8217;CbCr colorspace (ITU-R BT.601) (and chroma subsampled, if desired) before output. </p>
<p> <code>ppmtoy4m</code> and <code>y4mtoppm</code> are inverses of each other; you can pipe the output of one into the other, and vice-versa. Note that the subsampling and colorspace operations are lossy in both directions. And, when converting to PPM, information on interlacing and sample aspect ratio is lost (but can be reconstructed by supplying command-line arguments to <code>ppmtoy4m</code>). </p>
<h2>OPTIONS</h2>
<p> <code>ppmtoy4m</code> accepts the following options: </p>
<dl>
<dt><code>-o</code><i> num</i></p>
<dd> Frame offset: skip output of the first &#8216;num&#8217; frames. (default: 0)</p>
<dt><code>-n</code><i> num</i></p>
<dd> Output a total of &#8216;num&#8217; output frames. Use &#8216;0&#8217; to specify all frames. (default: 0)</p>
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
<dt><code>-B</code></p>
<dd> Interpret data as being BGR rather than RGB.</p>
<dt><code>-I</code><i> x</i></p>
<dd> Set interlacing mode, used to interpret the PPM image(s), and also encoded in output stream. (default: &#8216;p&#8217;)<br />
&nbsp;<wbr>p &#8211; progressive, non-interlaced<br />
&nbsp;<wbr>t &#8211; top/upper-field-first interlaced<br />
&nbsp;<wbr>b &#8211; bottom/lower-field-first interlaced</p>
<dt><code>-L</code></p>
<dd> For interlaced streams, treat each PPM image as two interleaved fields. (Otherwise, two PPM images will be read for each frame; one per field.)</p>
<dt><code>-r</code></p>
<dd> Repeat last input frame until output is complete. If &#8216;-n 0&#8217; is also specified, last input frame will be repeated forever.</p>
<dt><code>-S</code><i> mode</i></p>
<dd> Set chroma subsampling mode. (default: 444)<br />
&nbsp;<wbr>444 &#8211; 4:4:4&nbsp;<wbr>(no subsampling)<br />
420jpeg &#8211; 4:2:0 JPEG/MPEG-1, interstitial cositing&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>420mpeg2 &#8211; 4:2:0 MPEG-2, horizontal cositing </p>
<p> The subsampled modes use a lousy subsampling filter; better results will be achieved by passing the default 4:4:4 output to a scaler which supports subsampling, such as <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1).</p>
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
<dd> ppmtoy4m -n 15 -r some-image.ppm</dl>
<p> To convert a series of Targa format images (in the current directory) to a YUV4MPEG2 stream displayed by yuvplay: </p>
<dl>
<dt>
<dd> ls *.tga | xargs -n1 tgatoppm | ppmtoy4m | yuvplay</dl>
<h2>AUTHOR</h2>
<p> This man page was written by Matt Marjanovic.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-y4mtoppm/">y4mtoppm</a></code>(1), <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvplay/">yuvplay</a></code>(1) </p>
<h2>Index</h2>
