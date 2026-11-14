---
title: "png2yuv(1)"
name: "png2yuv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-png2yuv/"
description: "png2yuv – Convert PNG images to the YUV4MPEG stream format."
---

<h2 class="name">NAME</h2>
<p> png2yuv &#8211; Convert PNG images to the YUV4MPEG stream format.</p>
<h2>SYNOPSIS</h2>
<p> <code>png2yuv</code> [<code>-b</code> <i>num</i>] [<code>-f</code> <i>num</i>] [<code>-I</code> <i>num</i>] [<code>-L</code> <i>num</i>] [<code>-n</code> num<code>]</code> [<code>-l</code> <i>num</i>] [<code>-j</code> <i>filename</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>png2yuv</code> decompresses a sequence of PNG files and pipes the image data to stdout as a YUV4MPEG2 stream. Any 8bit/pixel PNG format supported by libpng can be read. stdout will be filled with the YUV4MPEG movie data stream, so be prepared to pipe it on to mpeg2enc or to write it into a file. </p>
<p> <code>This tool is incomplete.</code> The alternative utility you are probably looking for is <code><a href="/docs/linux/man/1-ppmtoy4m/">ppmtoy4m</a></code>(1), which is also included in MJPEGtools. </p>
<h2>OPTIONS</h2>
<p> <code>png2yuv</code> accepts the following options: </p>
<dl>
<dt><code>-b</code><i> num</i></p>
<dd> Frame offset: skip output of the first &#8216;num&#8217; frames. (default: 0)</p>
<dt><code>-f</code><i> num</i></p>
<dd> Set the frame rate of stream accepts the same numbers. Not default, this option has to be specified.</p>
<dt><code>-I</code><i> num</i></p>
<dd> interlacing mode: p = none / progressive<br />
 t = top field first<br />
 b = bottom field first<br />
 No default, this option has to be specified.</p>
<dt><code>-L</code><i> num</i></p>
<dd> 0 = non-interleaved (two successive fields per PNG file)<br />
 1 = interleaved fields</p>
<dt><code>-l</code><i> num</i></p>
<dd> Specifies the number of loops (default: 0 loops )</p>
<dt><code>-S</code><i> samp_mode</i></p>
<dd> chroma subsampling mode, only for professionals, for more info see ppmtoy4m and the YUV guide on <a rel="nofollow" href="http://www.mir.com/DMG/.">http://www.mir.com/DMG/.</a><br />
 default: 420_jpeg<br />
 When this option is not used the given range of images is only processed once. If you use this option and as number 1, jpeg2yv will loop forever writing the image to stdout. When you use n &gt; 1 it will loop. n-time till it finishes.</p>
<dt><code>-n</code><i> num</i></p>
<dd> Specifies the nummber of frames to process. (default: all = -1)</p>
<dt><code>-j</code><i> {1}%{2}d{3}</i></p>
<dd> Read PNG frames with the name components as follows:<br />
&nbsp;<wbr>{1}&nbsp;<wbr>PNG filename prefix&nbsp;<wbr>(e g: picture_&nbsp;<wbr>)<br />
&nbsp;<wbr>{2}&nbsp;<wbr>Counting placeholder&nbsp;<wbr>(like in C, printf, eg 06&nbsp;<wbr>))<br />
&nbsp;<wbr>{3}&nbsp;<wbr>File extension. Something like this: .png A correct description of the files could look like this: picture_%06d.png</p>
<dt><code>-v</code><i> num</i></p>
<dd> Verbosity level (0, 1 or 2) </p>
</dl>
<h2>BUGS</h2>
<p> The frame rate description does not seem to be up to date. The NTSC integer ratios are not supported (use floating point instead). As workaround specify a PAL (25) or native FILM (24) and set the right frame rate in mpeg2enc with the -F option. Interlaced handling is not implemented yet. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Gernot Ziegler.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-ppmtoy4m/">ppmtoy4m</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-yuvmedianfilter/">yuvmedianfilter</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
