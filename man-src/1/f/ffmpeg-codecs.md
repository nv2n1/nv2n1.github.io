---

title: "ffmpeg-codecs(1)"
name: "ffmpeg-codecs"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-codecs/"
description: "ffmpeg-codecs – FFmpeg codecs"
---

<p> ffmpeg-codecs &#8211; FFmpeg codecs </p>
<h2>DESCRIPTION</h2>
<p> This document describes the codecs (decoders and encoders) provided by the libavcodec library.</p>
<h2>CODEC OPTIONS</h2>
<p> libavcodec provides some generic global options, which can be set on all the encoders and decoders. In addition each codec may support so-called private options, which are specific for a given codec. </p>
<p> Sometimes, a global option may only affect a specific kind of codec, and may be nonsensical or ignored by another, so you need to be aware of the meaning of the specified options. Also some options are meant only for decoding or encoding. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, or by setting the value explicitly in the <tt>&quot;AVCodecContext&quot;</tt> options or using the <i>libavutil/opt.h</i> API for programmatic use. </p>
<p> The list of supported options follow:</p>
<dl>
<dt><code>b</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Set bitrate in bits/s. Default value is 200K.</dd>
<dt><code>ab</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></dt>
<dd> Set audio bitrate (in bits/s). Default value is 128K.</dd>
<dt><code>bt</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to min/max bitrate. Lowering tolerance too much has an adverse effect on quality.</dd>
<dt><code>flags</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></dt>
<dd> Set generic flags. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>mv4</code></dt>
<dd> Use four motion vector by macroblock (mpeg4).</dd>
<dt><code>qpel</code></dt>
<dd> Use 1/4 pel motion compensation.</dd>
<dt><code>loop</code></dt>
<dd> Use loop filter.</dd>
<dt><code>qscale</code></dt>
<dd> Use fixed qscale.</dd>
<dt><code>pass1</code></dt>
<dd> Use internal 2pass ratecontrol in first pass mode.</dd>
<dt><code>pass2</code></dt>
<dd> Use internal 2pass ratecontrol in second pass mode.</dd>
<dt><code>gray</code></dt>
<dd> Only decode/encode grayscale.</dd>
<dt><code>psnr</code></dt>
<dd> Set error[?] variables during encoding.</dd>
<dt><code>truncated</code></dt>
<dd> Input bitstream might be randomly truncated.</dd>
<dt><code>drop_changed</code></dt>
<dd> Don&#8217;t output frames whose parameters differ from first decoded frame in stream. Error AVERROR_INPUT_CHANGED is returned when a frame is dropped.</dd>
<dt><code>ildct</code></dt>
<dd> Use interlaced DCT.</dd>
<dt><code>low_delay</code></dt>
<dd> Force low delay.</dd>
<dt><code>global_header</code></dt>
<dd> Place global headers in extradata instead of every keyframe.</dd>
<dt><code>bitexact</code></dt>
<dd> Only write platform-, build- and time-independent data. (except (I)DCT). This ensures that file and data checksums are reproducible and match between platforms. Its primary use is for regression testing.</dd>
<dt><code>aic</code></dt>
<dd> Apply H263 advanced intra coding / mpeg4 ac prediction.</dd>
<dt><code>ilme</code></dt>
<dd> Apply interlaced motion estimation.</dd>
<dt><code>cgop</code></dt>
<dd> Use closed gop.</dd>
<dt><code>output_corrupt</code></dt>
<dd> Output even potentially corrupted frames.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>time_base</code> <i>rational number</i></dt>
<dd> Set codec time base. </dd>
<p> It is the fundamental unit of time (in seconds) in terms of which frame timestamps are represented. For fixed-fps content, timebase should be <tt>&quot;1 / frame_rate&quot;</tt> and timestamp increments should be identically 1.</p>
<dt><code>g</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set the group of picture (GOP) size. Default value is 12.</dd>
<dt><code>ar</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio</i><code>)</code></dt>
<dd> Set audio sampling rate (in Hz).</dd>
<dt><code>ac</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio</i><code>)</code></dt>
<dd> Set number of audio channels.</dd>
<dt><code>cutoff</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></dt>
<dd> Set cutoff bandwidth. (Supported only by selected encoders, see their respective documentation sections.)</dd>
<dt><code>frame_size</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></dt>
<dd> Set audio frame size. </dd>
<p> Each submitted frame except the last must contain exactly frame_size samples per channel. May be 0 when the codec has CODEC_CAP_VARIABLE_FRAME_SIZE set, in that case the frame size is not restricted. It is set by some decoders to indicate constant frame size.</p>
<dt><code>frame_number</code> <i>integer</i></dt>
<dd> Set the frame number.</dd>
<dt><code>delay</code> <i>integer</i></dt>
<dd>
</dd><dt><code>qcomp</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set video quantizer scale compression (VBR). It is used as a constant in the ratecontrol equation. Recommended range for default rc_eq: 0.0-1.0.</dd>
<dt><code>qblur</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set video quantizer scale blur (VBR).</dd>
<dt><code>qmin</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set min video quantizer scale (VBR). Must be included between -1 and 69, default value is 2.</dd>
<dt><code>qmax</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set max video quantizer scale (VBR). Must be included between -1 and 1024, default value is 31.</dd>
<dt><code>qdiff</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set max difference between the quantizer scale (VBR).</dd>
<dt><code>bf</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set max number of B frames between non-B-frames. </dd>
<p> Must be an integer between -1 and 16. 0 means that B-frames are disabled. If a value of -1 is used, it will choose an automatic value depending on the encoder. </p>
<p> Default value is 0.</p>
<dt><code>b_qfactor</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set qp factor between P and B frames.</dd>
<dt><code>b_strategy</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set strategy to choose between I/P/B-frames.</dd>
<dt><code>ps</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set RTP payload size in bytes.</dd>
<dt><code>mv_bits</code> <i>integer</i></dt>
<dd>
</dd><dt><code>header_bits</code> <i>integer</i></dt>
<dd>
</dd><dt><code>i_tex_bits</code> <i>integer</i></dt>
<dd>
</dd><dt><code>p_tex_bits</code> <i>integer</i></dt>
<dd>
</dd><dt><code>i_count</code> <i>integer</i></dt>
<dd>
</dd><dt><code>p_count</code> <i>integer</i></dt>
<dd>
</dd><dt><code>skip_count</code> <i>integer</i></dt>
<dd>
</dd><dt><code>misc_bits</code> <i>integer</i></dt>
<dd>
</dd><dt><code>frame_bits</code> <i>integer</i></dt>
<dd>
</dd><dt><code>codec_tag</code> <i>integer</i></dt>
<dd>
</dd><dt><code>bug</code> <i>flags</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Workaround not auto detected encoder bugs. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>autodetect</code></dt>
<dd>
</dd><dt><code>xvid_ilace</code></dt>
<dd> Xvid interlacing bug (autodetected if fourcc==XVIX)</dd>
<dt><code>ump4</code></dt>
<dd> (autodetected if fourcc==UMP4)</dd>
<dt><code>no_padding</code></dt>
<dd> padding bug (autodetected)</dd>
<dt><code>amv</code></dt>
<dd>
</dd><dt><code>qpel_chroma</code></dt>
<dd>
</dd><dt><code>std_qpel</code></dt>
<dd> old standard qpel (autodetected per fourcc/version)</dd>
<dt><code>qpel_chroma2</code></dt>
<dd>
</dd><dt><code>direct_blocksize</code></dt>
<dd> direct-qpel-blocksize bug (autodetected per fourcc/version)</dd>
<dt><code>edge</code></dt>
<dd> edge padding bug (autodetected per fourcc/version)</dd>
<dt><code>hpel_chroma</code></dt>
<dd>
</dd><dt><code>dc_clip</code></dt>
<dd>
</dd><dt><code>ms</code></dt>
<dd> Workaround various bugs in microsoft broken decoders.</dd>
<dt><code>trunc</code></dt>
<dd> trancated frames</dd></dl>
</dl>
<dl>
</dl>
<dt><code>strict</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio,video</i><code>)</code></dt>
<dd> Specify how strictly to follow the standards. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>very</code></dt>
<dd> strictly conform to an older more strict version of the spec or reference software</dd>
<dt><code>strict</code></dt>
<dd> strictly conform to all the things in the spec no matter what consequences</dd>
<dt><code>normal</code></dt>
<dd>
</dd><dt><code>unofficial</code></dt>
<dd> allow unofficial extensions</dd>
<dt><code>experimental</code></dt>
<dd> allow non standardized experimental things, experimental (unfinished/work in progress/not well tested) decoders and encoders. Note: experimental decoders can pose a security risk, do not use this for decoding untrusted input.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>b_qoffset</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set QP offset between P and B frames.</dd>
<dt><code>err_detect</code> <i>flags</i> <code>(</code><i>decoding,audio,video</i><code>)</code></dt>
<dd> Set error detection flags. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>crccheck</code></dt>
<dd> verify embedded CRCs</dd>
<dt><code>bitstream</code></dt>
<dd> detect bitstream specification deviations</dd>
<dt><code>buffer</code></dt>
<dd> detect improper bitstream length</dd>
<dt><code>explode</code></dt>
<dd> abort decoding on minor error detection</dd>
<dt><code>ignore_err</code></dt>
<dd> ignore decoding errors, and continue decoding. This is useful if you want to analyze the content of a video and thus want everything to be decoded no matter what. This option will not result in a video that is pleasing to watch in case of errors.</dd>
<dt><code>careful</code></dt>
<dd> consider things that violate the spec and have not been seen in the wild as errors</dd>
<dt><code>compliant</code></dt>
<dd> consider all spec non compliancies as errors</dd>
<dt><code>aggressive</code></dt>
<dd> consider things that a sane encoder should not do as an error</dd></dl>
</dl>
<dl>
</dl>
<dt><code>has_b_frames</code> <i>integer</i></dt>
<dd>
</dd><dt><code>block_align</code> <i>integer</i></dt>
<dd>
</dd><dt><code>mpeg_quant</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Use MPEG quantizers instead of H.263.</dd>
<dt><code>rc_override_count</code> <i>integer</i></dt>
<dd>
</dd><dt><code>maxrate</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Set max bitrate tolerance (in bits/s). Requires bufsize to be set.</dd>
<dt><code>minrate</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Set min bitrate tolerance (in bits/s). Most useful in setting up a CBR encode. It is of little use elsewise.</dd>
<dt><code>bufsize</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Set ratecontrol buffer size (in bits).</dd>
<dt><code>i_qfactor</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set QP factor between P and I frames.</dd>
<dt><code>i_qoffset</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set QP offset between P and I frames.</dd>
<dt><code>dct</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set DCT algorithm. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> autoselect a good one (default)</dd>
<dt><code>fastint</code></dt>
<dd> fast integer</dd>
<dt><code>int</code></dt>
<dd> accurate integer</dd>
<dt><code>mmx</code></dt>
<dd>
</dd><dt><code>altivec</code></dt>
<dd>
</dd><dt><code>faan</code></dt>
<dd> floating point AAN DCT</dd></dl>
</dl>
<dl>
</dl>
<dt><code>lumi_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Compress bright areas stronger than medium ones.</dd>
<dt><code>tcplx_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set temporal complexity masking.</dd>
<dt><code>scplx_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set spatial complexity masking.</dd>
<dt><code>p_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set inter masking.</dd>
<dt><code>dark_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Compress dark areas stronger than medium ones.</dd>
<dt><code>idct</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Select IDCT implementation. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd>
</dd><dt><code>int</code></dt>
<dd>
</dd><dt><code>simple</code></dt>
<dd>
</dd><dt><code>simplemmx</code></dt>
<dd>
</dd><dt><code>simpleauto</code></dt>
<dd> Automatically pick a IDCT compatible with the simple one</dd>
<dt><code>arm</code></dt>
<dd>
</dd><dt><code>altivec</code></dt>
<dd>
</dd><dt><code>sh4</code></dt>
<dd>
</dd><dt><code>simplearm</code></dt>
<dd>
</dd><dt><code>simplearmv5te</code></dt>
<dd>
</dd><dt><code>simplearmv6</code></dt>
<dd>
</dd><dt><code>simpleneon</code></dt>
<dd>
</dd><dt><code>xvid</code></dt>
<dd>
</dd><dt><code>faani</code></dt>
<dd> floating point AAN IDCT</dd></dl>
</dl>
<dl>
</dl>
<dt><code>slice_count</code> <i>integer</i></dt>
<dd>
</dd><dt><code>ec</code> <i>flags</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Set error concealment strategy. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>guess_mvs</code></dt>
<dd> iterative motion vector (MV) search (slow)</dd>
<dt><code>deblock</code></dt>
<dd> use strong deblock filter for damaged MBs</dd>
<dt><code>favor_inter</code></dt>
<dd> favor predicting from the previous frame instead of the current</dd></dl>
</dl>
<dl>
</dl>
<dt><code>bits_per_coded_sample</code> <i>integer</i></dt>
<dd>
</dd><dt><code>pred</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set prediction method. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>left</code></dt>
<dd>
</dd><dt><code>plane</code></dt>
<dd>
</dd><dt><code>median</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>aspect</code> <i>rational number</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set sample aspect ratio.</dd>
<dt><code>sar</code> <i>rational number</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set sample aspect ratio. Alias to <i>aspect</i>.</dd>
<dt><code>debug</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></dt>
<dd> Print specific debug info. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>pict</code></dt>
<dd> picture info</dd>
<dt><code>rc</code></dt>
<dd> rate control</dd>
<dt><code>bitstream</code></dt>
<dd>
</dd><dt><code>mb_type</code></dt>
<dd> macroblock (MB) type</dd>
<dt><code>qp</code></dt>
<dd> per-block quantization parameter (QP)</dd>
<dt><code>dct_coeff</code></dt>
<dd>
</dd><dt><code>green_metadata</code></dt>
<dd> display complexity metadata for the upcoming frame, GoP or for a given duration.</dd>
<dt><code>skip</code></dt>
<dd>
</dd><dt><code>startcode</code></dt>
<dd>
</dd><dt><code>er</code></dt>
<dd> error recognition</dd>
<dt><code>mmco</code></dt>
<dd> memory management control operations (H.264)</dd>
<dt><code>bugs</code></dt>
<dd>
</dd><dt><code>buffers</code></dt>
<dd> picture buffer allocations</dd>
<dt><code>thread_ops</code></dt>
<dd> threading operations</dd>
<dt><code>nomc</code></dt>
<dd> skip motion compensation</dd></dl>
</dl>
<dl>
</dl>
<dt><code>cmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set full pel me compare function. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>sad</code></dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt><code>sse</code></dt>
<dd> sum of squared errors</dd>
<dt><code>satd</code></dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt><code>dct</code></dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt><code>psnr</code></dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt><code>bit</code></dt>
<dd> number of bits needed for the block</dd>
<dt><code>rd</code></dt>
<dd> rate distortion optimal, slow</dd>
<dt><code>zero</code></dt>
<dd> 0</dd>
<dt><code>vsad</code></dt>
<dd> sum of absolute vertical differences</dd>
<dt><code>vsse</code></dt>
<dd> sum of squared vertical differences</dd>
<dt><code>nsse</code></dt>
<dd> noise preserving sum of squared differences</dd>
<dt><code>w53</code></dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt><code>w97</code></dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt><code>dctmax</code></dt>
<dd>
</dd><dt><code>chroma</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>subcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set sub pel me compare function. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>sad</code></dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt><code>sse</code></dt>
<dd> sum of squared errors</dd>
<dt><code>satd</code></dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt><code>dct</code></dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt><code>psnr</code></dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt><code>bit</code></dt>
<dd> number of bits needed for the block</dd>
<dt><code>rd</code></dt>
<dd> rate distortion optimal, slow</dd>
<dt><code>zero</code></dt>
<dd> 0</dd>
<dt><code>vsad</code></dt>
<dd> sum of absolute vertical differences</dd>
<dt><code>vsse</code></dt>
<dd> sum of squared vertical differences</dd>
<dt><code>nsse</code></dt>
<dd> noise preserving sum of squared differences</dd>
<dt><code>w53</code></dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt><code>w97</code></dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt><code>dctmax</code></dt>
<dd>
</dd><dt><code>chroma</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>mbcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set macroblock compare function. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>sad</code></dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt><code>sse</code></dt>
<dd> sum of squared errors</dd>
<dt><code>satd</code></dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt><code>dct</code></dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt><code>psnr</code></dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt><code>bit</code></dt>
<dd> number of bits needed for the block</dd>
<dt><code>rd</code></dt>
<dd> rate distortion optimal, slow</dd>
<dt><code>zero</code></dt>
<dd> 0</dd>
<dt><code>vsad</code></dt>
<dd> sum of absolute vertical differences</dd>
<dt><code>vsse</code></dt>
<dd> sum of squared vertical differences</dd>
<dt><code>nsse</code></dt>
<dd> noise preserving sum of squared differences</dd>
<dt><code>w53</code></dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt><code>w97</code></dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt><code>dctmax</code></dt>
<dd>
</dd><dt><code>chroma</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>ildctcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set interlaced dct compare function. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>sad</code></dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt><code>sse</code></dt>
<dd> sum of squared errors</dd>
<dt><code>satd</code></dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt><code>dct</code></dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt><code>psnr</code></dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt><code>bit</code></dt>
<dd> number of bits needed for the block</dd>
<dt><code>rd</code></dt>
<dd> rate distortion optimal, slow</dd>
<dt><code>zero</code></dt>
<dd> 0</dd>
<dt><code>vsad</code></dt>
<dd> sum of absolute vertical differences</dd>
<dt><code>vsse</code></dt>
<dd> sum of squared vertical differences</dd>
<dt><code>nsse</code></dt>
<dd> noise preserving sum of squared differences</dd>
<dt><code>w53</code></dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt><code>w97</code></dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt><code>dctmax</code></dt>
<dd>
</dd><dt><code>chroma</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>dia_size</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set diamond type &amp; size for motion estimation.</dd>
<dl>
<dl>
<dt><code>(1024, </code><code>INT_MAX</code><code>)</code></dt>
<dd> full motion estimation(slowest)</dd>
<dt><code>(768, 1024]</code></dt>
<dd> umh motion estimation</dd>
<dt><code>(512, 768]</code></dt>
<dd> hex motion estimation</dd>
<dt><code>(256, 512]</code></dt>
<dd> l2s diamond motion estimation</dd>
<dt><code>[2,256]</code></dt>
<dd> var diamond motion estimation</dd>
<dt><code>(-1, 2)</code></dt>
<dd> small diamond motion estimation</dd>
<dt><code>-1</code></dt>
<dd> funny diamond motion estimation</dd>
<dt><code>(</code><code>INT_MIN,</code><code> -1)</code></dt>
<dd> sab diamond motion estimation</dd></dl>
</dl>
<dl>
</dl>
<dt><code>last_pred</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set amount of motion predictors from the previous frame.</dd>
<dt><code>preme</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set pre motion estimation.</dd>
<dt><code>precmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set pre motion estimation compare function. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>sad</code></dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt><code>sse</code></dt>
<dd> sum of squared errors</dd>
<dt><code>satd</code></dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt><code>dct</code></dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt><code>psnr</code></dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt><code>bit</code></dt>
<dd> number of bits needed for the block</dd>
<dt><code>rd</code></dt>
<dd> rate distortion optimal, slow</dd>
<dt><code>zero</code></dt>
<dd> 0</dd>
<dt><code>vsad</code></dt>
<dd> sum of absolute vertical differences</dd>
<dt><code>vsse</code></dt>
<dd> sum of squared vertical differences</dd>
<dt><code>nsse</code></dt>
<dd> noise preserving sum of squared differences</dd>
<dt><code>w53</code></dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt><code>w97</code></dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt><code>dctmax</code></dt>
<dd>
</dd><dt><code>chroma</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>pre_dia_size</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set diamond type &amp; size for motion estimation pre-pass.</dd>
<dt><code>subq</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set sub pel motion estimation quality.</dd>
<dt><code>me_range</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set limit motion vectors range (1023 for DivX player).</dd>
<dt><code>global_quality</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd>
</dd><dt><code>coder</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>vlc</code></dt>
<dd> variable length coder / huffman coder</dd>
<dt><code>ac</code></dt>
<dd> arithmetic coder</dd>
<dt><code>raw</code></dt>
<dd> raw (no encoding)</dd>
<dt><code>rle</code></dt>
<dd> run-length coder</dd></dl>
</dl>
<dl>
</dl>
<dt><code>context</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set context model.</dd>
<dt><code>slice_flags</code> <i>integer</i></dt>
<dd>
</dd><dt><code>mbd</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set macroblock decision algorithm (high quality mode). </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>simple</code></dt>
<dd> use mbcmp (default)</dd>
<dt><code>bits</code></dt>
<dd> use fewest bits</dd>
<dt><code>rd</code></dt>
<dd> use best rate distortion</dd></dl>
</dl>
<dl>
</dl>
<dt><code>sc_threshold</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set scene change threshold.</dd>
<dt><code>nr</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set noise reduction.</dd>
<dt><code>rc_init_occupancy</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set number of bits which should be loaded into the rc buffer before decoding starts.</dd>
<dt><code>flags2</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>fast</code></dt>
<dd> Allow non spec compliant speedup tricks.</dd>
<dt><code>noout</code></dt>
<dd> Skip bitstream encoding.</dd>
<dt><code>ignorecrop</code></dt>
<dd> Ignore cropping information from sps.</dd>
<dt><code>local_header</code></dt>
<dd> Place global headers at every keyframe instead of in extradata.</dd>
<dt><code>chunks</code></dt>
<dd> Frame data might be split into multiple chunks.</dd>
<dt><code>showall</code></dt>
<dd> Show all frames before the first keyframe.</dd>
<dt><code>export_mvs</code></dt>
<dd> Export motion vectors into frame side-data (see <tt>&quot;AV_FRAME_DATA_MOTION_VECTORS&quot;</tt>) for codecs that support it. See also <i>doc/examples/export_mvs.c</i>.</dd>
<dt><code>skip_manual</code></dt>
<dd> Do not skip samples and export skip information as frame side data.</dd>
<dt><code>ass_ro_flush_noop</code></dt>
<dd> Do not reset ASS ReadOrder field on flush.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>export_side_data</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>mvs</code></dt>
<dd> Export motion vectors into frame side-data (see <tt>&quot;AV_FRAME_DATA_MOTION_VECTORS&quot;</tt>) for codecs that support it. See also <i>doc/examples/export_mvs.c</i>.</dd>
<dt><code>prft</code></dt>
<dd> Export encoder Producer Reference Time into packet side-data (see <tt>&quot;AV_PKT_DATA_PRFT&quot;</tt>) for codecs that support it.</dd>
<dt><code>venc_params</code></dt>
<dd> Export video encoding parameters through frame side data (see <tt>&quot;AV_FRAME_DATA_VIDEO_ENC_PARAMS&quot;</tt>) for codecs that support it. At present, those are H.264 and VP9.</dd>
<dt><code>film_grain</code></dt>
<dd> Export film grain parameters through frame side data (see <tt>&quot;AV_FRAME_DATA_FILM_GRAIN_PARAMS&quot;</tt>). Supported at present by AV1 decoders.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>threads</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Set the number of threads to be used, in case the selected codec implementation supports multi-threading. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>auto, 0</code></dt>
<dd> automatically select the number of threads to set</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>auto</code>.</dd></dl>
<dt><code>dc</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set intra_dc_precision.</dd>
<dt><code>nssew</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set nsse weight.</dd>
<dt><code>skip_top</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Set number of macroblock rows at the top which are skipped.</dd>
<dt><code>skip_bottom</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Set number of macroblock rows at the bottom which are skipped.</dd>
<dt><code>profile</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Set encoder codec profile. Default value is <code>unknown</code>. Encoder specific profiles are documented in the relevant encoder documentation.</dd>
<dt><code>level</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>unknown</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>lowres</code> <i>integer</i> <code>(</code><i>decoding,audio,video</i><code>)</code></dt>
<dd> Decode at 1= 1/2, 2=1/4, 3=1/8 resolutions.</dd>
<dt><code>skip_threshold</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set frame skip threshold.</dd>
<dt><code>skip_factor</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set frame skip factor.</dd>
<dt><code>skip_exp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set frame skip exponent. Negative values behave identical to the corresponding positive ones, except that the score is normalized. Positive values exist primarily for compatibility reasons and are not so useful.</dd>
<dt><code>skipcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set frame skip compare function. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>sad</code></dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt><code>sse</code></dt>
<dd> sum of squared errors</dd>
<dt><code>satd</code></dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt><code>dct</code></dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt><code>psnr</code></dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt><code>bit</code></dt>
<dd> number of bits needed for the block</dd>
<dt><code>rd</code></dt>
<dd> rate distortion optimal, slow</dd>
<dt><code>zero</code></dt>
<dd> 0</dd>
<dt><code>vsad</code></dt>
<dd> sum of absolute vertical differences</dd>
<dt><code>vsse</code></dt>
<dd> sum of squared vertical differences</dd>
<dt><code>nsse</code></dt>
<dd> noise preserving sum of squared differences</dd>
<dt><code>w53</code></dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt><code>w97</code></dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt><code>dctmax</code></dt>
<dd>
</dd><dt><code>chroma</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>mblmin</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set min macroblock lagrange factor (VBR).</dd>
<dt><code>mblmax</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set max macroblock lagrange factor (VBR).</dd>
<dt><code>mepc</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set motion estimation bitrate penalty compensation (1.0 = 256).</dd>
<dt><code>skip_loop_filter</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd>
</dd><dt><code>skip_idct</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd>
</dd><dt><code>skip_frame</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Make decoder discard processing depending on the frame type selected by the option value. </dd>
<p> <code>skip_loop_filter</code> skips frame loop filtering, <code>skip_idct</code> skips frame IDCT/dequantization, <code>skip_frame</code> skips decoding. </p>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> Discard no frame.</dd>
<dt><code>default</code></dt>
<dd> Discard useless frames like 0-sized frames.</dd>
<dt><code>noref</code></dt>
<dd> Discard all non-reference frames.</dd>
<dt><code>bidir</code></dt>
<dd> Discard all bidirectional frames.</dd>
<dt><code>nokey</code></dt>
<dd> Discard all frames excepts keyframes.</dd>
<dt><code>nointra</code></dt>
<dd> Discard all frames except I frames.</dd>
<dt><code>all</code></dt>
<dd> Discard all frames.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>default</code>.</dd></dl>
<dt><code>bidir_refine</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Refine the two motion vectors used in bidirectional macroblocks.</dd>
<dt><code>brd_scale</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Downscale frames for dynamic B-frame decision.</dd>
<dt><code>keyint_min</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set minimum interval between IDR-frames.</dd>
<dt><code>refs</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set reference frames to consider for motion compensation.</dd>
<dt><code>chromaoffset</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set chroma qp offset from luma.</dd>
<dt><code>trellis</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd> Set rate-distortion optimal quantization.</dd>
<dt><code>mv0_threshold</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd>
</dd><dt><code>b_sensitivity</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Adjust sensitivity of b_frame_strategy 1.</dd>
<dt><code>compression_level</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></dt>
<dd>
</dd><dt><code>min_prediction_order</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></dt>
<dd>
</dd><dt><code>max_prediction_order</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></dt>
<dd>
</dd><dt><code>timecode_frame_start</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Set GOP timecode frame start number, in non drop frame format.</dd>
<dt><code>bits_per_raw_sample</code> <i>integer</i></dt>
<dd>
</dd><dt><code>channel_layout</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio</i><code>)</code></dt>
<dd> Possible values:</dd>
<dt><code>request_channel_layout</code> <i>integer</i> <code>(</code><i>decoding,audio</i><code>)</code></dt>
<dd> Possible values:</dd>
<dt><code>rc_max_vbv_use</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd>
</dd><dt><code>rc_min_vbv_use</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd>
</dd><dt><code>ticks_per_frame</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio,video</i><code>)</code></dt>
<dd>
</dd><dt><code>color_primaries</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>bt709</code></dt>
<dd> BT.709</dd>
<dt><code>bt470m</code></dt>
<dd> BT.470 M</dd>
<dt><code>bt470bg</code></dt>
<dd> BT.470 BG</dd>
<dt><code>smpte170m</code></dt>
<dd> SMPTE 170 M</dd>
<dt><code>smpte240m</code></dt>
<dd> SMPTE 240 M</dd>
<dt><code>film</code></dt>
<dd> Film</dd>
<dt><code>bt2020</code></dt>
<dd> BT.2020</dd>
<dt><code>smpte428</code></dt>
<dd>
</dd><dt><code>smpte428_1</code></dt>
<dd> SMPTE ST 428-1</dd>
<dt><code>smpte431</code></dt>
<dd> SMPTE 431-2</dd>
<dt><code>smpte432</code></dt>
<dd> SMPTE 432-1</dd>
<dt><code>jedec-p22</code></dt>
<dd> JEDEC P22</dd></dl>
</dl>
<dl>
</dl>
<dt><code>color_trc</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>bt709</code></dt>
<dd> BT.709</dd>
<dt><code>gamma22</code></dt>
<dd> BT.470 M</dd>
<dt><code>gamma28</code></dt>
<dd> BT.470 BG</dd>
<dt><code>smpte170m</code></dt>
<dd> SMPTE 170 M</dd>
<dt><code>smpte240m</code></dt>
<dd> SMPTE 240 M</dd>
<dt><code>linear</code></dt>
<dd> Linear</dd>
<dt><code>log</code></dt>
<dd>
</dd><dt><code>log100</code></dt>
<dd> Log</dd>
<dt><code>log_sqrt</code></dt>
<dd>
</dd><dt><code>log316</code></dt>
<dd> Log square root</dd>
<dt><code>iec61966_2_4</code></dt>
<dd>
</dd><dt><code>iec61966-2-4</code></dt>
<dd> IEC 61966-2-4</dd>
<dt><code>bt1361</code></dt>
<dd>
</dd><dt><code>bt1361e</code></dt>
<dd> BT.1361</dd>
<dt><code>iec61966_2_1</code></dt>
<dd>
</dd><dt><code>iec61966-2-1</code></dt>
<dd> IEC 61966-2-1</dd>
<dt><code>bt2020_10</code></dt>
<dd>
</dd><dt><code>bt2020_10bit</code></dt>
<dd> BT.2020 &#8211; 10 bit</dd>
<dt><code>bt2020_12</code></dt>
<dd>
</dd><dt><code>bt2020_12bit</code></dt>
<dd> BT.2020 &#8211; 12 bit</dd>
<dt><code>smpte2084</code></dt>
<dd> SMPTE ST 2084</dd>
<dt><code>smpte428</code></dt>
<dd>
</dd><dt><code>smpte428_1</code></dt>
<dd> SMPTE ST 428-1</dd>
<dt><code>arib-std-b67</code></dt>
<dd> ARIB STD-B67</dd></dl>
</dl>
<dl>
</dl>
<dt><code>colorspace</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>rgb</code></dt>
<dd> RGB</dd>
<dt><code>bt709</code></dt>
<dd> BT.709</dd>
<dt><code>fcc</code></dt>
<dd> FCC</dd>
<dt><code>bt470bg</code></dt>
<dd> BT.470 BG</dd>
<dt><code>smpte170m</code></dt>
<dd> SMPTE 170 M</dd>
<dt><code>smpte240m</code></dt>
<dd> SMPTE 240 M</dd>
<dt><code>ycocg</code></dt>
<dd> YCOCG</dd>
<dt><code>bt2020nc</code></dt>
<dd>
</dd><dt><code>bt2020_ncl</code></dt>
<dd> BT.2020 NCL</dd>
<dt><code>bt2020c</code></dt>
<dd>
</dd><dt><code>bt2020_cl</code></dt>
<dd> BT.2020 CL</dd>
<dt><code>smpte2085</code></dt>
<dd> SMPTE 2085</dd>
<dt><code>chroma-derived-nc</code></dt>
<dd> Chroma-derived NCL</dd>
<dt><code>chroma-derived-c</code></dt>
<dd> Chroma-derived CL</dd>
<dt><code>ictcp</code></dt>
<dd> ICtCp</dd></dl>
</dl>
<dl>
</dl>
<dt><code>color_range</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> If used as input parameter, it serves as a hint to the decoder, which color_range the input has. Possible values:</dd>
<dl>
<dl>
<dt><code>tv</code></dt>
<dd>
</dd><dt><code>mpeg</code></dt>
<dd> MPEG (219*2^(n-8))</dd>
<dt><code>pc</code></dt>
<dd>
</dd><dt><code>jpeg</code></dt>
<dd> JPEG (2^n-1)</dd></dl>
</dl>
<dl>
</dl>
<dt><code>chroma_sample_location</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Possible values:</dd>
<dl>
<dl>
<dt><code>left</code></dt>
<dd>
</dd><dt><code>center</code></dt>
<dd>
</dd><dt><code>topleft</code></dt>
<dd>
</dd><dt><code>top</code></dt>
<dd>
</dd><dt><code>bottomleft</code></dt>
<dd>
</dd><dt><code>bottom</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>log_level_offset</code> <i>integer</i></dt>
<dd> Set the log level offset.</dd>
<dt><code>slices</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></dt>
<dd> Number of slices, used in parallelized encoding.</dd>
<dt><code>thread_type</code> <i>flags</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Select which multithreading methods to use. </dd>
<p> Use of <code>frame</code> will increase decoding delay by one frame per thread, so clients which cannot provide future frames should not use it. </p>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>slice</code></dt>
<dd> Decode more than one part of a single frame at once. </dd>
<p> Multithreading using slices works only when the video was encoded with slices.</p>
<dt><code>frame</code></dt>
<dd> Decode more than one frame at once.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>slice+frame</code>.</dd></dl>
<dt><code>audio_service_type</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></dt>
<dd> Set audio service type. </dd>
<p> Possible values:</p>
<dl>
<dl>
<dt><code>ma</code></dt>
<dd> Main Audio Service</dd>
<dt><code>ef</code></dt>
<dd> Effects</dd>
<dt><code>vi</code></dt>
<dd> Visually Impaired</dd>
<dt><code>hi</code></dt>
<dd> Hearing Impaired</dd>
<dt><code>di</code></dt>
<dd> Dialogue</dd>
<dt><code>co</code></dt>
<dd> Commentary</dd>
<dt><code>em</code></dt>
<dd> Emergency</dd>
<dt><code>vo</code></dt>
<dd> Voice Over</dd>
<dt><code>ka</code></dt>
<dd> Karaoke</dd></dl>
</dl>
<dl>
</dl>
<dt><code>request_sample_fmt</code> <i>sample_fmt</i> <code>(</code><i>decoding,audio</i><code>)</code></dt>
<dd> Set sample format audio decoders should prefer. Default value is <tt>&quot;none&quot;</tt>.</dd>
<dt><code>pkt_timebase</code> <i>rational number</i></dt>
<dd>
</dd><dt><code>sub_charenc</code> <i>encoding</i> <code>(</code><i>decoding,subtitles</i><code>)</code></dt>
<dd> Set the input subtitles character encoding.</dd>
<dt><code>field_order</code> <i>field_order</i> <code>(</code><i>video</i><code>)</code></dt>
<dd> Set/override the field order of the video. Possible values:</dd>
<dl>
<dl>
<dt><code>progressive</code></dt>
<dd> Progressive video</dd>
<dt><code>tt</code></dt>
<dd> Interlaced video, top field coded and displayed first</dd>
<dt><code>bb</code></dt>
<dd> Interlaced video, bottom field coded and displayed first</dd>
<dt><code>tb</code></dt>
<dd> Interlaced video, top coded first, bottom displayed first</dd>
<dt><code>bt</code></dt>
<dd> Interlaced video, bottom coded first, top displayed first</dd></dl>
</dl>
<dl>
</dl>
<dt><code>skip_alpha</code> <i>bool</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Set to 1 to disable processing alpha (transparency). This works like the <code>gray</code> flag in the <code>flags</code> option which skips chroma information instead of alpha. Default is 0.</dd>
<dt><code>codec_whitelist</code> <i>list</i> <code>(</code><i>input</i><code>)</code></dt>
<dd> &#8220;,&#8221; separated list of allowed decoders. By default all are allowed.</dd>
<dt><code>dump_separator</code> <i>string</i> <code>(</code><i>input</i><code>)</code></dt>
<dd> Separator used to separate the fields printed on the command line about the Stream parameters. For example, to separate the fields with newlines and indentation: </dd>
<pre>
        ffprobe -dump_separator &quot;
                                  &quot;  -i ~/videos/matrixbench_mpeg2.mpg
