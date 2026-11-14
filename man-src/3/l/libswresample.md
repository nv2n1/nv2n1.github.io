---
title: "libswresample(3)"
name: "libswresample"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libswresample/"
description: "libswresample – audio resampling library"
---

<h2 class="name">NAME</h2>
<p> libswresample &#8211; audio resampling library </p>
<h2>DESCRIPTION</h2>
<p> The libswresample library performs highly optimized audio resampling, rematrixing and sample format conversion operations. </p>
<p> Specifically, this library performs the following conversions:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Resampling</i>: is the process of changing the audio rate, for example from a high sample rate of 44100Hz to 8000Hz. Audio conversion from high to low sample rate is a lossy process. Several resampling options and algorithms are available.</p>
<dt>&bull;</p>
<dd> <i>Format conversion</i>: is the process of converting the type of samples, for example from 16-bit signed samples to unsigned 8-bit or float samples. It also handles packing conversion, when passing from packed layout (all samples belonging to distinct channels interleaved in the same buffer), to planar layout (all samples belonging to the same channel stored in a dedicated buffer or &#8220;plane&#8221;).</p>
<dt>&bull;</p>
<dd> <i>Rematrixing</i>: is the process of changing the channel layout, for example from stereo to mono. When the input channels cannot be mapped to the output streams, the process is lossy, since it involves different gain factors and mixing.</dl>
<p> Various other audio conversions (e.g. stretching and padding) are enabled through dedicated options.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></i>(1), <i><a href="/docs/linux/man/1-ffplay/">ffplay</a></i>(1), <i><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></i>(1), <i><a href="/docs/linux/man/1-ffserver/">ffserver</a></i>(1), <i><a href="/docs/linux/man/1-ffmpeg-resampler/">ffmpeg-resampler</a></i>(1), <i><a href="/docs/linux/man/3-libavutil/">libavutil</a></i>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
