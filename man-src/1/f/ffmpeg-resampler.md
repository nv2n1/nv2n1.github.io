---
title: "ffmpeg-resampler(1)"
name: "ffmpeg-resampler"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-resampler/"
description: "ffmpeg-resampler – FFmpeg Resampler"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-resampler &#8211; FFmpeg Resampler </p>
<h2>DESCRIPTION</h2>
<p> The FFmpeg resampler provides a high-level interface to the libswresample library audio resampling utilities. In particular it allows one to perform audio resampling, audio channel layout rematrixing, and convert audio format and packing layout.</p>
<h2>RESAMPLER OPTIONS</h2>
<p> The audio resampler supports the following named options. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, <i>option</i>=<i>value</i> for the aresample filter, by setting the value explicitly in the <tt>&quot;SwrContext&quot;</tt> options or using the <i>libavutil/opt.h</i> <font SIZE="-1">API</font> for programmatic use.</p>
<dl>
<dt><code>ich, in_channel_count</code></p>
<dd> Set the number of input channels. Default value is 0. Setting this value is not mandatory if the corresponding channel layout <code>in_channel_layout</code> is set.</p>
<dt><code>och, out_channel_count</code></p>
<dd> Set the number of output channels. Default value is 0. Setting this value is not mandatory if the corresponding channel layout <code>out_channel_layout</code> is set.</p>
<dt><code>uch, used_channel_count</code></p>
<dd> Set the number of used input channels. Default value is 0. This option is only used for special remapping.</p>
<dt><code>isr, in_sample_rate</code></p>
<dd> Set the input sample rate. Default value is 0.</p>
<dt><code>osr, out_sample_rate</code></p>
<dd> Set the output sample rate. Default value is 0.</p>
<dt><code>isf, in_sample_fmt</code></p>
<dd> Specify the input sample format. It is set by default to <tt>&quot;none&quot;</tt>.</p>
<dt><code>osf, out_sample_fmt</code></p>
<dd> Specify the output sample format. It is set by default to <tt>&quot;none&quot;</tt>.</p>
<dt><code>tsf, internal_sample_fmt</code></p>
<dd> Set the internal sample format. Default value is <tt>&quot;none&quot;</tt>. This will automatically be chosen when it is not explicitly set.</p>
<dt><code>icl, in_channel_layout</code></p>
<dd>
<dt><code>ocl, out_channel_layout</code></p>
<dd> Set the input/output channel layout. </p>
<p> See <code>the Channel Layout section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code> for the required syntax.</p>
<dt><code>clev, center_mix_level</code></p>
<dd> Set the center mix level. It is a value expressed in deciBel, and must be in the interval [-32,32].</p>
<dt><code>slev, surround_mix_level</code></p>
<dd> Set the surround mix level. It is a value expressed in deciBel, and must be in the interval [-32,32].</p>
<dt><code>lfe_mix_level</code></p>
<dd> Set <font SIZE="-1">LFE</font> mix into non <font SIZE="-1">LFE</font> level. It is used when there is a <font SIZE="-1">LFE</font> input but no <font SIZE="-1">LFE</font> output. It is a value expressed in deciBel, and must be in the interval [-32,32].</p>
<dt><code>rmvol, rematrix_volume</code></p>
<dd> Set rematrix volume. Default value is 1.0.</p>
<dt><code>rematrix_maxval</code></p>
<dd> Set maximum output value for rematrixing. This can be used to prevent clipping vs. preventing volume reduction. A value of 1.0 prevents clipping.</p>
<dt><code>flags, swr_flags</code></p>
<dd> Set flags used by the converter. Default value is 0. </p>
<p> It supports the following individual flags:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>res</code></p>
<dd> force resampling, this flag forces resampling to be used even when the input and output sample rates match.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>dither_scale</code></p>
<dd> Set the dither scale. Default value is 1.</p>
<dt><code>dither_method</code></p>
<dd> Set dither method. Default value is 0. </p>
<p> Supported values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>rectangular</code></p>
<dd> select rectangular dither</p>
<dt><code>triangular</code></p>
<dd> select triangular dither</p>
<dt><code>triangular_hp</code></p>
<dd> select triangular dither with high pass</p>
<dt><code>lipshitz</code></p>
<dd> select Lipshitz noise shaping dither.</p>
<dt><code>shibata</code></p>
<dd> select Shibata noise shaping dither.</p>
<dt><code>low_shibata</code></p>
<dd> select low Shibata noise shaping dither.</p>
<dt><code>high_shibata</code></p>
<dd> select high Shibata noise shaping dither.</p>
<dt><code>f_weighted</code></p>
<dd> select f-weighted noise shaping dither</p>
<dt><code>modified_e_weighted</code></p>
<dd> select modified-e-weighted noise shaping dither</p>
<dt><code>improved_e_weighted</code></p>
<dd> select improved-e-weighted noise shaping dither</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>resampler</code></p>
<dd> Set resampling engine. Default value is swr. </p>
<p> Supported values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>swr</code></p>
<dd> select the native <font SIZE="-1">SW</font> Resampler; filter options precision and cheby are not applicable in this case.</p>
<dt><code>soxr</code></p>
<dd> select the SoX Resampler (where available); compensation, and filter options filter_size, phase_shift, exact_rational, filter_type &amp; kaiser_beta, are not applicable in this case.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>filter_size</code></p>
<dd> For swr only, set resampling filter size, default value is 32.</p>
<dt><code>phase_shift</code></p>
<dd> For swr only, set resampling phase shift, default value is 10, and must be in the interval [0,30].</p>
<dt><code>linear_interp</code></p>
<dd> Use linear interpolation when enabled (the default). Disable it if you want to preserve speed instead of quality when exact_rational fails.</p>
<dt><code>exact_rational</code></p>
<dd> For swr only, when enabled, try to use exact phase_count based on input and output sample rate. However, if it is larger than <tt>&quot;1 &lt;&lt; phase_shift&quot;</tt>, the phase_count will be <tt>&quot;1 &lt;&lt; phase_shift&quot;</tt> as fallback. Default is enabled.</p>
<dt><code>cutoff</code></p>
<dd> Set cutoff frequency (swr: 6dB point; soxr: 0dB point) ratio; must be a float value between 0 and 1. Default value is 0.97 with swr, and 0.91 with soxr (which, with a sample-rate of 44100, preserves the entire audio band to 20kHz).</p>
<dt><code>precision</code></p>
<dd> For soxr only, the precision in bits to which the resampled signal will be calculated. The default value of 20 (which, with suitable dithering, is appropriate for a destination bit-depth of 16) gives SoX&#8217;s &#8216;High Quality&#8217;; a value of 28 gives SoX&#8217;s &#8216;Very High Quality&#8217;.</p>
<dt><code>cheby</code></p>
<dd> For soxr only, selects passband rolloff none (Chebyshev) &amp; higher-precision approximation for &#8216;irrational&#8217; ratios. Default value is 0.</p>
<dt><code>async</code></p>
<dd> For swr only, simple 1 parameter audio sync to timestamps using stretching, squeezing, filling and trimming. Setting this to 1 will enable filling and trimming, larger values represent the maximum amount in samples that the data may be stretched or squeezed for each second. Default value is 0, thus no compensation is applied to make the samples match the audio timestamps.</p>
<dt><code>first_pts</code></p>
<dd> For swr only, assume the first pts should be this value. The time unit is 1 / sample rate. This allows for padding/trimming at the start of stream. By default, no assumption is made about the first frame&#8217;s expected pts, so no padding or trimming is done. For example, this could be set to 0 to pad the beginning with silence if an audio stream starts after the video stream or to trim any samples with a negative pts due to encoder delay.</p>
<dt><code>min_comp</code></p>
<dd> For swr only, set the minimum difference between timestamps and audio data (in seconds) to trigger stretching/squeezing/filling or trimming of the data to make it match the timestamps. The default is that stretching/squeezing/filling and trimming is disabled (<code>min_comp</code> = <tt>&quot;FLT_MAX&quot;</tt>).</p>
<dt><code>min_hard_comp</code></p>
<dd> For swr only, set the minimum difference between timestamps and audio data (in seconds) to trigger adding/dropping samples to make it match the timestamps. This option effectively is a threshold to select between hard (trim/fill) and soft (squeeze/stretch) compensation. Note that all compensation is by default disabled through <code>min_comp</code>. The default is 0.1.</p>
<dt><code>comp_duration</code></p>
<dd> For swr only, set duration (in seconds) over which data is stretched/squeezed to make it match the timestamps. Must be a non-negative double float value, default value is 1.0.</p>
<dt><code>max_soft_comp</code></p>
<dd> For swr only, set maximum factor by which data is stretched/squeezed to make it match the timestamps. Must be a non-negative double float value, default value is 0.</p>
<dt><code>matrix_encoding</code></p>
<dd> Select matrixed stereo encoding. </p>
<p> It accepts the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> select none</p>
<dt><code>dolby</code></p>
<dd> select Dolby</p>
<dt><code>dplii</code></p>
<dd> select Dolby Pro Logic <font SIZE="-1">II</font></dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <tt>&quot;none&quot;</tt>.</dl>
<dt><code>filter_type</code></p>
<dd> For swr only, select resampling filter type. This only affects resampling operations. </p>
<p> It accepts the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cubic</code></p>
<dd> select cubic</p>
<dt><code>blackman_nuttall</code></p>
<dd> select Blackman Nuttall windowed sinc</p>
<dt><code>kaiser</code></p>
<dd> select Kaiser windowed sinc</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>kaiser_beta</code></p>
<dd> For swr only, set Kaiser window beta value. Must be a double float value in the interval [2,16], default value is 9.</p>
<dt><code>output_sample_bits</code></p>
<dd> For swr only, set number of used output sample bits for dithering. Must be an integer in the interval [0,64], default value is 0, which means it&#8217;s not used.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libswresample/">libswresample</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