</pre>
<dt><code>max_pixels</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></dt>
<dd> Maximum number of pixels per image. This value can be used to avoid out of memory failures due to large images.</dd>
<dt><code>apply_cropping</code> <i>bool</i> <code>(</code><i>decoding,video</i><code>)</code></dt>
<dd> Enable cropping if cropping parameters are multiples of the required alignment for the left and top parameters. If the alignment is not met the cropping will be partially applied to maintain alignment. Default is 1 (enabled). Note: The required alignment depends on if <tt>&quot;AV_CODEC_FLAG_UNALIGNED&quot;</tt> is set and the CPU. <tt>&quot;AV_CODEC_FLAG_UNALIGNED&quot;</tt> cannot be changed from the command line. Also hardware decoders will not apply left/top Cropping.</dd></dl>
<h2>DECODERS</h2>
<p> Decoders are configured elements in FFmpeg which allow the decoding of multimedia streams. </p>
<p> When you configure your FFmpeg build, all the supported native decoders are enabled by default. Decoders requiring an external library must be enabled manually via the corresponding <tt>&quot;--enable-lib&quot;</tt> option. You can list all available decoders using the configure option <tt>&quot;--list-decoders&quot;</tt>. </p>
<p> You can disable all the decoders with the configure option <tt>&quot;--disable-decoders&quot;</tt> and selectively enable / disable single decoders with the options <tt>&quot;--enable-decoder=</tt>DECODER<tt>&quot;</tt> / <tt>&quot;--disable-decoder=</tt>DECODER<tt>&quot;</tt>. </p>
<p> The option <tt>&quot;-decoders&quot;</tt> of the ff* tools will display the list of enabled decoders.</p>
<h2>VIDEO DECODERS</h2>
<p> A description of some of the currently available video decoders follows.</p>
<h3>av1</h3>
<p> AOMedia Video 1 (AV1) decoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>operating_point</code></dt>
<dd> Select an operating point of a scalable AV1 bitstream (0 &#8211; 31). Default is 0.</dd></dl>
<h3>rawvideo</h3>
<p> Raw video decoder. </p>
<p> This decoder decodes rawvideo streams. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>top</code> <i>top_field_first</i></dt>
<dd> Specify the assumed field type of the input video.</dd>
<dl>
<dl>
<dt><code>-1</code></dt>
<dd> the video is assumed to be progressive (default)</dd>
<dt><code>0</code></dt>
<dd> bottom-field-first is assumed</dd>
<dt><code>1</code></dt>
<dd> top-field-first is assumed</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>libdav1d</h3>
<p> dav1d AV1 decoder. </p>
<p> libdav1d allows libavcodec to decode the AOMedia Video 1 (AV1) codec. Requires the presence of the libdav1d headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libdav1d&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libdav1d wrapper.</p>
<dl>
<dt><code>framethreads</code></dt>
<dd> Set amount of frame threads to use during decoding. The default value is 0 (autodetect).</dd>
<dt><code>tilethreads</code></dt>
<dd> Set amount of tile threads to use during decoding. The default value is 0 (autodetect).</dd>
<dt><code>filmgrain</code></dt>
<dd> Apply film grain to the decoded video if present in the bitstream. Defaults to the internal default of the library.</dd>
<dt><code>oppoint</code></dt>
<dd> Select an operating point of a scalable AV1 bitstream (0 &#8211; 31). Defaults to the internal default of the library.</dd>
<dt><code>alllayers</code></dt>
<dd> Output all spatial layers of a scalable AV1 bitstream. The default value is false.</dd></dl>
<h3>libdavs2</h3>
<p> AVS2-P2/IEEE1857.4 video decoder wrapper. </p>
<p> This decoder allows libavcodec to decode AVS2 streams with davs2 library.</p>
<h3>libuavs3d</h3>
<p> AVS3-P2/IEEE1857.10 video decoder. </p>
<p> libuavs3d allows libavcodec to decode AVS3 streams. Requires the presence of the libuavs3d headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libuavs3d&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following option is supported by the libuavs3d wrapper.</p>
<dl>
<dt><code>frame_threads</code></dt>
<dd> Set amount of frame threads to use during decoding. The default value is 0 (autodetect).</dd></dl>
<h2>AUDIO DECODERS</h2>
<p> A description of some of the currently available audio decoders follows.</p>
<h3>ac3</h3>
<p> AC-3 audio decoder. </p>
<p> This decoder implements part of ATSC A/52:2010 and ETSI TS 102 366, as well as the undocumented RealAudio 3 (a.k.a. dnet). </p>
<p> <i></i><i>AC-3</i><i> Decoder Options</i></p>
<dl>
<dt><code>-drc_scale</code> <i>value</i></dt>
<dd> Dynamic Range Scale Factor. The factor to apply to dynamic range values from the AC-3 stream. This factor is applied exponentially. The default value is 1. There are 3 notable scale factor ranges:</dd>
<dl>
<dl>
<dt><code>drc_scale == 0</code></dt>
<dd> DRC disabled. Produces full range audio.</dd>
<dt><code>0 &lt; drc_scale &lt;= 1</code></dt>
<dd> DRC enabled. Applies a fraction of the stream DRC value. Audio reproduction is between full range and full compression.</dd>
<dt><code>drc_scale &gt; 1</code></dt>
<dd> DRC enabled. Applies drc_scale asymmetrically. Loud sounds are fully compressed. Soft sounds are enhanced.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>flac</h3>
<p> FLAC audio decoder. </p>
<p> This decoder aims to implement the complete FLAC specification from Xiph. </p>
<p> <i></i><i>FLAC</i><i> Decoder options</i></p>
<dl>
<dt><code>-use_buggy_lpc</code></dt>
<dd> The lavc FLAC encoder used to produce buggy streams with high lpc values (like the default value). This option makes it possible to decode such streams correctly by using lavc&#8217;s old buggy lpc logic for decoding.</dd></dl>
<h3>ffwavesynth</h3>
<p> Internal wave synthesizer. </p>
<p> This decoder generates wave patterns according to predefined sequences. Its use is purely internal and the format of the data it accepts is not publicly documented.</p>
<h3>libcelt</h3>
<p> libcelt decoder wrapper. </p>
<p> libcelt allows libavcodec to decode the Xiph CELT ultra-low delay audio codec. Requires the presence of the libcelt headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libcelt&quot;</tt>.</p>
<h3>libgsm</h3>
<p> libgsm decoder wrapper. </p>
<p> libgsm allows libavcodec to decode the GSM full rate audio codec. Requires the presence of the libgsm headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libgsm&quot;</tt>. </p>
<p> This decoder supports both the ordinary GSM and the Microsoft variant.</p>
<h3>libilbc</h3>
<p> libilbc decoder wrapper. </p>
<p> libilbc allows libavcodec to decode the Internet Low Bitrate Codec (iLBC) audio codec. Requires the presence of the libilbc headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libilbc&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following option is supported by the libilbc wrapper.</p>
<dl>
<dt><code>enhance</code></dt>
<dd> Enable the enhancement of the decoded audio when set to 1. The default value is 0 (disabled).</dd></dl>
<h3>libopencore-amrnb</h3>
<p> libopencore-amrnb decoder wrapper. </p>
<p> libopencore-amrnb allows libavcodec to decode the Adaptive Multi-Rate Narrowband audio codec. Using it requires the presence of the libopencore-amrnb headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopencore-amrnb&quot;</tt>. </p>
<p> An FFmpeg native decoder for AMR-NB exists, so users can decode AMR-NB without this library.</p>
<h3>libopencore-amrwb</h3>
<p> libopencore-amrwb decoder wrapper. </p>
<p> libopencore-amrwb allows libavcodec to decode the Adaptive Multi-Rate Wideband audio codec. Using it requires the presence of the libopencore-amrwb headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopencore-amrwb&quot;</tt>. </p>
<p> An FFmpeg native decoder for AMR-WB exists, so users can decode AMR-WB without this library.</p>
<h3>libopus</h3>
<p> libopus decoder wrapper. </p>
<p> libopus allows libavcodec to decode the Opus Interactive Audio Codec. Requires the presence of the libopus headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopus&quot;</tt>. </p>
<p> An FFmpeg native decoder for Opus exists, so users can decode Opus without this library.</p>
<h2>SUBTITLES DECODERS</h2>
<h3>libaribb24</h3>
<p> ARIB STD-B24 caption decoder. </p>
<p> Implements profiles A and C of the ARIB STD-B24 standard. </p>
<p> <i>libaribb24 Decoder Options</i></p>
<dl>
<dt><code>-aribb24-base-path</code> <i>path</i></dt>
<dd> Sets the base path for the libaribb24 library. This is utilized for reading of configuration files (for custom unicode conversions), and for dumping of non-text symbols as images under that location. </dd>
<p> Unset by default.</p>
<dt><code>-aribb24-skip-ruby-text</code> <i>boolean</i></dt>
<dd> Tells the decoder wrapper to skip text blocks that contain half-height ruby text. </dd>
<p> Enabled by default.</dl>
<h3>dvbsub</h3>
<p> <i>Options</i></p>
<dl>
<dt><code>compute_clut</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>-1</code></dt>
<dd> Compute clut if no matching CLUT is in the stream.</dd>
<dt><code>0</code></dt>
<dd> Never compute CLUT</dd>
<dt><code>1</code></dt>
<dd> Always compute CLUT and override the one provided in the stream.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>dvb_substream</code></dt>
<dd> Selects the dvb substream, or all substreams if -1 which is default.</dd></dl>
<h3>dvdsub</h3>
<p> This codec decodes the bitmap subtitles used in DVDs; the same subtitles can also be found in VobSub file pairs and in some Matroska files. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>palette</code></dt>
<dd> Specify the global palette used by the bitmaps. When stored in VobSub, the palette is normally specified in the index file; in Matroska, the palette is stored in the codec extra-data in the same format as in VobSub. In DVDs, the palette is stored in the IFO file, and therefore not available when reading from dumped VOB files. </dd>
<p> The format for this option is a string containing 16 24-bits hexadecimal numbers (without 0x prefix) separated by commas, for example <tt>&quot;0d00ee, ee450d, 101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1, 7b2a0e, 0d950c, 0f007b, cf0dec, cfa80c, 7c127b&quot;</tt>.</p>
<dt><code>ifo_palette</code></dt>
<dd> Specify the IFO file from which the global palette is obtained. (experimental)</dd>
<dt><code>forced_subs_only</code></dt>
<dd> Only decode subtitle entries marked as forced. Some titles have forced and non-forced subtitles in the same track. Setting this flag to <tt>1</tt> will only keep the forced subtitles. Default value is <tt>0</tt>.</dd></dl>
<h3>libzvbi-teletext</h3>
<p> Libzvbi allows libavcodec to decode DVB teletext pages and DVB teletext subtitles. Requires the presence of the libzvbi headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libzvbi&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>txt_page</code></dt>
<dd> List of teletext page numbers to decode. Pages that do not match the specified list are dropped. You may use the special <tt>&quot;*&quot;</tt> string to match all pages, or <tt>&quot;subtitle&quot;</tt> to match all subtitle pages. Default value is *.</dd>
<dt><code>txt_default_region</code></dt>
<dd> Set default character set used for decoding, a value between 0 and 87 (see ETS 300 706, Section 15, Table 32). Default value is -1, which does not override the libzvbi default. This option is needed for some legacy level 1.0 transmissions which cannot signal the proper charset.</dd>
<dt><code>txt_chop_top</code></dt>
<dd> Discards the top teletext line. Default value is 1.</dd>
<dt><code>txt_format</code></dt>
<dd> Specifies the format of the decoded subtitles.</dd>
<dl>
<dl>
<dt><code>bitmap</code></dt>
<dd> The default format, you should use this for teletext pages, because certain graphics and colors cannot be expressed in simple text or even ASS.</dd>
<dt><code>text</code></dt>
<dd> Simple text based output without formatting.</dd>
<dt><code>ass</code></dt>
<dd> Formatted ASS output, subtitle pages and teletext pages are returned in different styles, subtitle pages are stripped down to text, but an effort is made to keep the text alignment and the formatting.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>txt_left</code></dt>
<dd> X offset of generated bitmaps, default is 0.</dd>
<dt><code>txt_top</code></dt>
<dd> Y offset of generated bitmaps, default is 0.</dd>
<dt><code>txt_chop_spaces</code></dt>
<dd> Chops leading and trailing spaces and removes empty lines from the generated text. This option is useful for teletext based subtitles where empty spaces may be present at the start or at the end of the lines or empty lines may be present between the subtitle lines because of double-sized teletext characters. Default value is 1.</dd>
<dt><code>txt_duration</code></dt>
<dd> Sets the display duration of the decoded teletext pages or subtitles in milliseconds. Default value is -1 which means infinity or until the next subtitle event comes.</dd>
<dt><code>txt_transparent</code></dt>
<dd> Force transparent background of the generated teletext bitmaps. Default value is 0 which means an opaque background.</dd>
<dt><code>txt_opacity</code></dt>
<dd> Sets the opacity (0-255) of the teletext background. If <code>txt_transparent</code> is not set, it only affects characters between a start box and an end box, typically subtitles. Default value is 0 if <code>txt_transparent</code> is set, 255 otherwise.</dd></dl>
<h2>ENCODERS</h2>
<p> Encoders are configured elements in FFmpeg which allow the encoding of multimedia streams. </p>
<p> When you configure your FFmpeg build, all the supported native encoders are enabled by default. Encoders requiring an external library must be enabled manually via the corresponding <tt>&quot;--enable-lib&quot;</tt> option. You can list all available encoders using the configure option <tt>&quot;--list-encoders&quot;</tt>. </p>
<p> You can disable all the encoders with the configure option <tt>&quot;--disable-encoders&quot;</tt> and selectively enable / disable single encoders with the options <tt>&quot;--enable-encoder=</tt>ENCODER<tt>&quot;</tt> / <tt>&quot;--disable-encoder=</tt>ENCODER<tt>&quot;</tt>. </p>
<p> The option <tt>&quot;-encoders&quot;</tt> of the ff* tools will display the list of enabled encoders.</p>
<h2>AUDIO ENCODERS</h2>
<p> A description of some of the currently available audio encoders follows.</p>
<h3>aac</h3>
<p> Advanced Audio Coding (AAC) encoder. </p>
<p> This encoder is the default AAC encoder, natively implemented into FFmpeg. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Set bit rate in bits/s. Setting this automatically activates constant bit rate (CBR) mode. If this option is unspecified it is set to 128kbps.</dd>
<dt><code>q</code></dt>
<dd> Set quality for variable bit rate (VBR) mode. This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</dd>
<dt><code>cutoff</code></dt>
<dd> Set cutoff frequency. If unspecified will allow the encoder to dynamically adjust the cutoff to improve clarity on low bitrates.</dd>
<dt><code>aac_coder</code></dt>
<dd> Set AAC encoder coding method. Possible values:</dd>
<dl>
<dl>
<dt><code>twoloop</code></dt>
<dd> Two loop searching (TLS) method. </dd>
<p> This method first sets quantizers depending on band thresholds and then tries to find an optimal combination by adding or subtracting a specific value from all quantizers and adjusting some individual quantizer a little. Will tune itself based on whether <code>aac_is</code>, <code>aac_ms</code> and <code>aac_pns</code> are enabled.</p>
<dt><code>anmr</code></dt>
<dd> Average noise to mask ratio (ANMR) trellis-based solution. </dd>
<p> This is an experimental coder which currently produces a lower quality, is more unstable and is slower than the default twoloop coder but has potential. Currently has no support for the <code>aac_is</code> or <code>aac_pns</code> options. Not currently recommended.</p>
<dt><code>fast</code></dt>
<dd> Constant quantizer method. </dd>
<p> Uses a cheaper version of twoloop algorithm that doesn&#8217;t try to do as many clever adjustments. Worse with low bitrates (less than 64kbps), but is better and much faster at higher bitrates. This is the default choice for a coder</dl>
</dl>
<dl>
</dl>
<dt><code>aac_ms</code></dt>
<dd> Sets mid/side coding mode. The default value of &#8220;auto&#8221; will automatically use M/S with bands which will benefit from such coding. Can be forced for all bands using the value &#8220;enable&#8221;, which is mainly useful for debugging or disabled using &#8220;disable&#8221;.</dd>
<dt><code>aac_is</code></dt>
<dd> Sets intensity stereo coding tool usage. By default, it&#8217;s enabled and will automatically toggle IS for similar pairs of stereo bands if it&#8217;s beneficial. Can be disabled for debugging by setting the value to &#8220;disable&#8221;.</dd>
<dt><code>aac_pns</code></dt>
<dd> Uses perceptual noise substitution to replace low entropy high frequency bands with imperceptible white noise during the decoding process. By default, it&#8217;s enabled, but can be disabled for debugging purposes by using &#8220;disable&#8221;.</dd>
<dt><code>aac_tns</code></dt>
<dd> Enables the use of a multitap FIR filter which spans through the high frequency bands to hide quantization noise during the encoding process and is reverted by the decoder. As well as decreasing unpleasant artifacts in the high range this also reduces the entropy in the high bands and allows for more bits to be used by the mid-low bands. By default it&#8217;s enabled but can be disabled for debugging by setting the option to &#8220;disable&#8221;.</dd>
<dt><code>aac_ltp</code></dt>
<dd> Enables the use of the long term prediction extension which increases coding efficiency in very low bandwidth situations such as encoding of voice or solo piano music by extending constant harmonic peaks in bands throughout frames. This option is implied by profile:a aac_low and is incompatible with aac_pred. Use in conjunction with <code>-ar</code> to decrease the samplerate.</dd>
<dt><code>aac_pred</code></dt>
<dd> Enables the use of a more traditional style of prediction where the spectral coefficients transmitted are replaced by the difference of the current coefficients minus the previous &#8220;predicted&#8221; coefficients. In theory and sometimes in practice this can improve quality for low to mid bitrate audio. This option implies the aac_main profile and is incompatible with aac_ltp.</dd>
<dt><code>profile</code></dt>
<dd> Sets the encoding profile, possible values:</dd>
<dl>
<dl>
<dt><code>aac_low</code></dt>
<dd> The default, AAC &#8220;Low-complexity&#8221; profile. Is the most compatible and produces decent quality.</dd>
<dt><code>mpeg2_aac_low</code></dt>
<dd> Equivalent to <tt>&quot;-profile:a aac_low -aac_pns 0&quot;</tt>. PNS was introduced with the MPEG4 specifications.</dd>
<dt><code>aac_ltp</code></dt>
<dd> Long term prediction profile, is enabled by and will enable the <code>aac_ltp</code> option. Introduced in MPEG4.</dd>
<dt><code>aac_main</code></dt>
<dd> Main-type prediction profile, is enabled by and will enable the <code>aac_pred</code> option. Introduced in MPEG2.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> If this option is unspecified it is set to <code>aac_low</code>.</dd></dl>
</dl>
<h3>ac3 and ac3_fixed</h3>
<p> AC-3 audio encoders. </p>
<p> These encoders implement part of ATSC A/52:2010 and ETSI TS 102 366, as well as the undocumented RealAudio 3 (a.k.a. dnet). </p>
<p> The <i>ac3</i> encoder uses floating-point math, while the <i>ac3_fixed</i> encoder only uses fixed-point integer math. This does not mean that one is always faster, just that one or the other may be better suited to a particular system. The <i>ac3_fixed</i> encoder is not the default codec for any of the output formats, so it must be specified explicitly using the option <tt>&quot;-acodec ac3_fixed&quot;</tt> in order to use it. </p>
<p> <i></i><i>AC-3</i><i> Metadata</i> </p>
<p> The AC-3 metadata options are used to set parameters that describe the audio, but in most cases do not affect the audio encoding itself. Some of the options do directly affect or influence the decoding and playback of the resulting bitstream, while others are just for informational purposes. A few of the options will add bits to the output stream that could otherwise be used for audio data, and will thus affect the quality of the output. Those will be indicated accordingly with a note in the option list below. </p>
<p> These parameters are described in detail in several publicly-available documents.</p>
<dl>
<dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.atsc.org/cms/standards/a_52-2010.pdf">http://www.atsc.org/cms/standards/a_52-2010.pdf</a></code>&gt;&gt;</dt>
<dd>
</dd><dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.atsc.org/cms/standards/a_54a_with_corr_1.pdf">http://www.atsc.org/cms/standards/a_54a_with_corr_1.pdf</a></code>&gt;&gt;</dt>
<dd>
</dd><dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/18_Metadata.Guide.pdf">http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/18_Metadata.Guide.pdf</a></code>&gt;&gt;</dt>
<dd>
</dd><dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/46_DDEncodingGuidelines.pdf">http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/46_DDEncodingGuidelines.pdf</a></code>&gt;&gt;</dt>
<dd></dd></dl>
<p> Metadata Control Options</p>
<dl>
<dt><code>-per_frame_metadata</code> <i>boolean</i></dt>
<dd> Allow Per-Frame Metadata. Specifies if the encoder should check for changing metadata for each frame.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> The metadata values set at initialization will be used for every frame in the stream. (default)</dd>
<dt><code>1</code></dt>
<dd> Metadata values can be changed before encoding each frame.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Downmix Levels</p>
<dl>
<dt><code>-center_mixlev</code> <i>level</i></dt>
<dd> Center Mix Level. The amount of gain the decoder should apply to the center channel when downmixing to stereo. This field will only be written to the bitstream if a center channel is present. The value is specified as a scale factor. There are 3 valid values:</dd>
<dl>
<dl>
<dt><code>0.707</code></dt>
<dd> Apply -3dB gain</dd>
<dt><code>0.595</code></dt>
<dd> Apply -4.5dB gain (default)</dd>
<dt><code>0.500</code></dt>
<dd> Apply -6dB gain</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-surround_mixlev</code> <i>level</i></dt>
<dd> Surround Mix Level. The amount of gain the decoder should apply to the surround channel(s) when downmixing to stereo. This field will only be written to the bitstream if one or more surround channels are present. The value is specified as a scale factor. There are 3 valid values:</dd>
<dl>
<dl>
<dt><code>0.707</code></dt>
<dd> Apply -3dB gain</dd>
<dt><code>0.500</code></dt>
<dd> Apply -6dB gain (default)</dd>
<dt><code>0.000</code></dt>
<dd> Silence Surround Channel(s)</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Audio Production Information </p>
<p> Audio Production Information is optional information describing the mixing environment. Either none or both of the fields are written to the bitstream.</p>
<dl>
<dt><code>-mixing_level</code> <i>number</i></dt>
<dd> Mixing Level. Specifies peak sound pressure level (SPL) in the production environment when the mix was mastered. Valid values are 80 to 111, or -1 for unknown or not indicated. The default value is -1, but that value cannot be used if the Audio Production Information is written to the bitstream. Therefore, if the <tt>&quot;room_type&quot;</tt> option is not the default value, the <tt>&quot;mixing_level&quot;</tt> option must not be -1.</dd>
<dt><code>-room_type</code> <i>type</i></dt>
<dd> Room Type. Describes the equalization used during the final mixing session at the studio or on the dubbing stage. A large room is a dubbing stage with the industry standard X-curve equalization; a small room has flat equalization. This field will not be written to the bitstream if both the <tt>&quot;mixing_level&quot;</tt> option and the <tt>&quot;room_type&quot;</tt> option have the default values.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>notindicated</code></dt>
<dd> Not Indicated (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>large</code></dt>
<dd> Large Room</dd>
<dt><code>2</code></dt>
<dd>
</dd><dt><code>small</code></dt>
<dd> Small Room</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Other Metadata Options</p>
<dl>
<dt><code>-copyright</code> <i>boolean</i></dt>
<dd> Copyright Indicator. Specifies whether a copyright exists for this audio.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>off</code></dt>
<dd> No Copyright Exists (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>on</code></dt>
<dd> Copyright Exists</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-dialnorm</code> <i>value</i></dt>
<dd> Dialogue Normalization. Indicates how far the average dialogue level of the program is below digital 100% full scale (0 dBFS). This parameter determines a level shift during audio reproduction that sets the average volume of the dialogue to a preset level. The goal is to match volume level between program sources. A value of -31dB will result in no volume level change, relative to the source volume, during audio reproduction. Valid values are whole numbers in the range -31 to -1, with -31 being the default.</dd>
<dt><code>-dsur_mode</code> <i>mode</i></dt>
<dd> Dolby Surround Mode. Specifies whether the stereo signal uses Dolby Surround (Pro Logic). This field will only be written to the bitstream if the audio stream is stereo. Using this option does <code>NOT</code> mean the encoder will actually apply Dolby Surround processing.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>notindicated</code></dt>
<dd> Not Indicated (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>off</code></dt>
<dd> Not Dolby Surround Encoded</dd>
<dt><code>2</code></dt>
<dd>
</dd><dt><code>on</code></dt>
<dd> Dolby Surround Encoded</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-original</code> <i>boolean</i></dt>
<dd> Original Bit Stream Indicator. Specifies whether this audio is from the original source and not a copy.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>off</code></dt>
<dd> Not Original Source</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>on</code></dt>
<dd> Original Source (default)</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> <i>Extended Bitstream Information</i> </p>
<p> The extended bitstream options are part of the Alternate Bit Stream Syntax as specified in Annex D of the A/52:2010 standard. It is grouped into 2 parts. If any one parameter in a group is specified, all values in that group will be written to the bitstream. Default values are used for those that are written but have not been specified. If the mixing levels are written, the decoder will use these values instead of the ones specified in the <tt>&quot;center_mixlev&quot;</tt> and <tt>&quot;surround_mixlev&quot;</tt> options if it supports the Alternate Bit Stream Syntax. </p>
<p> Extended Bitstream Information &#8211; Part 1</p>
<dl>
<dt><code>-dmix_mode</code> <i>mode</i></dt>
<dd> Preferred Stereo Downmix Mode. Allows the user to select either Lt/Rt (Dolby Surround) or Lo/Ro (normal stereo) as the preferred stereo downmix mode.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>notindicated</code></dt>
<dd> Not Indicated (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>ltrt</code></dt>
<dd> Lt/Rt Downmix Preferred</dd>
<dt><code>2</code></dt>
<dd>
</dd><dt><code>loro</code></dt>
<dd> Lo/Ro Downmix Preferred</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-ltrt_cmixlev</code> <i>level</i></dt>
<dd> Lt/Rt Center Mix Level. The amount of gain the decoder should apply to the center channel when downmixing to stereo in Lt/Rt mode.</dd>
<dl>
<dl>
<dt><code>1.414</code></dt>
<dd> Apply +3dB gain</dd>
<dt><code>1.189</code></dt>
<dd> Apply +1.5dB gain</dd>
<dt><code>1.000</code></dt>
<dd> Apply 0dB gain</dd>
<dt><code>0.841</code></dt>
<dd> Apply -1.5dB gain</dd>
<dt><code>0.707</code></dt>
<dd> Apply -3.0dB gain</dd>
<dt><code>0.595</code></dt>
<dd> Apply -4.5dB gain (default)</dd>
<dt><code>0.500</code></dt>
<dd> Apply -6.0dB gain</dd>
<dt><code>0.000</code></dt>
<dd> Silence Center Channel</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-ltrt_surmixlev</code> <i>level</i></dt>
<dd> Lt/Rt Surround Mix Level. The amount of gain the decoder should apply to the surround channel(s) when downmixing to stereo in Lt/Rt mode.</dd>
<dl>
<dl>
<dt><code>0.841</code></dt>
<dd> Apply -1.5dB gain</dd>
<dt><code>0.707</code></dt>
<dd> Apply -3.0dB gain</dd>
<dt><code>0.595</code></dt>
<dd> Apply -4.5dB gain</dd>
<dt><code>0.500</code></dt>
<dd> Apply -6.0dB gain (default)</dd>
<dt><code>0.000</code></dt>
<dd> Silence Surround Channel(s)</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-loro_cmixlev</code> <i>level</i></dt>
<dd> Lo/Ro Center Mix Level. The amount of gain the decoder should apply to the center channel when downmixing to stereo in Lo/Ro mode.</dd>
<dl>
<dl>
<dt><code>1.414</code></dt>
<dd> Apply +3dB gain</dd>
<dt><code>1.189</code></dt>
<dd> Apply +1.5dB gain</dd>
<dt><code>1.000</code></dt>
<dd> Apply 0dB gain</dd>
<dt><code>0.841</code></dt>
<dd> Apply -1.5dB gain</dd>
<dt><code>0.707</code></dt>
<dd> Apply -3.0dB gain</dd>
<dt><code>0.595</code></dt>
<dd> Apply -4.5dB gain (default)</dd>
<dt><code>0.500</code></dt>
<dd> Apply -6.0dB gain</dd>
<dt><code>0.000</code></dt>
<dd> Silence Center Channel</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-loro_surmixlev</code> <i>level</i></dt>
<dd> Lo/Ro Surround Mix Level. The amount of gain the decoder should apply to the surround channel(s) when downmixing to stereo in Lo/Ro mode.</dd>
<dl>
<dl>
<dt><code>0.841</code></dt>
<dd> Apply -1.5dB gain</dd>
<dt><code>0.707</code></dt>
<dd> Apply -3.0dB gain</dd>
<dt><code>0.595</code></dt>
<dd> Apply -4.5dB gain</dd>
<dt><code>0.500</code></dt>
<dd> Apply -6.0dB gain (default)</dd>
<dt><code>0.000</code></dt>
<dd> Silence Surround Channel(s)</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Extended Bitstream Information &#8211; Part 2</p>
<dl>
<dt><code>-dsurex_mode</code> <i>mode</i></dt>
<dd> Dolby Surround EX Mode. Indicates whether the stream uses Dolby Surround EX (7.1 matrixed to 5.1). Using this option does <code>NOT</code> mean the encoder will actually apply Dolby Surround EX processing.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>notindicated</code></dt>
<dd> Not Indicated (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>on</code></dt>
<dd> Dolby Surround EX Off</dd>
<dt><code>2</code></dt>
<dd>
</dd><dt><code>off</code></dt>
<dd> Dolby Surround EX On</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-dheadphone_mode</code> <i>mode</i></dt>
<dd> Dolby Headphone Mode. Indicates whether the stream uses Dolby Headphone encoding (multi-channel matrixed to 2.0 for use with headphones). Using this option does <code>NOT</code> mean the encoder will actually apply Dolby Headphone processing.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>notindicated</code></dt>
<dd> Not Indicated (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>on</code></dt>
<dd> Dolby Headphone Off</dd>
<dt><code>2</code></dt>
<dd>
</dd><dt><code>off</code></dt>
<dd> Dolby Headphone On</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-ad_conv_type</code> <i>type</i></dt>
<dd> A/D Converter Type. Indicates whether the audio has passed through HDCD A/D conversion.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>standard</code></dt>
<dd> Standard A/D Converter (default)</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>hdcd</code></dt>
<dd> HDCD A/D Converter</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> <i>Other </i><i>AC-3</i><i> Encoding Options</i></p>
<dl>
<dt><code>-stereo_rematrixing</code> <i>boolean</i></dt>
<dd> Stereo Rematrixing. Enables/Disables use of rematrixing for stereo input. This is an optional AC-3 feature that increases quality by selectively encoding the left/right channels as mid/side. This option is enabled by default, and it is highly recommended that it be left as enabled except for testing purposes.</dd>
<dt><code>cutoff</code> <i>frequency</i></dt>
<dd> Set lowpass cutoff frequency. If unspecified, the encoder selects a default determined by various other encoding parameters.</dd></dl>
<p> <i>Floating-Point-Only </i><i>AC-3</i><i> Encoding Options</i> </p>
<p> These options are only valid for the floating-point encoder and do not exist for the fixed-point encoder due to the corresponding features not being implemented in fixed-point.</p>
<dl>
<dt><code>-channel_coupling</code> <i>boolean</i></dt>
<dd> Enables/Disables use of channel coupling, which is an optional AC-3 feature that increases quality by combining high frequency information from multiple channels into a single channel. The per-channel high frequency information is sent with less accuracy in both the frequency and time domains. This allows more bits to be used for lower frequencies while preserving enough information to reconstruct the high frequencies. This option is enabled by default for the floating-point encoder and should generally be left as enabled except for testing purposes or to increase encoding speed.</dd>
<dl>
<dl>
<dt><code>-1</code></dt>
<dd>
</dd><dt><code>auto</code></dt>
<dd> Selected by Encoder (default)</dd>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>off</code></dt>
<dd> Disable Channel Coupling</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>on</code></dt>
<dd> Enable Channel Coupling</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-cpl_start_band</code> <i>number</i></dt>
<dd> Coupling Start Band. Sets the channel coupling start band, from 1 to 15. If a value higher than the bandwidth is used, it will be reduced to 1 less than the coupling end band. If <i>auto</i> is used, the start band will be determined by the encoder based on the bit rate, sample rate, and channel layout. This option has no effect if channel coupling is disabled.</dd>
<dl>
<dl>
<dt><code>-1</code></dt>
<dd>
</dd><dt><code>auto</code></dt>
<dd> Selected by Encoder (default)</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>flac</h3>
<p> FLAC (Free Lossless Audio Codec) Encoder </p>
<p> <i>Options</i> </p>
<p> The following options are supported by FFmpeg&#8217;s flac encoder.</p>
<dl>
<dt><code>compression_level</code></dt>
<dd> Sets the compression level, which chooses defaults for many other options if they are not set explicitly. Valid values are from 0 to 12, 5 is the default.</dd>
<dt><code>frame_size</code></dt>
<dd> Sets the size of the frames in samples per channel.</dd>
<dt><code>lpc_coeff_precision</code></dt>
<dd> Sets the LPC coefficient precision, valid values are from 1 to 15, 15 is the default.</dd>
<dt><code>lpc_type</code></dt>
<dd> Sets the first stage LPC algorithm</dd>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> LPC is not used</dd>
<dt><code>fixed</code></dt>
<dd> fixed LPC coefficients</dd>
<dt><code>levinson</code></dt>
<dd>
</dd><dt><code>cholesky</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>lpc_passes</code></dt>
<dd> Number of passes to use for Cholesky factorization during LPC analysis</dd>
<dt><code>min_partition_order</code></dt>
<dd> The minimum partition order</dd>
<dt><code>max_partition_order</code></dt>
<dd> The maximum partition order</dd>
<dt><code>prediction_order_method</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>estimation</code></dt>
<dd>
</dd><dt><code>2level</code></dt>
<dd>
</dd><dt><code>4level</code></dt>
<dd>
</dd><dt><code>8level</code></dt>
<dd>
</dd><dt><code>search</code></dt>
<dd> Bruteforce search</dd>
<dt><code>log</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>ch_mode</code></dt>
<dd> Channel mode</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> The mode is chosen automatically for each frame</dd>
<dt><code>indep</code></dt>
<dd> Channels are independently coded</dd>
<dt><code>left_side</code></dt>
<dd>
</dd><dt><code>right_side</code></dt>
<dd>
</dd><dt><code>mid_side</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>exact_rice_parameters</code></dt>
<dd> Chooses if rice parameters are calculated exactly or approximately. if set to 1 then they are chosen exactly, which slows the code down slightly and improves compression slightly.</dd>
<dt><code>multi_dim_quant</code></dt>
<dd> Multi Dimensional Quantization. If set to 1 then a 2nd stage LPC algorithm is applied after the first stage to finetune the coefficients. This is quite slow and slightly improves compression.</dd></dl>
<h3>opus</h3>
<p> Opus encoder. </p>
<p> This is a native FFmpeg encoder for the Opus format. Currently its in development and only implements the CELT part of the codec. Its quality is usually worse and at best is equal to the libopus encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Set bit rate in bits/s. If unspecified it uses the number of channels and the layout to make a good guess.</dd>
<dt><code>opus_delay</code></dt>
<dd> Sets the maximum delay in milliseconds. Lower delays than 20ms will very quickly decrease quality.</dd></dl>
<h3>libfdk_aac</h3>
<p> libfdk-aac AAC (Advanced Audio Coding) encoder wrapper. </p>
<p> The libfdk-aac library is based on the Fraunhofer FDK AAC code from the Android project. </p>
<p> Requires the presence of the libfdk-aac headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libfdk-aac&quot;</tt>. The library is also incompatible with GPL, so if you allow the use of GPL, you should configure with <tt>&quot;--enable-gpl --enable-nonfree --enable-libfdk-aac&quot;</tt>. </p>
<p> This encoder has support for the AAC-HE profiles. </p>
<p> VBR encoding, enabled through the <code>vbr</code> or <code>flags +qscale</code> options, is experimental and only works with some combinations of parameters. </p>
<p> Support for encoding 7.1 audio is only available with libfdk-aac 0.1.3 or higher. </p>
<p> For more information see the fdk-aac project at &lt;<code><a rel="nofollow" href="http://sourceforge.net/p/opencore-amr/fdk-aac/">http://sourceforge.net/p/opencore-amr/fdk-aac/</a></code>&gt;. </p>
<p> <i>Options</i> </p>
<p> The following options are mapped on the shared FFmpeg codec options.</p>
<dl>
<dt><code>b</code></dt>
<dd> Set bit rate in bits/s. If the bitrate is not explicitly specified, it is automatically set to a suitable value depending on the selected profile. </dd>
<p> In case VBR mode is enabled the option is ignored.</p>
<dt><code>ar</code></dt>
<dd> Set audio sampling rate (in Hz).</dd>
<dt><code>channels</code></dt>
<dd> Set the number of audio channels.</dd>
<dt><code>flags +qscale</code></dt>
<dd> Enable fixed quality, VBR (Variable Bit Rate) mode. Note that VBR is implicitly enabled when the <code>vbr</code> value is positive.</dd>
<dt><code>cutoff</code></dt>
<dd> Set cutoff frequency. If not specified (or explicitly set to 0) it will use a value automatically computed by the library. Default value is 0.</dd>
<dt><code>profile</code></dt>
<dd> Set audio profile. </dd>
<p> The following profiles are recognized:</p>
<dl>
<dl>
<dt><code>aac_low</code></dt>
<dd> Low Complexity AAC (LC)</dd>
<dt><code>aac_he</code></dt>
<dd> High Efficiency AAC (HE-AAC)</dd>
<dt><code>aac_he_v2</code></dt>
<dd> High Efficiency AAC version 2 (HE-AACv2)</dd>
<dt><code>aac_ld</code></dt>
<dd> Low Delay AAC (LD)</dd>
<dt><code>aac_eld</code></dt>
<dd> Enhanced Low Delay AAC (ELD)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> If not specified it is set to <code>aac_low</code>.</dd></dl>
</dl>
<p> The following are private options of the libfdk_aac encoder.</p>
<dl>
<dt><code>afterburner</code></dt>
<dd> Enable afterburner feature if set to 1, disabled if set to 0. This improves the quality but also the required processing power. </dd>
<p> Default value is 1.</p>
<dt><code>eld_sbr</code></dt>
<dd> Enable SBR (Spectral Band Replication) for ELD if set to 1, disabled if set to 0. </dd>
<p> Default value is 0.</p>
<dt><code>eld_v2</code></dt>
<dd> Enable ELDv2 (LD-MPS extension for ELD stereo signals) for ELDv2 if set to 1, disabled if set to 0. </dd>
<p> Note that option is available when fdk-aac version (AACENCODER_LIB_VL0.AACENCODER_LIB_VL1.AACENCODER_LIB_VL2) &gt; (4.0.0). </p>
<p> Default value is 0.</p>
<dt><code>signaling</code></dt>
<dd> Set SBR/PS signaling style. </dd>
<p> It can assume one of the following values:</p>
<dl>
<dl>
<dt><code>default</code></dt>
<dd> choose signaling implicitly (explicit hierarchical by default, implicit if global header is disabled)</dd>
<dt><code>implicit</code></dt>
<dd> implicit backwards compatible signaling</dd>
<dt><code>explicit_sbr</code></dt>
<dd> explicit SBR, implicit PS signaling</dd>
<dt><code>explicit_hierarchical</code></dt>
<dd> explicit hierarchical signaling</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>default</code>.</dd></dl>
<dt><code>latm</code></dt>
<dd> Output LATM/LOAS encapsulated data if set to 1, disabled if set to 0. </dd>
<p> Default value is 0.</p>
<dt><code>header_period</code></dt>
<dd> Set StreamMuxConfig and PCE repetition period (in frames) for sending in-band configuration buffers within LATM/LOAS transport layer. </dd>
<p> Must be a 16-bits non-negative integer. </p>
<p> Default value is 0.</p>
<dt><code>vbr</code></dt>
<dd> Set VBR mode, from 1 to 5. 1 is lowest quality (though still pretty good) and 5 is highest quality. A value of 0 will disable VBR, and CBR (Constant Bit Rate) is enabled. </dd>
<p> Currently only the <code>aac_low</code> profile supports VBR encoding. </p>
<p> VBR modes 1-5 correspond to roughly the following average bit rates:</p>
<dl>
<dl>
<dt><code>1</code></dt>
<dd> 32 kbps/channel</dd>
<dt><code>2</code></dt>
<dd> 40 kbps/channel</dd>
<dt><code>3</code></dt>
<dd> 48-56 kbps/channel</dd>
<dt><code>4</code></dt>
<dd> 64 kbps/channel</dd>
<dt><code>5</code></dt>
<dd> about 80-96 kbps/channel</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is 0.</dd></dl>
</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</dt>
<dd> Use <code>ffmpeg</code> to convert an audio file to VBR AAC in an M4A (MP4) container: </dd>
<pre>
        ffmpeg -i input.wav -codec:a libfdk_aac -vbr 3 output.m4a
</pre>
<dt>&bull;</dt>
<dd> Use <code>ffmpeg</code> to convert an audio file to CBR 64k kbps AAC, using the High-Efficiency AAC profile: </dd>
<pre>
        ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he -b:a 64k output.m4a
</pre>
</dl>
<h3>libmp3lame</h3>
<p> LAME (Lame Ain&#8217;t an MP3 Encoder) MP3 encoder wrapper. </p>
<p> Requires the presence of the libmp3lame headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libmp3lame&quot;</tt>. </p>
<p> See <code>libshine</code> for a fixed-point MP3 encoder, although with a lower quality. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libmp3lame wrapper. The <code>lame</code>-equivalent of the options are listed in parentheses.</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></dt>
<dd> Set bitrate expressed in bits/s for CBR or ABR. LAME <tt>&quot;bitrate&quot;</tt> is expressed in kilobits/s.</dd>
<dt><code>q (</code><i>-V</i><code>)</code></dt>
<dd> Set constant quality setting for VBR. This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</dd>
<dt><code>compression_level (</code><i>-q</i><code>)</code></dt>
<dd> Set algorithm quality. Valid arguments are integers in the 0-9 range, with 0 meaning highest quality but slowest, and 9 meaning fastest while producing the worst quality.</dd>
<dt><code>cutoff (</code><i>&#8211;lowpass</i><code>)</code></dt>
<dd> Set lowpass cutoff frequency. If unspecified, the encoder dynamically adjusts the cutoff.</dd>
<dt><code>reservoir</code></dt>
<dd> Enable use of bit reservoir when set to 1. Default value is 1. LAME has this enabled by default, but can be overridden by use <code>&#8211;nores</code> option.</dd>
<dt><code>joint_stereo (</code><i>-m j</i><code>)</code></dt>
<dd> Enable the encoder to use (on a frame by frame basis) either L/R stereo or mid/side stereo. Default value is 1.</dd>
<dt><code>abr (</code><i>&#8211;abr</i><code>)</code></dt>
<dd> Enable the encoder to use ABR when set to 1. The <code>lame</code> <code>&#8211;abr</code> sets the target bitrate, while this options only tells FFmpeg to use ABR still relies on <code>b</code> to set bitrate.</dd></dl>
<h3>libopencore-amrnb</h3>
<p> OpenCORE Adaptive Multi-Rate Narrowband encoder. </p>
<p> Requires the presence of the libopencore-amrnb headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopencore-amrnb --enable-version3&quot;</tt>. </p>
<p> This is a mono-only encoder. Officially it only supports 8000Hz sample rate, but you can override it by setting <code>strict</code> to <code>unofficial</code> or lower. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Set bitrate in bits per second. Only the following bitrates are supported, otherwise libavcodec will round to the nearest valid bitrate.</dd>
<dl>
<dl>
<dt><code>4750</code></dt>
<dd>
</dd><dt><code>5150</code></dt>
<dd>
</dd><dt><code>5900</code></dt>
<dd>
</dd><dt><code>6700</code></dt>
<dd>
</dd><dt><code>7400</code></dt>
<dd>
</dd><dt><code>7950</code></dt>
<dd>
</dd><dt><code>10200</code></dt>
<dd>
</dd><dt><code>12200</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>dtx</code></dt>
<dd> Allow discontinuous transmission (generate comfort noise) when set to 1. The default value is 0 (disabled).</dd></dl>
<h3>libopus</h3>
<p> libopus Opus Interactive Audio Codec encoder wrapper. </p>
<p> Requires the presence of the libopus headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopus&quot;</tt>. </p>
<p> <i>Option Mapping</i> </p>
<p> Most libopus options are modelled after the <code>opusenc</code> utility from opus-tools. The following is an option mapping chart describing options supported by the libopus wrapper, and their <code>opusenc</code>-equivalent in parentheses.</p>
<dl>
<dt><code>b (</code><i>bitrate</i><code>)</code></dt>
<dd> Set the bit rate in bits/s. FFmpeg&#8217;s <code>b</code> option is expressed in bits/s, while <code>opusenc</code>&#8216;s <code>bitrate</code> in kilobits/s.</dd>
<dt><code>vbr (</code><i>vbr</i><code>,</code> <i>hard-cbr</i><code>, and</code> <i>cvbr</i><code>)</code></dt>
<dd> Set VBR mode. The FFmpeg <code>vbr</code> option has the following valid arguments, with the <code>opusenc</code> equivalent options in parentheses:</dd>
<dl>
<dl>
<dt><code>off (</code><i>hard-cbr</i><code>)</code></dt>
<dd> Use constant bit rate encoding.</dd>
<dt><code>on (</code><i>vbr</i><code>)</code></dt>
<dd> Use variable bit rate encoding (the default).</dd>
<dt><code>constrained (</code><i>cvbr</i><code>)</code></dt>
<dd> Use constrained variable bit rate encoding.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>compression_level (</code><i>comp</i><code>)</code></dt>
<dd> Set encoding algorithm complexity. Valid options are integers in the 0-10 range. 0 gives the fastest encodes but lower quality, while 10 gives the highest quality but slowest encoding. The default is 10.</dd>
<dt><code>frame_duration (</code><i>framesize</i><code>)</code></dt>
<dd> Set maximum frame size, or duration of a frame in milliseconds. The argument must be exactly the following: 2.5, 5, 10, 20, 40, 60. Smaller frame sizes achieve lower latency but less quality at a given bitrate. Sizes greater than 20ms are only interesting at fairly low bitrates. The default is 20ms.</dd>
<dt><code>packet_loss (</code><i>expect-loss</i><code>)</code></dt>
<dd> Set expected packet loss percentage. The default is 0.</dd>
<dt><code>fec (</code><i>n/a</i><code>)</code></dt>
<dd> Enable inband forward error correction. <code>packet_loss</code> must be non-zero to take advantage &#8211; frequency of FEC &#8216;side-data&#8217; is proportional to expected packet loss. Default is disabled.</dd>
<dt><code>application (N.A.)</code></dt>
<dd> Set intended application type. Valid options are listed below:</dd>
<dl>
<dl>
<dt><code>voip</code></dt>
<dd> Favor improved speech intelligibility.</dd>
<dt><code>audio</code></dt>
<dd> Favor faithfulness to the input (the default).</dd>
<dt><code>lowdelay</code></dt>
<dd> Restrict to only the lowest delay modes.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>cutoff (N.A.)</code></dt>
<dd> Set cutoff bandwidth in Hz. The argument must be exactly one of the following: 4000, 6000, 8000, 12000, or 20000, corresponding to narrowband, mediumband, wideband, super wideband, and fullband respectively. The default is 0 (cutoff disabled).</dd>
<dt><code>mapping_family (</code><i>mapping_family</i><code>)</code></dt>
<dd> Set channel mapping family to be used by the encoder. The default value of -1 uses mapping family 0 for mono and stereo inputs, and mapping family 1 otherwise. The default also disables the surround masking and LFE bandwidth optimzations in libopus, and requires that the input contains 8 channels or fewer. </dd>
<p> Other values include 0 for mono and stereo, 1 for surround sound with masking and LFE bandwidth optimizations, and 255 for independent streams with an unspecified channel layout.</p>
<dt><code>apply_phase_inv (N.A.) (requires libopus &gt;= 1.2)</code></dt>
<dd> If set to 0, disables the use of phase inversion for intensity stereo, improving the quality of mono downmixes, but slightly reducing normal stereo quality. The default is 1 (phase inversion enabled).</dd></dl>
<h3>libshine</h3>
<p> Shine Fixed-Point MP3 encoder wrapper. </p>
<p> Shine is a fixed-point MP3 encoder. It has a far better performance on platforms without an FPU, e.g. armel CPUs, and some phones and tablets. However, as it is more targeted on performance than quality, it is not on par with LAME and other production-grade encoders quality-wise. Also, according to the project&#8217;s homepage, this encoder may not be free of bugs as the code was written a long time ago and the project was dead for at least 5 years. </p>
<p> This encoder only supports stereo and mono input. This is also CBR-only. </p>
<p> The original project (last updated in early 2007) is at &lt;<code><a rel="nofollow" href="http://sourceforge.net/projects/libshine-fxp/">http://sourceforge.net/projects/libshine-fxp/</a></code>&gt;. We only support the updated fork by the Savonet/Liquidsoap project at &lt;<code><a rel="nofollow" href="https://github.com/savonet/shine">https://github.com/savonet/shine</a></code>&gt;. </p>
<p> Requires the presence of the libshine headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libshine&quot;</tt>. </p>
<p> See also <code>libmp3lame</code>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libshine wrapper. The <code>shineenc</code>-equivalent of the options are listed in parentheses.</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></dt>
<dd> Set bitrate expressed in bits/s for CBR. <code>shineenc</code> <code>-b</code> option is expressed in kilobits/s.</dd></dl>
<h3>libtwolame</h3>
<p> TwoLAME MP2 encoder wrapper. </p>
<p> Requires the presence of the libtwolame headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libtwolame&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libtwolame wrapper. The <code>twolame</code>-equivalent options follow the FFmpeg ones and are in parentheses.</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></dt>
<dd> Set bitrate expressed in bits/s for CBR. <code>twolame</code> <code>b</code> option is expressed in kilobits/s. Default value is 128k.</dd>
<dt><code>q (</code><i>-V</i><code>)</code></dt>
<dd> Set quality for experimental VBR support. Maximum value range is from -50 to 50, useful range is from -10 to 10. The higher the value, the better the quality. This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</dd>
<dt><code>mode (</code><i>&#8211;mode</i><code>)</code></dt>
<dd> Set the mode of the resulting audio. Possible values:</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> Choose mode automatically based on the input. This is the default.</dd>
<dt><code>stereo</code></dt>
<dd> Stereo</dd>
<dt><code>joint_stereo</code></dt>
<dd> Joint stereo</dd>
<dt><code>dual_channel</code></dt>
<dd> Dual channel</dd>
<dt><code>mono</code></dt>
<dd> Mono</dd></dl>
</dl>
<dl>
</dl>
<dt><code>psymodel (</code><i>&#8211;psyc-mode</i><code>)</code></dt>
<dd> Set psychoacoustic model to use in encoding. The argument must be an integer between -1 and 4, inclusive. The higher the value, the better the quality. The default value is 3.</dd>
<dt><code>energy_levels (</code><i>&#8211;energy</i><code>)</code></dt>
<dd> Enable energy levels extensions when set to 1. The default value is 0 (disabled).</dd>
<dt><code>error_protection (</code><i>&#8211;protect</i><code>)</code></dt>
<dd> Enable CRC error protection when set to 1. The default value is 0 (disabled).</dd>
<dt><code>copyright (</code><i>&#8211;copyright</i><code>)</code></dt>
<dd> Set MPEG audio copyright flag when set to 1. The default value is 0 (disabled).</dd>
<dt><code>original (</code><i>&#8211;original</i><code>)</code></dt>
<dd> Set MPEG audio original flag when set to 1. The default value is 0 (disabled).</dd></dl>
<h3>libvo-amrwbenc</h3>
<p> VisualOn Adaptive Multi-Rate Wideband encoder. </p>
<p> Requires the presence of the libvo-amrwbenc headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libvo-amrwbenc --enable-version3&quot;</tt>. </p>
<p> This is a mono-only encoder. Officially it only supports 16000Hz sample rate, but you can override it by setting <code>strict</code> to <code>unofficial</code> or lower. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Set bitrate in bits/s. Only the following bitrates are supported, otherwise libavcodec will round to the nearest valid bitrate.</dd>
<dl>
<dl>
<dt><code>6600</code></dt>
<dd>
</dd><dt><code>8850</code></dt>
<dd>
</dd><dt><code>12650</code></dt>
<dd>
</dd><dt><code>14250</code></dt>
<dd>
</dd><dt><code>15850</code></dt>
<dd>
</dd><dt><code>18250</code></dt>
<dd>
</dd><dt><code>19850</code></dt>
<dd>
</dd><dt><code>23050</code></dt>
<dd>
</dd><dt><code>23850</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>dtx</code></dt>
<dd> Allow discontinuous transmission (generate comfort noise) when set to 1. The default value is 0 (disabled).</dd></dl>
<h3>libvorbis</h3>
<p> libvorbis encoder wrapper. </p>
<p> Requires the presence of the libvorbisenc headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libvorbis&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libvorbis wrapper. The <code>oggenc</code>-equivalent of the options are listed in parentheses. </p>
<p> To get a more accurate and extensive documentation of the libvorbis options, consult the libvorbisenc&#8217;s and <code>oggenc</code>&#8216;s documentations. See &lt;<code><a rel="nofollow" href="http://xiph.org/vorbis/">http://xiph.org/vorbis/</a></code>&gt;, &lt;<code><a rel="nofollow" href="http://wiki.xiph.org/Vorbis-tools">http://wiki.xiph.org/Vorbis-tools</a></code>&gt;, and <code><a href="/docs/linux/man/1-oggenc/">oggenc</a></code>(1).</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></dt>
<dd> Set bitrate expressed in bits/s for ABR. <code>oggenc</code> <code>-b</code> is expressed in kilobits/s.</dd>
<dt><code>q (</code><i>-q</i><code>)</code></dt>
<dd> Set constant quality setting for VBR. The value should be a float number in the range of -1.0 to 10.0. The higher the value, the better the quality. The default value is <code>3.0</code>. </dd>
<p> This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</p>
<dt><code>cutoff (</code><i>&#8211;advanced-encode-option lowpass_frequency=N</i><code>)</code></dt>
<dd> Set cutoff bandwidth in Hz, a value of 0 disables cutoff. <code>oggenc</code>&#8216;s related option is expressed in kHz. The default value is <code>0</code> (cutoff disabled).</dd>
<dt><code>minrate (</code><i>-m</i><code>)</code></dt>
<dd> Set minimum bitrate expressed in bits/s. <code>oggenc</code> <code>-m</code> is expressed in kilobits/s.</dd>
<dt><code>maxrate (</code><i>-M</i><code>)</code></dt>
<dd> Set maximum bitrate expressed in bits/s. <code>oggenc</code> <code>-M</code> is expressed in kilobits/s. This only has effect on ABR mode.</dd>
<dt><code>iblock (</code><i>&#8211;advanced-encode-option impulse_noisetune=N</i><code>)</code></dt>
<dd> Set noise floor bias for impulse blocks. The value is a float number from -15.0 to 0.0. A negative bias instructs the encoder to pay special attention to the crispness of transients in the encoded audio. The tradeoff for better transient response is a higher bitrate.</dd></dl>
<h3>mjpeg</h3>
<p> Motion JPEG encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>huffman</code></dt>
<dd> Set the huffman encoding strategy. Possible values:</dd>
<dl>
<dl>
<dt><code>default</code></dt>
<dd> Use the default huffman tables. This is the default strategy.</dd>
<dt><code>optimal</code></dt>
<dd> Compute and use optimal huffman tables.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>wavpack</h3>
<p> WavPack lossless audio encoder. </p>
<p> <i>Options</i> </p>
<p> The equivalent options for <code>wavpack</code> command line utility are listed in parentheses. </p>
<p> Shared options </p>
<p> The following shared options are effective for this encoder. Only special notes about this particular encoder will be documented here. For the general meaning of the options, see <code>the Codec Options chapter</code>.</p>
<dl>
<dt><code>frame_size (</code><i>&#8211;blocksize</i><code>)</code></dt>
<dd> For this encoder, the range for this option is between 128 and 131072. Default is automatically decided based on sample rate and number of channel. </dd>
<p> For the complete formula of calculating default, see <i>libavcodec/wavpackenc.c</i>.</p>
<dt><code>compression_level (</code><i>-f</i><code>,</code> <i>-h</i><code>,</code> <i>-hh</i><code>, and</code> <i>-x</i><code>)</code></dt>
<dd></dd></dl>
<p> Private options</p>
<dl>
<dt><code>joint_stereo (</code><i>-j</i><code>)</code></dt>
<dd> Set whether to enable joint stereo. Valid values are:</dd>
<dl>
<dl>
<dt><code>on (</code><i>1</i><code>)</code></dt>
<dd> Force mid/side audio encoding.</dd>
<dt><code>off (</code><i>0</i><code>)</code></dt>
<dd> Force left/right audio encoding.</dd>
<dt><code>auto</code></dt>
<dd> Let the encoder decide automatically.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>optimize_mono</code></dt>
<dd> Set whether to enable optimization for mono. This option is only effective for non-mono streams. Available values:</dd>
<dl>
<dl>
<dt><code>on</code></dt>
<dd> enabled</dd>
<dt><code>off</code></dt>
<dd> disabled</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>VIDEO ENCODERS</h2>
<p> A description of some of the currently available video encoders follows.</p>
<h3>GIF</h3>
<p> GIF image/animation encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>gifflags</code> <i>integer</i></dt>
<dd> Sets the flags used for GIF encoding.</dd>
<dl>
<dl>
<dt><code>offsetting</code></dt>
<dd> Enables picture offsetting. </dd>
<p> Default is enabled.</p>
<dt><code>transdiff</code></dt>
<dd> Enables transparency detection between frames. </dd>
<p> Default is enabled.</dl>
</dl>
<dl>
</dl>
<dt><code>gifimage</code> <i>integer</i></dt>
<dd> Enables encoding one full GIF image per frame, rather than an animated GIF. </dd>
<p> Default value is <code>0</code>.</p>
<dt><code>global_palette</code> <i>integer</i></dt>
<dd> Writes a palette to the global GIF header where feasible. </dd>
<p> If disabled, every frame will always have a palette written, even if there is a global palette supplied. </p>
<p> Default value is <code>1</code>.</dl>
<h3>Hap</h3>
<p> Vidvox Hap video encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>format</code> <i>integer</i></dt>
<dd> Specifies the Hap format to encode.</dd>
<dl>
<dl>
<dt><code>hap</code></dt>
<dd>
</dd><dt><code>hap_alpha</code></dt>
<dd>
</dd><dt><code>hap_q</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>hap</code>.</dd></dl>
<dt><code>chunks</code> <i>integer</i></dt>
<dd> Specifies the number of chunks to split frames into, between 1 and 64. This permits multithreaded decoding of large frames, potentially at the cost of data-rate. The encoder may modify this value to divide frames evenly. </dd>
<p> Default value is <i>1</i>.</p>
<dt><code>compressor</code> <i>integer</i></dt>
<dd> Specifies the second-stage compressor to use. If set to <code>none</code>, <code>chunks</code> will be limited to 1, as chunked uncompressed frames offer no benefit.</dd>
<dl>
<dl>
<dt><code>none</code></dt>
<dd>
</dd><dt><code>snappy</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>snappy</code>.</dd></dl>
</dl>
<h3>jpeg2000</h3>
<p> The native jpeg 2000 encoder is lossy by default, the <tt>&quot;-q:v&quot;</tt> option can be used to set the encoding quality. Lossless encoding can be selected with <tt>&quot;-pred 1&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>format</code> <i>integer</i></dt>
<dd> Can be set to either <tt>&quot;j2k&quot;</tt> or <tt>&quot;jp2&quot;</tt> (the default) that makes it possible to store non-rgb pix_fmts.</dd>
<dt><code>tile_width</code> <i>integer</i></dt>
<dd> Sets tile width. Range is 1 to 1073741824. Default is 256.</dd>
<dt><code>tile_height</code> <i>integer</i></dt>
<dd> Sets tile height. Range is 1 to 1073741824. Default is 256.</dd>
<dt><code>pred</code> <i>integer</i></dt>
<dd> Allows setting the discrete wavelet transform (DWT) type</dd>
<dl>
<dl>
<dt><code>dwt97int (Lossy)</code></dt>
<dd>
</dd><dt><code>dwt53 (Lossless)</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default is <tt>&quot;dwt97int&quot;</tt></dd></dl>
<dt><code>sop</code> <i>boolean</i></dt>
<dd> Enable this to add SOP marker at the start of each packet. Disabled by default.</dd>
<dt><code>eph</code> <i>boolean</i></dt>
<dd> Enable this to add EPH marker at the end of each packet header. Disabled by default.</dd>
<dt><code>prog</code> <i>integer</i></dt>
<dd> Sets the progression order to be used by the encoder. Possible values are:</dd>
<dl>
<dl>
<dt><code>lrcp</code></dt>
<dd>
</dd><dt><code>rlcp</code></dt>
<dd>
</dd><dt><code>rpcl</code></dt>
<dd>
</dd><dt><code>pcrl</code></dt>
<dd>
</dd><dt><code>cprl</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Set to <tt>&quot;lrcp&quot;</tt> by default.</dd></dl>
<dt><code>layer_rates</code> <i>string</i></dt>
<dd> By default, when this option is not used, compression is done using the quality metric. This option allows for compression using compression ratio. The compression ratio for each level could be specified. The compression ratio of a layer <tt>&quot;l&quot;</tt> species the what ratio of total file size is contained in the first <tt>&quot;l&quot;</tt> layers. </dd>
<p> Example usage: </p>
<pre>
        ffmpeg -i input.bmp -c:v jpeg2000 -layer_rates &quot;100,10,1&quot; output.j2k
</pre>
<p> This would compress the image to contain 3 layers, where the data contained in the first layer would be compressed by 1000 times, compressed by 100 in the first two layers, and shall contain all data while using all 3 layers.</dl>
<h3>librav1e</h3>
<p> rav1e AV1 encoder wrapper. </p>
<p> Requires the presence of the rav1e headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-librav1e&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>qmax</code></dt>
<dd> Sets the maximum quantizer to use when using bitrate mode.</dd>
<dt><code>qmin</code></dt>
<dd> Sets the minimum quantizer to use when using bitrate mode.</dd>
<dt><code>qp</code></dt>
<dd> Uses quantizer mode to encode at the given quantizer (0-255).</dd>
<dt><code>speed</code></dt>
<dd> Selects the speed preset (0-10) to encode with.</dd>
<dt><code>tiles</code></dt>
<dd> Selects how many tiles to encode with.</dd>
<dt><code>tile-rows</code></dt>
<dd> Selects how many rows of tiles to encode with.</dd>
<dt><code>tile-columns</code></dt>
<dd> Selects how many columns of tiles to encode with.</dd>
<dt><code>rav1e-params</code></dt>
<dd> Set rav1e options using a list of <i>key</i>=<i>value</i> pairs separated by &#8220;:&#8221;. See <code>rav1e &#8211;help</code> for a list of options. </dd>
<p> For example to specify librav1e encoding options with <code>-rav1e-params</code>: </p>
<pre>
        ffmpeg -i input -c:v librav1e -b:v 500K -rav1e-params speed=5:low_latency=true output.mp4
</pre>
</dl>
<h3>libaom-av1</h3>
<p> libaom AV1 encoder wrapper. </p>
<p> Requires the presence of the libaom headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libaom&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The wrapper supports the following standard libavcodec options:</p>
<dl>
<dt><code>b</code></dt>
<dd> Set bitrate target in bits/second. By default this will use variable-bitrate mode. If <code>maxrate</code> and <code>minrate</code> are also set to the same value then it will use constant-bitrate mode, otherwise if <code>crf</code> is set as well then it will use constrained-quality mode.</dd>
<dt><code>g keyint_min</code></dt>
<dd> Set key frame placement. The GOP size sets the maximum distance between key frames; if zero the output stream will be intra-only. The minimum distance is ignored unless it is the same as the GOP size, in which case key frames will always appear at a fixed interval. Not set by default, so without this option the library has completely free choice about where to place key frames.</dd>
<dt><code>qmin qmax</code></dt>
<dd> Set minimum/maximum quantisation values. Valid range is from 0 to 63 (warning: this does not match the quantiser values actually used by AV1 &#8211; divide by four to map real quantiser values to this range). Defaults to min/max (no constraint).</dd>
<dt><code>minrate maxrate bufsize rc_init_occupancy</code></dt>
<dd> Set rate control buffering parameters. Not used if not set &#8211; defaults to unconstrained variable bitrate.</dd>
<dt><code>threads</code></dt>
<dd> Set the number of threads to use while encoding. This may require the <code>tiles</code> or <code>row-mt</code> options to also be set to actually use the specified number of threads fully. Defaults to the number of hardware threads supported by the host machine.</dd>
<dt><code>profile</code></dt>
<dd> Set the encoding profile. Defaults to using the profile which matches the bit depth and chroma subsampling of the input.</dd></dl>
<p> The wrapper also has some specific options:</p>
<dl>
<dt><code>cpu-used</code></dt>
<dd> Set the quality/encoding speed tradeoff. Valid range is from 0 to 8, higher numbers indicating greater speed and lower quality. The default value is 1, which will be slow and high quality.</dd>
<dt><code>auto-alt-ref</code></dt>
<dd> Enable use of alternate reference frames. Defaults to the internal default of the library.</dd>
<dt><code>arnr-max-frames (</code><i>frames</i><code>)</code></dt>
<dd> Set altref noise reduction max frame count. Default is -1.</dd>
<dt><code>arnr-strength (</code><i>strength</i><code>)</code></dt>
<dd> Set altref noise reduction filter strength. Range is -1 to 6. Default is -1.</dd>
<dt><code>aq-mode (</code><i>aq-mode</i><code>)</code></dt>
<dd> Set adaptive quantization mode. Possible values:</dd>
<dl>
<dl>
<dt><code>none (</code><i>0</i><code>)</code></dt>
<dd> Disabled.</dd>
<dt><code>variance (</code><i>1</i><code>)</code></dt>
<dd> Variance-based.</dd>
<dt><code>complexity (</code><i>2</i><code>)</code></dt>
<dd> Complexity-based.</dd>
<dt><code>cyclic (</code><i>3</i><code>)</code></dt>
<dd> Cyclic refresh.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>tune (</code><i>tune</i><code>)</code></dt>
<dd> Set the distortion metric the encoder is tuned with. Default is <tt>&quot;psnr&quot;</tt>.</dd>
<dl>
<dl>
<dt><code>psnr (</code><i>0</i><code>)</code></dt>
<dd>
</dd><dt><code>ssim (</code><i>1</i><code>)</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>lag-in-frames</code></dt>
<dd> Set the maximum number of frames which the encoder may keep in flight at any one time for lookahead purposes. Defaults to the internal default of the library.</dd>
<dt><code>error-resilience</code></dt>
<dd> Enable error resilience features:</dd>
<dl>
<dl>
<dt><code>default</code></dt>
<dd> Improve resilience against losses of whole frames.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Not enabled by default.</dd></dl>
<dt><code>crf</code></dt>
<dd> Set the quality/size tradeoff for constant-quality (no bitrate target) and constrained-quality (with maximum bitrate target) modes. Valid range is 0 to 63, higher numbers indicating lower quality and smaller output size. Only used if set; by default only the bitrate target is used.</dd>
<dt><code>static-thresh</code></dt>
<dd> Set a change threshold on blocks below which they will be skipped by the encoder. Defined in arbitrary units as a nonnegative integer, defaulting to zero (no blocks are skipped).</dd>
<dt><code>drop-threshold</code></dt>
<dd> Set a threshold for dropping frames when close to rate control bounds. Defined as a percentage of the target buffer &#8211; when the rate control buffer falls below this percentage, frames will be dropped until it has refilled above the threshold. Defaults to zero (no frames are dropped).</dd>
<dt><code>denoise-noise-level (</code><i>level</i><code>)</code></dt>
<dd> Amount of noise to be removed for grain synthesis. Grain synthesis is disabled if this option is not set or set to 0.</dd>
<dt><code>denoise-block-size (</code><i>pixels</i><code>)</code></dt>
<dd> Block size used for denoising for grain synthesis. If not set, AV1 codec uses the default value of 32.</dd>
<dt><code>undershoot-pct (</code><i>pct</i><code>)</code></dt>
<dd> Set datarate undershoot (min) percentage of the target bitrate. Range is -1 to 100. Default is -1.</dd>
<dt><code>overshoot-pct (</code><i>pct</i><code>)</code></dt>
<dd> Set datarate overshoot (max) percentage of the target bitrate. Range is -1 to 1000. Default is -1.</dd>
<dt><code>minsection-pct (</code><i>pct</i><code>)</code></dt>
<dd> Minimum percentage variation of the GOP bitrate from the target bitrate. If minsection-pct is not set, the libaomenc wrapper computes it as follows: <tt>&quot;(minrate * 100 / bitrate)&quot;</tt>. Range is -1 to 100. Default is -1 (unset).</dd>
<dt><code>maxsection-pct (</code><i>pct</i><code>)</code></dt>
<dd> Maximum percentage variation of the GOP bitrate from the target bitrate. If maxsection-pct is not set, the libaomenc wrapper computes it as follows: <tt>&quot;(maxrate * 100 / bitrate)&quot;</tt>. Range is -1 to 5000. Default is -1 (unset).</dd>
<dt><code>frame-parallel (</code><i>boolean</i><code>)</code></dt>
<dd> Enable frame parallel decodability features. Default is true.</dd>
<dt><code>tiles</code></dt>
<dd> Set the number of tiles to encode the input video with, as columns x rows. Larger numbers allow greater parallelism in both encoding and decoding, but may decrease coding efficiency. Defaults to the minimum number of tiles required by the size of the input video (this is 1&#215;1 (that is, a single tile) for sizes up to and including 4K).</dd>
<dt><code>tile-columns tile-rows</code></dt>
<dd> Set the number of tiles as log2 of the number of tile rows and columns. Provided for compatibility with libvpx/VP9.</dd>
<dt><code>row-mt (Requires libaom &gt;= 1.0.0-759-g90a15f4f2)</code></dt>
<dd> Enable row based multi-threading. Disabled by default.</dd>
<dt><code>enable-cdef (</code><i>boolean</i><code>)</code></dt>
<dd> Enable Constrained Directional Enhancement Filter. The libaom-av1 encoder enables CDEF by default.</dd>
<dt><code>enable-restoration (</code><i>boolean</i><code>)</code></dt>
<dd> Enable Loop Restoration Filter. Default is true for libaom-av1.</dd>
<dt><code>enable-global-motion (</code><i>boolean</i><code>)</code></dt>
<dd> Enable the use of global motion for block prediction. Default is true.</dd>
<dt><code>enable-intrabc (</code><i>boolean</i><code>)</code></dt>
<dd> Enable block copy mode for intra block prediction. This mode is useful for screen content. Default is true.</dd>
<dt><code>enable-rect-partitions (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable rectangular partitions. Default is true.</dd>
<dt><code>enable-1to4-partitions (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable 1:4/4:1 partitions. Default is true.</dd>
<dt><code>enable-ab-partitions (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable AB shape partitions. Default is true.</dd>
<dt><code>enable-angle-delta (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable angle delta intra prediction. Default is true.</dd>
<dt><code>enable-cfl-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable chroma predicted from luma intra prediction. Default is true.</dd>
<dt><code>enable-filter-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable filter intra predictor. Default is true.</dd>
<dt><code>enable-intra-edge-filter (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable intra edge filter. Default is true.</dd>
<dt><code>enable-smooth-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable smooth intra prediction mode. Default is true.</dd>
<dt><code>enable-paeth-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable paeth predictor in intra prediction. Default is true.</dd>
<dt><code>enable-palette (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable palette prediction mode. Default is true.</dd>
<dt><code>enable-flip-idtx (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable extended transform type, including FLIPADST_DCT, DCT_FLIPADST, FLIPADST_FLIPADST, ADST_FLIPADST, FLIPADST_ADST, IDTX, V_DCT, H_DCT, V_ADST, H_ADST, V_FLIPADST, H_FLIPADST. Default is true.</dd>
<dt><code>enable-tx64 (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable 64-pt transform. Default is true.</dd>
<dt><code>reduced-tx-type-set (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Use reduced set of transform types. Default is false.</dd>
<dt><code>use-intra-dct-only (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Use DCT only for INTRA modes. Default is false.</dd>
<dt><code>use-inter-dct-only (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Use DCT only for INTER modes. Default is false.</dd>
<dt><code>use-intra-default-tx-only (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Use Default-transform only for INTRA modes. Default is false.</dd>
<dt><code>enable-ref-frame-mvs (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable temporal mv prediction. Default is true.</dd>
<dt><code>enable-reduced-reference-set (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Use reduced set of single and compound references. Default is false.</dd>
<dt><code>enable-obmc (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable obmc. Default is true.</dd>
<dt><code>enable-dual-filter (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable dual filter. Default is true.</dd>
<dt><code>enable-diff-wtd-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable difference-weighted compound. Default is true.</dd>
<dt><code>enable-dist-wtd-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable distance-weighted compound. Default is true.</dd>
<dt><code>enable-onesided-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable one sided compound. Default is true.</dd>
<dt><code>enable-interinter-wedge (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable interinter wedge compound. Default is true.</dd>
<dt><code>enable-interintra-wedge (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable interintra wedge compound. Default is true.</dd>
<dt><code>enable-masked-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable masked compound. Default is true.</dd>
<dt><code>enable-interintra-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable interintra compound. Default is true.</dd>
<dt><code>enable-smooth-interintra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></dt>
<dd> Enable smooth interintra mode. Default is true.</dd>
<dt><code>aom-params</code></dt>
<dd> Set libaom options using a list of <i>key</i>=<i>value</i> pairs separated by &#8220;:&#8221;. For a list of supported options, see <code>aomenc &#8211;help</code> under the section &#8220;AV1 Specific Options&#8221;. </dd>
<p> For example to specify libaom encoding options with <code>-aom-params</code>: </p>
<pre>
        ffmpeg -i input -c:v libaom-av1 -b:v 500K -aom-params tune=psnr:enable-tpl-model=1 output.mp4
</pre>
</dl>
<h3>libsvtav1</h3>
<p> SVT-AV1 encoder wrapper. </p>
<p> Requires the presence of the SVT-AV1 headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libsvtav1&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>profile</code></dt>
<dd> Set the encoding profile.</dd>
<dt><code>level</code></dt>
<dd> Set the operating point level.</dd>
<dt><code>tier</code></dt>
<dd> Set the operating point tier.</dd>
<dt><code>rc</code></dt>
<dd> Set the rate control mode to use. </dd>
<p> Possible modes:</p>
<dl>
<dl>
<dt><code>cqp</code></dt>
<dd> Constant quantizer: use fixed values of qindex (dependent on the frame type) throughout the stream. This mode is the default.</dd>
<dt><code>vbr</code></dt>
<dd> Variable bitrate: use a target bitrate for the whole stream.</dd>
<dt><code>cvbr</code></dt>
<dd> Constrained variable bitrate: use a target bitrate for each GOP.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>qmax</code></dt>
<dd> Set the maximum quantizer to use when using a bitrate mode.</dd>
<dt><code>qmin</code></dt>
<dd> Set the minimum quantizer to use when using a bitrate mode.</dd>
<dt><code>qp</code></dt>
<dd> Set the quantizer used in cqp rate control mode (0-63).</dd>
<dt><code>sc_detection</code></dt>
<dd> Enable scene change detection.</dd>
<dt><code>la_depth</code></dt>
<dd> Set number of frames to look ahead (0-120).</dd>
<dt><code>preset</code></dt>
<dd> Set the quality-speed tradeoff, in the range 0 to 8. Higher values are faster but lower quality. Defaults to 8 (highest speed).</dd>
<dt><code>tile_rows</code></dt>
<dd> Set log2 of the number of rows of tiles to use (0-6).</dd>
<dt><code>tile_columns</code></dt>
<dd> Set log2 of the number of columns of tiles to use (0-4).</dd></dl>
<h3>libkvazaar</h3>
<p> Kvazaar H.265/HEVC encoder. </p>
<p> Requires the presence of the libkvazaar headers and library during configuration. You need to explicitly configure the build with <code>&#8211;enable-libkvazaar</code>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Set target video bitrate in bit/s and enable rate control.</dd>
<dt><code>kvazaar-params</code></dt>
<dd> Set kvazaar parameters as a list of <i>name</i>=<i>value</i> pairs separated by commas (,). See kvazaar documentation for a list of options.</dd></dl>
<h3>libopenh264</h3>
<p> Cisco libopenh264 H.264/MPEG-4 AVC encoder wrapper. </p>
<p> This encoder requires the presence of the libopenh264 headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopenh264&quot;</tt>. The library is detected using <code>pkg-config</code>. </p>
<p> For more information about the library see &lt;<code><a rel="nofollow" href="http://www.openh264.org">http://www.openh264.org</a></code>&gt;. </p>
<p> <i>Options</i> </p>
<p> The following FFmpeg global options affect the configurations of the libopenh264 encoder.</p>
<dl>
<dt><code>b</code></dt>
<dd> Set the bitrate (as a number of bits per second).</dd>
<dt><code>g</code></dt>
<dd> Set the GOP size.</dd>
<dt><code>maxrate</code></dt>
<dd> Set the max bitrate (as a number of bits per second).</dd>
<dt><code>flags +global_header</code></dt>
<dd> Set global header in the bitstream.</dd>
<dt><code>slices</code></dt>
<dd> Set the number of slices, used in parallelized encoding. Default value is 0. This is only used when <code>slice_mode</code> is set to <code>fixed</code>.</dd>
<dt><code>slice_mode</code></dt>
<dd> Set slice mode. Can assume one of the following possible values:</dd>
<dl>
<dl>
<dt><code>fixed</code></dt>
<dd> a fixed number of slices</dd>
<dt><code>rowmb</code></dt>
<dd> one slice per row of macroblocks</dd>
<dt><code>auto</code></dt>
<dd> automatic number of slices according to number of threads</dd>
<dt><code>dyn</code></dt>
<dd> dynamic slicing</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Default value is <code>auto</code>.</dd></dl>
<dt><code>loopfilter</code></dt>
<dd> Enable loop filter, if set to 1 (automatically enabled). To disable set a value of 0.</dd>
<dt><code>profile</code></dt>
<dd> Set profile restrictions. If set to the value of <code>main</code> enable CABAC (set the <tt>&quot;SEncParamExt.iEntropyCodingModeFlag&quot;</tt> flag to 1).</dd>
<dt><code>max_nal_size</code></dt>
<dd> Set maximum NAL size in bytes.</dd>
<dt><code>allow_skip_frames</code></dt>
<dd> Allow skipping frames to hit the target bitrate if set to 1.</dd></dl>
<h3>libtheora</h3>
<p> libtheora Theora encoder wrapper. </p>
<p> Requires the presence of the libtheora headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libtheora&quot;</tt>. </p>
<p> For more information about the libtheora project see &lt;<code><a rel="nofollow" href="http://www.theora.org/">http://www.theora.org/</a></code>&gt;. </p>
<p> <i>Options</i> </p>
<p> The following global options are mapped to internal libtheora options which affect the quality and the bitrate of the encoded stream.</p>
<dl>
<dt><code>b</code></dt>
<dd> Set the video bitrate in bit/s for CBR (Constant Bit Rate) mode. In case VBR (Variable Bit Rate) mode is enabled this option is ignored.</dd>
<dt><code>flags</code></dt>
<dd> Used to enable constant quality mode (VBR) encoding through the <code>qscale</code> flag, and to enable the <tt>&quot;pass1&quot;</tt> and <tt>&quot;pass2&quot;</tt> modes.</dd>
<dt><code>g</code></dt>
<dd> Set the GOP size.</dd>
<dt><code>global_quality</code></dt>
<dd> Set the global quality as an integer in lambda units. </dd>
<p> Only relevant when VBR mode is enabled with <tt>&quot;flags +qscale&quot;</tt>. The value is converted to QP units by dividing it by <tt>&quot;FF_QP2LAMBDA&quot;</tt>, clipped in the [0 &#8211; 10] range, and then multiplied by 6.3 to get a value in the native libtheora range [0-63]. A higher value corresponds to a higher quality.</p>
<dt><code>q</code></dt>
<dd> Enable VBR mode when set to a non-negative value, and set constant quality value as a double floating point value in QP units. </dd>
<p> The value is clipped in the [0-10] range, and then multiplied by 6.3 to get a value in the native libtheora range [0-63]. </p>
<p> This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</dt>
<dd> Set maximum constant quality (VBR) encoding with <code>ffmpeg</code>: </dd>
<pre>
        ffmpeg -i INPUT -codec:v libtheora -q:v 10 OUTPUT.ogg
</pre>
<dt>&bull;</dt>
<dd> Use <code>ffmpeg</code> to convert a CBR 1000 kbps Theora video stream: </dd>
<pre>
        ffmpeg -i INPUT -codec:v libtheora -b:v 1000k OUTPUT.ogg
</pre>
</dl>
<h3>libvpx</h3>
<p> VP8/VP9 format supported through libvpx. </p>
<p> Requires the presence of the libvpx headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libvpx&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libvpx wrapper. The <code>vpxenc</code>-equivalent options or values are listed in parentheses for easy migration. </p>
<p> To reduce the duplication of documentation, only the private options and some others requiring special attention are documented here. For the documentation of the undocumented generic options, see <code>the Codec Options chapter</code>. </p>
<p> To get more documentation of the libvpx options, invoke the command <code>ffmpeg -h encoder=libvpx</code>, <code>ffmpeg -h encoder=libvpx-vp9</code> or <code>vpxenc &#8211;help</code>. Further information is available in the libvpx API documentation.</p>
<dl>
<dt><code>b (</code><i>target-bitrate</i><code>)</code></dt>
<dd> Set bitrate in bits/s. Note that FFmpeg&#8217;s <code>b</code> option is expressed in bits/s, while <code>vpxenc</code>&#8216;s <code>target-bitrate</code> is in kilobits/s.</dd>
<dt><code>g (</code><i>kf-max-dist</i><code>)</code></dt>
<dd>
</dd><dt><code>keyint_min (</code><i>kf-min-dist</i><code>)</code></dt>
<dd>
</dd><dt><code>qmin (</code><i>min-q</i><code>)</code></dt>
<dd>
</dd><dt><code>qmax (</code><i>max-q</i><code>)</code></dt>
<dd>
</dd><dt><code>bufsize (</code><i>buf-sz</i><code>,</code> <i>buf-optimal-sz</i><code>)</code></dt>
<dd> Set ratecontrol buffer size (in bits). Note <code>vpxenc</code>&#8216;s options are specified in milliseconds, the libvpx wrapper converts this value as follows: <tt>&quot;buf-sz = bufsize * 1000 / bitrate&quot;</tt>, <tt>&quot;buf-optimal-sz = bufsize * 1000 / bitrate * 5 / 6&quot;</tt>.</dd>
<dt><code>rc_init_occupancy (</code><i>buf-initial-sz</i><code>)</code></dt>
<dd> Set number of bits which should be loaded into the rc buffer before decoding starts. Note <code>vpxenc</code>&#8216;s option is specified in milliseconds, the libvpx wrapper converts this value as follows: <tt>&quot;rc_init_occupancy * 1000 / bitrate&quot;</tt>.</dd>
<dt><code>undershoot-pct</code></dt>
<dd> Set datarate undershoot (min) percentage of the target bitrate.</dd>
<dt><code>overshoot-pct</code></dt>
<dd> Set datarate overshoot (max) percentage of the target bitrate.</dd>
<dt><code>skip_threshold (</code><i>drop-frame</i><code>)</code></dt>
<dd>
</dd><dt><code>qcomp (</code><i>bias-pct</i><code>)</code></dt>
<dd>
</dd><dt><code>maxrate (</code><i>maxsection-pct</i><code>)</code></dt>
<dd> Set GOP max bitrate in bits/s. Note <code>vpxenc</code>&#8216;s option is specified as a percentage of the target bitrate, the libvpx wrapper converts this value as follows: <tt>&quot;(maxrate * 100 / bitrate)&quot;</tt>.</dd>
<dt><code>minrate (</code><i>minsection-pct</i><code>)</code></dt>
<dd> Set GOP min bitrate in bits/s. Note <code>vpxenc</code>&#8216;s option is specified as a percentage of the target bitrate, the libvpx wrapper converts this value as follows: <tt>&quot;(minrate * 100 / bitrate)&quot;</tt>.</dd>
<dt><code>minrate, maxrate, b</code> <i>end-usage=cbr</i></dt>
<dd> <tt>&quot;(minrate == maxrate == bitrate)&quot;</tt>.</dd>
<dt><code>crf (</code><i>end-usage=cq</i><code>,</code> <i>cq-level</i><code>)</code></dt>
<dd>
</dd><dt><code>tune (</code><i>tune</i><code>)</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>psnr (</code><i>psnr</i><code>)</code></dt>
<dd>
</dd><dt><code>ssim (</code><i>ssim</i><code>)</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>quality, deadline (</code><i>deadline</i><code>)</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>best</code></dt>
<dd> Use best quality deadline. Poorly named and quite slow, this option should be avoided as it may give worse quality output than good.</dd>
<dt><code>good</code></dt>
<dd> Use good quality deadline. This is a good trade-off between speed and quality when used with the <code>cpu-used</code> option.</dd>
<dt><code>realtime</code></dt>
<dd> Use realtime quality deadline.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>speed, cpu-used (</code><i>cpu-used</i><code>)</code></dt>
<dd> Set quality/speed ratio modifier. Higher values speed up the encode at the cost of quality.</dd>
<dt><code>nr (</code><i>noise-sensitivity</i><code>)</code></dt>
<dd>
</dd><dt><code>static-thresh</code></dt>
<dd> Set a change threshold on blocks below which they will be skipped by the encoder.</dd>
<dt><code>slices (</code><i>token-parts</i><code>)</code></dt>
<dd> Note that FFmpeg&#8217;s <code>slices</code> option gives the total number of partitions, while <code>vpxenc</code>&#8216;s <code>token-parts</code> is given as <tt>&quot;log2(partitions)&quot;</tt>.</dd>
<dt><code>max-intra-rate</code></dt>
<dd> Set maximum I-frame bitrate as a percentage of the target bitrate. A value of 0 means unlimited.</dd>
<dt><code>force_key_frames</code></dt>
<dd> <tt>&quot;VPX_EFLAG_FORCE_KF&quot;</tt></dd>
<dt><code>Alternate reference frame related</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>auto-alt-ref</code></dt>
<dd> Enable use of alternate reference frames (2-pass only). Values greater than 1 enable multi-layer alternate reference frames (VP9 only).</dd>
<dt><code>arnr-maxframes</code></dt>
<dd> Set altref noise reduction max frame count.</dd>
<dt><code>arnr-type</code></dt>
<dd> Set altref noise reduction filter type: backward, forward, centered.</dd>
<dt><code>arnr-strength</code></dt>
<dd> Set altref noise reduction filter strength.</dd>
<dt><code>rc-lookahead, lag-in-frames (</code><i>lag-in-frames</i><code>)</code></dt>
<dd> Set number of frames to look ahead for frametype and ratecontrol.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>error-resilient</code></dt>
<dd> Enable error resiliency features.</dd>
<dt><code>sharpness</code> <i>integer</i></dt>
<dd> Increase sharpness at the expense of lower PSNR. The valid range is [0, 7].</dd>
<dt><code>ts-parameters</code></dt>
<dd> Sets the temporal scalability configuration using a :-separated list of key=value pairs. For example, to specify temporal scalability parameters with <tt>&quot;ffmpeg&quot;</tt>: </dd>
<pre>
        ffmpeg -i INPUT -c:v libvpx -ts-parameters ts_number_layers=3:\
        ts_target_bitrate=250,500,1000:ts_rate_decimator=4,2,1:\
        ts_periodicity=4:ts_layer_id=0,2,1,2:ts_layering_mode=3 OUTPUT
</pre>
<p> Below is a brief explanation of each of the parameters, please refer to <tt>&quot;struct vpx_codec_enc_cfg&quot;</tt> in <tt>&quot;vpx/vpx_encoder.h&quot;</tt> for more details.</p>
<dl>
<dl>
<dt><code>ts_number_layers</code></dt>
<dd> Number of temporal coding layers.</dd>
<dt><code>ts_target_bitrate</code></dt>
<dd> Target bitrate for each temporal layer (in kbps). (bitrate should be inclusive of the lower temporal layer).</dd>
<dt><code>ts_rate_decimator</code></dt>
<dd> Frame rate decimation factor for each temporal layer.</dd>
<dt><code>ts_periodicity</code></dt>
<dd> Length of the sequence defining frame temporal layer membership.</dd>
<dt><code>ts_layer_id</code></dt>
<dd> Template defining the membership of frames to temporal layers.</dd>
<dt><code>ts_layering_mode</code></dt>
<dd> (optional) Selecting the temporal structure from a set of pre-defined temporal layering modes. Currently supports the following options.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> No temporal layering flags are provided internally, relies on flags being passed in using <tt>&quot;metadata&quot;</tt> field in <tt>&quot;AVFrame&quot;</tt> with following keys.</dd>
<dl>
<dl>
<dt><code>vp8-flags</code></dt>
<dd> Sets the flags passed into the encoder to indicate the referencing scheme for the current frame. Refer to function <tt>&quot;vpx_codec_encode&quot;</tt> in <tt>&quot;vpx/vpx_encoder.h&quot;</tt> for more details.</dd>
<dt><code>temporal_id</code></dt>
<dd> Explicitly sets the temporal id of the current frame to encode.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>2</code></dt>
<dd> Two temporal layers. 0-1&#8230;</dd>
<dt><code>3</code></dt>
<dd> Three temporal layers. 0-2-1-2&#8230;; with single reference frame.</dd>
<dt><code>4</code></dt>
<dd> Same as option &#8220;3&#8221;, except there is a dependency between the two temporal layer 2 frames within the temporal period.</dd></dl>
</dl>
<dl>
</dl>
</dl>
</dl>
<dl>
</dl>
<dt><code>VP9-specific options</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>lossless</code></dt>
<dd> Enable lossless mode.</dd>
<dt><code>tile-columns</code></dt>
<dd> Set number of tile columns to use. Note this is given as <tt>&quot;log2(tile_columns)&quot;</tt>. For example, 8 tile columns would be requested by setting the <code>tile-columns</code> option to 3.</dd>
<dt><code>tile-rows</code></dt>
<dd> Set number of tile rows to use. Note this is given as <tt>&quot;log2(tile_rows)&quot;</tt>. For example, 4 tile rows would be requested by setting the <code>tile-rows</code> option to 2.</dd>
<dt><code>frame-parallel</code></dt>
<dd> Enable frame parallel decodability features.</dd>
<dt><code>aq-mode</code></dt>
<dd> Set adaptive quantization mode (0: off (default), 1: variance 2: complexity, 3: cyclic refresh, 4: equator360).</dd>
<dt><code>colorspace</code> <i>color-space</i></dt>
<dd> Set input color space. The VP9 bitstream supports signaling the following colorspaces:</dd>
<dl>
<dl>
<dt><code>rgb </code>sRGB</dt>
<dd>
</dd><dt><code>bt709 </code>bt709</dt>
<dd>
</dd><dt><code>unspecified </code>unknown</dt>
<dd>
</dd><dt><code>bt470bg </code>bt601</dt>
<dd>
</dd><dt><code>smpte170m </code>smpte170</dt>
<dd>
</dd><dt><code>smpte240m </code>smpte240</dt>
<dd>
</dd><dt><code>bt2020_ncl </code>bt2020</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>row-mt</code> <i>boolean</i></dt>
<dd> Enable row based multi-threading.</dd>
<dt><code>tune-content</code></dt>
<dd> Set content type: default (0), screen (1), film (2).</dd>
<dt><code>corpus-complexity</code></dt>
<dd> Corpus VBR mode is a variant of standard VBR where the complexity distribution midpoint is passed in rather than calculated for a specific clip or chunk. </dd>
<p> The valid range is [0, 10000]. 0 (default) uses standard VBR.</p>
<dt><code>enable-tpl</code> <i>boolean</i></dt>
<dd> Enable temporal dependency model.</dd>
<dt><code>ref-frame-config</code></dt>
<dd> Using per-frame metadata, set members of the structure <tt>&quot;vpx_svc_ref_frame_config_t&quot;</tt> in <tt>&quot;vpx/vp8cx.h&quot;</tt> to fine-control referencing schemes and frame buffer management. Use a :-separated list of key=value pairs. For example, </dd>
<pre>
        av_dict_set(&amp;av_frame-&gt;metadata, &quot;ref-frame-config&quot;, \
        &quot;rfc_update_buffer_slot=7:rfc_lst_fb_idx=0:rfc_gld_fb_idx=1:rfc_alt_fb_idx=2:rfc_reference_last=0:rfc_reference_golden=0:rfc_reference_alt_ref=0&quot;);
</pre>
<dl>
<dl>
<dt><code>rfc_update_buffer_slot</code></dt>
<dd> Indicates the buffer slot number to update</dd>
<dt><code>rfc_update_last</code></dt>
<dd> Indicates whether to update the LAST frame</dd>
<dt><code>rfc_update_golden</code></dt>
<dd> Indicates whether to update GOLDEN frame</dd>
<dt><code>rfc_update_alt_ref</code></dt>
<dd> Indicates whether to update ALT_REF frame</dd>
<dt><code>rfc_lst_fb_idx</code></dt>
<dd> LAST frame buffer index</dd>
<dt><code>rfc_gld_fb_idx</code></dt>
<dd> GOLDEN frame buffer index</dd>
<dt><code>rfc_alt_fb_idx</code></dt>
<dd> ALT_REF frame buffer index</dd>
<dt><code>rfc_reference_last</code></dt>
<dd> Indicates whether to reference LAST frame</dd>
<dt><code>rfc_reference_golden</code></dt>
<dd> Indicates whether to reference GOLDEN frame</dd>
<dt><code>rfc_reference_alt_ref</code></dt>
<dd> Indicates whether to reference ALT_REF frame</dd>
<dt><code>rfc_reference_duration</code></dt>
<dd> Indicates frame duration</dd></dl>
</dl>
<dl>
</dl>
</dl>
</dl>
<dl>
</dl>
</dl>
<p> For more information about libvpx see: &lt;<code><a rel="nofollow" href="http://www.webmproject.org/">http://www.webmproject.org/</a></code>&gt;</p>
<h3>libwebp</h3>
<p> libwebp WebP Image encoder wrapper </p>
<p> libwebp is Google&#8217;s official encoder for WebP images. It can encode in either lossy or lossless mode. Lossy images are essentially a wrapper around a VP8 frame. Lossless images are a separate codec developed by Google. </p>
<p> <i>Pixel Format</i> </p>
<p> Currently, libwebp only supports YUV420 for lossy and RGB for lossless due to limitations of the format and libwebp. Alpha is supported for either mode. Because of API limitations, if RGB is passed in when encoding lossy or YUV is passed in for encoding lossless, the pixel format will automatically be converted using functions from libwebp. This is not ideal and is done only for convenience. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>-lossless</code> <i>boolean</i></dt>
<dd> Enables/Disables use of lossless mode. Default is 0.</dd>
<dt><code>-compression_level</code> <i>integer</i></dt>
<dd> For lossy, this is a quality/speed tradeoff. Higher values give better quality for a given size at the cost of increased encoding time. For lossless, this is a size/speed tradeoff. Higher values give smaller size at the cost of increased encoding time. More specifically, it controls the number of extra algorithms and compression tools used, and varies the combination of these tools. This maps to the <i>method</i> option in libwebp. The valid range is 0 to 6. Default is 4.</dd>
<dt><code>-qscale</code> <i>float</i></dt>
<dd> For lossy encoding, this controls image quality, 0 to 100. For lossless encoding, this controls the effort and time spent at compressing more. The default value is 75. Note that for usage via libavcodec, this option is called <i>global_quality</i> and must be multiplied by <i></i><i>FF_QP2LAMBDA</i><i></i>.</dd>
<dt><code>-preset</code> <i>type</i></dt>
<dd> Configuration preset. This does some automatic settings based on the general type of the image.</dd>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> Do not use a preset.</dd>
<dt><code>default</code></dt>
<dd> Use the encoder default.</dd>
<dt><code>picture</code></dt>
<dd> Digital picture, like portrait, inner shot</dd>
<dt><code>photo</code></dt>
<dd> Outdoor photograph, with natural lighting</dd>
<dt><code>drawing</code></dt>
<dd> Hand or line drawing, with high-contrast details</dd>
<dt><code>icon</code></dt>
<dd> Small-sized colorful images</dd>
<dt><code>text</code></dt>
<dd> Text-like</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>libx264, libx264rgb</h3>
<p> x264 H.264/MPEG-4 AVC encoder wrapper. </p>
<p> This encoder requires the presence of the libx264 headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libx264&quot;</tt>. </p>
<p> libx264 supports an impressive number of features, including 8&#215;8 and 4&#215;4 adaptive spatial transform, adaptive B-frame placement, CAVLC/CABAC entropy coding, interlacing (MBAFF), lossless mode, psy optimizations for detail retention (adaptive quantization, psy-RD, psy-trellis). </p>
<p> Many libx264 encoder options are mapped to FFmpeg global codec options, while unique encoder options are provided through private options. Additionally the <code>x264opts</code> and <code>x264-params</code> private options allows one to pass a list of key=value tuples as accepted by the libx264 <tt>&quot;x264_param_parse&quot;</tt> function. </p>
<p> The x264 project website is at &lt;<code><a rel="nofollow" href="http://www.videolan.org/developers/x264.html">http://www.videolan.org/developers/x264.html</a></code>&gt;. </p>
<p> The libx264rgb encoder is the same as libx264, except it accepts packed RGB pixel formats as input instead of YUV. </p>
<p> <i>Supported Pixel Formats</i> </p>
<p> x264 supports 8- to 10-bit color spaces. The exact bit depth is controlled at x264&#8217;s configure time. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libx264 wrapper. The <code>x264</code>-equivalent options or values are listed in parentheses for easy migration. </p>
<p> To reduce the duplication of documentation, only the private options and some others requiring special attention are documented here. For the documentation of the undocumented generic options, see <code>the Codec Options chapter</code>. </p>
<p> To get a more accurate and extensive documentation of the libx264 options, invoke the command <code>x264 &#8211;fullhelp</code> or consult the libx264 documentation.</p>
<dl>
<dt><code>b (</code><i>bitrate</i><code>)</code></dt>
<dd> Set bitrate in bits/s. Note that FFmpeg&#8217;s <code>b</code> option is expressed in bits/s, while <code>x264</code>&#8216;s <code>bitrate</code> is in kilobits/s.</dd>
<dt><code>bf (</code><i>bframes</i><code>)</code></dt>
<dd>
</dd><dt><code>g (</code><i>keyint</i><code>)</code></dt>
<dd>
</dd><dt><code>qmin (</code><i>qpmin</i><code>)</code></dt>
<dd> Minimum quantizer scale.</dd>
<dt><code>qmax (</code><i>qpmax</i><code>)</code></dt>
<dd> Maximum quantizer scale.</dd>
<dt><code>qdiff (</code><i>qpstep</i><code>)</code></dt>
<dd> Maximum difference between quantizer scales.</dd>
<dt><code>qblur (</code><i>qblur</i><code>)</code></dt>
<dd> Quantizer curve blur</dd>
<dt><code>qcomp (</code><i>qcomp</i><code>)</code></dt>
<dd> Quantizer curve compression factor</dd>
<dt><code>refs (</code><i>ref</i><code>)</code></dt>
<dd> Number of reference frames each P-frame can use. The range is from <i>0-16</i>.</dd>
<dt><code>sc_threshold (</code><i>scenecut</i><code>)</code></dt>
<dd> Sets the threshold for the scene change detection.</dd>
<dt><code>trellis (</code><i>trellis</i><code>)</code></dt>
<dd> Performs Trellis quantization to increase efficiency. Enabled by default.</dd>
<dt><code>nr (</code><i>nr</i><code>)</code></dt>
<dd>
</dd><dt><code>me_range (</code><i>merange</i><code>)</code></dt>
<dd> Maximum range of the motion search in pixels.</dd>
<dt><code>me_method (</code><i>me</i><code>)</code></dt>
<dd> Set motion estimation method. Possible values in the decreasing order of speed:</dd>
<dl>
<dl>
<dt><code>dia (</code><i>dia</i><code>)</code></dt>
<dd>
</dd><dt><code>epzs (</code><i>dia</i><code>)</code></dt>
<dd> Diamond search with radius 1 (fastest). <code>epzs</code> is an alias for <code>dia</code>.</dd>
<dt><code>hex (</code><i>hex</i><code>)</code></dt>
<dd> Hexagonal search with radius 2.</dd>
<dt><code>umh (</code><i>umh</i><code>)</code></dt>
<dd> Uneven multi-hexagon search.</dd>
<dt><code>esa (</code><i>esa</i><code>)</code></dt>
<dd> Exhaustive search.</dd>
<dt><code>tesa (</code><i>tesa</i><code>)</code></dt>
<dd> Hadamard exhaustive search (slowest).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>forced-idr</code></dt>
<dd> Normally, when forcing a I-frame type, the encoder can select any type of I-frame. This option forces it to choose an IDR-frame.</dd>
<dt><code>subq (</code><i>subme</i><code>)</code></dt>
<dd> Sub-pixel motion estimation method.</dd>
<dt><code>b_strategy (</code><i>b-adapt</i><code>)</code></dt>
<dd> Adaptive B-frame placement decision algorithm. Use only on first-pass.</dd>
<dt><code>keyint_min (</code><i>min-keyint</i><code>)</code></dt>
<dd> Minimum GOP size.</dd>
<dt><code>coder</code></dt>
<dd> Set entropy encoder. Possible values:</dd>
<dl>
<dl>
<dt><code>ac</code></dt>
<dd> Enable CABAC.</dd>
<dt><code>vlc</code></dt>
<dd> Enable CAVLC and disable CABAC. It generates the same effect as <code>x264</code>&#8216;s <code>&#8211;no-cabac</code> option.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>cmp</code></dt>
<dd> Set full pixel motion estimation comparison algorithm. Possible values:</dd>
<dl>
<dl>
<dt><code>chroma</code></dt>
<dd> Enable chroma in motion estimation.</dd>
<dt><code>sad</code></dt>
<dd> Ignore chroma in motion estimation. It generates the same effect as <code>x264</code>&#8216;s <code>&#8211;no-chroma-me</code> option.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>threads (</code><i>threads</i><code>)</code></dt>
<dd> Number of encoding threads.</dd>
<dt><code>thread_type</code></dt>
<dd> Set multithreading technique. Possible values:</dd>
<dl>
<dl>
<dt><code>slice</code></dt>
<dd> Slice-based multithreading. It generates the same effect as <code>x264</code>&#8216;s <code>&#8211;sliced-threads</code> option.</dd>
<dt><code>frame</code></dt>
<dd> Frame-based multithreading.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>flags</code></dt>
<dd> Set encoding flags. It can be used to disable closed GOP and enable open GOP by setting it to <tt>&quot;-cgop&quot;</tt>. The result is similar to the behavior of <code>x264</code>&#8216;s <code>&#8211;open-gop</code> option.</dd>
<dt><code>rc_init_occupancy (</code><i>vbv-init</i><code>)</code></dt>
<dd>
</dd><dt><code>preset (</code><i>preset</i><code>)</code></dt>
<dd> Set the encoding preset.</dd>
<dt><code>tune (</code><i>tune</i><code>)</code></dt>
<dd> Set tuning of the encoding params.</dd>
<dt><code>profile (</code><i>profile</i><code>)</code></dt>
<dd> Set profile restrictions.</dd>
<dt><code>fastfirstpass</code></dt>
<dd> Enable fast settings when encoding first pass, when set to 1. When set to 0, it has the same effect of <code>x264</code>&#8216;s <code>&#8211;slow-firstpass</code> option.</dd>
<dt><code>crf (</code><i>crf</i><code>)</code></dt>
<dd> Set the quality for constant quality mode.</dd>
<dt><code>crf_max (</code><i>crf-max</i><code>)</code></dt>
<dd> In CRF mode, prevents VBV from lowering quality beyond this point.</dd>
<dt><code>qp (</code><i>qp</i><code>)</code></dt>
<dd> Set constant quantization rate control method parameter.</dd>
<dt><code>aq-mode (</code><i>aq-mode</i><code>)</code></dt>
<dd> Set AQ method. Possible values:</dd>
<dl>
<dl>
<dt><code>none (</code><i>0</i><code>)</code></dt>
<dd> Disabled.</dd>
<dt><code>variance (</code><i>1</i><code>)</code></dt>
<dd> Variance AQ (complexity mask).</dd>
<dt><code>autovariance (</code><i>2</i><code>)</code></dt>
<dd> Auto-variance AQ (experimental).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>aq-strength (</code><i>aq-strength</i><code>)</code></dt>
<dd> Set AQ strength, reduce blocking and blurring in flat and textured areas.</dd>
<dt><code>psy</code></dt>
<dd> Use psychovisual optimizations when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-psy</code> option.</dd>
<dt><code>psy-rd (</code><i>psy-rd</i><code>)</code></dt>
<dd> Set strength of psychovisual optimization, in <i>psy-rd</i>:<i>psy-trellis</i> format.</dd>
<dt><code>rc-lookahead (</code><i>rc-lookahead</i><code>)</code></dt>
<dd> Set number of frames to look ahead for frametype and ratecontrol.</dd>
<dt><code>weightb</code></dt>
<dd> Enable weighted prediction for B-frames when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-weightb</code> option.</dd>
<dt><code>weightp (</code><i>weightp</i><code>)</code></dt>
<dd> Set weighted prediction method for P-frames. Possible values:</dd>
<dl>
<dl>
<dt><code>none (</code><i>0</i><code>)</code></dt>
<dd> Disabled</dd>
<dt><code>simple (</code><i>1</i><code>)</code></dt>
<dd> Enable only weighted refs</dd>
<dt><code>smart (</code><i>2</i><code>)</code></dt>
<dd> Enable both weighted refs and duplicates</dd></dl>
</dl>
<dl>
</dl>
<dt><code>ssim (</code><i>ssim</i><code>)</code></dt>
<dd> Enable calculation and printing SSIM stats after the encoding.</dd>
<dt><code>intra-refresh (</code><i>intra-refresh</i><code>)</code></dt>
<dd> Enable the use of Periodic Intra Refresh instead of IDR frames when set to 1.</dd>
<dt><code>avcintra-class (</code><i>class</i><code>)</code></dt>
<dd> Configure the encoder to generate AVC-Intra. Valid values are 50,100 and 200</dd>
<dt><code>bluray-compat (</code><i>bluray-compat</i><code>)</code></dt>
<dd> Configure the encoder to be compatible with the bluray standard. It is a shorthand for setting &#8220;bluray-compat=1 force-cfr=1&#8221;.</dd>
<dt><code>b-bias (</code><i>b-bias</i><code>)</code></dt>
<dd> Set the influence on how often B-frames are used.</dd>
<dt><code>b-pyramid (</code><i>b-pyramid</i><code>)</code></dt>
<dd> Set method for keeping of some B-frames as references. Possible values:</dd>
<dl>
<dl>
<dt><code>none (</code><i>none</i><code>)</code></dt>
<dd> Disabled.</dd>
<dt><code>strict (</code><i>strict</i><code>)</code></dt>
<dd> Strictly hierarchical pyramid.</dd>
<dt><code>normal (</code><i>normal</i><code>)</code></dt>
<dd> Non-strict (not Blu-ray compatible).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>mixed-refs</code></dt>
<dd> Enable the use of one reference per partition, as opposed to one reference per macroblock when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-mixed-refs</code> option.</dd>
<dt><code>8x8dct</code></dt>
<dd> Enable adaptive spatial transform (high profile 8&#215;8 transform) when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-8x8dct</code> option.</dd>
<dt><code>fast-pskip</code></dt>
<dd> Enable early SKIP detection on P-frames when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-fast-pskip</code> option.</dd>
<dt><code>aud (</code><i>aud</i><code>)</code></dt>
<dd> Enable use of access unit delimiters when set to 1.</dd>
<dt><code>mbtree</code></dt>
<dd> Enable use macroblock tree ratecontrol when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-mbtree</code> option.</dd>
<dt><code>deblock (</code><i>deblock</i><code>)</code></dt>
<dd> Set loop filter parameters, in <i>alpha</i>:<i>beta</i> form.</dd>
<dt><code>cplxblur (</code><i>cplxblur</i><code>)</code></dt>
<dd> Set fluctuations reduction in QP (before curve compression).</dd>
<dt><code>partitions (</code><i>partitions</i><code>)</code></dt>
<dd> Set partitions to consider as a comma-separated list of. Possible values in the list:</dd>
<dl>
<dl>
<dt><code>p8x8</code></dt>
<dd> 8&#215;8 P-frame partition.</dd>
<dt><code>p4x4</code></dt>
<dd> 4&#215;4 P-frame partition.</dd>
<dt><code>b8x8</code></dt>
<dd> 4&#215;4 B-frame partition.</dd>
<dt><code>i8x8</code></dt>
<dd> 8&#215;8 I-frame partition.</dd>
<dt><code>i4x4</code></dt>
<dd> 4&#215;4 I-frame partition. (Enabling <code>p4x4</code> requires <code>p8x8</code> to be enabled. Enabling <code>i8x8</code> requires adaptive spatial transform (<code>8x8dct</code> option) to be enabled.)</dd>
<dt><code>none (</code><i>none</i><code>)</code></dt>
<dd> Do not consider any partitions.</dd>
<dt><code>all (</code><i>all</i><code>)</code></dt>
<dd> Consider every partition.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>direct-pred (</code><i>direct</i><code>)</code></dt>
<dd> Set direct MV prediction mode. Possible values:</dd>
<dl>
<dl>
<dt><code>none (</code><i>none</i><code>)</code></dt>
<dd> Disable MV prediction.</dd>
<dt><code>spatial (</code><i>spatial</i><code>)</code></dt>
<dd> Enable spatial predicting.</dd>
<dt><code>temporal (</code><i>temporal</i><code>)</code></dt>
<dd> Enable temporal predicting.</dd>
<dt><code>auto (</code><i>auto</i><code>)</code></dt>
<dd> Automatically decided.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>slice-max-size (</code><i>slice-max-size</i><code>)</code></dt>
<dd> Set the limit of the size of each slice in bytes. If not specified but RTP payload size (<code>ps</code>) is specified, that is used.</dd>
<dt><code>stats (</code><i>stats</i><code>)</code></dt>
<dd> Set the file name for multi-pass stats.</dd>
<dt><code>nal-hrd (</code><i>nal-hrd</i><code>)</code></dt>
<dd> Set signal HRD information (requires <code>vbv-bufsize</code> to be set). Possible values:</dd>
<dl>
<dl>
<dt><code>none (</code><i>none</i><code>)</code></dt>
<dd> Disable HRD information signaling.</dd>
<dt><code>vbr (</code><i>vbr</i><code>)</code></dt>
<dd> Variable bit rate.</dd>
<dt><code>cbr (</code><i>cbr</i><code>)</code></dt>
<dd> Constant bit rate (not allowed in MP4 container).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>x264opts (N.A.)</code></dt>
<dd> Set any x264 option, see <code>x264 &#8211;fullhelp</code> for a list. </dd>
<p> Argument is a list of <i>key</i>=<i>value</i> couples separated by &#8220;:&#8221;. In <i>filter</i> and <i>psy-rd</i> options that use &#8220;:&#8221; as a separator themselves, use &#8220;,&#8221; instead. They accept it as well since long ago but this is kept undocumented for some reason. </p>
<p> For example to specify libx264 encoding options with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i foo.mpg -c:v libx264 -x264opts keyint=123:min-keyint=20 -an out.mkv
</pre>
<dt><code>a53cc</code> <i>boolean</i></dt>
<dd> Import closed captions (which must be ATSC compatible format) into output. Only the mpeg2 and h264 decoders provide these. Default is 1 (on).</dd>
<dt><code>x264-params (N.A.)</code></dt>
<dd> Override the x264 configuration using a :-separated list of key=value parameters. </dd>
<p> This option is functionally the same as the <code>x264opts</code>, but is duplicated for compatibility with the Libav fork. </p>
<p> For example to specify libx264 encoding options with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i INPUT -c:v libx264 -x264-params level=30:bframes=0:weightp=0:\
        cabac=0:ref=1:vbv-maxrate=768:vbv-bufsize=2000:analyse=all:me=umh:\
        no-fast-pskip=1:subq=6:8x8dct=0:trellis=0 OUTPUT
</pre>
</dl>
<p> Encoding ffpresets for common usages are provided so they can be used with the general presets system (e.g. passing the <code>pre</code> option).</p>
<h3>libx265</h3>
<p> x265 H.265/HEVC encoder wrapper. </p>
<p> This encoder requires the presence of the libx265 headers and library during configuration. You need to explicitly configure the build with <code>&#8211;enable-libx265</code>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Sets target video bitrate.</dd>
<dt><code>bf</code></dt>
<dd>
</dd><dt><code>g</code></dt>
<dd> Set the GOP size.</dd>
<dt><code>keyint_min</code></dt>
<dd> Minimum GOP size.</dd>
<dt><code>refs</code></dt>
<dd> Number of reference frames each P-frame can use. The range is from <i>1-16</i>.</dd>
<dt><code>preset</code></dt>
<dd> Set the x265 preset.</dd>
<dt><code>tune</code></dt>
<dd> Set the x265 tune parameter.</dd>
<dt><code>profile</code></dt>
<dd> Set profile restrictions.</dd>
<dt><code>crf</code></dt>
<dd> Set the quality for constant quality mode.</dd>
<dt><code>qp</code></dt>
<dd> Set constant quantization rate control method parameter.</dd>
<dt><code>qmin</code></dt>
<dd> Minimum quantizer scale.</dd>
<dt><code>qmax</code></dt>
<dd> Maximum quantizer scale.</dd>
<dt><code>qdiff</code></dt>
<dd> Maximum difference between quantizer scales.</dd>
<dt><code>qblur</code></dt>
<dd> Quantizer curve blur</dd>
<dt><code>qcomp</code></dt>
<dd> Quantizer curve compression factor</dd>
<dt><code>i_qfactor</code></dt>
<dd>
</dd><dt><code>b_qfactor</code></dt>
<dd>
</dd><dt><code>forced-idr</code></dt>
<dd> Normally, when forcing a I-frame type, the encoder can select any type of I-frame. This option forces it to choose an IDR-frame.</dd>
<dt><code>x265-params</code></dt>
<dd> Set x265 options using a list of <i>key</i>=<i>value</i> couples separated by &#8220;:&#8221;. See <code>x265 &#8211;help</code> for a list of options. </dd>
<p> For example to specify libx265 encoding options with <code>-x265-params</code>: </p>
<pre>
        ffmpeg -i input -c:v libx265 -x265-params crf=26:psy-rd=1 output.mp4
</pre>
</dl>
<h3>libxavs2</h3>
<p> xavs2 AVS2-P2/IEEE1857.4 encoder wrapper. </p>
<p> This encoder requires the presence of the libxavs2 headers and library during configuration. You need to explicitly configure the build with <code>&#8211;enable-libxavs2</code>. </p>
<p> The following standard libavcodec options are used:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>b</code> / <code>bit_rate</code></dd>
<dt>&bull;</dt>
<dd> <code>g</code> / <code>gop_size</code></dd>
<dt>&bull;</dt>
<dd> <code>bf</code> / <code>max_b_frames</code></dd></dl>
<p> The encoder also has its own specific options: </p>
<p> <i>Options</i></p>
<dl>
<dt><code>lcu_row_threads</code></dt>
<dd> Set the number of parallel threads for rows from 1 to 8 (default 5).</dd>
<dt><code>initial_qp</code></dt>
<dd> Set the xavs2 quantization parameter from 1 to 63 (default 34). This is used to set the initial qp for the first frame.</dd>
<dt><code>qp</code></dt>
<dd> Set the xavs2 quantization parameter from 1 to 63 (default 34). This is used to set the qp value under constant-QP mode.</dd>
<dt><code>max_qp</code></dt>
<dd> Set the max qp for rate control from 1 to 63 (default 55).</dd>
<dt><code>min_qp</code></dt>
<dd> Set the min qp for rate control from 1 to 63 (default 20).</dd>
<dt><code>speed_level</code></dt>
<dd> Set the Speed level from 0 to 9 (default 0). Higher is better but slower.</dd>
<dt><code>log_level</code></dt>
<dd> Set the log level from -1 to 3 (default 0). -1: none, 0: error, 1: warning, 2: info, 3: debug.</dd>
<dt><code>xavs2-params</code></dt>
<dd> Set xavs2 options using a list of <i>key</i>=<i>value</i> couples separated by &#8220;:&#8221;. </dd>
<p> For example to specify libxavs2 encoding options with <code>-xavs2-params</code>: </p>
<pre>
        ffmpeg -i input -c:v libxavs2 -xavs2-params RdoqLevel=0 output.avs2
</pre>
</dl>
<h3>libxvid</h3>
<p> Xvid MPEG-4 Part 2 encoder wrapper. </p>
<p> This encoder requires the presence of the libxvidcore headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libxvid --enable-gpl&quot;</tt>. </p>
<p> The native <tt>&quot;mpeg4&quot;</tt> encoder supports the MPEG-4 Part 2 format, so users can encode to this format without this library. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libxvid wrapper. Some of the following options are listed but are not documented, and correspond to shared codec options. See <code>the Codec Options chapter</code> for their documentation. The other shared options which are not listed have no effect for the libxvid encoder.</p>
<dl>
<dt><code>b</code></dt>
<dd>
</dd><dt><code>g</code></dt>
<dd>
</dd><dt><code>qmin</code></dt>
<dd>
</dd><dt><code>qmax</code></dt>
<dd>
</dd><dt><code>mpeg_quant</code></dt>
<dd>
</dd><dt><code>threads</code></dt>
<dd>
</dd><dt><code>bf</code></dt>
<dd>
</dd><dt><code>b_qfactor</code></dt>
<dd>
</dd><dt><code>b_qoffset</code></dt>
<dd>
</dd><dt><code>flags</code></dt>
<dd> Set specific encoding flags. Possible values:</dd>
<dl>
<dl>
<dt><code>mv4</code></dt>
<dd> Use four motion vector by macroblock.</dd>
<dt><code>aic</code></dt>
<dd> Enable high quality AC prediction.</dd>
<dt><code>gray</code></dt>
<dd> Only encode grayscale.</dd>
<dt><code>gmc</code></dt>
<dd> Enable the use of global motion compensation (GMC).</dd>
<dt><code>qpel</code></dt>
<dd> Enable quarter-pixel motion compensation.</dd>
<dt><code>cgop</code></dt>
<dd> Enable closed GOP.</dd>
<dt><code>global_header</code></dt>
<dd> Place global headers in extradata instead of every keyframe.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>trellis</code></dt>
<dd>
</dd><dt><code>me_method</code></dt>
<dd> Set motion estimation method. Possible values in decreasing order of speed and increasing order of quality:</dd>
<dl>
<dl>
<dt><code>zero</code></dt>
<dd> Use no motion estimation (default).</dd>
<dt><code>phods</code></dt>
<dd>
</dd><dt><code>x1</code></dt>
<dd>
</dd><dt><code>log</code></dt>
<dd> Enable advanced diamond zonal search for 16&#215;16 blocks and half-pixel refinement for 16&#215;16 blocks. <code>x1</code> and <code>log</code> are aliases for <code>phods</code>.</dd>
<dt><code>epzs</code></dt>
<dd> Enable all of the things described above, plus advanced diamond zonal search for 8&#215;8 blocks, half-pixel refinement for 8&#215;8 blocks, and motion estimation on chroma planes.</dd>
<dt><code>full</code></dt>
<dd> Enable all of the things described above, plus extended 16&#215;16 and 8&#215;8 blocks search.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>mbd</code></dt>
<dd> Set macroblock decision algorithm. Possible values in the increasing order of quality:</dd>
<dl>
<dl>
<dt><code>simple</code></dt>
<dd> Use macroblock comparing function algorithm (default).</dd>
<dt><code>bits</code></dt>
<dd> Enable rate distortion-based half pixel and quarter pixel refinement for 16&#215;16 blocks.</dd>
<dt><code>rd</code></dt>
<dd> Enable all of the things described above, plus rate distortion-based half pixel and quarter pixel refinement for 8&#215;8 blocks, and rate distortion-based search using square pattern.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>lumi_aq</code></dt>
<dd> Enable lumi masking adaptive quantization when set to 1. Default is 0 (disabled).</dd>
<dt><code>variance_aq</code></dt>
<dd> Enable variance adaptive quantization when set to 1. Default is 0 (disabled). </dd>
<p> When combined with <code>lumi_aq</code>, the resulting quality will not be better than any of the two specified individually. In other words, the resulting quality will be the worse one of the two effects.</p>
<dt><code>ssim</code></dt>
<dd> Set structural similarity (SSIM) displaying method. Possible values:</dd>
<dl>
<dl>
<dt><code>off</code></dt>
<dd> Disable displaying of SSIM information.</dd>
<dt><code>avg</code></dt>
<dd> Output average SSIM at the end of encoding to stdout. The format of showing the average SSIM is: </dd>
<pre>
        Average SSIM: %f
</pre>
<p> For users who are not familiar with C, <tt>%f</tt> means a float number, or a decimal (e.g. 0.939232).</p>
<dt><code>frame</code></dt>
<dd> Output both per-frame SSIM data during encoding and average SSIM at the end of encoding to stdout. The format of per-frame information is: </dd>
<pre>
               SSIM: avg: %1.3f min: %1.3f max: %1.3f
</pre>
<p> For users who are not familiar with C, <tt>%1</tt>.3f means a float number rounded to 3 digits after the dot (e.g. 0.932).</dl>
</dl>
<dl>
</dl>
<dt><code>ssim_acc</code></dt>
<dd> Set SSIM accuracy. Valid options are integers within the range of 0-4, while 0 gives the most accurate result and 4 computes the fastest.</dd></dl>
<h3>MediaFoundation</h3>
<p> This provides wrappers to encoders (both audio and video) in the MediaFoundation framework. It can access both SW and HW encoders. Video encoders can take input in either of nv12 or yuv420p form (some encoders support both, some support only either &#8211; in practice, nv12 is the safer choice, especially among HW encoders).</p>
<h3>mpeg2</h3>
<p> MPEG-2 video encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>profile</code></dt>
<dd> Select the mpeg2 profile to encode:</dd>
<dl>
<dl>
<dt><code>422</code></dt>
<dd>
</dd><dt><code>high</code></dt>
<dd>
</dd><dt><code>ss</code></dt>
<dd> Spatially Scalable</dd>
<dt><code>snr</code></dt>
<dd> SNR Scalable</dd>
<dt><code>main</code></dt>
<dd>
</dd><dt><code>simple</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>level</code></dt>
<dd> Select the mpeg2 level to encode:</dd>
<dl>
<dl>
<dt><code>high</code></dt>
<dd>
</dd><dt><code>high1440</code></dt>
<dd>
</dd><dt><code>main</code></dt>
<dd>
</dd><dt><code>low</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>seq_disp_ext</code> <i>integer</i></dt>
<dd> Specifies if the encoder should write a sequence_display_extension to the output.</dd>
<dl>
<dl>
<dt><code>-1</code></dt>
<dd>
</dd><dt><code>auto</code></dt>
<dd> Decide automatically to write it or not (this is the default) by checking if the data to be written is different from the default or unspecified values.</dd>
<dt><code>0</code></dt>
<dd>
</dd><dt><code>never</code></dt>
<dd> Never write it.</dd>
<dt><code>1</code></dt>
<dd>
</dd><dt><code>always</code></dt>
<dd> Always write it.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>video_format</code> <i>integer</i></dt>
<dd> Specifies the video_format written into the sequence display extension indicating the source of the video pictures. The default is <code>unspecified</code>, can be <code>component</code>, <code>pal</code>, <code>ntsc</code>, <code>secam</code> or <code>mac</code>. For maximum compatibility, use <code>component</code>.</dd>
<dt><code>a53cc</code> <i>boolean</i></dt>
<dd> Import closed captions (which must be ATSC compatible format) into output. Default is 1 (on).</dd></dl>
<h3>png</h3>
<p> PNG image encoder. </p>
<p> <i>Private options</i></p>
<dl>
<dt><code>dpi</code> <i>integer</i></dt>
<dd> Set physical density of pixels, in dots per inch, unset by default</dd>
<dt><code>dpm</code> <i>integer</i></dt>
<dd> Set physical density of pixels, in dots per meter, unset by default</dd></dl>
<h3>ProRes</h3>
<p> Apple ProRes encoder. </p>
<p> FFmpeg contains 2 ProRes encoders, the prores-aw and prores-ks encoder. The used encoder can be chosen with the <tt>&quot;-vcodec&quot;</tt> option. </p>
<p> <i>Private Options for prores-ks</i></p>
<dl>
<dt><code>profile</code> <i>integer</i></dt>
<dd> Select the ProRes profile to encode</dd>
<dl>
<dl>
<dt><code>proxy</code></dt>
<dd>
</dd><dt><code>lt</code></dt>
<dd>
</dd><dt><code>standard</code></dt>
<dd>
</dd><dt><code>hq</code></dt>
<dd>
</dd><dt><code>4444</code></dt>
<dd>
</dd><dt><code>4444xq</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>quant_mat</code> <i>integer</i></dt>
<dd> Select quantization matrix.</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd>
</dd><dt><code>default</code></dt>
<dd>
</dd><dt><code>proxy</code></dt>
<dd>
</dd><dt><code>lt</code></dt>
<dd>
</dd><dt><code>standard</code></dt>
<dd>
</dd><dt><code>hq</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> If set to <i>auto</i>, the matrix matching the profile will be picked. If not set, the matrix providing the highest quality, <i>default</i>, will be picked.</dd></dl>
<dt><code>bits_per_mb</code> <i>integer</i></dt>
<dd> How many bits to allot for coding one macroblock. Different profiles use between 200 and 2400 bits per macroblock, the maximum is 8000.</dd>
<dt><code>mbs_per_slice</code> <i>integer</i></dt>
<dd> Number of macroblocks in each slice (1-8); the default value (8) should be good in almost all situations.</dd>
<dt><code>vendor</code> <i>string</i></dt>
<dd> Override the 4-byte vendor ID. A custom vendor ID like <i>apl0</i> would claim the stream was produced by the Apple encoder.</dd>
<dt><code>alpha_bits</code> <i>integer</i></dt>
<dd> Specify number of bits for alpha component. Possible values are <i>0</i>, <i>8</i> and <i>16</i>. Use <i>0</i> to disable alpha plane coding.</dd></dl>
<p> <i>Speed considerations</i> </p>
<p> In the default mode of operation the encoder has to honor frame constraints (i.e. not produce frames with size bigger than requested) while still making output picture as good as possible. A frame containing a lot of small details is harder to compress and the encoder would spend more time searching for appropriate quantizers for each slice. </p>
<p> Setting a higher <code>bits_per_mb</code> limit will improve the speed. </p>
<p> For the fastest encoding speed set the <code>qscale</code> parameter (4 is the recommended value) and do not set a size constraint.</p>
<h3>QSV encoders</h3>
<p> The family of Intel QuickSync Video encoders (MPEG-2, H.264, HEVC, JPEG/MJPEG and VP9) </p>
<p> The ratecontrol method is selected as follows:</p>
<dl>
<dt>&bull;</dt>
<dd> When <code>global_quality</code> is specified, a quality-based mode is used. Specifically this means either</dd>
<dl>
<dl>
<dt>&#8211;</dt>
<dd> <i></i><i>CQP</i><i></i> &#8211; constant quantizer scale, when the <code>qscale</code> codec flag is also set (the <code>-qscale</code> ffmpeg option).</dd>
<dt>&#8211;</dt>
<dd> <i></i><i>LA_ICQ</i><i></i> &#8211; intelligent constant quality with lookahead, when the <code>look_ahead</code> option is also set.</dd>
<dt>&#8211;</dt>
<dd> <i></i><i>ICQ</i><i></i> &#8212; intelligent constant quality otherwise.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> Otherwise, a bitrate-based mode is used. For all of those, you should specify at least the desired average bitrate with the <code>b</code> option.</dd>
<dl>
<dl>
<dt>&#8211;</dt>
<dd> <i></i><i>LA</i><i></i> &#8211; VBR with lookahead, when the <code>look_ahead</code> option is specified.</dd>
<dt>&#8211;</dt>
<dd> <i></i><i>VCM</i><i></i> &#8211; video conferencing mode, when the <code>vcm</code> option is set.</dd>
<dt>&#8211;</dt>
<dd> <i></i><i>CBR</i><i></i> &#8211; constant bitrate, when <code>maxrate</code> is specified and equal to the average bitrate.</dd>
<dt>&#8211;</dt>
<dd> <i></i><i>VBR</i><i></i> &#8211; variable bitrate, when <code>maxrate</code> is specified, but is higher than the average bitrate.</dd>
<dt>&#8211;</dt>
<dd> <i></i><i>AVBR</i><i></i> &#8211; average VBR mode, when <code>maxrate</code> is not specified. This mode is further configured by the <code>avbr_accuracy</code> and <code>avbr_convergence</code> options.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Note that depending on your system, a different mode than the one you specified may be selected by the encoder. Set the verbosity level to <i>verbose</i> or higher to see the actual settings used by the QSV runtime. </p>
<p> Additional libavcodec global options are mapped to MSDK options as follows:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>g/gop_size</code> -&gt; <code>GopPicSize</code></dd>
<dt>&bull;</dt>
<dd> <code>bf/max_b_frames</code>+1 -&gt; <code>GopRefDist</code></dd>
<dt>&bull;</dt>
<dd> <code>rc_init_occupancy/rc_initial_buffer_occupancy</code> -&gt; <code>InitialDelayInKB</code></dd>
<dt>&bull;</dt>
<dd> <code>slices</code> -&gt; <code>NumSlice</code></dd>
<dt>&bull;</dt>
<dd> <code>refs</code> -&gt; <code>NumRefFrame</code></dd>
<dt>&bull;</dt>
<dd> <code>b_strategy/b_frame_strategy</code> -&gt; <code>BRefType</code></dd>
<dt>&bull;</dt>
<dd> <code>cgop/CLOSED_GOP</code> codec flag -&gt; <code>GopOptFlag</code></dd>
<dt>&bull;</dt>
<dd> For the <i></i><i>CQP</i><i></i> mode, the <code>i_qfactor/i_qoffset</code> and <code>b_qfactor/b_qoffset</code> set the difference between <i></i><i>QPP</i><i></i> and <i></i><i>QPI</i><i></i>, and <i></i><i>QPP</i><i></i> and <i></i><i>QPB</i><i></i> respectively.</dd>
<dt>&bull;</dt>
<dd> Setting the <code>coder</code> option to the value <i>vlc</i> will make the H.264 encoder use CAVLC instead of CABAC.</dd></dl>
<h3>snow</h3>
<p> <i>Options</i></p>
<dl>
<dt><code>iterative_dia_size</code></dt>
<dd> dia size for the iterative motion estimation</dd></dl>
<h3>VAAPI encoders</h3>
<p> Wrappers for hardware encoders accessible via VAAPI. </p>
<p> These encoders only accept input in VAAPI hardware surfaces. If you have input in software frames, use the <code>hwupload</code> filter to upload them to the GPU. </p>
<p> The following standard libavcodec options are used:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>g</code> / <code>gop_size</code></dd>
<dt>&bull;</dt>
<dd> <code>bf</code> / <code>max_b_frames</code></dd>
<dt>&bull;</dt>
<dd> <code>profile</code> </dd>
<p> If not set, this will be determined automatically from the format of the input frames and the profiles supported by the driver.</p>
<dt>&bull;</dt>
<dd> <code>level</code></dd>
<dt>&bull;</dt>
<dd> <code>b</code> / <code>bit_rate</code></dd>
<dt>&bull;</dt>
<dd> <code>maxrate</code> / <code>rc_max_rate</code></dd>
<dt>&bull;</dt>
<dd> <code>bufsize</code> / <code>rc_buffer_size</code></dd>
<dt>&bull;</dt>
<dd> <code>rc_init_occupancy</code> / <code>rc_initial_buffer_occupancy</code></dd>
<dt>&bull;</dt>
<dd> <code>compression_level</code> </dd>
<p> Speed / quality tradeoff: higher values are faster / worse quality.</p>
<dt>&bull;</dt>
<dd> <code>q</code> / <code>global_quality</code> </dd>
<p> Size / quality tradeoff: higher values are smaller / worse quality.</p>
<dt>&bull;</dt>
<dd> <code>qmin</code></dd>
<dt>&bull;</dt>
<dd> <code>qmax</code></dd>
<dt>&bull;</dt>
<dd> <code>i_qfactor</code> / <code>i_quant_factor</code></dd>
<dt>&bull;</dt>
<dd> <code>i_qoffset</code> / <code>i_quant_offset</code></dd>
<dt>&bull;</dt>
<dd> <code>b_qfactor</code> / <code>b_quant_factor</code></dd>
<dt>&bull;</dt>
<dd> <code>b_qoffset</code> / <code>b_quant_offset</code></dd>
<dt>&bull;</dt>
<dd> <code>slices</code></dd></dl>
<p> All encoders support the following options:</p>
<dl>
<dt><code>low_power</code></dt>
<dd> Some drivers/platforms offer a second encoder for some codecs intended to use less power than the default encoder; setting this option will attempt to use that encoder. Note that it may support a reduced feature set, so some other options may not be available in this mode.</dd>
<dt><code>idr_interval</code></dt>
<dd> Set the number of normal intra frames between full-refresh (IDR) frames in open-GOP mode. The intra frames are still IRAPs, but will not include global headers and may have non-decodable leading pictures.</dd>
<dt><code>b_depth</code></dt>
<dd> Set the B-frame reference depth. When set to one (the default), all B-frames will refer only to P- or I-frames. When set to greater values multiple layers of B-frames will be present, frames in each layer only referring to frames in higher layers.</dd>
<dt><code>rc_mode</code></dt>
<dd> Set the rate control mode to use. A given driver may only support a subset of modes. </dd>
<p> Possible modes:</p>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> Choose the mode automatically based on driver support and the other options. This is the default.</dd>
<dt><code>CQP</code></dt>
<dd> Constant-quality.</dd>
<dt><code>CBR</code></dt>
<dd> Constant-bitrate.</dd>
<dt><code>VBR</code></dt>
<dd> Variable-bitrate.</dd>
<dt><code>ICQ</code></dt>
<dd> Intelligent constant-quality.</dd>
<dt><code>QVBR</code></dt>
<dd> Quality-defined variable-bitrate.</dd>
<dt><code>AVBR</code></dt>
<dd> Average variable bitrate.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Each encoder also has its own specific options:</p>
<dl>
<dt><code>h264_vaapi</code></dt>
<dd> <code>profile</code> sets the value of <i>profile_idc</i> and the <i>constraint_set*_flag</i>s. <code>level</code> sets the value of <i>level_idc</i>.</dd>
<dl>
<dl>
<dt><code>coder</code></dt>
<dd> Set entropy encoder (default is <i>cabac</i>). Possible values:</dd>
<dl>
<dl>
<dt><code>ac</code></dt>
<dd>
</dd><dt><code>cabac</code></dt>
<dd> Use CABAC.</dd>
<dt><code>vlc</code></dt>
<dd>
</dd><dt><code>cavlc</code></dt>
<dd> Use CAVLC.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>aud</code></dt>
<dd> Include access unit delimiters in the stream (not included by default).</dd>
<dt><code>sei</code></dt>
<dd> Set SEI message types to include. Some combination of the following values:</dd>
<dl>
<dl>
<dt><code>identifier</code></dt>
<dd> Include a <i>user_data_unregistered</i> message containing information about the encoder.</dd>
<dt><code>timing</code></dt>
<dd> Include picture timing parameters (<i>buffering_period</i> and <i>pic_timing</i> messages).</dd>
<dt><code>recovery_point</code></dt>
<dd> Include recovery points where appropriate (<i>recovery_point</i> messages).</dd></dl>
</dl>
<dl>
</dl>
</dl>
</dl>
<dl>
</dl>
<dt><code>hevc_vaapi</code></dt>
<dd> <code>profile</code> and <code>level</code> set the values of <i>general_profile_idc</i> and <i>general_level_idc</i> respectively.</dd>
<dl>
<dl>
<dt><code>aud</code></dt>
<dd> Include access unit delimiters in the stream (not included by default).</dd>
<dt><code>tier</code></dt>
<dd> Set <i>general_tier_flag</i>. This may affect the level chosen for the stream if it is not explicitly specified.</dd>
<dt><code>sei</code></dt>
<dd> Set SEI message types to include. Some combination of the following values:</dd>
<dl>
<dl>
<dt><code>hdr</code></dt>
<dd> Include HDR metadata if the input frames have it (<i>mastering_display_colour_volume</i> and <i>content_light_level</i> messages).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>tiles</code></dt>
<dd> Set the number of tiles to encode the input video with, as columns x rows. Larger numbers allow greater parallelism in both encoding and decoding, but may decrease coding efficiency.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>mjpeg_vaapi</code></dt>
<dd> Only baseline DCT encoding is supported. The encoder always uses the standard quantisation and huffman tables &#8211; <code>global_quality</code> scales the standard quantisation table (range 1-100). </dd>
<p> For YUV, 4:2:0, 4:2:2 and 4:4:4 subsampling modes are supported. RGB is also supported, and will create an RGB JPEG.</p>
<dl>
<dl>
<dt><code>jfif</code></dt>
<dd> Include JFIF header in each frame (not included by default).</dd>
<dt><code>huffman</code></dt>
<dd> Include standard huffman tables (on by default). Turning this off will save a few hundred bytes in each output frame, but may lose compatibility with some JPEG decoders which don&#8217;t fully handle MJPEG.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>mpeg2_vaapi</code></dt>
<dd> <code>profile</code> and <code>level</code> set the value of <i>profile_and_level_indication</i>.</dd>
<dt><code>vp8_vaapi</code></dt>
<dd> B-frames are not supported. </dd>
<p> <code>global_quality</code> sets the <i>q_idx</i> used for non-key frames (range 0-127).</p>
<dl>
<dl>
<dt><code>loop_filter_level</code></dt>
<dd>
</dd><dt><code>loop_filter_sharpness</code></dt>
<dd> Manually set the loop filter parameters.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>vp9_vaapi</code></dt>
<dd> <code>global_quality</code> sets the <i>q_idx</i> used for P-frames (range 0-255).</dd>
<dl>
<dl>
<dt><code>loop_filter_level</code></dt>
<dd>
</dd><dt><code>loop_filter_sharpness</code></dt>
<dd> Manually set the loop filter parameters.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> B-frames are supported, but the output stream is always in encode order rather than display order. If B-frames are enabled, it may be necessary to use the <code>vp9_raw_reorder</code> bitstream filter to modify the output stream to display frames in the correct order. </p>
<p> Only normal frames are produced &#8211; the <code>vp9_superframe</code> bitstream filter may be required to produce a stream usable with all decoders.</dd></dl>
</dl>
<h3>vc2</h3>
<p> SMPTE VC-2 (previously BBC Dirac Pro). This codec was primarily aimed at professional broadcasting but since it supports yuv420, yuv422 and yuv444 at 8 (limited range or full range), 10 or 12 bits, this makes it suitable for other tasks which require low overhead and low compression (like screen recording). </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></dt>
<dd> Sets target video bitrate. Usually that&#8217;s around 1:6 of the uncompressed video bitrate (e.g. for 1920&#215;1080 50fps yuv422p10 that&#8217;s around 400Mbps). Higher values (close to the uncompressed bitrate) turn on lossless compression mode.</dd>
<dt><code>field_order</code></dt>
<dd> Enables field coding when set (e.g. to tt &#8211; top field first) for interlaced inputs. Should increase compression with interlaced content as it splits the fields and encodes each separately.</dd>
<dt><code>wavelet_depth</code></dt>
<dd> Sets the total amount of wavelet transforms to apply, between 1 and 5 (default). Lower values reduce compression and quality. Less capable decoders may not be able to handle values of <code>wavelet_depth</code> over 3.</dd>
<dt><code>wavelet_type</code></dt>
<dd> Sets the transform type. Currently only <i>5_3</i> (LeGall) and <i>9_7</i> (Deslauriers-Dubuc) are implemented, with 9_7 being the one with better compression and thus is the default.</dd>
<dt><code>slice_width</code></dt>
<dd>
</dd><dt><code>slice_height</code></dt>
<dd> Sets the slice size for each slice. Larger values result in better compression. For compatibility with other more limited decoders use <code>slice_width</code> of 32 and <code>slice_height</code> of 8.</dd>
<dt><code>tolerance</code></dt>
<dd> Sets the undershoot tolerance of the rate control system in percent. This is to prevent an expensive search from being run.</dd>
<dt><code>qm</code></dt>
<dd> Sets the quantization matrix preset to use by default or when <code>wavelet_depth</code> is set to 5</dd>
<dl>
<dl>
<dt>&#8211;</dt>
<dd> <i>default</i> Uses the default quantization matrix from the specifications, extended with values for the fifth level. This provides a good balance between keeping detail and omitting artifacts.</dd>
<dt>&#8211;</dt>
<dd> <i>flat</i> Use a completely zeroed out quantization matrix. This increases PSNR but might reduce perception. Use in bogus benchmarks.</dd>
<dt>&#8211;</dt>
<dd> <i>color</i> Reduces detail but attempts to preserve color at extremely low bitrates.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>SUBTITLES ENCODERS</h2>
<h3>dvdsub</h3>
<p> This codec encodes the bitmap subtitle format that is used in DVDs. Typically they are stored in VOBSUB file pairs (*.idx + *.sub), and they can also be used in Matroska files. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>palette</code></dt>
<dd> Specify the global palette used by the bitmaps. </dd>
<p> The format for this option is a string containing 16 24-bits hexadecimal numbers (without 0x prefix) separated by commas, for example <tt>&quot;0d00ee, ee450d, 101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1, 7b2a0e, 0d950c, 0f007b, cf0dec, cfa80c, 7c127b&quot;</tt>.</p>
<dt><code>even_rows_fix</code></dt>
<dd> When set to 1, enable a work-around that makes the number of pixel rows even in all subtitles. This fixes a problem with some players that cut off the bottom row if the number is odd. The work-around just adds a fully transparent row if needed. The overhead is low, typically one byte per subtitle on average. </dd>
<p> By default, this work-around is disabled.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavcodec/">libavcodec</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><i>MAINTAINERS</i><i></i> in the source code tree. </p>
