---

title: "ffmpeg-scaler(1)"
name: "ffmpeg-scaler"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-scaler/"
description: "ffmpeg-scaler – FFmpeg video scaling and pixel format converter"
---

<p> The FFmpeg rescaler provides a high-level interface to the libswscale library image conversion utilities. In particular it allows one to perform image rescaling and pixel format conversion.</p>
<h2>SCALER OPTIONS</h2>
<p> The video scaler supports the following named options. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, with a few API-only exceptions noted below. For programmatic use, they can be set explicitly in the <tt>&quot;SwsContext&quot;</tt> options or through the <i>libavutil/opt.h</i> <font SIZE="-1">API.</font></p>
<dl>
<dt><code>sws_flags</code></dt>
<dd> Set the scaler flags. This is also used to set the scaling algorithm. Only a single algorithm should be selected. Default value is <code>bicubic</code>. </dd>
<p> It accepts the following values:</p>
<dl>
<dl>
<dt><code>fast_bilinear</code></dt>
<dd> Select fast bilinear scaling algorithm.</dd>
<dt><code>bilinear</code></dt>
<dd> Select bilinear scaling algorithm.</dd>
<dt><code>bicubic</code></dt>
<dd> Select bicubic scaling algorithm.</dd>
<dt><code>experimental</code></dt>
<dd> Select experimental scaling algorithm.</dd>
<dt><code>neighbor</code></dt>
<dd> Select nearest neighbor rescaling algorithm.</dd>
<dt><code>area</code></dt>
<dd> Select averaging area rescaling algorithm.</dd>
<dt><code>bicublin</code></dt>
<dd> Select bicubic scaling algorithm for the luma component, bilinear for chroma components.</dd>
<dt><code>gauss</code></dt>
<dd> Select Gaussian rescaling algorithm.</dd>
<dt><code>sinc</code></dt>
<dd> Select sinc rescaling algorithm.</dd>
<dt><code>lanczos</code></dt>
<dd> Select Lanczos rescaling algorithm. The default width (alpha) is 3 and can be changed by setting <tt>&quot;param0&quot;</tt>.</dd>
<dt><code>spline</code></dt>
<dd> Select natural bicubic spline rescaling algorithm.</dd>
<dt><code>print_info</code></dt>
<dd> Enable printing/debug logging.</dd>
<dt><code>accurate_rnd</code></dt>
<dd> Enable accurate rounding.</dd>
<dt><code>full_chroma_int</code></dt>
<dd> Enable full chroma interpolation.</dd>
<dt><code>full_chroma_inp</code></dt>
<dd> Select full chroma input.</dd>
<dt><code>bitexact</code></dt>
<dd> Enable bitexact output.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>srcw</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></dt>
<dd> Set source width.</dd>
<dt><code>srch</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></dt>
<dd> Set source height.</dd>
<dt><code>dstw</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></dt>
<dd> Set destination width.</dd>
<dt><code>dsth</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></dt>
<dd> Set destination height.</dd>
<dt><code>src_format</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></dt>
<dd> Set source pixel format (must be expressed as an integer).</dd>
<dt><code>dst_format</code> <i>(</i><font SIZE="-1"><i>API</i></font><i> only)</i></dt>
<dd> Set destination pixel format (must be expressed as an integer).</dd>
<dt><code>src_range</code> <i>(boolean)</i></dt>
<dd> If value is set to <tt>1</tt>, indicates source is full range. Default value is <tt>0</tt>, which indicates source is limited range.</dd>
<dt><code>dst_range</code> <i>(boolean)</i></dt>
<dd> If value is set to <tt>1</tt>, enable full range for destination. Default value is <tt>0</tt>, which enables limited range.</dd>
<dt><code>param0, param1</code></dt>
<dd> Set scaling algorithm parameters. The specified values are specific of some scaling algorithms and ignored by others. The specified values are floating point number values.</dd>
<dt><code>sws_dither</code></dt>
<dd> Set the dithering algorithm. Accepts one of the following values. Default value is <code>auto</code>.</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> automatic choice</dd>
<dt><code>none</code></dt>
<dd> no dithering</dd>
<dt><code>bayer</code></dt>
<dd> bayer dither</dd>
<dt><code>ed</code></dt>
<dd> error diffusion dither</dd>
<dt><code>a_dither</code></dt>
<dd> arithmetic dither, based using addition</dd>
<dt><code>x_dither</code></dt>
<dd> arithmetic dither, based using xor (more random/less apparent patterning that a_dither).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>alphablend</code></dt>
<dd> Set the alpha blending to use when the input has alpha but the output does not. Default value is <code>none</code>.</dd>
<dl>
<dl>
<dt><code>uniform_color</code></dt>
<dd> Blend onto a uniform background color</dd>
<dt><code>checkerboard</code></dt>
<dd> Blend onto a checkerboard</dd>
<dt><code>none</code></dt>
<dd> No blending</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libswscale/">libswscale</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
