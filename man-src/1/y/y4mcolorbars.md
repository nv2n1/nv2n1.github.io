---
title: "y4mcolorbars(1)"
name: "y4mcolorbars"
section: "1"
letter: "y"
url: "/docs/linux/man/1-y4mcolorbars/"
description: "y4mcolorbars – Create a YUV4MPEG2 stream containing a colorbar test pattern"
---

<h2>NAME</h2>
<p> y4mcolorbars &#8211; Create a YUV4MPEG2 stream containing a colorbar test pattern </p>
<h2>SYNOPSIS</h2>
<p> <code>y4mcolorbars</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>y4mcolorbars</code> creates a YUV4MPEG2 stream consisting entirely of frames containing a colorbar test pattern. The pattern attempts to reproduce the standard SMPTE EG-1-1990 colorbar test signal as faithfully as possible, given the constraints of the Y&#8217;CbCr colorspace. </p>
<p> Output is to stdout to facilitate piping to other MJPEG tools. </p>
<h2>OPTIONS</h2>
<p> <code>y4mcolorbars</code> accepts the following options: </p>
<dl>
<dt><code>-n</code><i> num</i></p>
<dd> Output a total of &#8216;num&#8217; output frames. [default: 1]</p>
<dt><code>-F</code><i> n:d</i></p>
<dd> Set framerate encoded in output stream, as an exact integer ratio. Common rates are:<br />
&nbsp;<wbr>24000:1001 &#8211; NTSC 3:2 pulldown converted film<br />
&nbsp;<wbr>24:1 &#8211; native film<br />
&nbsp;<wbr>25:1 &#8211; PAL/SECAM<br />
&nbsp;<wbr>30000:1001 &#8211; NTSC video&nbsp;<wbr>[default]<br />
&nbsp;<wbr>50:1 &#8211; PAL field rate<br />
&nbsp;<wbr>60000:1001 &#8211; NTSC field rate</p>
<dt><code>-W</code><i> w</i></p>
<dd> Set frame width. [default: 720]</p>
<dt><code>-H</code><i> h</i></p>
<dd> Set frame height. [default: 480]</p>
<dt><code>-A</code><i> n:d</i></p>
<dd> Set pixel aspect ratio encoded in output stream, as an exact integer ratio. Common ratios are:<br />
&nbsp;<wbr>&nbsp;<wbr>1:1&nbsp;<wbr>&nbsp;<wbr>&#8211; square pixels&nbsp;<wbr>(e.g. computer graphics)<br />
&nbsp;<wbr>10:11 &#8211; CCIR-601 NTSC&nbsp;<wbr>[default]<br />
&nbsp;<wbr>59:54 &#8211; CCIR-601 PAL</p>
<dt><code>-I</code><i> x</i></p>
<dd> Set interlacing mode, used to interpret the PPM image(s), and also encoded in output stream.<br />
&nbsp;<wbr>p &#8211; progressive, non-interlaced&nbsp;<wbr>[default]<br />
&nbsp;<wbr>t &#8211; top/upper-field-first interlaced<br />
&nbsp;<wbr>b &#8211; bottom/lower-field-first interlaced</p>
<dt><code>-Q</code><i> n</i></p>
<dd> Data to place in the &quot;-I/+Q&quot; patches in the bottom row of the pattern:<br />
&nbsp;<wbr>0 &#8211;&nbsp;<wbr>&nbsp;<wbr>-I and&nbsp;<wbr>+Q at 20%&nbsp;<wbr>(20IRE)&nbsp;<wbr>&nbsp;<wbr>[default]<br />
&nbsp;<wbr>1 &#8211;&nbsp;<wbr>&nbsp;<wbr>-I and&nbsp;<wbr>+Q at 50%&nbsp;<wbr>(50IRE)<br />
&nbsp;<wbr>2 &#8211;&nbsp;<wbr>&nbsp;<wbr>+Cb and&nbsp;<wbr>+Cr at 100% </p>
<dt><code>-S</code><i> mode</i></p>
<dd> Set chroma subsampling mode.<br />
&nbsp;<wbr>444 &#8211; 4:4:4&nbsp;<wbr>(no subsampling)&nbsp;<wbr>[default]<br />
420jpeg &#8211; 4:2:0 JPEG/MPEG-1, interstitial cositing&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>420mpeg2 &#8211; 4:2:0 MPEG-2, horizontal cositing </p>
<p> The supported subsampled modes use a lousy subsampling filter; better results will be achieved by passing the default 4:4:4 output to a scaler which supports subsampling, such as <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1).</p>
<dt><code>-v</code><i> [0,1,2]</i></p>
<dd> Set verbosity level.<br />
&nbsp;<wbr>0 &#8211;&nbsp;<wbr>&nbsp;<wbr>warnings and errors only.<br />
&nbsp;<wbr>1 &#8211;&nbsp;<wbr>&nbsp;<wbr>add informative messages, too.&nbsp;<wbr>[default]<br />
&nbsp;<wbr>2 &#8211;&nbsp;<wbr>&nbsp;<wbr>add chatty debugging message, too. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To create and display 200 frames of colorbars corresponding to a top-field-first interlaced 4:3 NTSC source: </p>
<dl>
<dt>
<dd> y4mcolorbars -n 200 -It -S 420jpeg | yuvplay</dl>
<p> To create and display 200 frames of colorbars corresponding to a bottom-field-first interlaced 4:3 PAL source: </p>
<dl>
<dt>
<dd> y4mcolorbars -n 200 -H 576 -F 25:1 -A 59:54 -Ib | yuvplay</dl>
<h2>BUGS</h2>
<p> First, it&#8217;s not clear to the author (who hasn&#8217;t actually ever seen the SMPTE EG-1-1990 document itself) what the absolute excursion of the -I and +Q regions is supposed to be; however, the phase is correct, and that should be the critical feature. Second, the PLUGE bars, of -4 and +4 IRE, can never be precisely synthesized &#8212; the Y&#8217; digital space maps [16,235] over the full luma excursion, but the full luma excursion in analog space depends on whether or not 7.5 IRE NTSC setup is being used by whatever device eventually produces the analog output. However, the difference is within 1-bit of Y&#8217; accuracy anyway. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Matt Marjanovic.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-y4mscaler/">y4mscaler</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvplay/">yuvplay</a></code>(1) </p>
<h2>Index</h2>
