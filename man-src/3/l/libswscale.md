---
title: "libswscale(3)"
name: "libswscale"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libswscale/"
description: "libswscale – video scaling and pixel format conversion library"
---

<h2 class="name">NAME</h2>
<p> libswscale &#8211; video scaling and pixel format conversion library </p>
<h2>DESCRIPTION</h2>
<p> The libswscale library performs highly optimized image scaling and colorspace and pixel format conversion operations. </p>
<p> Specifically, this library performs the following conversions:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Rescaling</i>: is the process of changing the video size. Several rescaling options and algorithms are available. This is usually a lossy process.</p>
<dt>&bull;</p>
<dd> <i>Pixel format conversion</i>: is the process of converting the image format and colorspace of the image, for example from planar <font SIZE="-1">YUV420P</font> to <font SIZE="-1">RGB24</font> packed. It also handles packing conversion, that is converts from packed layout (all pixels belonging to distinct planes interleaved in the same buffer), to planar layout (all samples belonging to the same plane stored in a dedicated buffer or &#8220;plane&#8221;). </p>
<p> This is usually a lossy process in case the source and destination colorspaces differ.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></i>(1), <i><a href="/docs/linux/man/1-ffplay/">ffplay</a></i>(1), <i><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></i>(1), <i><a href="/docs/linux/man/1-ffserver/">ffserver</a></i>(1), <i><a href="/docs/linux/man/1-ffmpeg-scaler/">ffmpeg-scaler</a></i>(1), <i><a href="/docs/linux/man/3-libavutil/">libavutil</a></i>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
