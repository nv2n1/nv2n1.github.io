---
title: "ffmpeg-scaler(1)"
name: "ffmpeg-scaler"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-scaler/"
description: "ffmpeg-scaler – FFmpeg video scaling and pixel format converter"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-scaler &#8211; FFmpeg video scaling and pixel format converter </p>
<h2>DESCRIPTION</h2>
<p> The FFmpeg rescaler provides a high-level interface to the libswscale library image conversion utilities. In particular it allows one to perform image rescaling and pixel format conversion.</p>
<h2>SCALER OPTIONS</h2>
<p> The video scaler supports the following named options. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, with a few API-only exceptions noted below. For programmatic use, they can be set explicitly in the <tt>&quot;SwsContext&quot;</tt> options or through the <i>libavutil/opt.h</i> <font SIZE="-1">API.</font></p>
<dl>
<dt><code>sws_flags</code></p>
<dd> Set the scaler flags. This is also used to set the scaling algorithm. Only a single algorithm should be selected. Default value is <code>bicubic</code>. </p>
<p> It accepts the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fast_bilinear</code></p>
<dd> Select fast bilinear scaling algorithm.</p>
<dt><code>bilinear</code></p>
<dd> Select bilinear scaling algorithm.</p>
<dt><code>bicubic</code></p>
<dd> Select bicubic scaling algorithm.</p>
<dt><code>experimental</code></p>
<dd> Select experimental scaling algorithm.</p>
<dt><code>neighbor</code></p>
<dd> Select nearest neighbor rescaling algorithm.</p>
<dt><code>area</code></p>
<dd> Select averaging area rescaling algorithm.</p>
<dt><code>bicublin</code></p>
<dd> Select bicubic scaling algorithm for the luma component, bilinear for chroma components.</p>
<dt><code>gauss</code></p>
<dd> Select Gaussian rescaling algorithm.</p>
<dt><code>sinc</code></p>
<dd> Select sinc rescaling algorithm.</p>
<dt><code>lanczos</code></p>
<dd> Select Lanczos rescaling algorithm. The default width (alpha) is 3 and can be changed by setting <tt>&quot;param0&quot;</tt>.</p>
<dt><code>spline</code></p>
<dd> Select natural bicubic spline rescaling algorithm.</p>
<dt><code>print_info</code></p>
<dd> Enable printing/debug logging.</p>
<dt><code>accurate_rnd</code></p>
<dd> Enable accurate rounding.</p>
<dt><code>full_chroma_int</code></p>
<dd> Enable full chroma interpolation.</p>
<dt><code>full_chroma_inp</code></p>
<dd> Select full chroma input.</p>
<dt><code>bitexact</code></p>
<dd> Enable bitexact output.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>srcw</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></p>
<dd> Set source width.</p>
<dt><code>srch</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></p>
<dd> Set source height.</p>
<dt><code>dstw</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></p>
<dd> Set destination width.</p>
<dt><code>dsth</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></p>
<dd> Set destination height.</p>
<dt><code>src_format</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></p>
<dd> Set source pixel format (must be expressed as an integer).</p>
<dt><code>dst_format</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></p>
<dd> Set destination pixel format (must be expressed as an integer).</p>
<dt><code>src_range</code> <i>(boolean)</i></p>
<dd> If value is set to <tt>1</tt>, indicates source is full range. Default value is <tt>0</tt>, which indicates source is limited range.</p>
<dt><code>dst_range</code> <i>(boolean)</i></p>
<dd> If value is set to <tt>1</tt>, enable full range for destination. Default value is <tt>0</tt>, which enables limited range.</p>
<dt><code>param0, param1</code></p>
<dd> Set scaling algorithm parameters. The specified values are specific of some scaling algorithms and ignored by others. The specified values are floating point number values.</p>
<dt><code>sws_dither</code></p>
<dd> Set the dithering algorithm. Accepts one of the following values. Default value is <code>auto</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> automatic choice</p>
<dt><code>none</code></p>
<dd> no dithering</p>
<dt><code>bayer</code></p>
<dd> bayer dither</p>
<dt><code>ed</code></p>
<dd> error diffusion dither</p>
<dt><code>a_dither</code></p>
<dd> arithmetic dither, based using addition</p>
<dt><code>x_dither</code></p>
<dd> arithmetic dither, based using xor (more random/less apparent patterning that a_dither).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>alphablend</code></p>
<dd> Set the alpha blending to use when the input has alpha but the output does not. Default value is <code>none</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>uniform_color</code></p>
<dd> Blend onto a uniform background color</p>
<dt><code>checkerboard</code></p>
<dd> Blend onto a checkerboard</p>
<dt><code>none</code></p>
<dd> No blending</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libswscale/">libswscale</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
