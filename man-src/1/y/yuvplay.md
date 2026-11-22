---

title: "yuvplay(1)"
name: "yuvplay"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvplay/"
description: "yuvplay – Display YUV4MPEG2 streams (using SDL)"
---

<p> yuvplay &#8211; Display YUV4MPEG2 streams (using SDL)</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvplay</code> [<code>options</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvplay</code> produces on-screen playback of a YUV4MPEG2 stream which is provided to stdin, typically through piping from the stdout of <code><a href="/docs/linux/man/1-lavpipe/">lavpipe</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2dec/">mpeg2dec</a></code>(1) or a similar program. It should be noted that for pure playback lavplay should be a superior option. yuvplay is intended primarily as a debugging or diagnostic utility when setting up video processing pipelines. </p>
<h2>OPTIONS</h2>
<p> <code>yuvplay</code> accepts the following options:</p>
<dl>
<dt><code>-s</code><i>&nbsp;<wbr>WxH</i></dt>
<dd> The size of the SDL window. By default, it uses the size of the input video stream scaled to yield 1:1 pixels (using the sample aspect ratio encoded in the stream header). However, you can specify any size you want. WxH is the width x height of the scaled window. </dd>
<dt><code>-t</code><i>title</i></dt>
<dd> Set the window title. </dd>
<dt><code>-f</code><i> num</i></dt>
<dd> Override the framerate specified in the input stream header. </dd>
<dt><code>-c</code></dt>
<dd> By default, yuvplay will try to play at the framerate of the input movie. With this option, yuvplay will just play all the frames as fast as it can. </dd>
<dt><code>-v</code><i>&nbsp;<wbr>[0,</i><code>1,</code><i>2]</i></dt>
<dd> Set the verbosity of user feedback. Default is &quot;1&quot;: errors, warnings, and info messages. </dd>
</dl>
<h2>AUTHOR</h2>
<p> This man page was originally written by Ronald Bultje (and since edited by Matt Marjanovic).<br/>
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br/>
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</dt>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lavpipe/">lavpipe</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1) <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1) </p>
