---
title: "jpeg2yuv(1)"
name: "jpeg2yuv"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpeg2yuv/"
description: "jpeg2yuv – Convert jpeg images to the yuv format."
---

<h2 class="name">NAME</h2>
<p> jpeg2yuv &#8211; Convert jpeg images to the yuv format.</p>
<h2>SYNOPSIS</h2>
<p> <code>jpeg2yuv</code> [<code>-b</code> <i>num</i>] [<code>-f</code> <i>num</i>] [<code>-I</code> <i>num</i>] [<code>-A</code> <i>ratio</i>] [<code>-L</code> <i>num</i>] [<code>-n</code> num<code>]</code> [<code>-l</code> <i>num</i>] [<code>-j</code> <i>filename</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>jpeg2yuv</code> decompresses a sequence of JPEG files and pipes the image data to stdout as a YUV4MPEG2 stream. Any JPEG format supported by libjpeg can be read. stdout will be filled with the YUV4MPEG2 movie data stream, so be prepared to pipe it on to mpeg2enc or to write it into a file. </p>
<h2>OPTIONS</h2>
<p> <code>jpeg2yuv</code> accepts the following options: </p>
<dl>
<dt><code>-b</code><i> num</i></p>
<dd> Frame offset: skip output of the first &#8216;num&#8217; frames. (default: 0)</p>
<dt><code>-f</code><i> num</i></p>
<dd> Set the frame rate of stream accepts the same numbers. No default, this option has to be specified.</p>
<dt><code>-A</code><i> ratio</i></p>
<dd> Sample aspect ratio. Default is square pixels (1:1)</p>
<dt><code>-I</code><i> num</i></p>
<dd> interlacing mode: p = none / progressive<br />
 t = top field first<br />
 b = bottom field first<br />
 No default, this option has to be specified.</p>
<dt><code>-L</code><i> num</i></p>
<dd> 0 = non-interlaced (two successive fields per JPEG file)<br />
 1 = interlaced fields</p>
<dt><code>-l</code><i> num</i></p>
<dd> Specifies the number of loops (default: 0 loops )<br />
 When this option is not used the given range of images is only processed once. If you use this option with num of -1 jpeg2yuv will loop forever writing the image to stdout. When you use n &gt; 0 it will loop n-times till it finishes.</p>
<dt><code>-n</code><i> num</i></p>
<dd> Specifies the number of frames to process. (default: all = -1)</p>
<dt><code>-j</code><i> {1}%{2}d{3}</i></p>
<dd> Read JPEG frames with the name components as follows:<br />
&nbsp;<wbr>{1}&nbsp;<wbr>JPEG filename prefix&nbsp;<wbr>(e g: picture_&nbsp;<wbr>)<br />
&nbsp;<wbr>{2}&nbsp;<wbr>Counting placeholder&nbsp;<wbr>(like in C, printf, eg 06&nbsp;<wbr>))<br />
&nbsp;<wbr>{3}&nbsp;<wbr>File extension. Something like this: .jpg A correct description of the files could look like this: picture_%06d.jpg </p>
<p> If this option is omited, the filenames are read from stdin. For example:<br />
&nbsp;<wbr>$ls&nbsp;<wbr>*jpg | jpeg2yuv -f 25 -I p&nbsp;<wbr>&gt;&nbsp;<wbr>result.yuv</p>
<dt><code>-R</code><i> 1 or 0</i></p>
<dd> rescale YUV color values from 0-255 to 16-235 (default: 1)</p>
<dt><code>-v</code><i> num</i></p>
<dd> Verbosity level (0, 1 or 2) </p>
</dl>
<h2>BUGS</h2>
<p> The frame rate description seems not to be up to date. The NTSC integer ratios seem not to be supported. As a workaround specify a PAL (25) or FILM (24) and set the right frame rate in mpeg2enc with the -F option. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Bernhard Praschinger.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-ppmtoy4m/">ppmtoy4m</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-yuvmedianfilter/">yuvmedianfilter</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
