---
title: "ffmpeg-codecs(1)"
name: "ffmpeg-codecs"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-codecs/"
description: "ffmpeg-codecs – FFmpeg codecs"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-codecs &#8211; FFmpeg codecs </p>
<h2>DESCRIPTION</h2>
<p> This document describes the codecs (decoders and encoders) provided by the libavcodec library.</p>
<h2>CODEC OPTIONS</h2>
<p> libavcodec provides some generic global options, which can be set on all the encoders and decoders. In addition each codec may support so-called private options, which are specific for a given codec. </p>
<p> Sometimes, a global option may only affect a specific kind of codec, and may be nonsensical or ignored by another, so you need to be aware of the meaning of the specified options. Also some options are meant only for decoding or encoding. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, or by setting the value explicitly in the <tt>&quot;AVCodecContext&quot;</tt> options or using the <i>libavutil/opt.h</i> <font SIZE="-1">API</font> for programmatic use. </p>
<p> The list of supported options follow:</p>
<dl>
<dt><code>b</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Set bitrate in bits/s. Default value is 200K.</p>
<dt><code>ab</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></p>
<dd> Set audio bitrate (in bits/s). Default value is 128K.</p>
<dt><code>bt</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to min/max bitrate. Lowering tolerance too much has an adverse effect on quality.</p>
<dt><code>flags</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></p>
<dd> Set generic flags. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mv4</code></p>
<dd> Use four motion vector by macroblock (mpeg4).</p>
<dt><code>qpel</code></p>
<dd> Use 1/4 pel motion compensation.</p>
<dt><code>loop</code></p>
<dd> Use loop filter.</p>
<dt><code>qscale</code></p>
<dd> Use fixed qscale.</p>
<dt><code>pass1</code></p>
<dd> Use internal 2pass ratecontrol in first pass mode.</p>
<dt><code>pass2</code></p>
<dd> Use internal 2pass ratecontrol in second pass mode.</p>
<dt><code>gray</code></p>
<dd> Only decode/encode grayscale.</p>
<dt><code>psnr</code></p>
<dd> Set error[?] variables during encoding.</p>
<dt><code>truncated</code></p>
<dd> Input bitstream might be randomly truncated.</p>
<dt><code>drop_changed</code></p>
<dd> Don&#8217;t output frames whose parameters differ from first decoded frame in stream. Error <font SIZE="-1">AVERROR_INPUT_CHANGED</font> is returned when a frame is dropped.</p>
<dt><code>ildct</code></p>
<dd> Use interlaced <font SIZE="-1">DCT.</font></p>
<dt><code>low_delay</code></p>
<dd> Force low delay.</p>
<dt><code>global_header</code></p>
<dd> Place global headers in extradata instead of every keyframe.</p>
<dt><code>bitexact</code></p>
<dd> Only write platform-, build- and time-independent data. (except (I)DCT). This ensures that file and data checksums are reproducible and match between platforms. Its primary use is for regression testing.</p>
<dt><code>aic</code></p>
<dd> Apply H263 advanced intra coding / mpeg4 ac prediction.</p>
<dt><code>ilme</code></p>
<dd> Apply interlaced motion estimation.</p>
<dt><code>cgop</code></p>
<dd> Use closed gop.</p>
<dt><code>output_corrupt</code></p>
<dd> Output even potentially corrupted frames.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>time_base</code> <i>rational number</i></p>
<dd> Set codec time base. </p>
<p> It is the fundamental unit of time (in seconds) in terms of which frame timestamps are represented. For fixed-fps content, timebase should be <tt>&quot;1 / frame_rate&quot;</tt> and timestamp increments should be identically 1.</p>
<dt><code>g</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set the group of picture (<font SIZE="-1">GOP</font>) size. Default value is 12.</p>
<dt><code>ar</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio</i><code>)</code></p>
<dd> Set audio sampling rate (in Hz).</p>
<dt><code>ac</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio</i><code>)</code></p>
<dd> Set number of audio channels.</p>
<dt><code>cutoff</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></p>
<dd> Set cutoff bandwidth. (Supported only by selected encoders, see their respective documentation sections.)</p>
<dt><code>frame_size</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></p>
<dd> Set audio frame size. </p>
<p> Each submitted frame except the last must contain exactly frame_size samples per channel. May be 0 when the codec has <font SIZE="-1">CODEC_CAP_VARIABLE_FRAME_SIZE</font> set, in that case the frame size is not restricted. It is set by some decoders to indicate constant frame size.</p>
<dt><code>frame_number</code> <i>integer</i></p>
<dd> Set the frame number.</p>
<dt><code>delay</code> <i>integer</i></p>
<dd>
<dt><code>qcomp</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set video quantizer scale compression (<font SIZE="-1">VBR</font>). It is used as a constant in the ratecontrol equation. Recommended range for default rc_eq: 0.0-1.0.</p>
<dt><code>qblur</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set video quantizer scale blur (<font SIZE="-1">VBR</font>).</p>
<dt><code>qmin</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set min video quantizer scale (<font SIZE="-1">VBR</font>). Must be included between -1 and 69, default value is 2.</p>
<dt><code>qmax</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set max video quantizer scale (<font SIZE="-1">VBR</font>). Must be included between -1 and 1024, default value is 31.</p>
<dt><code>qdiff</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set max difference between the quantizer scale (<font SIZE="-1">VBR</font>).</p>
<dt><code>bf</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set max number of B frames between non-B-frames. </p>
<p> Must be an integer between -1 and 16. 0 means that B-frames are disabled. If a value of -1 is used, it will choose an automatic value depending on the encoder. </p>
<p> Default value is 0.</p>
<dt><code>b_qfactor</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set qp factor between P and B frames.</p>
<dt><code>b_strategy</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set strategy to choose between I/P/B-frames.</p>
<dt><code>ps</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set <font SIZE="-1">RTP</font> payload size in bytes.</p>
<dt><code>mv_bits</code> <i>integer</i></p>
<dd>
<dt><code>header_bits</code> <i>integer</i></p>
<dd>
<dt><code>i_tex_bits</code> <i>integer</i></p>
<dd>
<dt><code>p_tex_bits</code> <i>integer</i></p>
<dd>
<dt><code>i_count</code> <i>integer</i></p>
<dd>
<dt><code>p_count</code> <i>integer</i></p>
<dd>
<dt><code>skip_count</code> <i>integer</i></p>
<dd>
<dt><code>misc_bits</code> <i>integer</i></p>
<dd>
<dt><code>frame_bits</code> <i>integer</i></p>
<dd>
<dt><code>codec_tag</code> <i>integer</i></p>
<dd>
<dt><code>bug</code> <i>flags</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Workaround not auto detected encoder bugs. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>autodetect</code></p>
<dd>
<dt><code>xvid_ilace</code></p>
<dd> Xvid interlacing bug (autodetected if fourcc==XVIX)</p>
<dt><code>ump4</code></p>
<dd> (autodetected if fourcc==UMP4)</p>
<dt><code>no_padding</code></p>
<dd> padding bug (autodetected)</p>
<dt><code>amv</code></p>
<dd>
<dt><code>qpel_chroma</code></p>
<dd>
<dt><code>std_qpel</code></p>
<dd> old standard qpel (autodetected per fourcc/version)</p>
<dt><code>qpel_chroma2</code></p>
<dd>
<dt><code>direct_blocksize</code></p>
<dd> direct-qpel-blocksize bug (autodetected per fourcc/version)</p>
<dt><code>edge</code></p>
<dd> edge padding bug (autodetected per fourcc/version)</p>
<dt><code>hpel_chroma</code></p>
<dd>
<dt><code>dc_clip</code></p>
<dd>
<dt><code>ms</code></p>
<dd> Workaround various bugs in microsoft broken decoders.</p>
<dt><code>trunc</code></p>
<dd> trancated frames</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>strict</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio,video</i><code>)</code></p>
<dd> Specify how strictly to follow the standards. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>very</code></p>
<dd> strictly conform to an older more strict version of the spec or reference software</p>
<dt><code>strict</code></p>
<dd> strictly conform to all the things in the spec no matter what consequences</p>
<dt><code>normal</code></p>
<dd>
<dt><code>unofficial</code></p>
<dd> allow unofficial extensions</p>
<dt><code>experimental</code></p>
<dd> allow non standardized experimental things, experimental (unfinished/work in progress/not well tested) decoders and encoders. Note: experimental decoders can pose a security risk, do not use this for decoding untrusted input.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>b_qoffset</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set <font SIZE="-1">QP</font> offset between P and B frames.</p>
<dt><code>err_detect</code> <i>flags</i> <code>(</code><i>decoding,audio,video</i><code>)</code></p>
<dd> Set error detection flags. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>crccheck</code></p>
<dd> verify embedded CRCs</p>
<dt><code>bitstream</code></p>
<dd> detect bitstream specification deviations</p>
<dt><code>buffer</code></p>
<dd> detect improper bitstream length</p>
<dt><code>explode</code></p>
<dd> abort decoding on minor error detection</p>
<dt><code>ignore_err</code></p>
<dd> ignore decoding errors, and continue decoding. This is useful if you want to analyze the content of a video and thus want everything to be decoded no matter what. This option will not result in a video that is pleasing to watch in case of errors.</p>
<dt><code>careful</code></p>
<dd> consider things that violate the spec and have not been seen in the wild as errors</p>
<dt><code>compliant</code></p>
<dd> consider all spec non compliancies as errors</p>
<dt><code>aggressive</code></p>
<dd> consider things that a sane encoder should not do as an error</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>has_b_frames</code> <i>integer</i></p>
<dd>
<dt><code>block_align</code> <i>integer</i></p>
<dd>
<dt><code>mpeg_quant</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Use <font SIZE="-1">MPEG</font> quantizers instead of H.263.</p>
<dt><code>rc_override_count</code> <i>integer</i></p>
<dd>
<dt><code>maxrate</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Set max bitrate tolerance (in bits/s). Requires bufsize to be set.</p>
<dt><code>minrate</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Set min bitrate tolerance (in bits/s). Most useful in setting up a <font SIZE="-1">CBR</font> encode. It is of little use elsewise.</p>
<dt><code>bufsize</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Set ratecontrol buffer size (in bits).</p>
<dt><code>i_qfactor</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set <font SIZE="-1">QP</font> factor between P and I frames.</p>
<dt><code>i_qoffset</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set <font SIZE="-1">QP</font> offset between P and I frames.</p>
<dt><code>dct</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set <font SIZE="-1">DCT</font> algorithm. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> autoselect a good one (default)</p>
<dt><code>fastint</code></p>
<dd> fast integer</p>
<dt><code>int</code></p>
<dd> accurate integer</p>
<dt><code>mmx</code></p>
<dd>
<dt><code>altivec</code></p>
<dd>
<dt><code>faan</code></p>
<dd> floating point <font SIZE="-1">AAN DCT</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>lumi_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Compress bright areas stronger than medium ones.</p>
<dt><code>tcplx_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set temporal complexity masking.</p>
<dt><code>scplx_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set spatial complexity masking.</p>
<dt><code>p_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set inter masking.</p>
<dt><code>dark_mask</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Compress dark areas stronger than medium ones.</p>
<dt><code>idct</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Select <font SIZE="-1">IDCT</font> implementation. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd>
<dt><code>int</code></p>
<dd>
<dt><code>simple</code></p>
<dd>
<dt><code>simplemmx</code></p>
<dd>
<dt><code>simpleauto</code></p>
<dd> Automatically pick a <font SIZE="-1">IDCT</font> compatible with the simple one</p>
<dt><code>arm</code></p>
<dd>
<dt><code>altivec</code></p>
<dd>
<dt><code>sh4</code></p>
<dd>
<dt><code>simplearm</code></p>
<dd>
<dt><code>simplearmv5te</code></p>
<dd>
<dt><code>simplearmv6</code></p>
<dd>
<dt><code>simpleneon</code></p>
<dd>
<dt><code>xvid</code></p>
<dd>
<dt><code>faani</code></p>
<dd> floating point <font SIZE="-1">AAN IDCT</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>slice_count</code> <i>integer</i></p>
<dd>
<dt><code>ec</code> <i>flags</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Set error concealment strategy. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>guess_mvs</code></p>
<dd> iterative motion vector (<font SIZE="-1">MV</font>) search (slow)</p>
<dt><code>deblock</code></p>
<dd> use strong deblock filter for damaged MBs</p>
<dt><code>favor_inter</code></p>
<dd> favor predicting from the previous frame instead of the current</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>bits_per_coded_sample</code> <i>integer</i></p>
<dd>
<dt><code>pred</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set prediction method. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>left</code></p>
<dd>
<dt><code>plane</code></p>
<dd>
<dt><code>median</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>aspect</code> <i>rational number</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set sample aspect ratio.</p>
<dt><code>sar</code> <i>rational number</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set sample aspect ratio. Alias to <i>aspect</i>.</p>
<dt><code>debug</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></p>
<dd> Print specific debug info. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>pict</code></p>
<dd> picture info</p>
<dt><code>rc</code></p>
<dd> rate control</p>
<dt><code>bitstream</code></p>
<dd>
<dt><code>mb_type</code></p>
<dd> macroblock (<font SIZE="-1">MB</font>) type</p>
<dt><code>qp</code></p>
<dd> per-block quantization parameter (<font SIZE="-1">QP</font>)</p>
<dt><code>dct_coeff</code></p>
<dd>
<dt><code>green_metadata</code></p>
<dd> display complexity metadata for the upcoming frame, GoP or for a given duration.</p>
<dt><code>skip</code></p>
<dd>
<dt><code>startcode</code></p>
<dd>
<dt><code>er</code></p>
<dd> error recognition</p>
<dt><code>mmco</code></p>
<dd> memory management control operations (H.264)</p>
<dt><code>bugs</code></p>
<dd>
<dt><code>buffers</code></p>
<dd> picture buffer allocations</p>
<dt><code>thread_ops</code></p>
<dd> threading operations</p>
<dt><code>nomc</code></p>
<dd> skip motion compensation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>cmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set full pel me compare function. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sad</code></p>
<dd> sum of absolute differences, fast (default)</p>
<dt><code>sse</code></p>
<dd> sum of squared errors</p>
<dt><code>satd</code></p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt><code>dct</code></p>
<dd> sum of absolute <font SIZE="-1">DCT</font> transformed differences</p>
<dt><code>psnr</code></p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt><code>bit</code></p>
<dd> number of bits needed for the block</p>
<dt><code>rd</code></p>
<dd> rate distortion optimal, slow</p>
<dt><code>zero</code></p>
<dd> 0</p>
<dt><code>vsad</code></p>
<dd> sum of absolute vertical differences</p>
<dt><code>vsse</code></p>
<dd> sum of squared vertical differences</p>
<dt><code>nsse</code></p>
<dd> noise preserving sum of squared differences</p>
<dt><code>w53</code></p>
<dd> 5/3 wavelet, only used in snow</p>
<dt><code>w97</code></p>
<dd> 9/7 wavelet, only used in snow</p>
<dt><code>dctmax</code></p>
<dd>
<dt><code>chroma</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>subcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set sub pel me compare function. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sad</code></p>
<dd> sum of absolute differences, fast (default)</p>
<dt><code>sse</code></p>
<dd> sum of squared errors</p>
<dt><code>satd</code></p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt><code>dct</code></p>
<dd> sum of absolute <font SIZE="-1">DCT</font> transformed differences</p>
<dt><code>psnr</code></p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt><code>bit</code></p>
<dd> number of bits needed for the block</p>
<dt><code>rd</code></p>
<dd> rate distortion optimal, slow</p>
<dt><code>zero</code></p>
<dd> 0</p>
<dt><code>vsad</code></p>
<dd> sum of absolute vertical differences</p>
<dt><code>vsse</code></p>
<dd> sum of squared vertical differences</p>
<dt><code>nsse</code></p>
<dd> noise preserving sum of squared differences</p>
<dt><code>w53</code></p>
<dd> 5/3 wavelet, only used in snow</p>
<dt><code>w97</code></p>
<dd> 9/7 wavelet, only used in snow</p>
<dt><code>dctmax</code></p>
<dd>
<dt><code>chroma</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mbcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set macroblock compare function. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sad</code></p>
<dd> sum of absolute differences, fast (default)</p>
<dt><code>sse</code></p>
<dd> sum of squared errors</p>
<dt><code>satd</code></p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt><code>dct</code></p>
<dd> sum of absolute <font SIZE="-1">DCT</font> transformed differences</p>
<dt><code>psnr</code></p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt><code>bit</code></p>
<dd> number of bits needed for the block</p>
<dt><code>rd</code></p>
<dd> rate distortion optimal, slow</p>
<dt><code>zero</code></p>
<dd> 0</p>
<dt><code>vsad</code></p>
<dd> sum of absolute vertical differences</p>
<dt><code>vsse</code></p>
<dd> sum of squared vertical differences</p>
<dt><code>nsse</code></p>
<dd> noise preserving sum of squared differences</p>
<dt><code>w53</code></p>
<dd> 5/3 wavelet, only used in snow</p>
<dt><code>w97</code></p>
<dd> 9/7 wavelet, only used in snow</p>
<dt><code>dctmax</code></p>
<dd>
<dt><code>chroma</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>ildctcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set interlaced dct compare function. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sad</code></p>
<dd> sum of absolute differences, fast (default)</p>
<dt><code>sse</code></p>
<dd> sum of squared errors</p>
<dt><code>satd</code></p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt><code>dct</code></p>
<dd> sum of absolute <font SIZE="-1">DCT</font> transformed differences</p>
<dt><code>psnr</code></p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt><code>bit</code></p>
<dd> number of bits needed for the block</p>
<dt><code>rd</code></p>
<dd> rate distortion optimal, slow</p>
<dt><code>zero</code></p>
<dd> 0</p>
<dt><code>vsad</code></p>
<dd> sum of absolute vertical differences</p>
<dt><code>vsse</code></p>
<dd> sum of squared vertical differences</p>
<dt><code>nsse</code></p>
<dd> noise preserving sum of squared differences</p>
<dt><code>w53</code></p>
<dd> 5/3 wavelet, only used in snow</p>
<dt><code>w97</code></p>
<dd> 9/7 wavelet, only used in snow</p>
<dt><code>dctmax</code></p>
<dd>
<dt><code>chroma</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>dia_size</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set diamond type &amp; size for motion estimation.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>(1024, </code><font SIZE="-1"><code>INT_MAX</code></font><code>)</code></p>
<dd> full motion estimation(slowest)</p>
<dt><code>(768, 1024]</code></p>
<dd> umh motion estimation</p>
<dt><code>(512, 768]</code></p>
<dd> hex motion estimation</p>
<dt><code>(256, 512]</code></p>
<dd> l2s diamond motion estimation</p>
<dt><code>[2,256]</code></p>
<dd> var diamond motion estimation</p>
<dt><code>(-1, 2)</code></p>
<dd> small diamond motion estimation</p>
<dt><code>-1</code></p>
<dd> funny diamond motion estimation</p>
<dt><code>(</code><font SIZE="-1"><code>INT_MIN,</code></font><code> -1)</code></p>
<dd> sab diamond motion estimation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>last_pred</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set amount of motion predictors from the previous frame.</p>
<dt><code>preme</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set pre motion estimation.</p>
<dt><code>precmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set pre motion estimation compare function. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sad</code></p>
<dd> sum of absolute differences, fast (default)</p>
<dt><code>sse</code></p>
<dd> sum of squared errors</p>
<dt><code>satd</code></p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt><code>dct</code></p>
<dd> sum of absolute <font SIZE="-1">DCT</font> transformed differences</p>
<dt><code>psnr</code></p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt><code>bit</code></p>
<dd> number of bits needed for the block</p>
<dt><code>rd</code></p>
<dd> rate distortion optimal, slow</p>
<dt><code>zero</code></p>
<dd> 0</p>
<dt><code>vsad</code></p>
<dd> sum of absolute vertical differences</p>
<dt><code>vsse</code></p>
<dd> sum of squared vertical differences</p>
<dt><code>nsse</code></p>
<dd> noise preserving sum of squared differences</p>
<dt><code>w53</code></p>
<dd> 5/3 wavelet, only used in snow</p>
<dt><code>w97</code></p>
<dd> 9/7 wavelet, only used in snow</p>
<dt><code>dctmax</code></p>
<dd>
<dt><code>chroma</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>pre_dia_size</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set diamond type &amp; size for motion estimation pre-pass.</p>
<dt><code>subq</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set sub pel motion estimation quality.</p>
<dt><code>me_range</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set limit motion vectors range (1023 for DivX player).</p>
<dt><code>global_quality</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd>
<dt><code>coder</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>vlc</code></p>
<dd> variable length coder / huffman coder</p>
<dt><code>ac</code></p>
<dd> arithmetic coder</p>
<dt><code>raw</code></p>
<dd> raw (no encoding)</p>
<dt><code>rle</code></p>
<dd> run-length coder</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>context</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set context model.</p>
<dt><code>slice_flags</code> <i>integer</i></p>
<dd>
<dt><code>mbd</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set macroblock decision algorithm (high quality mode). </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>simple</code></p>
<dd> use mbcmp (default)</p>
<dt><code>bits</code></p>
<dd> use fewest bits</p>
<dt><code>rd</code></p>
<dd> use best rate distortion</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>sc_threshold</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set scene change threshold.</p>
<dt><code>nr</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set noise reduction.</p>
<dt><code>rc_init_occupancy</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set number of bits which should be loaded into the rc buffer before decoding starts.</p>
<dt><code>flags2</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fast</code></p>
<dd> Allow non spec compliant speedup tricks.</p>
<dt><code>noout</code></p>
<dd> Skip bitstream encoding.</p>
<dt><code>ignorecrop</code></p>
<dd> Ignore cropping information from sps.</p>
<dt><code>local_header</code></p>
<dd> Place global headers at every keyframe instead of in extradata.</p>
<dt><code>chunks</code></p>
<dd> Frame data might be split into multiple chunks.</p>
<dt><code>showall</code></p>
<dd> Show all frames before the first keyframe.</p>
<dt><code>export_mvs</code></p>
<dd> Export motion vectors into frame side-data (see <tt>&quot;AV_FRAME_DATA_MOTION_VECTORS&quot;</tt>) for codecs that support it. See also <i>doc/examples/export_mvs.c</i>.</p>
<dt><code>skip_manual</code></p>
<dd> Do not skip samples and export skip information as frame side data.</p>
<dt><code>ass_ro_flush_noop</code></p>
<dd> Do not reset <font SIZE="-1">ASS</font> ReadOrder field on flush.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>export_side_data</code> <i>flags</i> <code>(</code><i>decoding/encoding,audio,video,subtitles</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mvs</code></p>
<dd> Export motion vectors into frame side-data (see <tt>&quot;AV_FRAME_DATA_MOTION_VECTORS&quot;</tt>) for codecs that support it. See also <i>doc/examples/export_mvs.c</i>.</p>
<dt><code>prft</code></p>
<dd> Export encoder Producer Reference Time into packet side-data (see <tt>&quot;AV_PKT_DATA_PRFT&quot;</tt>) for codecs that support it.</p>
<dt><code>venc_params</code></p>
<dd> Export video encoding parameters through frame side data (see <tt>&quot;AV_FRAME_DATA_VIDEO_ENC_PARAMS&quot;</tt>) for codecs that support it. At present, those are H.264 and <font SIZE="-1">VP9.</font></p>
<dt><code>film_grain</code></p>
<dd> Export film grain parameters through frame side data (see <tt>&quot;AV_FRAME_DATA_FILM_GRAIN_PARAMS&quot;</tt>). Supported at present by <font SIZE="-1">AV1</font> decoders.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>threads</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Set the number of threads to be used, in case the selected codec implementation supports multi-threading. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto, 0</code></p>
<dd> automatically select the number of threads to set</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>auto</code>.</dl>
<dt><code>dc</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set intra_dc_precision.</p>
<dt><code>nssew</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set nsse weight.</p>
<dt><code>skip_top</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Set number of macroblock rows at the top which are skipped.</p>
<dt><code>skip_bottom</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Set number of macroblock rows at the bottom which are skipped.</p>
<dt><code>profile</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Set encoder codec profile. Default value is <code>unknown</code>. Encoder specific profiles are documented in the relevant encoder documentation.</p>
<dt><code>level</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>unknown</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>lowres</code> <i>integer</i> <code>(</code><i>decoding,audio,video</i><code>)</code></p>
<dd> Decode at 1= 1/2, 2=1/4, 3=1/8 resolutions.</p>
<dt><code>skip_threshold</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set frame skip threshold.</p>
<dt><code>skip_factor</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set frame skip factor.</p>
<dt><code>skip_exp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set frame skip exponent. Negative values behave identical to the corresponding positive ones, except that the score is normalized. Positive values exist primarily for compatibility reasons and are not so useful.</p>
<dt><code>skipcmp</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set frame skip compare function. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sad</code></p>
<dd> sum of absolute differences, fast (default)</p>
<dt><code>sse</code></p>
<dd> sum of squared errors</p>
<dt><code>satd</code></p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt><code>dct</code></p>
<dd> sum of absolute <font SIZE="-1">DCT</font> transformed differences</p>
<dt><code>psnr</code></p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt><code>bit</code></p>
<dd> number of bits needed for the block</p>
<dt><code>rd</code></p>
<dd> rate distortion optimal, slow</p>
<dt><code>zero</code></p>
<dd> 0</p>
<dt><code>vsad</code></p>
<dd> sum of absolute vertical differences</p>
<dt><code>vsse</code></p>
<dd> sum of squared vertical differences</p>
<dt><code>nsse</code></p>
<dd> noise preserving sum of squared differences</p>
<dt><code>w53</code></p>
<dd> 5/3 wavelet, only used in snow</p>
<dt><code>w97</code></p>
<dd> 9/7 wavelet, only used in snow</p>
<dt><code>dctmax</code></p>
<dd>
<dt><code>chroma</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mblmin</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set min macroblock lagrange factor (<font SIZE="-1">VBR</font>).</p>
<dt><code>mblmax</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set max macroblock lagrange factor (<font SIZE="-1">VBR</font>).</p>
<dt><code>mepc</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set motion estimation bitrate penalty compensation (1.0 = 256).</p>
<dt><code>skip_loop_filter</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd>
<dt><code>skip_idct</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd>
<dt><code>skip_frame</code> <i>integer</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Make decoder discard processing depending on the frame type selected by the option value. </p>
<p> <code>skip_loop_filter</code> skips frame loop filtering, <code>skip_idct</code> skips frame IDCT/dequantization, <code>skip_frame</code> skips decoding. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Discard no frame.</p>
<dt><code>default</code></p>
<dd> Discard useless frames like 0-sized frames.</p>
<dt><code>noref</code></p>
<dd> Discard all non-reference frames.</p>
<dt><code>bidir</code></p>
<dd> Discard all bidirectional frames.</p>
<dt><code>nokey</code></p>
<dd> Discard all frames excepts keyframes.</p>
<dt><code>nointra</code></p>
<dd> Discard all frames except I frames.</p>
<dt><code>all</code></p>
<dd> Discard all frames.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>default</code>.</dl>
<dt><code>bidir_refine</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Refine the two motion vectors used in bidirectional macroblocks.</p>
<dt><code>brd_scale</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Downscale frames for dynamic B-frame decision.</p>
<dt><code>keyint_min</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set minimum interval between IDR-frames.</p>
<dt><code>refs</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set reference frames to consider for motion compensation.</p>
<dt><code>chromaoffset</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set chroma qp offset from luma.</p>
<dt><code>trellis</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd> Set rate-distortion optimal quantization.</p>
<dt><code>mv0_threshold</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd>
<dt><code>b_sensitivity</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Adjust sensitivity of b_frame_strategy 1.</p>
<dt><code>compression_level</code> <i>integer</i> <code>(</code><i>encoding,audio,video</i><code>)</code></p>
<dd>
<dt><code>min_prediction_order</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></p>
<dd>
<dt><code>max_prediction_order</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></p>
<dd>
<dt><code>timecode_frame_start</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Set <font SIZE="-1">GOP</font> timecode frame start number, in non drop frame format.</p>
<dt><code>bits_per_raw_sample</code> <i>integer</i></p>
<dd>
<dt><code>channel_layout</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio</i><code>)</code></p>
<dd> Possible values:</p>
<dt><code>request_channel_layout</code> <i>integer</i> <code>(</code><i>decoding,audio</i><code>)</code></p>
<dd> Possible values:</p>
<dt><code>rc_max_vbv_use</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd>
<dt><code>rc_min_vbv_use</code> <i>float</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd>
<dt><code>ticks_per_frame</code> <i>integer</i> <code>(</code><i>decoding/encoding,audio,video</i><code>)</code></p>
<dd>
<dt><code>color_primaries</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bt709</code></p>
<dd> <font SIZE="-1">BT.709</font></p>
<dt><code>bt470m</code></p>
<dd> <font SIZE="-1">BT.470 M</font></p>
<dt><code>bt470bg</code></p>
<dd> <font SIZE="-1">BT.470 BG</font></p>
<dt><code>smpte170m</code></p>
<dd> <font SIZE="-1">SMPTE 170 M</font></p>
<dt><code>smpte240m</code></p>
<dd> <font SIZE="-1">SMPTE 240 M</font></p>
<dt><code>film</code></p>
<dd> Film</p>
<dt><code>bt2020</code></p>
<dd> <font SIZE="-1">BT.2020</font></p>
<dt><code>smpte428</code></p>
<dd>
<dt><code>smpte428_1</code></p>
<dd> <font SIZE="-1">SMPTE ST 428-1</font></p>
<dt><code>smpte431</code></p>
<dd> <font SIZE="-1">SMPTE 431-2</font></p>
<dt><code>smpte432</code></p>
<dd> <font SIZE="-1">SMPTE 432-1</font></p>
<dt><code>jedec-p22</code></p>
<dd> <font SIZE="-1">JEDEC P22</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>color_trc</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bt709</code></p>
<dd> <font SIZE="-1">BT.709</font></p>
<dt><code>gamma22</code></p>
<dd> <font SIZE="-1">BT.470 M</font></p>
<dt><code>gamma28</code></p>
<dd> <font SIZE="-1">BT.470 BG</font></p>
<dt><code>smpte170m</code></p>
<dd> <font SIZE="-1">SMPTE 170 M</font></p>
<dt><code>smpte240m</code></p>
<dd> <font SIZE="-1">SMPTE 240 M</font></p>
<dt><code>linear</code></p>
<dd> Linear</p>
<dt><code>log</code></p>
<dd>
<dt><code>log100</code></p>
<dd> Log</p>
<dt><code>log_sqrt</code></p>
<dd>
<dt><code>log316</code></p>
<dd> Log square root</p>
<dt><code>iec61966_2_4</code></p>
<dd>
<dt><code>iec61966-2-4</code></p>
<dd> <font SIZE="-1">IEC 61966-2-4</font></p>
<dt><code>bt1361</code></p>
<dd>
<dt><code>bt1361e</code></p>
<dd> <font SIZE="-1">BT.1361</font></p>
<dt><code>iec61966_2_1</code></p>
<dd>
<dt><code>iec61966-2-1</code></p>
<dd> <font SIZE="-1">IEC 61966-2-1</font></p>
<dt><code>bt2020_10</code></p>
<dd>
<dt><code>bt2020_10bit</code></p>
<dd> <font SIZE="-1">BT.2020</font> &#8211; 10 bit</p>
<dt><code>bt2020_12</code></p>
<dd>
<dt><code>bt2020_12bit</code></p>
<dd> <font SIZE="-1">BT.2020</font> &#8211; 12 bit</p>
<dt><code>smpte2084</code></p>
<dd> <font SIZE="-1">SMPTE ST 2084</font></p>
<dt><code>smpte428</code></p>
<dd>
<dt><code>smpte428_1</code></p>
<dd> <font SIZE="-1">SMPTE ST 428-1</font></p>
<dt><code>arib-std-b67</code></p>
<dd> <font SIZE="-1">ARIB STD-B67</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>colorspace</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>rgb</code></p>
<dd> <font SIZE="-1">RGB</font></p>
<dt><code>bt709</code></p>
<dd> <font SIZE="-1">BT.709</font></p>
<dt><code>fcc</code></p>
<dd> <font SIZE="-1">FCC</font></p>
<dt><code>bt470bg</code></p>
<dd> <font SIZE="-1">BT.470 BG</font></p>
<dt><code>smpte170m</code></p>
<dd> <font SIZE="-1">SMPTE 170 M</font></p>
<dt><code>smpte240m</code></p>
<dd> <font SIZE="-1">SMPTE 240 M</font></p>
<dt><code>ycocg</code></p>
<dd> <font SIZE="-1">YCOCG</font></p>
<dt><code>bt2020nc</code></p>
<dd>
<dt><code>bt2020_ncl</code></p>
<dd> <font SIZE="-1">BT.2020 NCL</font></p>
<dt><code>bt2020c</code></p>
<dd>
<dt><code>bt2020_cl</code></p>
<dd> <font SIZE="-1">BT.2020 CL</font></p>
<dt><code>smpte2085</code></p>
<dd> <font SIZE="-1">SMPTE 2085</font></p>
<dt><code>chroma-derived-nc</code></p>
<dd> Chroma-derived <font SIZE="-1">NCL</font></p>
<dt><code>chroma-derived-c</code></p>
<dd> Chroma-derived <font SIZE="-1">CL</font></p>
<dt><code>ictcp</code></p>
<dd> ICtCp</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>color_range</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> If used as input parameter, it serves as a hint to the decoder, which color_range the input has. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>tv</code></p>
<dd>
<dt><code>mpeg</code></p>
<dd> <font SIZE="-1">MPEG</font> (219*2^(n-8))</p>
<dt><code>pc</code></p>
<dd>
<dt><code>jpeg</code></p>
<dd> <font SIZE="-1">JPEG</font> (2^n-1)</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>chroma_sample_location</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>left</code></p>
<dd>
<dt><code>center</code></p>
<dd>
<dt><code>topleft</code></p>
<dd>
<dt><code>top</code></p>
<dd>
<dt><code>bottomleft</code></p>
<dd>
<dt><code>bottom</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>log_level_offset</code> <i>integer</i></p>
<dd> Set the log level offset.</p>
<dt><code>slices</code> <i>integer</i> <code>(</code><i>encoding,video</i><code>)</code></p>
<dd> Number of slices, used in parallelized encoding.</p>
<dt><code>thread_type</code> <i>flags</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Select which multithreading methods to use. </p>
<p> Use of <code>frame</code> will increase decoding delay by one frame per thread, so clients which cannot provide future frames should not use it. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>slice</code></p>
<dd> Decode more than one part of a single frame at once. </p>
<p> Multithreading using slices works only when the video was encoded with slices.</p>
<dt><code>frame</code></p>
<dd> Decode more than one frame at once.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>slice+frame</code>.</dl>
<dt><code>audio_service_type</code> <i>integer</i> <code>(</code><i>encoding,audio</i><code>)</code></p>
<dd> Set audio service type. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ma</code></p>
<dd> Main Audio Service</p>
<dt><code>ef</code></p>
<dd> Effects</p>
<dt><code>vi</code></p>
<dd> Visually Impaired</p>
<dt><code>hi</code></p>
<dd> Hearing Impaired</p>
<dt><code>di</code></p>
<dd> Dialogue</p>
<dt><code>co</code></p>
<dd> Commentary</p>
<dt><code>em</code></p>
<dd> Emergency</p>
<dt><code>vo</code></p>
<dd> Voice Over</p>
<dt><code>ka</code></p>
<dd> Karaoke</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>request_sample_fmt</code> <i>sample_fmt</i> <code>(</code><i>decoding,audio</i><code>)</code></p>
<dd> Set sample format audio decoders should prefer. Default value is <tt>&quot;none&quot;</tt>.</p>
<dt><code>pkt_timebase</code> <i>rational number</i></p>
<dd>
<dt><code>sub_charenc</code> <i>encoding</i> <code>(</code><i>decoding,subtitles</i><code>)</code></p>
<dd> Set the input subtitles character encoding.</p>
<dt><code>field_order</code> <i>field_order</i> <code>(</code><i>video</i><code>)</code></p>
<dd> Set/override the field order of the video. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>progressive</code></p>
<dd> Progressive video</p>
<dt><code>tt</code></p>
<dd> Interlaced video, top field coded and displayed first</p>
<dt><code>bb</code></p>
<dd> Interlaced video, bottom field coded and displayed first</p>
<dt><code>tb</code></p>
<dd> Interlaced video, top coded first, bottom displayed first</p>
<dt><code>bt</code></p>
<dd> Interlaced video, bottom coded first, top displayed first</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>skip_alpha</code> <i>bool</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Set to 1 to disable processing alpha (transparency). This works like the <code>gray</code> flag in the <code>flags</code> option which skips chroma information instead of alpha. Default is 0.</p>
<dt><code>codec_whitelist</code> <i>list</i> <code>(</code><i>input</i><code>)</code></p>
<dd> &#8220;,&#8221; separated list of allowed decoders. By default all are allowed.</p>
<dt><code>dump_separator</code> <i>string</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Separator used to separate the fields printed on the command line about the Stream parameters. For example, to separate the fields with newlines and indentation: </p>
<pre>
        ffprobe -dump_separator &quot;
                                  &quot;  -i ~/videos/matrixbench_mpeg2.mpg
</pre>
<dt><code>max_pixels</code> <i>integer</i> <code>(</code><i>decoding/encoding,video</i><code>)</code></p>
<dd> Maximum number of pixels per image. This value can be used to avoid out of memory failures due to large images.</p>
<dt><code>apply_cropping</code> <i>bool</i> <code>(</code><i>decoding,video</i><code>)</code></p>
<dd> Enable cropping if cropping parameters are multiples of the required alignment for the left and top parameters. If the alignment is not met the cropping will be partially applied to maintain alignment. Default is 1 (enabled). Note: The required alignment depends on if <tt>&quot;AV_CODEC_FLAG_UNALIGNED&quot;</tt> is set and the <font SIZE="-1">CPU.</font> <tt>&quot;AV_CODEC_FLAG_UNALIGNED&quot;</tt> cannot be changed from the command line. Also hardware decoders will not apply left/top Cropping.</dl>
<h2>DECODERS</h2>
<p> Decoders are configured elements in FFmpeg which allow the decoding of multimedia streams. </p>
<p> When you configure your FFmpeg build, all the supported native decoders are enabled by default. Decoders requiring an external library must be enabled manually via the corresponding <tt>&quot;--enable-lib&quot;</tt> option. You can list all available decoders using the configure option <tt>&quot;--list-decoders&quot;</tt>. </p>
<p> You can disable all the decoders with the configure option <tt>&quot;--disable-decoders&quot;</tt> and selectively enable / disable single decoders with the options <tt>&quot;--enable-decoder=</tt>DECODER<tt>&quot;</tt> / <tt>&quot;--disable-decoder=</tt>DECODER<tt>&quot;</tt>. </p>
<p> The option <tt>&quot;-decoders&quot;</tt> of the ff* tools will display the list of enabled decoders.</p>
<h2>VIDEO DECODERS</h2>
<p> A description of some of the currently available video decoders follows.</p>
<h3>av1</h3>
<p> AOMedia Video 1 (<font SIZE="-1">AV1</font>) decoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>operating_point</code></p>
<dd> Select an operating point of a scalable <font SIZE="-1">AV1</font> bitstream (0 &#8211; 31). Default is 0.</dl>
<h3>rawvideo</h3>
<p> Raw video decoder. </p>
<p> This decoder decodes rawvideo streams. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>top</code> <i>top_field_first</i></p>
<dd> Specify the assumed field type of the input video.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd> the video is assumed to be progressive (default)</p>
<dt><code>0</code></p>
<dd> bottom-field-first is assumed</p>
<dt><code>1</code></p>
<dd> top-field-first is assumed</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>libdav1d</h3>
<p> dav1d <font SIZE="-1">AV1</font> decoder. </p>
<p> libdav1d allows libavcodec to decode the AOMedia Video 1 (<font SIZE="-1">AV1</font>) codec. Requires the presence of the libdav1d headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libdav1d&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libdav1d wrapper.</p>
<dl>
<dt><code>framethreads</code></p>
<dd> Set amount of frame threads to use during decoding. The default value is 0 (autodetect).</p>
<dt><code>tilethreads</code></p>
<dd> Set amount of tile threads to use during decoding. The default value is 0 (autodetect).</p>
<dt><code>filmgrain</code></p>
<dd> Apply film grain to the decoded video if present in the bitstream. Defaults to the internal default of the library.</p>
<dt><code>oppoint</code></p>
<dd> Select an operating point of a scalable <font SIZE="-1">AV1</font> bitstream (0 &#8211; 31). Defaults to the internal default of the library.</p>
<dt><code>alllayers</code></p>
<dd> Output all spatial layers of a scalable <font SIZE="-1">AV1</font> bitstream. The default value is false.</dl>
<h3>libdavs2</h3>
<p> <font SIZE="-1">AVS2-P2/IEEE1857.4</font> video decoder wrapper. </p>
<p> This decoder allows libavcodec to decode <font SIZE="-1">AVS2</font> streams with davs2 library.</p>
<h3>libuavs3d</h3>
<p> <font SIZE="-1">AVS3-P2/IEEE1857.10</font> video decoder. </p>
<p> libuavs3d allows libavcodec to decode <font SIZE="-1">AVS3</font> streams. Requires the presence of the libuavs3d headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libuavs3d&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following option is supported by the libuavs3d wrapper.</p>
<dl>
<dt><code>frame_threads</code></p>
<dd> Set amount of frame threads to use during decoding. The default value is 0 (autodetect).</dl>
<h2>AUDIO DECODERS</h2>
<p> A description of some of the currently available audio decoders follows.</p>
<h3>ac3</h3>
<p> <font SIZE="-1">AC-3</font> audio decoder. </p>
<p> This decoder implements part of <font SIZE="-1">ATSC A/52:2010</font> and <font SIZE="-1">ETSI TS 102 366,</font> as well as the undocumented RealAudio 3 (a.k.a. dnet). </p>
<p> <i></i><font SIZE="-1"><i>AC-3</i></font><i> Decoder Options</i></p>
<dl>
<dt><code>-drc_scale</code> <i>value</i></p>
<dd> Dynamic Range Scale Factor. The factor to apply to dynamic range values from the <font SIZE="-1">AC-3</font> stream. This factor is applied exponentially. The default value is 1. There are 3 notable scale factor ranges:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>drc_scale == 0</code></p>
<dd> <font SIZE="-1">DRC</font> disabled. Produces full range audio.</p>
<dt><code>0 &lt; drc_scale &lt;= 1</code></p>
<dd> <font SIZE="-1">DRC</font> enabled. Applies a fraction of the stream <font SIZE="-1">DRC</font> value. Audio reproduction is between full range and full compression.</p>
<dt><code>drc_scale &gt; 1</code></p>
<dd> <font SIZE="-1">DRC</font> enabled. Applies drc_scale asymmetrically. Loud sounds are fully compressed. Soft sounds are enhanced.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>flac</h3>
<p> <font SIZE="-1">FLAC</font> audio decoder. </p>
<p> This decoder aims to implement the complete <font SIZE="-1">FLAC</font> specification from Xiph. </p>
<p> <i></i><font SIZE="-1"><i>FLAC</i></font><i> Decoder options</i></p>
<dl>
<dt><code>-use_buggy_lpc</code></p>
<dd> The lavc <font SIZE="-1">FLAC</font> encoder used to produce buggy streams with high lpc values (like the default value). This option makes it possible to decode such streams correctly by using lavc&#8217;s old buggy lpc logic for decoding.</dl>
<h3>ffwavesynth</h3>
<p> Internal wave synthesizer. </p>
<p> This decoder generates wave patterns according to predefined sequences. Its use is purely internal and the format of the data it accepts is not publicly documented.</p>
<h3>libcelt</h3>
<p> libcelt decoder wrapper. </p>
<p> libcelt allows libavcodec to decode the Xiph <font SIZE="-1">CELT</font> ultra-low delay audio codec. Requires the presence of the libcelt headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libcelt&quot;</tt>.</p>
<h3>libgsm</h3>
<p> libgsm decoder wrapper. </p>
<p> libgsm allows libavcodec to decode the <font SIZE="-1">GSM</font> full rate audio codec. Requires the presence of the libgsm headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libgsm&quot;</tt>. </p>
<p> This decoder supports both the ordinary <font SIZE="-1">GSM</font> and the Microsoft variant.</p>
<h3>libilbc</h3>
<p> libilbc decoder wrapper. </p>
<p> libilbc allows libavcodec to decode the Internet Low Bitrate Codec (iLBC) audio codec. Requires the presence of the libilbc headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libilbc&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following option is supported by the libilbc wrapper.</p>
<dl>
<dt><code>enhance</code></p>
<dd> Enable the enhancement of the decoded audio when set to 1. The default value is 0 (disabled).</dl>
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
<p> <font SIZE="-1">ARIB STD-B24</font> caption decoder. </p>
<p> Implements profiles A and C of the <font SIZE="-1">ARIB STD-B24</font> standard. </p>
<p> <i>libaribb24 Decoder Options</i></p>
<dl>
<dt><code>-aribb24-base-path</code> <i>path</i></p>
<dd> Sets the base path for the libaribb24 library. This is utilized for reading of configuration files (for custom unicode conversions), and for dumping of non-text symbols as images under that location. </p>
<p> Unset by default.</p>
<dt><code>-aribb24-skip-ruby-text</code> <i>boolean</i></p>
<dd> Tells the decoder wrapper to skip text blocks that contain half-height ruby text. </p>
<p> Enabled by default.</dl>
<h3>dvbsub</h3>
<p> <i>Options</i></p>
<dl>
<dt><code>compute_clut</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd> Compute clut if no matching <font SIZE="-1">CLUT</font> is in the stream.</p>
<dt><code>0</code></p>
<dd> Never compute <font SIZE="-1">CLUT</font></p>
<dt><code>1</code></p>
<dd> Always compute <font SIZE="-1">CLUT</font> and override the one provided in the stream.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>dvb_substream</code></p>
<dd> Selects the dvb substream, or all substreams if -1 which is default.</dl>
<h3>dvdsub</h3>
<p> This codec decodes the bitmap subtitles used in DVDs; the same subtitles can also be found in VobSub file pairs and in some Matroska files. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>palette</code></p>
<dd> Specify the global palette used by the bitmaps. When stored in VobSub, the palette is normally specified in the index file; in Matroska, the palette is stored in the codec extra-data in the same format as in VobSub. In DVDs, the palette is stored in the <font SIZE="-1">IFO</font> file, and therefore not available when reading from dumped <font SIZE="-1">VOB</font> files. </p>
<p> The format for this option is a string containing 16 24-bits hexadecimal numbers (without 0x prefix) separated by commas, for example <tt>&quot;0d00ee, ee450d, 101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1, 7b2a0e, 0d950c, 0f007b, cf0dec, cfa80c, 7c127b&quot;</tt>.</p>
<dt><code>ifo_palette</code></p>
<dd> Specify the <font SIZE="-1">IFO</font> file from which the global palette is obtained. (experimental)</p>
<dt><code>forced_subs_only</code></p>
<dd> Only decode subtitle entries marked as forced. Some titles have forced and non-forced subtitles in the same track. Setting this flag to <tt>1</tt> will only keep the forced subtitles. Default value is <tt>0</tt>.</dl>
<h3>libzvbi-teletext</h3>
<p> Libzvbi allows libavcodec to decode <font SIZE="-1">DVB</font> teletext pages and <font SIZE="-1">DVB</font> teletext subtitles. Requires the presence of the libzvbi headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libzvbi&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>txt_page</code></p>
<dd> List of teletext page numbers to decode. Pages that do not match the specified list are dropped. You may use the special <tt>&quot;*&quot;</tt> string to match all pages, or <tt>&quot;subtitle&quot;</tt> to match all subtitle pages. Default value is *.</p>
<dt><code>txt_default_region</code></p>
<dd> Set default character set used for decoding, a value between 0 and 87 (see <font SIZE="-1">ETS 300 706,</font> Section 15, Table 32). Default value is -1, which does not override the libzvbi default. This option is needed for some legacy level 1.0 transmissions which cannot signal the proper charset.</p>
<dt><code>txt_chop_top</code></p>
<dd> Discards the top teletext line. Default value is 1.</p>
<dt><code>txt_format</code></p>
<dd> Specifies the format of the decoded subtitles.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bitmap</code></p>
<dd> The default format, you should use this for teletext pages, because certain graphics and colors cannot be expressed in simple text or even <font SIZE="-1">ASS.</font></p>
<dt><code>text</code></p>
<dd> Simple text based output without formatting.</p>
<dt><code>ass</code></p>
<dd> Formatted <font SIZE="-1">ASS</font> output, subtitle pages and teletext pages are returned in different styles, subtitle pages are stripped down to text, but an effort is made to keep the text alignment and the formatting.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>txt_left</code></p>
<dd> X offset of generated bitmaps, default is 0.</p>
<dt><code>txt_top</code></p>
<dd> Y offset of generated bitmaps, default is 0.</p>
<dt><code>txt_chop_spaces</code></p>
<dd> Chops leading and trailing spaces and removes empty lines from the generated text. This option is useful for teletext based subtitles where empty spaces may be present at the start or at the end of the lines or empty lines may be present between the subtitle lines because of double-sized teletext characters. Default value is 1.</p>
<dt><code>txt_duration</code></p>
<dd> Sets the display duration of the decoded teletext pages or subtitles in milliseconds. Default value is -1 which means infinity or until the next subtitle event comes.</p>
<dt><code>txt_transparent</code></p>
<dd> Force transparent background of the generated teletext bitmaps. Default value is 0 which means an opaque background.</p>
<dt><code>txt_opacity</code></p>
<dd> Sets the opacity (0-255) of the teletext background. If <code>txt_transparent</code> is not set, it only affects characters between a start box and an end box, typically subtitles. Default value is 0 if <code>txt_transparent</code> is set, 255 otherwise.</dl>
<h2>ENCODERS</h2>
<p> Encoders are configured elements in FFmpeg which allow the encoding of multimedia streams. </p>
<p> When you configure your FFmpeg build, all the supported native encoders are enabled by default. Encoders requiring an external library must be enabled manually via the corresponding <tt>&quot;--enable-lib&quot;</tt> option. You can list all available encoders using the configure option <tt>&quot;--list-encoders&quot;</tt>. </p>
<p> You can disable all the encoders with the configure option <tt>&quot;--disable-encoders&quot;</tt> and selectively enable / disable single encoders with the options <tt>&quot;--enable-encoder=</tt>ENCODER<tt>&quot;</tt> / <tt>&quot;--disable-encoder=</tt>ENCODER<tt>&quot;</tt>. </p>
<p> The option <tt>&quot;-encoders&quot;</tt> of the ff* tools will display the list of enabled encoders.</p>
<h2>AUDIO ENCODERS</h2>
<p> A description of some of the currently available audio encoders follows.</p>
<h3>aac</h3>
<p> Advanced Audio Coding (<font SIZE="-1">AAC</font>) encoder. </p>
<p> This encoder is the default <font SIZE="-1">AAC</font> encoder, natively implemented into FFmpeg. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></p>
<dd> Set bit rate in bits/s. Setting this automatically activates constant bit rate (<font SIZE="-1">CBR</font>) mode. If this option is unspecified it is set to 128kbps.</p>
<dt><code>q</code></p>
<dd> Set quality for variable bit rate (<font SIZE="-1">VBR</font>) mode. This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</p>
<dt><code>cutoff</code></p>
<dd> Set cutoff frequency. If unspecified will allow the encoder to dynamically adjust the cutoff to improve clarity on low bitrates.</p>
<dt><code>aac_coder</code></p>
<dd> Set <font SIZE="-1">AAC</font> encoder coding method. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>twoloop</code></p>
<dd> Two loop searching (<font SIZE="-1">TLS</font>) method. </p>
<p> This method first sets quantizers depending on band thresholds and then tries to find an optimal combination by adding or subtracting a specific value from all quantizers and adjusting some individual quantizer a little. Will tune itself based on whether <code>aac_is</code>, <code>aac_ms</code> and <code>aac_pns</code> are enabled.</p>
<dt><code>anmr</code></p>
<dd> Average noise to mask ratio (<font SIZE="-1">ANMR</font>) trellis-based solution. </p>
<p> This is an experimental coder which currently produces a lower quality, is more unstable and is slower than the default twoloop coder but has potential. Currently has no support for the <code>aac_is</code> or <code>aac_pns</code> options. Not currently recommended.</p>
<dt><code>fast</code></p>
<dd> Constant quantizer method. </p>
<p> Uses a cheaper version of twoloop algorithm that doesn&#8217;t try to do as many clever adjustments. Worse with low bitrates (less than 64kbps), but is better and much faster at higher bitrates. This is the default choice for a coder</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>aac_ms</code></p>
<dd> Sets mid/side coding mode. The default value of &#8220;auto&#8221; will automatically use M/S with bands which will benefit from such coding. Can be forced for all bands using the value &#8220;enable&#8221;, which is mainly useful for debugging or disabled using &#8220;disable&#8221;.</p>
<dt><code>aac_is</code></p>
<dd> Sets intensity stereo coding tool usage. By default, it&#8217;s enabled and will automatically toggle <font SIZE="-1">IS</font> for similar pairs of stereo bands if it&#8217;s beneficial. Can be disabled for debugging by setting the value to &#8220;disable&#8221;.</p>
<dt><code>aac_pns</code></p>
<dd> Uses perceptual noise substitution to replace low entropy high frequency bands with imperceptible white noise during the decoding process. By default, it&#8217;s enabled, but can be disabled for debugging purposes by using &#8220;disable&#8221;.</p>
<dt><code>aac_tns</code></p>
<dd> Enables the use of a multitap <font SIZE="-1">FIR</font> filter which spans through the high frequency bands to hide quantization noise during the encoding process and is reverted by the decoder. As well as decreasing unpleasant artifacts in the high range this also reduces the entropy in the high bands and allows for more bits to be used by the mid-low bands. By default it&#8217;s enabled but can be disabled for debugging by setting the option to &#8220;disable&#8221;.</p>
<dt><code>aac_ltp</code></p>
<dd> Enables the use of the long term prediction extension which increases coding efficiency in very low bandwidth situations such as encoding of voice or solo piano music by extending constant harmonic peaks in bands throughout frames. This option is implied by profile:a aac_low and is incompatible with aac_pred. Use in conjunction with <code>-ar</code> to decrease the samplerate.</p>
<dt><code>aac_pred</code></p>
<dd> Enables the use of a more traditional style of prediction where the spectral coefficients transmitted are replaced by the difference of the current coefficients minus the previous &#8220;predicted&#8221; coefficients. In theory and sometimes in practice this can improve quality for low to mid bitrate audio. This option implies the aac_main profile and is incompatible with aac_ltp.</p>
<dt><code>profile</code></p>
<dd> Sets the encoding profile, possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>aac_low</code></p>
<dd> The default, <font SIZE="-1">AAC</font> &#8220;Low-complexity&#8221; profile. Is the most compatible and produces decent quality.</p>
<dt><code>mpeg2_aac_low</code></p>
<dd> Equivalent to <tt>&quot;-profile:a aac_low -aac_pns 0&quot;</tt>. <font SIZE="-1">PNS</font> was introduced with the <font SIZE="-1">MPEG4</font> specifications.</p>
<dt><code>aac_ltp</code></p>
<dd> Long term prediction profile, is enabled by and will enable the <code>aac_ltp</code> option. Introduced in <font SIZE="-1">MPEG4.</font></p>
<dt><code>aac_main</code></p>
<dd> Main-type prediction profile, is enabled by and will enable the <code>aac_pred</code> option. Introduced in <font SIZE="-1">MPEG2.</font></dl>
</dl>
<dl>
<dt>
<dd>
<p> If this option is unspecified it is set to <code>aac_low</code>.</dl>
</dl>
<h3>ac3 and ac3_fixed</h3>
<p> <font SIZE="-1">AC-3</font> audio encoders. </p>
<p> These encoders implement part of <font SIZE="-1">ATSC A/52:2010</font> and <font SIZE="-1">ETSI TS 102 366,</font> as well as the undocumented RealAudio 3 (a.k.a. dnet). </p>
<p> The <i>ac3</i> encoder uses floating-point math, while the <i>ac3_fixed</i> encoder only uses fixed-point integer math. This does not mean that one is always faster, just that one or the other may be better suited to a particular system. The <i>ac3_fixed</i> encoder is not the default codec for any of the output formats, so it must be specified explicitly using the option <tt>&quot;-acodec ac3_fixed&quot;</tt> in order to use it. </p>
<p> <i></i><font SIZE="-1"><i>AC-3</i></font><i> Metadata</i> </p>
<p> The <font SIZE="-1">AC-3</font> metadata options are used to set parameters that describe the audio, but in most cases do not affect the audio encoding itself. Some of the options do directly affect or influence the decoding and playback of the resulting bitstream, while others are just for informational purposes. A few of the options will add bits to the output stream that could otherwise be used for audio data, and will thus affect the quality of the output. Those will be indicated accordingly with a note in the option list below. </p>
<p> These parameters are described in detail in several publicly-available documents.</p>
<dl>
<dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.atsc.org/cms/standards/a_52-2010.pdf">http://www.atsc.org/cms/standards/a_52-2010.pdf</a></code>&gt;&gt;</p>
<dd>
<dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.atsc.org/cms/standards/a_54a_with_corr_1.pdf">http://www.atsc.org/cms/standards/a_54a_with_corr_1.pdf</a></code>&gt;&gt;</p>
<dd>
<dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/18_Metadata.Guide.pdf">http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/18_Metadata.Guide.pdf</a></code>&gt;&gt;</p>
<dd>
<dt>*&lt;&lt;<code><a rel="nofollow" href="http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/46_DDEncodingGuidelines.pdf">http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/46_DDEncodingGuidelines.pdf</a></code>&gt;&gt;</p>
<dd></dl>
<p> Metadata Control Options</p>
<dl>
<dt><code>-per_frame_metadata</code> <i>boolean</i></p>
<dd> Allow Per-Frame Metadata. Specifies if the encoder should check for changing metadata for each frame.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> The metadata values set at initialization will be used for every frame in the stream. (default)</p>
<dt><code>1</code></p>
<dd> Metadata values can be changed before encoding each frame.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Downmix Levels</p>
<dl>
<dt><code>-center_mixlev</code> <i>level</i></p>
<dd> Center Mix Level. The amount of gain the decoder should apply to the center channel when downmixing to stereo. This field will only be written to the bitstream if a center channel is present. The value is specified as a scale factor. There are 3 valid values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0.707</code></p>
<dd> Apply -3dB gain</p>
<dt><code>0.595</code></p>
<dd> Apply -4.5dB gain (default)</p>
<dt><code>0.500</code></p>
<dd> Apply -6dB gain</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-surround_mixlev</code> <i>level</i></p>
<dd> Surround Mix Level. The amount of gain the decoder should apply to the surround channel(s) when downmixing to stereo. This field will only be written to the bitstream if one or more surround channels are present. The value is specified as a scale factor. There are 3 valid values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0.707</code></p>
<dd> Apply -3dB gain</p>
<dt><code>0.500</code></p>
<dd> Apply -6dB gain (default)</p>
<dt><code>0.000</code></p>
<dd> Silence Surround Channel(s)</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Audio Production Information </p>
<p> Audio Production Information is optional information describing the mixing environment. Either none or both of the fields are written to the bitstream.</p>
<dl>
<dt><code>-mixing_level</code> <i>number</i></p>
<dd> Mixing Level. Specifies peak sound pressure level (<font SIZE="-1">SPL</font>) in the production environment when the mix was mastered. Valid values are 80 to 111, or -1 for unknown or not indicated. The default value is -1, but that value cannot be used if the Audio Production Information is written to the bitstream. Therefore, if the <tt>&quot;room_type&quot;</tt> option is not the default value, the <tt>&quot;mixing_level&quot;</tt> option must not be -1.</p>
<dt><code>-room_type</code> <i>type</i></p>
<dd> Room Type. Describes the equalization used during the final mixing session at the studio or on the dubbing stage. A large room is a dubbing stage with the industry standard X-curve equalization; a small room has flat equalization. This field will not be written to the bitstream if both the <tt>&quot;mixing_level&quot;</tt> option and the <tt>&quot;room_type&quot;</tt> option have the default values.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>notindicated</code></p>
<dd> Not Indicated (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>large</code></p>
<dd> Large Room</p>
<dt><code>2</code></p>
<dd>
<dt><code>small</code></p>
<dd> Small Room</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Other Metadata Options</p>
<dl>
<dt><code>-copyright</code> <i>boolean</i></p>
<dd> Copyright Indicator. Specifies whether a copyright exists for this audio.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>off</code></p>
<dd> No Copyright Exists (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>on</code></p>
<dd> Copyright Exists</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-dialnorm</code> <i>value</i></p>
<dd> Dialogue Normalization. Indicates how far the average dialogue level of the program is below digital 100% full scale (0 dBFS). This parameter determines a level shift during audio reproduction that sets the average volume of the dialogue to a preset level. The goal is to match volume level between program sources. A value of -31dB will result in no volume level change, relative to the source volume, during audio reproduction. Valid values are whole numbers in the range -31 to -1, with -31 being the default.</p>
<dt><code>-dsur_mode</code> <i>mode</i></p>
<dd> Dolby Surround Mode. Specifies whether the stereo signal uses Dolby Surround (Pro Logic). This field will only be written to the bitstream if the audio stream is stereo. Using this option does <font SIZE="-1"><code>NOT</code></font> mean the encoder will actually apply Dolby Surround processing.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>notindicated</code></p>
<dd> Not Indicated (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>off</code></p>
<dd> Not Dolby Surround Encoded</p>
<dt><code>2</code></p>
<dd>
<dt><code>on</code></p>
<dd> Dolby Surround Encoded</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-original</code> <i>boolean</i></p>
<dd> Original Bit Stream Indicator. Specifies whether this audio is from the original source and not a copy.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>off</code></p>
<dd> Not Original Source</p>
<dt><code>1</code></p>
<dd>
<dt><code>on</code></p>
<dd> Original Source (default)</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>Extended Bitstream Information</i> </p>
<p> The extended bitstream options are part of the Alternate Bit Stream Syntax as specified in Annex D of the A/52:2010 standard. It is grouped into 2 parts. If any one parameter in a group is specified, all values in that group will be written to the bitstream. Default values are used for those that are written but have not been specified. If the mixing levels are written, the decoder will use these values instead of the ones specified in the <tt>&quot;center_mixlev&quot;</tt> and <tt>&quot;surround_mixlev&quot;</tt> options if it supports the Alternate Bit Stream Syntax. </p>
<p> Extended Bitstream Information &#8211; Part 1</p>
<dl>
<dt><code>-dmix_mode</code> <i>mode</i></p>
<dd> Preferred Stereo Downmix Mode. Allows the user to select either Lt/Rt (Dolby Surround) or Lo/Ro (normal stereo) as the preferred stereo downmix mode.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>notindicated</code></p>
<dd> Not Indicated (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>ltrt</code></p>
<dd> Lt/Rt Downmix Preferred</p>
<dt><code>2</code></p>
<dd>
<dt><code>loro</code></p>
<dd> Lo/Ro Downmix Preferred</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-ltrt_cmixlev</code> <i>level</i></p>
<dd> Lt/Rt Center Mix Level. The amount of gain the decoder should apply to the center channel when downmixing to stereo in Lt/Rt mode.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1.414</code></p>
<dd> Apply +3dB gain</p>
<dt><code>1.189</code></p>
<dd> Apply +1.5dB gain</p>
<dt><code>1.000</code></p>
<dd> Apply 0dB gain</p>
<dt><code>0.841</code></p>
<dd> Apply -1.5dB gain</p>
<dt><code>0.707</code></p>
<dd> Apply -3.0dB gain</p>
<dt><code>0.595</code></p>
<dd> Apply -4.5dB gain (default)</p>
<dt><code>0.500</code></p>
<dd> Apply -6.0dB gain</p>
<dt><code>0.000</code></p>
<dd> Silence Center Channel</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-ltrt_surmixlev</code> <i>level</i></p>
<dd> Lt/Rt Surround Mix Level. The amount of gain the decoder should apply to the surround channel(s) when downmixing to stereo in Lt/Rt mode.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0.841</code></p>
<dd> Apply -1.5dB gain</p>
<dt><code>0.707</code></p>
<dd> Apply -3.0dB gain</p>
<dt><code>0.595</code></p>
<dd> Apply -4.5dB gain</p>
<dt><code>0.500</code></p>
<dd> Apply -6.0dB gain (default)</p>
<dt><code>0.000</code></p>
<dd> Silence Surround Channel(s)</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-loro_cmixlev</code> <i>level</i></p>
<dd> Lo/Ro Center Mix Level. The amount of gain the decoder should apply to the center channel when downmixing to stereo in Lo/Ro mode.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1.414</code></p>
<dd> Apply +3dB gain</p>
<dt><code>1.189</code></p>
<dd> Apply +1.5dB gain</p>
<dt><code>1.000</code></p>
<dd> Apply 0dB gain</p>
<dt><code>0.841</code></p>
<dd> Apply -1.5dB gain</p>
<dt><code>0.707</code></p>
<dd> Apply -3.0dB gain</p>
<dt><code>0.595</code></p>
<dd> Apply -4.5dB gain (default)</p>
<dt><code>0.500</code></p>
<dd> Apply -6.0dB gain</p>
<dt><code>0.000</code></p>
<dd> Silence Center Channel</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-loro_surmixlev</code> <i>level</i></p>
<dd> Lo/Ro Surround Mix Level. The amount of gain the decoder should apply to the surround channel(s) when downmixing to stereo in Lo/Ro mode.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0.841</code></p>
<dd> Apply -1.5dB gain</p>
<dt><code>0.707</code></p>
<dd> Apply -3.0dB gain</p>
<dt><code>0.595</code></p>
<dd> Apply -4.5dB gain</p>
<dt><code>0.500</code></p>
<dd> Apply -6.0dB gain (default)</p>
<dt><code>0.000</code></p>
<dd> Silence Surround Channel(s)</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Extended Bitstream Information &#8211; Part 2</p>
<dl>
<dt><code>-dsurex_mode</code> <i>mode</i></p>
<dd> Dolby Surround <font SIZE="-1">EX</font> Mode. Indicates whether the stream uses Dolby Surround <font SIZE="-1">EX</font> (7.1 matrixed to 5.1). Using this option does <font SIZE="-1"><code>NOT</code></font> mean the encoder will actually apply Dolby Surround <font SIZE="-1">EX</font> processing.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>notindicated</code></p>
<dd> Not Indicated (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>on</code></p>
<dd> Dolby Surround <font SIZE="-1">EX</font> Off</p>
<dt><code>2</code></p>
<dd>
<dt><code>off</code></p>
<dd> Dolby Surround <font SIZE="-1">EX</font> On</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-dheadphone_mode</code> <i>mode</i></p>
<dd> Dolby Headphone Mode. Indicates whether the stream uses Dolby Headphone encoding (multi-channel matrixed to 2.0 for use with headphones). Using this option does <font SIZE="-1"><code>NOT</code></font> mean the encoder will actually apply Dolby Headphone processing.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>notindicated</code></p>
<dd> Not Indicated (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>on</code></p>
<dd> Dolby Headphone Off</p>
<dt><code>2</code></p>
<dd>
<dt><code>off</code></p>
<dd> Dolby Headphone On</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-ad_conv_type</code> <i>type</i></p>
<dd> A/D Converter Type. Indicates whether the audio has passed through <font SIZE="-1">HDCD A/D</font> conversion.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd>
<dt><code>standard</code></p>
<dd> Standard A/D Converter (default)</p>
<dt><code>1</code></p>
<dd>
<dt><code>hdcd</code></p>
<dd> <font SIZE="-1">HDCD A/D</font> Converter</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>Other </i><font SIZE="-1"><i>AC-3</i></font><i> Encoding Options</i></p>
<dl>
<dt><code>-stereo_rematrixing</code> <i>boolean</i></p>
<dd> Stereo Rematrixing. Enables/Disables use of rematrixing for stereo input. This is an optional <font SIZE="-1">AC-3</font> feature that increases quality by selectively encoding the left/right channels as mid/side. This option is enabled by default, and it is highly recommended that it be left as enabled except for testing purposes.</p>
<dt><code>cutoff</code> <i>frequency</i></p>
<dd> Set lowpass cutoff frequency. If unspecified, the encoder selects a default determined by various other encoding parameters.</dl>
<p> <i>Floating-Point-Only </i><font SIZE="-1"><i>AC-3</i></font><i> Encoding Options</i> </p>
<p> These options are only valid for the floating-point encoder and do not exist for the fixed-point encoder due to the corresponding features not being implemented in fixed-point.</p>
<dl>
<dt><code>-channel_coupling</code> <i>boolean</i></p>
<dd> Enables/Disables use of channel coupling, which is an optional <font SIZE="-1">AC-3</font> feature that increases quality by combining high frequency information from multiple channels into a single channel. The per-channel high frequency information is sent with less accuracy in both the frequency and time domains. This allows more bits to be used for lower frequencies while preserving enough information to reconstruct the high frequencies. This option is enabled by default for the floating-point encoder and should generally be left as enabled except for testing purposes or to increase encoding speed.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd>
<dt><code>auto</code></p>
<dd> Selected by Encoder (default)</p>
<dt><code>0</code></p>
<dd>
<dt><code>off</code></p>
<dd> Disable Channel Coupling</p>
<dt><code>1</code></p>
<dd>
<dt><code>on</code></p>
<dd> Enable Channel Coupling</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-cpl_start_band</code> <i>number</i></p>
<dd> Coupling Start Band. Sets the channel coupling start band, from 1 to 15. If a value higher than the bandwidth is used, it will be reduced to 1 less than the coupling end band. If <i>auto</i> is used, the start band will be determined by the encoder based on the bit rate, sample rate, and channel layout. This option has no effect if channel coupling is disabled.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd>
<dt><code>auto</code></p>
<dd> Selected by Encoder (default)</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>flac</h3>
<p> <font SIZE="-1">FLAC</font> (Free Lossless Audio Codec) Encoder </p>
<p> <i>Options</i> </p>
<p> The following options are supported by FFmpeg&#8217;s flac encoder.</p>
<dl>
<dt><code>compression_level</code></p>
<dd> Sets the compression level, which chooses defaults for many other options if they are not set explicitly. Valid values are from 0 to 12, 5 is the default.</p>
<dt><code>frame_size</code></p>
<dd> Sets the size of the frames in samples per channel.</p>
<dt><code>lpc_coeff_precision</code></p>
<dd> Sets the <font SIZE="-1">LPC</font> coefficient precision, valid values are from 1 to 15, 15 is the default.</p>
<dt><code>lpc_type</code></p>
<dd> Sets the first stage <font SIZE="-1">LPC</font> algorithm</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> <font SIZE="-1">LPC</font> is not used</p>
<dt><code>fixed</code></p>
<dd> fixed <font SIZE="-1">LPC</font> coefficients</p>
<dt><code>levinson</code></p>
<dd>
<dt><code>cholesky</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>lpc_passes</code></p>
<dd> Number of passes to use for Cholesky factorization during <font SIZE="-1">LPC</font> analysis</p>
<dt><code>min_partition_order</code></p>
<dd> The minimum partition order</p>
<dt><code>max_partition_order</code></p>
<dd> The maximum partition order</p>
<dt><code>prediction_order_method</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>estimation</code></p>
<dd>
<dt><code>2level</code></p>
<dd>
<dt><code>4level</code></p>
<dd>
<dt><code>8level</code></p>
<dd>
<dt><code>search</code></p>
<dd> Bruteforce search</p>
<dt><code>log</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>ch_mode</code></p>
<dd> Channel mode</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> The mode is chosen automatically for each frame</p>
<dt><code>indep</code></p>
<dd> Channels are independently coded</p>
<dt><code>left_side</code></p>
<dd>
<dt><code>right_side</code></p>
<dd>
<dt><code>mid_side</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>exact_rice_parameters</code></p>
<dd> Chooses if rice parameters are calculated exactly or approximately. if set to 1 then they are chosen exactly, which slows the code down slightly and improves compression slightly.</p>
<dt><code>multi_dim_quant</code></p>
<dd> Multi Dimensional Quantization. If set to 1 then a 2nd stage <font SIZE="-1">LPC</font> algorithm is applied after the first stage to finetune the coefficients. This is quite slow and slightly improves compression.</dl>
<h3>opus</h3>
<p> Opus encoder. </p>
<p> This is a native FFmpeg encoder for the Opus format. Currently its in development and only implements the <font SIZE="-1">CELT</font> part of the codec. Its quality is usually worse and at best is equal to the libopus encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></p>
<dd> Set bit rate in bits/s. If unspecified it uses the number of channels and the layout to make a good guess.</p>
<dt><code>opus_delay</code></p>
<dd> Sets the maximum delay in milliseconds. Lower delays than 20ms will very quickly decrease quality.</dl>
<h3>libfdk_aac</h3>
<p> libfdk-aac <font SIZE="-1">AAC</font> (Advanced Audio Coding) encoder wrapper. </p>
<p> The libfdk-aac library is based on the Fraunhofer <font SIZE="-1">FDK AAC</font> code from the Android project. </p>
<p> Requires the presence of the libfdk-aac headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libfdk-aac&quot;</tt>. The library is also incompatible with <font SIZE="-1">GPL,</font> so if you allow the use of <font SIZE="-1">GPL,</font> you should configure with <tt>&quot;--enable-gpl --enable-nonfree --enable-libfdk-aac&quot;</tt>. </p>
<p> This encoder has support for the AAC-HE profiles. </p>
<p> <font SIZE="-1">VBR</font> encoding, enabled through the <code>vbr</code> or <code>flags +qscale</code> options, is experimental and only works with some combinations of parameters. </p>
<p> Support for encoding 7.1 audio is only available with libfdk-aac 0.1.3 or higher. </p>
<p> For more information see the fdk-aac project at &lt;<code><a rel="nofollow" href="http://sourceforge.net/p/opencore-amr/fdk-aac/">http://sourceforge.net/p/opencore-amr/fdk-aac/</a></code>&gt;. </p>
<p> <i>Options</i> </p>
<p> The following options are mapped on the shared FFmpeg codec options.</p>
<dl>
<dt><code>b</code></p>
<dd> Set bit rate in bits/s. If the bitrate is not explicitly specified, it is automatically set to a suitable value depending on the selected profile. </p>
<p> In case <font SIZE="-1">VBR</font> mode is enabled the option is ignored.</p>
<dt><code>ar</code></p>
<dd> Set audio sampling rate (in Hz).</p>
<dt><code>channels</code></p>
<dd> Set the number of audio channels.</p>
<dt><code>flags +qscale</code></p>
<dd> Enable fixed quality, <font SIZE="-1">VBR</font> (Variable Bit Rate) mode. Note that <font SIZE="-1">VBR</font> is implicitly enabled when the <code>vbr</code> value is positive.</p>
<dt><code>cutoff</code></p>
<dd> Set cutoff frequency. If not specified (or explicitly set to 0) it will use a value automatically computed by the library. Default value is 0.</p>
<dt><code>profile</code></p>
<dd> Set audio profile. </p>
<p> The following profiles are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>aac_low</code></p>
<dd> Low Complexity <font SIZE="-1">AAC</font> (<font SIZE="-1">LC</font>)</p>
<dt><code>aac_he</code></p>
<dd> High Efficiency <font SIZE="-1">AAC</font> (HE-AAC)</p>
<dt><code>aac_he_v2</code></p>
<dd> High Efficiency <font SIZE="-1">AAC</font> version 2 (HE-AACv2)</p>
<dt><code>aac_ld</code></p>
<dd> Low Delay <font SIZE="-1">AAC</font> (<font SIZE="-1">LD</font>)</p>
<dt><code>aac_eld</code></p>
<dd> Enhanced Low Delay <font SIZE="-1">AAC</font> (<font SIZE="-1">ELD</font>)</dl>
</dl>
<dl>
<dt>
<dd>
<p> If not specified it is set to <code>aac_low</code>.</dl>
</dl>
<p> The following are private options of the libfdk_aac encoder.</p>
<dl>
<dt><code>afterburner</code></p>
<dd> Enable afterburner feature if set to 1, disabled if set to 0. This improves the quality but also the required processing power. </p>
<p> Default value is 1.</p>
<dt><code>eld_sbr</code></p>
<dd> Enable <font SIZE="-1">SBR</font> (Spectral Band Replication) for <font SIZE="-1">ELD</font> if set to 1, disabled if set to 0. </p>
<p> Default value is 0.</p>
<dt><code>eld_v2</code></p>
<dd> Enable ELDv2 (LD-MPS extension for <font SIZE="-1">ELD</font> stereo signals) for ELDv2 if set to 1, disabled if set to 0. </p>
<p> Note that option is available when fdk-aac version (<font SIZE="-1">AACENCODER_LIB_VL0.AACENCODER_LIB_VL1.AACENCODER_LIB_VL2</font>) &gt; (4.0.0). </p>
<p> Default value is 0.</p>
<dt><code>signaling</code></p>
<dd> Set <font SIZE="-1">SBR/PS</font> signaling style. </p>
<p> It can assume one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd> choose signaling implicitly (explicit hierarchical by default, implicit if global header is disabled)</p>
<dt><code>implicit</code></p>
<dd> implicit backwards compatible signaling</p>
<dt><code>explicit_sbr</code></p>
<dd> explicit <font SIZE="-1">SBR,</font> implicit <font SIZE="-1">PS</font> signaling</p>
<dt><code>explicit_hierarchical</code></p>
<dd> explicit hierarchical signaling</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>default</code>.</dl>
<dt><code>latm</code></p>
<dd> Output <font SIZE="-1">LATM/LOAS</font> encapsulated data if set to 1, disabled if set to 0. </p>
<p> Default value is 0.</p>
<dt><code>header_period</code></p>
<dd> Set StreamMuxConfig and <font SIZE="-1">PCE</font> repetition period (in frames) for sending in-band configuration buffers within <font SIZE="-1">LATM/LOAS</font> transport layer. </p>
<p> Must be a 16-bits non-negative integer. </p>
<p> Default value is 0.</p>
<dt><code>vbr</code></p>
<dd> Set <font SIZE="-1">VBR</font> mode, from 1 to 5. 1 is lowest quality (though still pretty good) and 5 is highest quality. A value of 0 will disable <font SIZE="-1">VBR,</font> and <font SIZE="-1">CBR</font> (Constant Bit Rate) is enabled. </p>
<p> Currently only the <code>aac_low</code> profile supports <font SIZE="-1">VBR</font> encoding. </p>
<p> <font SIZE="-1">VBR</font> modes 1-5 correspond to roughly the following average bit rates:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1</code></p>
<dd> 32 kbps/channel</p>
<dt><code>2</code></p>
<dd> 40 kbps/channel</p>
<dt><code>3</code></p>
<dd> 48-56 kbps/channel</p>
<dt><code>4</code></p>
<dd> 64 kbps/channel</p>
<dt><code>5</code></p>
<dd> about 80-96 kbps/channel</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is 0.</dl>
</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to convert an audio file to <font SIZE="-1">VBR AAC</font> in an M4A (<font SIZE="-1">MP4</font>) container: </p>
<pre>
        ffmpeg -i input.wav -codec:a libfdk_aac -vbr 3 output.m4a
</pre>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to convert an audio file to <font SIZE="-1">CBR</font> 64k kbps <font SIZE="-1">AAC,</font> using the High-Efficiency <font SIZE="-1">AAC</font> profile: </p>
<pre>
        ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he -b:a 64k output.m4a
</pre>
</dl>
<h3>libmp3lame</h3>
<p> <font SIZE="-1">LAME</font> (Lame Ain&#8217;t an <font SIZE="-1">MP3</font> Encoder) <font SIZE="-1">MP3</font> encoder wrapper. </p>
<p> Requires the presence of the libmp3lame headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libmp3lame&quot;</tt>. </p>
<p> See <code>libshine</code> for a fixed-point <font SIZE="-1">MP3</font> encoder, although with a lower quality. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libmp3lame wrapper. The <code>lame</code>-equivalent of the options are listed in parentheses.</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></p>
<dd> Set bitrate expressed in bits/s for <font SIZE="-1">CBR</font> or <font SIZE="-1">ABR. LAME</font> <tt>&quot;bitrate&quot;</tt> is expressed in kilobits/s.</p>
<dt><code>q (</code><i>-V</i><code>)</code></p>
<dd> Set constant quality setting for <font SIZE="-1">VBR.</font> This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</p>
<dt><code>compression_level (</code><i>-q</i><code>)</code></p>
<dd> Set algorithm quality. Valid arguments are integers in the 0-9 range, with 0 meaning highest quality but slowest, and 9 meaning fastest while producing the worst quality.</p>
<dt><code>cutoff (</code><i>&#8211;lowpass</i><code>)</code></p>
<dd> Set lowpass cutoff frequency. If unspecified, the encoder dynamically adjusts the cutoff.</p>
<dt><code>reservoir</code></p>
<dd> Enable use of bit reservoir when set to 1. Default value is 1. <font SIZE="-1">LAME</font> has this enabled by default, but can be overridden by use <code>&#8211;nores</code> option.</p>
<dt><code>joint_stereo (</code><i>-m j</i><code>)</code></p>
<dd> Enable the encoder to use (on a frame by frame basis) either L/R stereo or mid/side stereo. Default value is 1.</p>
<dt><code>abr (</code><i>&#8211;abr</i><code>)</code></p>
<dd> Enable the encoder to use <font SIZE="-1">ABR</font> when set to 1. The <code>lame</code> <code>&#8211;abr</code> sets the target bitrate, while this options only tells FFmpeg to use <font SIZE="-1">ABR</font> still relies on <code>b</code> to set bitrate.</dl>
<h3>libopencore-amrnb</h3>
<p> OpenCORE Adaptive Multi-Rate Narrowband encoder. </p>
<p> Requires the presence of the libopencore-amrnb headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopencore-amrnb --enable-version3&quot;</tt>. </p>
<p> This is a mono-only encoder. Officially it only supports 8000Hz sample rate, but you can override it by setting <code>strict</code> to <code>unofficial</code> or lower. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></p>
<dd> Set bitrate in bits per second. Only the following bitrates are supported, otherwise libavcodec will round to the nearest valid bitrate.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>4750</code></p>
<dd>
<dt><code>5150</code></p>
<dd>
<dt><code>5900</code></p>
<dd>
<dt><code>6700</code></p>
<dd>
<dt><code>7400</code></p>
<dd>
<dt><code>7950</code></p>
<dd>
<dt><code>10200</code></p>
<dd>
<dt><code>12200</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>dtx</code></p>
<dd> Allow discontinuous transmission (generate comfort noise) when set to 1. The default value is 0 (disabled).</dl>
<h3>libopus</h3>
<p> libopus Opus Interactive Audio Codec encoder wrapper. </p>
<p> Requires the presence of the libopus headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopus&quot;</tt>. </p>
<p> <i>Option Mapping</i> </p>
<p> Most libopus options are modelled after the <code>opusenc</code> utility from opus-tools. The following is an option mapping chart describing options supported by the libopus wrapper, and their <code>opusenc</code>-equivalent in parentheses.</p>
<dl>
<dt><code>b (</code><i>bitrate</i><code>)</code></p>
<dd> Set the bit rate in bits/s. FFmpeg&#8217;s <code>b</code> option is expressed in bits/s, while <code>opusenc</code>&#8216;s <code>bitrate</code> in kilobits/s.</p>
<dt><code>vbr (</code><i>vbr</i><code>,</code> <i>hard-cbr</i><code>, and</code> <i>cvbr</i><code>)</code></p>
<dd> Set <font SIZE="-1">VBR</font> mode. The FFmpeg <code>vbr</code> option has the following valid arguments, with the <code>opusenc</code> equivalent options in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>off (</code><i>hard-cbr</i><code>)</code></p>
<dd> Use constant bit rate encoding.</p>
<dt><code>on (</code><i>vbr</i><code>)</code></p>
<dd> Use variable bit rate encoding (the default).</p>
<dt><code>constrained (</code><i>cvbr</i><code>)</code></p>
<dd> Use constrained variable bit rate encoding.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>compression_level (</code><i>comp</i><code>)</code></p>
<dd> Set encoding algorithm complexity. Valid options are integers in the 0-10 range. 0 gives the fastest encodes but lower quality, while 10 gives the highest quality but slowest encoding. The default is 10.</p>
<dt><code>frame_duration (</code><i>framesize</i><code>)</code></p>
<dd> Set maximum frame size, or duration of a frame in milliseconds. The argument must be exactly the following: 2.5, 5, 10, 20, 40, 60. Smaller frame sizes achieve lower latency but less quality at a given bitrate. Sizes greater than 20ms are only interesting at fairly low bitrates. The default is 20ms.</p>
<dt><code>packet_loss (</code><i>expect-loss</i><code>)</code></p>
<dd> Set expected packet loss percentage. The default is 0.</p>
<dt><code>fec (</code><i>n/a</i><code>)</code></p>
<dd> Enable inband forward error correction. <code>packet_loss</code> must be non-zero to take advantage &#8211; frequency of <font SIZE="-1">FEC</font> &#8216;side-data&#8217; is proportional to expected packet loss. Default is disabled.</p>
<dt><code>application (N.A.)</code></p>
<dd> Set intended application type. Valid options are listed below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>voip</code></p>
<dd> Favor improved speech intelligibility.</p>
<dt><code>audio</code></p>
<dd> Favor faithfulness to the input (the default).</p>
<dt><code>lowdelay</code></p>
<dd> Restrict to only the lowest delay modes.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>cutoff (N.A.)</code></p>
<dd> Set cutoff bandwidth in Hz. The argument must be exactly one of the following: 4000, 6000, 8000, 12000, or 20000, corresponding to narrowband, mediumband, wideband, super wideband, and fullband respectively. The default is 0 (cutoff disabled).</p>
<dt><code>mapping_family (</code><i>mapping_family</i><code>)</code></p>
<dd> Set channel mapping family to be used by the encoder. The default value of -1 uses mapping family 0 for mono and stereo inputs, and mapping family 1 otherwise. The default also disables the surround masking and <font SIZE="-1">LFE</font> bandwidth optimzations in libopus, and requires that the input contains 8 channels or fewer. </p>
<p> Other values include 0 for mono and stereo, 1 for surround sound with masking and <font SIZE="-1">LFE</font> bandwidth optimizations, and 255 for independent streams with an unspecified channel layout.</p>
<dt><code>apply_phase_inv (N.A.) (requires libopus &gt;= 1.2)</code></p>
<dd> If set to 0, disables the use of phase inversion for intensity stereo, improving the quality of mono downmixes, but slightly reducing normal stereo quality. The default is 1 (phase inversion enabled).</dl>
<h3>libshine</h3>
<p> Shine Fixed-Point <font SIZE="-1">MP3</font> encoder wrapper. </p>
<p> Shine is a fixed-point <font SIZE="-1">MP3</font> encoder. It has a far better performance on platforms without an <font SIZE="-1">FPU,</font> e.g. armel CPUs, and some phones and tablets. However, as it is more targeted on performance than quality, it is not on par with <font SIZE="-1">LAME</font> and other production-grade encoders quality-wise. Also, according to the project&#8217;s homepage, this encoder may not be free of bugs as the code was written a long time ago and the project was dead for at least 5 years. </p>
<p> This encoder only supports stereo and mono input. This is also CBR-only. </p>
<p> The original project (last updated in early 2007) is at &lt;<code><a rel="nofollow" href="http://sourceforge.net/projects/libshine-fxp/">http://sourceforge.net/projects/libshine-fxp/</a></code>&gt;. We only support the updated fork by the Savonet/Liquidsoap project at &lt;<code><a rel="nofollow" href="https://github.com/savonet/shine">https://github.com/savonet/shine</a></code>&gt;. </p>
<p> Requires the presence of the libshine headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libshine&quot;</tt>. </p>
<p> See also <code>libmp3lame</code>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libshine wrapper. The <code>shineenc</code>-equivalent of the options are listed in parentheses.</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></p>
<dd> Set bitrate expressed in bits/s for <font SIZE="-1">CBR.</font> <code>shineenc</code> <code>-b</code> option is expressed in kilobits/s.</dl>
<h3>libtwolame</h3>
<p> TwoLAME <font SIZE="-1">MP2</font> encoder wrapper. </p>
<p> Requires the presence of the libtwolame headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libtwolame&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libtwolame wrapper. The <code>twolame</code>-equivalent options follow the FFmpeg ones and are in parentheses.</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></p>
<dd> Set bitrate expressed in bits/s for <font SIZE="-1">CBR.</font> <code>twolame</code> <code>b</code> option is expressed in kilobits/s. Default value is 128k.</p>
<dt><code>q (</code><i>-V</i><code>)</code></p>
<dd> Set quality for experimental <font SIZE="-1">VBR</font> support. Maximum value range is from -50 to 50, useful range is from -10 to 10. The higher the value, the better the quality. This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</p>
<dt><code>mode (</code><i>&#8211;mode</i><code>)</code></p>
<dd> Set the mode of the resulting audio. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> Choose mode automatically based on the input. This is the default.</p>
<dt><code>stereo</code></p>
<dd> Stereo</p>
<dt><code>joint_stereo</code></p>
<dd> Joint stereo</p>
<dt><code>dual_channel</code></p>
<dd> Dual channel</p>
<dt><code>mono</code></p>
<dd> Mono</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>psymodel (</code><i>&#8211;psyc-mode</i><code>)</code></p>
<dd> Set psychoacoustic model to use in encoding. The argument must be an integer between -1 and 4, inclusive. The higher the value, the better the quality. The default value is 3.</p>
<dt><code>energy_levels (</code><i>&#8211;energy</i><code>)</code></p>
<dd> Enable energy levels extensions when set to 1. The default value is 0 (disabled).</p>
<dt><code>error_protection (</code><i>&#8211;protect</i><code>)</code></p>
<dd> Enable <font SIZE="-1">CRC</font> error protection when set to 1. The default value is 0 (disabled).</p>
<dt><code>copyright (</code><i>&#8211;copyright</i><code>)</code></p>
<dd> Set <font SIZE="-1">MPEG</font> audio copyright flag when set to 1. The default value is 0 (disabled).</p>
<dt><code>original (</code><i>&#8211;original</i><code>)</code></p>
<dd> Set <font SIZE="-1">MPEG</font> audio original flag when set to 1. The default value is 0 (disabled).</dl>
<h3>libvo-amrwbenc</h3>
<p> VisualOn Adaptive Multi-Rate Wideband encoder. </p>
<p> Requires the presence of the libvo-amrwbenc headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libvo-amrwbenc --enable-version3&quot;</tt>. </p>
<p> This is a mono-only encoder. Officially it only supports 16000Hz sample rate, but you can override it by setting <code>strict</code> to <code>unofficial</code> or lower. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></p>
<dd> Set bitrate in bits/s. Only the following bitrates are supported, otherwise libavcodec will round to the nearest valid bitrate.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>6600</code></p>
<dd>
<dt><code>8850</code></p>
<dd>
<dt><code>12650</code></p>
<dd>
<dt><code>14250</code></p>
<dd>
<dt><code>15850</code></p>
<dd>
<dt><code>18250</code></p>
<dd>
<dt><code>19850</code></p>
<dd>
<dt><code>23050</code></p>
<dd>
<dt><code>23850</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>dtx</code></p>
<dd> Allow discontinuous transmission (generate comfort noise) when set to 1. The default value is 0 (disabled).</dl>
<h3>libvorbis</h3>
<p> libvorbis encoder wrapper. </p>
<p> Requires the presence of the libvorbisenc headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libvorbis&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libvorbis wrapper. The <code>oggenc</code>-equivalent of the options are listed in parentheses. </p>
<p> To get a more accurate and extensive documentation of the libvorbis options, consult the libvorbisenc&#8217;s and <code>oggenc</code>&#8216;s documentations. See &lt;<code><a rel="nofollow" href="http://xiph.org/vorbis/">http://xiph.org/vorbis/</a></code>&gt;, &lt;<code><a rel="nofollow" href="http://wiki.xiph.org/Vorbis-tools">http://wiki.xiph.org/Vorbis-tools</a></code>&gt;, and <code><a href="/docs/linux/man/1-oggenc/">oggenc</a></code>(1).</p>
<dl>
<dt><code>b (</code><i>-b</i><code>)</code></p>
<dd> Set bitrate expressed in bits/s for <font SIZE="-1">ABR.</font> <code>oggenc</code> <code>-b</code> is expressed in kilobits/s.</p>
<dt><code>q (</code><i>-q</i><code>)</code></p>
<dd> Set constant quality setting for <font SIZE="-1">VBR.</font> The value should be a float number in the range of -1.0 to 10.0. The higher the value, the better the quality. The default value is <code>3.0</code>. </p>
<p> This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</p>
<dt><code>cutoff (</code><i>&#8211;advanced-encode-option lowpass_frequency=N</i><code>)</code></p>
<dd> Set cutoff bandwidth in Hz, a value of 0 disables cutoff. <code>oggenc</code>&#8216;s related option is expressed in kHz. The default value is <code>0</code> (cutoff disabled).</p>
<dt><code>minrate (</code><i>-m</i><code>)</code></p>
<dd> Set minimum bitrate expressed in bits/s. <code>oggenc</code> <code>-m</code> is expressed in kilobits/s.</p>
<dt><code>maxrate (</code><i>-M</i><code>)</code></p>
<dd> Set maximum bitrate expressed in bits/s. <code>oggenc</code> <code>-M</code> is expressed in kilobits/s. This only has effect on <font SIZE="-1">ABR</font> mode.</p>
<dt><code>iblock (</code><i>&#8211;advanced-encode-option impulse_noisetune=N</i><code>)</code></p>
<dd> Set noise floor bias for impulse blocks. The value is a float number from -15.0 to 0.0. A negative bias instructs the encoder to pay special attention to the crispness of transients in the encoded audio. The tradeoff for better transient response is a higher bitrate.</dl>
<h3>mjpeg</h3>
<p> Motion <font SIZE="-1">JPEG</font> encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>huffman</code></p>
<dd> Set the huffman encoding strategy. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd> Use the default huffman tables. This is the default strategy.</p>
<dt><code>optimal</code></p>
<dd> Compute and use optimal huffman tables.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>wavpack</h3>
<p> WavPack lossless audio encoder. </p>
<p> <i>Options</i> </p>
<p> The equivalent options for <code>wavpack</code> command line utility are listed in parentheses. </p>
<p> Shared options </p>
<p> The following shared options are effective for this encoder. Only special notes about this particular encoder will be documented here. For the general meaning of the options, see <code>the Codec Options chapter</code>.</p>
<dl>
<dt><code>frame_size (</code><i>&#8211;blocksize</i><code>)</code></p>
<dd> For this encoder, the range for this option is between 128 and 131072. Default is automatically decided based on sample rate and number of channel. </p>
<p> For the complete formula of calculating default, see <i>libavcodec/wavpackenc.c</i>.</p>
<dt><code>compression_level (</code><i>-f</i><code>,</code> <i>-h</i><code>,</code> <i>-hh</i><code>, and</code> <i>-x</i><code>)</code></p>
<dd></dl>
<p> Private options</p>
<dl>
<dt><code>joint_stereo (</code><i>-j</i><code>)</code></p>
<dd> Set whether to enable joint stereo. Valid values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>on (</code><i>1</i><code>)</code></p>
<dd> Force mid/side audio encoding.</p>
<dt><code>off (</code><i>0</i><code>)</code></p>
<dd> Force left/right audio encoding.</p>
<dt><code>auto</code></p>
<dd> Let the encoder decide automatically.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>optimize_mono</code></p>
<dd> Set whether to enable optimization for mono. This option is only effective for non-mono streams. Available values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>on</code></p>
<dd> enabled</p>
<dt><code>off</code></p>
<dd> disabled</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>VIDEO ENCODERS</h2>
<p> A description of some of the currently available video encoders follows.</p>
<h3><font SIZE="-1">GIF</font></h3>
<p> <font SIZE="-1">GIF</font> image/animation encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>gifflags</code> <i>integer</i></p>
<dd> Sets the flags used for <font SIZE="-1">GIF</font> encoding.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>offsetting</code></p>
<dd> Enables picture offsetting. </p>
<p> Default is enabled.</p>
<dt><code>transdiff</code></p>
<dd> Enables transparency detection between frames. </p>
<p> Default is enabled.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>gifimage</code> <i>integer</i></p>
<dd> Enables encoding one full <font SIZE="-1">GIF</font> image per frame, rather than an animated <font SIZE="-1">GIF.</font> </p>
<p> Default value is <code>0</code>.</p>
<dt><code>global_palette</code> <i>integer</i></p>
<dd> Writes a palette to the global <font SIZE="-1">GIF</font> header where feasible. </p>
<p> If disabled, every frame will always have a palette written, even if there is a global palette supplied. </p>
<p> Default value is <code>1</code>.</dl>
<h3>Hap</h3>
<p> Vidvox Hap video encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>format</code> <i>integer</i></p>
<dd> Specifies the Hap format to encode.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>hap</code></p>
<dd>
<dt><code>hap_alpha</code></p>
<dd>
<dt><code>hap_q</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>hap</code>.</dl>
<dt><code>chunks</code> <i>integer</i></p>
<dd> Specifies the number of chunks to split frames into, between 1 and 64. This permits multithreaded decoding of large frames, potentially at the cost of data-rate. The encoder may modify this value to divide frames evenly. </p>
<p> Default value is <i>1</i>.</p>
<dt><code>compressor</code> <i>integer</i></p>
<dd> Specifies the second-stage compressor to use. If set to <code>none</code>, <code>chunks</code> will be limited to 1, as chunked uncompressed frames offer no benefit.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd>
<dt><code>snappy</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>snappy</code>.</dl>
</dl>
<h3>jpeg2000</h3>
<p> The native jpeg 2000 encoder is lossy by default, the <tt>&quot;-q:v&quot;</tt> option can be used to set the encoding quality. Lossless encoding can be selected with <tt>&quot;-pred 1&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>format</code> <i>integer</i></p>
<dd> Can be set to either <tt>&quot;j2k&quot;</tt> or <tt>&quot;jp2&quot;</tt> (the default) that makes it possible to store non-rgb pix_fmts.</p>
<dt><code>tile_width</code> <i>integer</i></p>
<dd> Sets tile width. Range is 1 to 1073741824. Default is 256.</p>
<dt><code>tile_height</code> <i>integer</i></p>
<dd> Sets tile height. Range is 1 to 1073741824. Default is 256.</p>
<dt><code>pred</code> <i>integer</i></p>
<dd> Allows setting the discrete wavelet transform (<font SIZE="-1">DWT</font>) type</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>dwt97int (Lossy)</code></p>
<dd>
<dt><code>dwt53 (Lossless)</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Default is <tt>&quot;dwt97int&quot;</tt></dl>
<dt><code>sop</code> <i>boolean</i></p>
<dd> Enable this to add <font SIZE="-1">SOP</font> marker at the start of each packet. Disabled by default.</p>
<dt><code>eph</code> <i>boolean</i></p>
<dd> Enable this to add <font SIZE="-1">EPH</font> marker at the end of each packet header. Disabled by default.</p>
<dt><code>prog</code> <i>integer</i></p>
<dd> Sets the progression order to be used by the encoder. Possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>lrcp</code></p>
<dd>
<dt><code>rlcp</code></p>
<dd>
<dt><code>rpcl</code></p>
<dd>
<dt><code>pcrl</code></p>
<dd>
<dt><code>cprl</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Set to <tt>&quot;lrcp&quot;</tt> by default.</dl>
<dt><code>layer_rates</code> <i>string</i></p>
<dd> By default, when this option is not used, compression is done using the quality metric. This option allows for compression using compression ratio. The compression ratio for each level could be specified. The compression ratio of a layer <tt>&quot;l&quot;</tt> species the what ratio of total file size is contained in the first <tt>&quot;l&quot;</tt> layers. </p>
<p> Example usage: </p>
<pre>
        ffmpeg -i input.bmp -c:v jpeg2000 -layer_rates &quot;100,10,1&quot; output.j2k
</pre>
<p> This would compress the image to contain 3 layers, where the data contained in the first layer would be compressed by 1000 times, compressed by 100 in the first two layers, and shall contain all data while using all 3 layers.</dl>
<h3>librav1e</h3>
<p> rav1e <font SIZE="-1">AV1</font> encoder wrapper. </p>
<p> Requires the presence of the rav1e headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-librav1e&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>qmax</code></p>
<dd> Sets the maximum quantizer to use when using bitrate mode.</p>
<dt><code>qmin</code></p>
<dd> Sets the minimum quantizer to use when using bitrate mode.</p>
<dt><code>qp</code></p>
<dd> Uses quantizer mode to encode at the given quantizer (0-255).</p>
<dt><code>speed</code></p>
<dd> Selects the speed preset (0-10) to encode with.</p>
<dt><code>tiles</code></p>
<dd> Selects how many tiles to encode with.</p>
<dt><code>tile-rows</code></p>
<dd> Selects how many rows of tiles to encode with.</p>
<dt><code>tile-columns</code></p>
<dd> Selects how many columns of tiles to encode with.</p>
<dt><code>rav1e-params</code></p>
<dd> Set rav1e options using a list of <i>key</i>=<i>value</i> pairs separated by &#8220;:&#8221;. See <code>rav1e &#8211;help</code> for a list of options. </p>
<p> For example to specify librav1e encoding options with <code>-rav1e-params</code>: </p>
<pre>
        ffmpeg -i input -c:v librav1e -b:v 500K -rav1e-params speed=5:low_latency=true output.mp4
</pre>
</dl>
<h3>libaom-av1</h3>
<p> libaom <font SIZE="-1">AV1</font> encoder wrapper. </p>
<p> Requires the presence of the libaom headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libaom&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The wrapper supports the following standard libavcodec options:</p>
<dl>
<dt><code>b</code></p>
<dd> Set bitrate target in bits/second. By default this will use variable-bitrate mode. If <code>maxrate</code> and <code>minrate</code> are also set to the same value then it will use constant-bitrate mode, otherwise if <code>crf</code> is set as well then it will use constrained-quality mode.</p>
<dt><code>g keyint_min</code></p>
<dd> Set key frame placement. The <font SIZE="-1">GOP</font> size sets the maximum distance between key frames; if zero the output stream will be intra-only. The minimum distance is ignored unless it is the same as the <font SIZE="-1">GOP</font> size, in which case key frames will always appear at a fixed interval. Not set by default, so without this option the library has completely free choice about where to place key frames.</p>
<dt><code>qmin qmax</code></p>
<dd> Set minimum/maximum quantisation values. Valid range is from 0 to 63 (warning: this does not match the quantiser values actually used by <font SIZE="-1">AV1</font> &#8211; divide by four to map real quantiser values to this range). Defaults to min/max (no constraint).</p>
<dt><code>minrate maxrate bufsize rc_init_occupancy</code></p>
<dd> Set rate control buffering parameters. Not used if not set &#8211; defaults to unconstrained variable bitrate.</p>
<dt><code>threads</code></p>
<dd> Set the number of threads to use while encoding. This may require the <code>tiles</code> or <code>row-mt</code> options to also be set to actually use the specified number of threads fully. Defaults to the number of hardware threads supported by the host machine.</p>
<dt><code>profile</code></p>
<dd> Set the encoding profile. Defaults to using the profile which matches the bit depth and chroma subsampling of the input.</dl>
<p> The wrapper also has some specific options:</p>
<dl>
<dt><code>cpu-used</code></p>
<dd> Set the quality/encoding speed tradeoff. Valid range is from 0 to 8, higher numbers indicating greater speed and lower quality. The default value is 1, which will be slow and high quality.</p>
<dt><code>auto-alt-ref</code></p>
<dd> Enable use of alternate reference frames. Defaults to the internal default of the library.</p>
<dt><code>arnr-max-frames (</code><i>frames</i><code>)</code></p>
<dd> Set altref noise reduction max frame count. Default is -1.</p>
<dt><code>arnr-strength (</code><i>strength</i><code>)</code></p>
<dd> Set altref noise reduction filter strength. Range is -1 to 6. Default is -1.</p>
<dt><code>aq-mode (</code><i>aq-mode</i><code>)</code></p>
<dd> Set adaptive quantization mode. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (</code><i>0</i><code>)</code></p>
<dd> Disabled.</p>
<dt><code>variance (</code><i>1</i><code>)</code></p>
<dd> Variance-based.</p>
<dt><code>complexity (</code><i>2</i><code>)</code></p>
<dd> Complexity-based.</p>
<dt><code>cyclic (</code><i>3</i><code>)</code></p>
<dd> Cyclic refresh.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>tune (</code><i>tune</i><code>)</code></p>
<dd> Set the distortion metric the encoder is tuned with. Default is <tt>&quot;psnr&quot;</tt>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>psnr (</code><i>0</i><code>)</code></p>
<dd>
<dt><code>ssim (</code><i>1</i><code>)</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>lag-in-frames</code></p>
<dd> Set the maximum number of frames which the encoder may keep in flight at any one time for lookahead purposes. Defaults to the internal default of the library.</p>
<dt><code>error-resilience</code></p>
<dd> Enable error resilience features:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd> Improve resilience against losses of whole frames.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Not enabled by default.</dl>
<dt><code>crf</code></p>
<dd> Set the quality/size tradeoff for constant-quality (no bitrate target) and constrained-quality (with maximum bitrate target) modes. Valid range is 0 to 63, higher numbers indicating lower quality and smaller output size. Only used if set; by default only the bitrate target is used.</p>
<dt><code>static-thresh</code></p>
<dd> Set a change threshold on blocks below which they will be skipped by the encoder. Defined in arbitrary units as a nonnegative integer, defaulting to zero (no blocks are skipped).</p>
<dt><code>drop-threshold</code></p>
<dd> Set a threshold for dropping frames when close to rate control bounds. Defined as a percentage of the target buffer &#8211; when the rate control buffer falls below this percentage, frames will be dropped until it has refilled above the threshold. Defaults to zero (no frames are dropped).</p>
<dt><code>denoise-noise-level (</code><i>level</i><code>)</code></p>
<dd> Amount of noise to be removed for grain synthesis. Grain synthesis is disabled if this option is not set or set to 0.</p>
<dt><code>denoise-block-size (</code><i>pixels</i><code>)</code></p>
<dd> Block size used for denoising for grain synthesis. If not set, <font SIZE="-1">AV1</font> codec uses the default value of 32.</p>
<dt><code>undershoot-pct (</code><i>pct</i><code>)</code></p>
<dd> Set datarate undershoot (min) percentage of the target bitrate. Range is -1 to 100. Default is -1.</p>
<dt><code>overshoot-pct (</code><i>pct</i><code>)</code></p>
<dd> Set datarate overshoot (max) percentage of the target bitrate. Range is -1 to 1000. Default is -1.</p>
<dt><code>minsection-pct (</code><i>pct</i><code>)</code></p>
<dd> Minimum percentage variation of the <font SIZE="-1">GOP</font> bitrate from the target bitrate. If minsection-pct is not set, the libaomenc wrapper computes it as follows: <tt>&quot;(minrate * 100 / bitrate)&quot;</tt>. Range is -1 to 100. Default is -1 (unset).</p>
<dt><code>maxsection-pct (</code><i>pct</i><code>)</code></p>
<dd> Maximum percentage variation of the <font SIZE="-1">GOP</font> bitrate from the target bitrate. If maxsection-pct is not set, the libaomenc wrapper computes it as follows: <tt>&quot;(maxrate * 100 / bitrate)&quot;</tt>. Range is -1 to 5000. Default is -1 (unset).</p>
<dt><code>frame-parallel (</code><i>boolean</i><code>)</code></p>
<dd> Enable frame parallel decodability features. Default is true.</p>
<dt><code>tiles</code></p>
<dd> Set the number of tiles to encode the input video with, as columns x rows. Larger numbers allow greater parallelism in both encoding and decoding, but may decrease coding efficiency. Defaults to the minimum number of tiles required by the size of the input video (this is 1&#215;1 (that is, a single tile) for sizes up to and including 4K).</p>
<dt><code>tile-columns tile-rows</code></p>
<dd> Set the number of tiles as log2 of the number of tile rows and columns. Provided for compatibility with libvpx/VP9.</p>
<dt><code>row-mt (Requires libaom &gt;= 1.0.0-759-g90a15f4f2)</code></p>
<dd> Enable row based multi-threading. Disabled by default.</p>
<dt><code>enable-cdef (</code><i>boolean</i><code>)</code></p>
<dd> Enable Constrained Directional Enhancement Filter. The libaom-av1 encoder enables <font SIZE="-1">CDEF</font> by default.</p>
<dt><code>enable-restoration (</code><i>boolean</i><code>)</code></p>
<dd> Enable Loop Restoration Filter. Default is true for libaom-av1.</p>
<dt><code>enable-global-motion (</code><i>boolean</i><code>)</code></p>
<dd> Enable the use of global motion for block prediction. Default is true.</p>
<dt><code>enable-intrabc (</code><i>boolean</i><code>)</code></p>
<dd> Enable block copy mode for intra block prediction. This mode is useful for screen content. Default is true.</p>
<dt><code>enable-rect-partitions (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable rectangular partitions. Default is true.</p>
<dt><code>enable-1to4-partitions (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable 1:4/4:1 partitions. Default is true.</p>
<dt><code>enable-ab-partitions (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable <font SIZE="-1">AB</font> shape partitions. Default is true.</p>
<dt><code>enable-angle-delta (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable angle delta intra prediction. Default is true.</p>
<dt><code>enable-cfl-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable chroma predicted from luma intra prediction. Default is true.</p>
<dt><code>enable-filter-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable filter intra predictor. Default is true.</p>
<dt><code>enable-intra-edge-filter (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable intra edge filter. Default is true.</p>
<dt><code>enable-smooth-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable smooth intra prediction mode. Default is true.</p>
<dt><code>enable-paeth-intra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable paeth predictor in intra prediction. Default is true.</p>
<dt><code>enable-palette (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable palette prediction mode. Default is true.</p>
<dt><code>enable-flip-idtx (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable extended transform type, including <font SIZE="-1">FLIPADST_DCT, DCT_FLIPADST, FLIPADST_FLIPADST, ADST_FLIPADST, FLIPADST_ADST, IDTX, V_DCT, H_DCT, V_ADST, H_ADST, V_FLIPADST, H_FLIPADST.</font> Default is true.</p>
<dt><code>enable-tx64 (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable 64-pt transform. Default is true.</p>
<dt><code>reduced-tx-type-set (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Use reduced set of transform types. Default is false.</p>
<dt><code>use-intra-dct-only (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Use <font SIZE="-1">DCT</font> only for <font SIZE="-1">INTRA</font> modes. Default is false.</p>
<dt><code>use-inter-dct-only (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Use <font SIZE="-1">DCT</font> only for <font SIZE="-1">INTER</font> modes. Default is false.</p>
<dt><code>use-intra-default-tx-only (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Use Default-transform only for <font SIZE="-1">INTRA</font> modes. Default is false.</p>
<dt><code>enable-ref-frame-mvs (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable temporal mv prediction. Default is true.</p>
<dt><code>enable-reduced-reference-set (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Use reduced set of single and compound references. Default is false.</p>
<dt><code>enable-obmc (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable obmc. Default is true.</p>
<dt><code>enable-dual-filter (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable dual filter. Default is true.</p>
<dt><code>enable-diff-wtd-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable difference-weighted compound. Default is true.</p>
<dt><code>enable-dist-wtd-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable distance-weighted compound. Default is true.</p>
<dt><code>enable-onesided-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable one sided compound. Default is true.</p>
<dt><code>enable-interinter-wedge (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable interinter wedge compound. Default is true.</p>
<dt><code>enable-interintra-wedge (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable interintra wedge compound. Default is true.</p>
<dt><code>enable-masked-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable masked compound. Default is true.</p>
<dt><code>enable-interintra-comp (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable interintra compound. Default is true.</p>
<dt><code>enable-smooth-interintra (</code><i>boolean</i><code>) (Requires libaom &gt;= v2.0.0)</code></p>
<dd> Enable smooth interintra mode. Default is true.</p>
<dt><code>aom-params</code></p>
<dd> Set libaom options using a list of <i>key</i>=<i>value</i> pairs separated by &#8220;:&#8221;. For a list of supported options, see <code>aomenc &#8211;help</code> under the section &#8220;<font SIZE="-1">AV1</font> Specific Options&#8221;. </p>
<p> For example to specify libaom encoding options with <code>-aom-params</code>: </p>
<pre>
        ffmpeg -i input -c:v libaom-av1 -b:v 500K -aom-params tune=psnr:enable-tpl-model=1 output.mp4
</pre>
</dl>
<h3>libsvtav1</h3>
<p> <font SIZE="-1">SVT-AV1</font> encoder wrapper. </p>
<p> Requires the presence of the <font SIZE="-1">SVT-AV1</font> headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libsvtav1&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>profile</code></p>
<dd> Set the encoding profile.</p>
<dt><code>level</code></p>
<dd> Set the operating point level.</p>
<dt><code>tier</code></p>
<dd> Set the operating point tier.</p>
<dt><code>rc</code></p>
<dd> Set the rate control mode to use. </p>
<p> Possible modes:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cqp</code></p>
<dd> Constant quantizer: use fixed values of qindex (dependent on the frame type) throughout the stream. This mode is the default.</p>
<dt><code>vbr</code></p>
<dd> Variable bitrate: use a target bitrate for the whole stream.</p>
<dt><code>cvbr</code></p>
<dd> Constrained variable bitrate: use a target bitrate for each <font SIZE="-1">GOP.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>qmax</code></p>
<dd> Set the maximum quantizer to use when using a bitrate mode.</p>
<dt><code>qmin</code></p>
<dd> Set the minimum quantizer to use when using a bitrate mode.</p>
<dt><code>qp</code></p>
<dd> Set the quantizer used in cqp rate control mode (0-63).</p>
<dt><code>sc_detection</code></p>
<dd> Enable scene change detection.</p>
<dt><code>la_depth</code></p>
<dd> Set number of frames to look ahead (0-120).</p>
<dt><code>preset</code></p>
<dd> Set the quality-speed tradeoff, in the range 0 to 8. Higher values are faster but lower quality. Defaults to 8 (highest speed).</p>
<dt><code>tile_rows</code></p>
<dd> Set log2 of the number of rows of tiles to use (0-6).</p>
<dt><code>tile_columns</code></p>
<dd> Set log2 of the number of columns of tiles to use (0-4).</dl>
<h3>libkvazaar</h3>
<p> Kvazaar H.265/HEVC encoder. </p>
<p> Requires the presence of the libkvazaar headers and library during configuration. You need to explicitly configure the build with <code>&#8211;enable-libkvazaar</code>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></p>
<dd> Set target video bitrate in bit/s and enable rate control.</p>
<dt><code>kvazaar-params</code></p>
<dd> Set kvazaar parameters as a list of <i>name</i>=<i>value</i> pairs separated by commas (,). See kvazaar documentation for a list of options.</dl>
<h3>libopenh264</h3>
<p> Cisco libopenh264 H.264/MPEG-4 <font SIZE="-1">AVC</font> encoder wrapper. </p>
<p> This encoder requires the presence of the libopenh264 headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libopenh264&quot;</tt>. The library is detected using <code>pkg-config</code>. </p>
<p> For more information about the library see &lt;<code><a rel="nofollow" href="http://www.openh264.org">http://www.openh264.org</a></code>&gt;. </p>
<p> <i>Options</i> </p>
<p> The following FFmpeg global options affect the configurations of the libopenh264 encoder.</p>
<dl>
<dt><code>b</code></p>
<dd> Set the bitrate (as a number of bits per second).</p>
<dt><code>g</code></p>
<dd> Set the <font SIZE="-1">GOP</font> size.</p>
<dt><code>maxrate</code></p>
<dd> Set the max bitrate (as a number of bits per second).</p>
<dt><code>flags +global_header</code></p>
<dd> Set global header in the bitstream.</p>
<dt><code>slices</code></p>
<dd> Set the number of slices, used in parallelized encoding. Default value is 0. This is only used when <code>slice_mode</code> is set to <code>fixed</code>.</p>
<dt><code>slice_mode</code></p>
<dd> Set slice mode. Can assume one of the following possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fixed</code></p>
<dd> a fixed number of slices</p>
<dt><code>rowmb</code></p>
<dd> one slice per row of macroblocks</p>
<dt><code>auto</code></p>
<dd> automatic number of slices according to number of threads</p>
<dt><code>dyn</code></p>
<dd> dynamic slicing</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>auto</code>.</dl>
<dt><code>loopfilter</code></p>
<dd> Enable loop filter, if set to 1 (automatically enabled). To disable set a value of 0.</p>
<dt><code>profile</code></p>
<dd> Set profile restrictions. If set to the value of <code>main</code> enable <font SIZE="-1">CABAC</font> (set the <tt>&quot;SEncParamExt.iEntropyCodingModeFlag&quot;</tt> flag to 1).</p>
<dt><code>max_nal_size</code></p>
<dd> Set maximum <font SIZE="-1">NAL</font> size in bytes.</p>
<dt><code>allow_skip_frames</code></p>
<dd> Allow skipping frames to hit the target bitrate if set to 1.</dl>
<h3>libtheora</h3>
<p> libtheora Theora encoder wrapper. </p>
<p> Requires the presence of the libtheora headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libtheora&quot;</tt>. </p>
<p> For more information about the libtheora project see &lt;<code><a rel="nofollow" href="http://www.theora.org/">http://www.theora.org/</a></code>&gt;. </p>
<p> <i>Options</i> </p>
<p> The following global options are mapped to internal libtheora options which affect the quality and the bitrate of the encoded stream.</p>
<dl>
<dt><code>b</code></p>
<dd> Set the video bitrate in bit/s for <font SIZE="-1">CBR</font> (Constant Bit Rate) mode. In case <font SIZE="-1">VBR</font> (Variable Bit Rate) mode is enabled this option is ignored.</p>
<dt><code>flags</code></p>
<dd> Used to enable constant quality mode (<font SIZE="-1">VBR</font>) encoding through the <code>qscale</code> flag, and to enable the <tt>&quot;pass1&quot;</tt> and <tt>&quot;pass2&quot;</tt> modes.</p>
<dt><code>g</code></p>
<dd> Set the <font SIZE="-1">GOP</font> size.</p>
<dt><code>global_quality</code></p>
<dd> Set the global quality as an integer in lambda units. </p>
<p> Only relevant when <font SIZE="-1">VBR</font> mode is enabled with <tt>&quot;flags +qscale&quot;</tt>. The value is converted to <font SIZE="-1">QP</font> units by dividing it by <tt>&quot;FF_QP2LAMBDA&quot;</tt>, clipped in the [0 &#8211; 10] range, and then multiplied by 6.3 to get a value in the native libtheora range [0-63]. A higher value corresponds to a higher quality.</p>
<dt><code>q</code></p>
<dd> Enable <font SIZE="-1">VBR</font> mode when set to a non-negative value, and set constant quality value as a double floating point value in <font SIZE="-1">QP</font> units. </p>
<p> The value is clipped in the [0-10] range, and then multiplied by 6.3 to get a value in the native libtheora range [0-63]. </p>
<p> This option is valid only using the <code>ffmpeg</code> command-line tool. For library interface users, use <code>global_quality</code>.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Set maximum constant quality (<font SIZE="-1">VBR</font>) encoding with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i INPUT -codec:v libtheora -q:v 10 OUTPUT.ogg
</pre>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to convert a <font SIZE="-1">CBR 1000</font> kbps Theora video stream: </p>
<pre>
        ffmpeg -i INPUT -codec:v libtheora -b:v 1000k OUTPUT.ogg
</pre>
</dl>
<h3>libvpx</h3>
<p> <font SIZE="-1">VP8/VP9</font> format supported through libvpx. </p>
<p> Requires the presence of the libvpx headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libvpx&quot;</tt>. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libvpx wrapper. The <code>vpxenc</code>-equivalent options or values are listed in parentheses for easy migration. </p>
<p> To reduce the duplication of documentation, only the private options and some others requiring special attention are documented here. For the documentation of the undocumented generic options, see <code>the Codec Options chapter</code>. </p>
<p> To get more documentation of the libvpx options, invoke the command <code>ffmpeg -h encoder=libvpx</code>, <code>ffmpeg -h encoder=libvpx-vp9</code> or <code>vpxenc &#8211;help</code>. Further information is available in the libvpx <font SIZE="-1">API</font> documentation.</p>
<dl>
<dt><code>b (</code><i>target-bitrate</i><code>)</code></p>
<dd> Set bitrate in bits/s. Note that FFmpeg&#8217;s <code>b</code> option is expressed in bits/s, while <code>vpxenc</code>&#8216;s <code>target-bitrate</code> is in kilobits/s.</p>
<dt><code>g (</code><i>kf-max-dist</i><code>)</code></p>
<dd>
<dt><code>keyint_min (</code><i>kf-min-dist</i><code>)</code></p>
<dd>
<dt><code>qmin (</code><i>min-q</i><code>)</code></p>
<dd>
<dt><code>qmax (</code><i>max-q</i><code>)</code></p>
<dd>
<dt><code>bufsize (</code><i>buf-sz</i><code>,</code> <i>buf-optimal-sz</i><code>)</code></p>
<dd> Set ratecontrol buffer size (in bits). Note <code>vpxenc</code>&#8216;s options are specified in milliseconds, the libvpx wrapper converts this value as follows: <tt>&quot;buf-sz = bufsize * 1000 / bitrate&quot;</tt>, <tt>&quot;buf-optimal-sz = bufsize * 1000 / bitrate * 5 / 6&quot;</tt>.</p>
<dt><code>rc_init_occupancy (</code><i>buf-initial-sz</i><code>)</code></p>
<dd> Set number of bits which should be loaded into the rc buffer before decoding starts. Note <code>vpxenc</code>&#8216;s option is specified in milliseconds, the libvpx wrapper converts this value as follows: <tt>&quot;rc_init_occupancy * 1000 / bitrate&quot;</tt>.</p>
<dt><code>undershoot-pct</code></p>
<dd> Set datarate undershoot (min) percentage of the target bitrate.</p>
<dt><code>overshoot-pct</code></p>
<dd> Set datarate overshoot (max) percentage of the target bitrate.</p>
<dt><code>skip_threshold (</code><i>drop-frame</i><code>)</code></p>
<dd>
<dt><code>qcomp (</code><i>bias-pct</i><code>)</code></p>
<dd>
<dt><code>maxrate (</code><i>maxsection-pct</i><code>)</code></p>
<dd> Set <font SIZE="-1">GOP</font> max bitrate in bits/s. Note <code>vpxenc</code>&#8216;s option is specified as a percentage of the target bitrate, the libvpx wrapper converts this value as follows: <tt>&quot;(maxrate * 100 / bitrate)&quot;</tt>.</p>
<dt><code>minrate (</code><i>minsection-pct</i><code>)</code></p>
<dd> Set <font SIZE="-1">GOP</font> min bitrate in bits/s. Note <code>vpxenc</code>&#8216;s option is specified as a percentage of the target bitrate, the libvpx wrapper converts this value as follows: <tt>&quot;(minrate * 100 / bitrate)&quot;</tt>.</p>
<dt><code>minrate, maxrate, b</code> <i>end-usage=cbr</i></p>
<dd> <tt>&quot;(minrate == maxrate == bitrate)&quot;</tt>.</p>
<dt><code>crf (</code><i>end-usage=cq</i><code>,</code> <i>cq-level</i><code>)</code></p>
<dd>
<dt><code>tune (</code><i>tune</i><code>)</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>psnr (</code><i>psnr</i><code>)</code></p>
<dd>
<dt><code>ssim (</code><i>ssim</i><code>)</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>quality, deadline (</code><i>deadline</i><code>)</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>best</code></p>
<dd> Use best quality deadline. Poorly named and quite slow, this option should be avoided as it may give worse quality output than good.</p>
<dt><code>good</code></p>
<dd> Use good quality deadline. This is a good trade-off between speed and quality when used with the <code>cpu-used</code> option.</p>
<dt><code>realtime</code></p>
<dd> Use realtime quality deadline.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>speed, cpu-used (</code><i>cpu-used</i><code>)</code></p>
<dd> Set quality/speed ratio modifier. Higher values speed up the encode at the cost of quality.</p>
<dt><code>nr (</code><i>noise-sensitivity</i><code>)</code></p>
<dd>
<dt><code>static-thresh</code></p>
<dd> Set a change threshold on blocks below which they will be skipped by the encoder.</p>
<dt><code>slices (</code><i>token-parts</i><code>)</code></p>
<dd> Note that FFmpeg&#8217;s <code>slices</code> option gives the total number of partitions, while <code>vpxenc</code>&#8216;s <code>token-parts</code> is given as <tt>&quot;log2(partitions)&quot;</tt>.</p>
<dt><code>max-intra-rate</code></p>
<dd> Set maximum I-frame bitrate as a percentage of the target bitrate. A value of 0 means unlimited.</p>
<dt><code>force_key_frames</code></p>
<dd> <tt>&quot;VPX_EFLAG_FORCE_KF&quot;</tt></p>
<dt><code>Alternate reference frame related</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto-alt-ref</code></p>
<dd> Enable use of alternate reference frames (2-pass only). Values greater than 1 enable multi-layer alternate reference frames (<font SIZE="-1">VP9</font> only).</p>
<dt><code>arnr-maxframes</code></p>
<dd> Set altref noise reduction max frame count.</p>
<dt><code>arnr-type</code></p>
<dd> Set altref noise reduction filter type: backward, forward, centered.</p>
<dt><code>arnr-strength</code></p>
<dd> Set altref noise reduction filter strength.</p>
<dt><code>rc-lookahead, lag-in-frames (</code><i>lag-in-frames</i><code>)</code></p>
<dd> Set number of frames to look ahead for frametype and ratecontrol.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>error-resilient</code></p>
<dd> Enable error resiliency features.</p>
<dt><code>sharpness</code> <i>integer</i></p>
<dd> Increase sharpness at the expense of lower <font SIZE="-1">PSNR.</font> The valid range is [0, 7].</p>
<dt><code>ts-parameters</code></p>
<dd> Sets the temporal scalability configuration using a :-separated list of key=value pairs. For example, to specify temporal scalability parameters with <tt>&quot;ffmpeg&quot;</tt>: </p>
<pre>
        ffmpeg -i INPUT -c:v libvpx -ts-parameters ts_number_layers=3:\
        ts_target_bitrate=250,500,1000:ts_rate_decimator=4,2,1:\
        ts_periodicity=4:ts_layer_id=0,2,1,2:ts_layering_mode=3 OUTPUT
</pre>
<p> Below is a brief explanation of each of the parameters, please refer to <tt>&quot;struct vpx_codec_enc_cfg&quot;</tt> in <tt>&quot;vpx/vpx_encoder.h&quot;</tt> for more details.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ts_number_layers</code></p>
<dd> Number of temporal coding layers.</p>
<dt><code>ts_target_bitrate</code></p>
<dd> Target bitrate for each temporal layer (in kbps). (bitrate should be inclusive of the lower temporal layer).</p>
<dt><code>ts_rate_decimator</code></p>
<dd> Frame rate decimation factor for each temporal layer.</p>
<dt><code>ts_periodicity</code></p>
<dd> Length of the sequence defining frame temporal layer membership.</p>
<dt><code>ts_layer_id</code></p>
<dd> Template defining the membership of frames to temporal layers.</p>
<dt><code>ts_layering_mode</code></p>
<dd> (optional) Selecting the temporal structure from a set of pre-defined temporal layering modes. Currently supports the following options.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> No temporal layering flags are provided internally, relies on flags being passed in using <tt>&quot;metadata&quot;</tt> field in <tt>&quot;AVFrame&quot;</tt> with following keys.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>vp8-flags</code></p>
<dd> Sets the flags passed into the encoder to indicate the referencing scheme for the current frame. Refer to function <tt>&quot;vpx_codec_encode&quot;</tt> in <tt>&quot;vpx/vpx_encoder.h&quot;</tt> for more details.</p>
<dt><code>temporal_id</code></p>
<dd> Explicitly sets the temporal id of the current frame to encode.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>2</code></p>
<dd> Two temporal layers. 0-1&#8230;</p>
<dt><code>3</code></p>
<dd> Three temporal layers. 0-2-1-2&#8230;; with single reference frame.</p>
<dt><code>4</code></p>
<dd> Same as option &#8220;3&#8221;, except there is a dependency between the two temporal layer 2 frames within the temporal period.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>VP9-specific options</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>lossless</code></p>
<dd> Enable lossless mode.</p>
<dt><code>tile-columns</code></p>
<dd> Set number of tile columns to use. Note this is given as <tt>&quot;log2(tile_columns)&quot;</tt>. For example, 8 tile columns would be requested by setting the <code>tile-columns</code> option to 3.</p>
<dt><code>tile-rows</code></p>
<dd> Set number of tile rows to use. Note this is given as <tt>&quot;log2(tile_rows)&quot;</tt>. For example, 4 tile rows would be requested by setting the <code>tile-rows</code> option to 2.</p>
<dt><code>frame-parallel</code></p>
<dd> Enable frame parallel decodability features.</p>
<dt><code>aq-mode</code></p>
<dd> Set adaptive quantization mode (0: off (default), 1: variance 2: complexity, 3: cyclic refresh, 4: equator360).</p>
<dt><code>colorspace</code> <i>color-space</i></p>
<dd> Set input color space. The <font SIZE="-1">VP9</font> bitstream supports signaling the following colorspaces:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>rgb </code>sRGB</p>
<dd>
<dt><code>bt709 </code>bt709</p>
<dd>
<dt><code>unspecified </code>unknown</p>
<dd>
<dt><code>bt470bg </code>bt601</p>
<dd>
<dt><code>smpte170m </code>smpte170</p>
<dd>
<dt><code>smpte240m </code>smpte240</p>
<dd>
<dt><code>bt2020_ncl </code>bt2020</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>row-mt</code> <i>boolean</i></p>
<dd> Enable row based multi-threading.</p>
<dt><code>tune-content</code></p>
<dd> Set content type: default (0), screen (1), film (2).</p>
<dt><code>corpus-complexity</code></p>
<dd> Corpus <font SIZE="-1">VBR</font> mode is a variant of standard <font SIZE="-1">VBR</font> where the complexity distribution midpoint is passed in rather than calculated for a specific clip or chunk. </p>
<p> The valid range is [0, 10000]. 0 (default) uses standard <font SIZE="-1">VBR.</font></p>
<dt><code>enable-tpl</code> <i>boolean</i></p>
<dd> Enable temporal dependency model.</p>
<dt><code>ref-frame-config</code></p>
<dd> Using per-frame metadata, set members of the structure <tt>&quot;vpx_svc_ref_frame_config_t&quot;</tt> in <tt>&quot;vpx/vp8cx.h&quot;</tt> to fine-control referencing schemes and frame buffer management. Use a :-separated list of key=value pairs. For example, </p>
<pre>
        av_dict_set(&amp;av_frame-&gt;metadata, &quot;ref-frame-config&quot;, \
        &quot;rfc_update_buffer_slot=7:rfc_lst_fb_idx=0:rfc_gld_fb_idx=1:rfc_alt_fb_idx=2:rfc_reference_last=0:rfc_reference_golden=0:rfc_reference_alt_ref=0&quot;);
</pre>
<dl>
<dt>
<dd>
<dl>
<dt><code>rfc_update_buffer_slot</code></p>
<dd> Indicates the buffer slot number to update</p>
<dt><code>rfc_update_last</code></p>
<dd> Indicates whether to update the <font SIZE="-1">LAST</font> frame</p>
<dt><code>rfc_update_golden</code></p>
<dd> Indicates whether to update <font SIZE="-1">GOLDEN</font> frame</p>
<dt><code>rfc_update_alt_ref</code></p>
<dd> Indicates whether to update <font SIZE="-1">ALT_REF</font> frame</p>
<dt><code>rfc_lst_fb_idx</code></p>
<dd> <font SIZE="-1">LAST</font> frame buffer index</p>
<dt><code>rfc_gld_fb_idx</code></p>
<dd> <font SIZE="-1">GOLDEN</font> frame buffer index</p>
<dt><code>rfc_alt_fb_idx</code></p>
<dd> <font SIZE="-1">ALT_REF</font> frame buffer index</p>
<dt><code>rfc_reference_last</code></p>
<dd> Indicates whether to reference <font SIZE="-1">LAST</font> frame</p>
<dt><code>rfc_reference_golden</code></p>
<dd> Indicates whether to reference <font SIZE="-1">GOLDEN</font> frame</p>
<dt><code>rfc_reference_alt_ref</code></p>
<dd> Indicates whether to reference <font SIZE="-1">ALT_REF</font> frame</p>
<dt><code>rfc_reference_duration</code></p>
<dd> Indicates frame duration</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> For more information about libvpx see: &lt;<code><a rel="nofollow" href="http://www.webmproject.org/">http://www.webmproject.org/</a></code>&gt;</p>
<h3>libwebp</h3>
<p> libwebp WebP Image encoder wrapper </p>
<p> libwebp is Google&#8217;s official encoder for WebP images. It can encode in either lossy or lossless mode. Lossy images are essentially a wrapper around a <font SIZE="-1">VP8</font> frame. Lossless images are a separate codec developed by Google. </p>
<p> <i>Pixel Format</i> </p>
<p> Currently, libwebp only supports <font SIZE="-1">YUV420</font> for lossy and <font SIZE="-1">RGB</font> for lossless due to limitations of the format and libwebp. Alpha is supported for either mode. Because of <font SIZE="-1">API</font> limitations, if <font SIZE="-1">RGB</font> is passed in when encoding lossy or <font SIZE="-1">YUV</font> is passed in for encoding lossless, the pixel format will automatically be converted using functions from libwebp. This is not ideal and is done only for convenience. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>-lossless</code> <i>boolean</i></p>
<dd> Enables/Disables use of lossless mode. Default is 0.</p>
<dt><code>-compression_level</code> <i>integer</i></p>
<dd> For lossy, this is a quality/speed tradeoff. Higher values give better quality for a given size at the cost of increased encoding time. For lossless, this is a size/speed tradeoff. Higher values give smaller size at the cost of increased encoding time. More specifically, it controls the number of extra algorithms and compression tools used, and varies the combination of these tools. This maps to the <i>method</i> option in libwebp. The valid range is 0 to 6. Default is 4.</p>
<dt><code>-qscale</code> <i>float</i></p>
<dd> For lossy encoding, this controls image quality, 0 to 100. For lossless encoding, this controls the effort and time spent at compressing more. The default value is 75. Note that for usage via libavcodec, this option is called <i>global_quality</i> and must be multiplied by <i></i><font SIZE="-1"><i>FF_QP2LAMBDA</i></font><i></i>.</p>
<dt><code>-preset</code> <i>type</i></p>
<dd> Configuration preset. This does some automatic settings based on the general type of the image.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Do not use a preset.</p>
<dt><code>default</code></p>
<dd> Use the encoder default.</p>
<dt><code>picture</code></p>
<dd> Digital picture, like portrait, inner shot</p>
<dt><code>photo</code></p>
<dd> Outdoor photograph, with natural lighting</p>
<dt><code>drawing</code></p>
<dd> Hand or line drawing, with high-contrast details</p>
<dt><code>icon</code></p>
<dd> Small-sized colorful images</p>
<dt><code>text</code></p>
<dd> Text-like</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>libx264, libx264rgb</h3>
<p> x264 H.264/MPEG-4 <font SIZE="-1">AVC</font> encoder wrapper. </p>
<p> This encoder requires the presence of the libx264 headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libx264&quot;</tt>. </p>
<p> libx264 supports an impressive number of features, including 8&#215;8 and 4&#215;4 adaptive spatial transform, adaptive B-frame placement, <font SIZE="-1">CAVLC/CABAC</font> entropy coding, interlacing (<font SIZE="-1">MBAFF</font>), lossless mode, psy optimizations for detail retention (adaptive quantization, psy-RD, psy-trellis). </p>
<p> Many libx264 encoder options are mapped to FFmpeg global codec options, while unique encoder options are provided through private options. Additionally the <code>x264opts</code> and <code>x264-params</code> private options allows one to pass a list of key=value tuples as accepted by the libx264 <tt>&quot;x264_param_parse&quot;</tt> function. </p>
<p> The x264 project website is at &lt;<code><a rel="nofollow" href="http://www.videolan.org/developers/x264.html">http://www.videolan.org/developers/x264.html</a></code>&gt;. </p>
<p> The libx264rgb encoder is the same as libx264, except it accepts packed <font SIZE="-1">RGB</font> pixel formats as input instead of <font SIZE="-1">YUV.</font> </p>
<p> <i>Supported Pixel Formats</i> </p>
<p> x264 supports 8- to 10-bit color spaces. The exact bit depth is controlled at x264&#8217;s configure time. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libx264 wrapper. The <code>x264</code>-equivalent options or values are listed in parentheses for easy migration. </p>
<p> To reduce the duplication of documentation, only the private options and some others requiring special attention are documented here. For the documentation of the undocumented generic options, see <code>the Codec Options chapter</code>. </p>
<p> To get a more accurate and extensive documentation of the libx264 options, invoke the command <code>x264 &#8211;fullhelp</code> or consult the libx264 documentation.</p>
<dl>
<dt><code>b (</code><i>bitrate</i><code>)</code></p>
<dd> Set bitrate in bits/s. Note that FFmpeg&#8217;s <code>b</code> option is expressed in bits/s, while <code>x264</code>&#8216;s <code>bitrate</code> is in kilobits/s.</p>
<dt><code>bf (</code><i>bframes</i><code>)</code></p>
<dd>
<dt><code>g (</code><i>keyint</i><code>)</code></p>
<dd>
<dt><code>qmin (</code><i>qpmin</i><code>)</code></p>
<dd> Minimum quantizer scale.</p>
<dt><code>qmax (</code><i>qpmax</i><code>)</code></p>
<dd> Maximum quantizer scale.</p>
<dt><code>qdiff (</code><i>qpstep</i><code>)</code></p>
<dd> Maximum difference between quantizer scales.</p>
<dt><code>qblur (</code><i>qblur</i><code>)</code></p>
<dd> Quantizer curve blur</p>
<dt><code>qcomp (</code><i>qcomp</i><code>)</code></p>
<dd> Quantizer curve compression factor</p>
<dt><code>refs (</code><i>ref</i><code>)</code></p>
<dd> Number of reference frames each P-frame can use. The range is from <i>0-16</i>.</p>
<dt><code>sc_threshold (</code><i>scenecut</i><code>)</code></p>
<dd> Sets the threshold for the scene change detection.</p>
<dt><code>trellis (</code><i>trellis</i><code>)</code></p>
<dd> Performs Trellis quantization to increase efficiency. Enabled by default.</p>
<dt><code>nr (</code><i>nr</i><code>)</code></p>
<dd>
<dt><code>me_range (</code><i>merange</i><code>)</code></p>
<dd> Maximum range of the motion search in pixels.</p>
<dt><code>me_method (</code><i>me</i><code>)</code></p>
<dd> Set motion estimation method. Possible values in the decreasing order of speed:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>dia (</code><i>dia</i><code>)</code></p>
<dd>
<dt><code>epzs (</code><i>dia</i><code>)</code></p>
<dd> Diamond search with radius 1 (fastest). <code>epzs</code> is an alias for <code>dia</code>.</p>
<dt><code>hex (</code><i>hex</i><code>)</code></p>
<dd> Hexagonal search with radius 2.</p>
<dt><code>umh (</code><i>umh</i><code>)</code></p>
<dd> Uneven multi-hexagon search.</p>
<dt><code>esa (</code><i>esa</i><code>)</code></p>
<dd> Exhaustive search.</p>
<dt><code>tesa (</code><i>tesa</i><code>)</code></p>
<dd> Hadamard exhaustive search (slowest).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>forced-idr</code></p>
<dd> Normally, when forcing a I-frame type, the encoder can select any type of I-frame. This option forces it to choose an IDR-frame.</p>
<dt><code>subq (</code><i>subme</i><code>)</code></p>
<dd> Sub-pixel motion estimation method.</p>
<dt><code>b_strategy (</code><i>b-adapt</i><code>)</code></p>
<dd> Adaptive B-frame placement decision algorithm. Use only on first-pass.</p>
<dt><code>keyint_min (</code><i>min-keyint</i><code>)</code></p>
<dd> Minimum <font SIZE="-1">GOP</font> size.</p>
<dt><code>coder</code></p>
<dd> Set entropy encoder. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ac</code></p>
<dd> Enable <font SIZE="-1">CABAC.</font></p>
<dt><code>vlc</code></p>
<dd> Enable <font SIZE="-1">CAVLC</font> and disable <font SIZE="-1">CABAC.</font> It generates the same effect as <code>x264</code>&#8216;s <code>&#8211;no-cabac</code> option.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>cmp</code></p>
<dd> Set full pixel motion estimation comparison algorithm. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>chroma</code></p>
<dd> Enable chroma in motion estimation.</p>
<dt><code>sad</code></p>
<dd> Ignore chroma in motion estimation. It generates the same effect as <code>x264</code>&#8216;s <code>&#8211;no-chroma-me</code> option.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>threads (</code><i>threads</i><code>)</code></p>
<dd> Number of encoding threads.</p>
<dt><code>thread_type</code></p>
<dd> Set multithreading technique. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>slice</code></p>
<dd> Slice-based multithreading. It generates the same effect as <code>x264</code>&#8216;s <code>&#8211;sliced-threads</code> option.</p>
<dt><code>frame</code></p>
<dd> Frame-based multithreading.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>flags</code></p>
<dd> Set encoding flags. It can be used to disable closed <font SIZE="-1">GOP</font> and enable open <font SIZE="-1">GOP</font> by setting it to <tt>&quot;-cgop&quot;</tt>. The result is similar to the behavior of <code>x264</code>&#8216;s <code>&#8211;open-gop</code> option.</p>
<dt><code>rc_init_occupancy (</code><i>vbv-init</i><code>)</code></p>
<dd>
<dt><code>preset (</code><i>preset</i><code>)</code></p>
<dd> Set the encoding preset.</p>
<dt><code>tune (</code><i>tune</i><code>)</code></p>
<dd> Set tuning of the encoding params.</p>
<dt><code>profile (</code><i>profile</i><code>)</code></p>
<dd> Set profile restrictions.</p>
<dt><code>fastfirstpass</code></p>
<dd> Enable fast settings when encoding first pass, when set to 1. When set to 0, it has the same effect of <code>x264</code>&#8216;s <code>&#8211;slow-firstpass</code> option.</p>
<dt><code>crf (</code><i>crf</i><code>)</code></p>
<dd> Set the quality for constant quality mode.</p>
<dt><code>crf_max (</code><i>crf-max</i><code>)</code></p>
<dd> In <font SIZE="-1">CRF</font> mode, prevents <font SIZE="-1">VBV</font> from lowering quality beyond this point.</p>
<dt><code>qp (</code><i>qp</i><code>)</code></p>
<dd> Set constant quantization rate control method parameter.</p>
<dt><code>aq-mode (</code><i>aq-mode</i><code>)</code></p>
<dd> Set <font SIZE="-1">AQ</font> method. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (</code><i>0</i><code>)</code></p>
<dd> Disabled.</p>
<dt><code>variance (</code><i>1</i><code>)</code></p>
<dd> Variance <font SIZE="-1">AQ</font> (complexity mask).</p>
<dt><code>autovariance (</code><i>2</i><code>)</code></p>
<dd> Auto-variance <font SIZE="-1">AQ</font> (experimental).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>aq-strength (</code><i>aq-strength</i><code>)</code></p>
<dd> Set <font SIZE="-1">AQ</font> strength, reduce blocking and blurring in flat and textured areas.</p>
<dt><code>psy</code></p>
<dd> Use psychovisual optimizations when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-psy</code> option.</p>
<dt><code>psy-rd (</code><i>psy-rd</i><code>)</code></p>
<dd> Set strength of psychovisual optimization, in <i>psy-rd</i>:<i>psy-trellis</i> format.</p>
<dt><code>rc-lookahead (</code><i>rc-lookahead</i><code>)</code></p>
<dd> Set number of frames to look ahead for frametype and ratecontrol.</p>
<dt><code>weightb</code></p>
<dd> Enable weighted prediction for B-frames when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-weightb</code> option.</p>
<dt><code>weightp (</code><i>weightp</i><code>)</code></p>
<dd> Set weighted prediction method for P-frames. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (</code><i>0</i><code>)</code></p>
<dd> Disabled</p>
<dt><code>simple (</code><i>1</i><code>)</code></p>
<dd> Enable only weighted refs</p>
<dt><code>smart (</code><i>2</i><code>)</code></p>
<dd> Enable both weighted refs and duplicates</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>ssim (</code><i>ssim</i><code>)</code></p>
<dd> Enable calculation and printing <font SIZE="-1">SSIM</font> stats after the encoding.</p>
<dt><code>intra-refresh (</code><i>intra-refresh</i><code>)</code></p>
<dd> Enable the use of Periodic Intra Refresh instead of <font SIZE="-1">IDR</font> frames when set to 1.</p>
<dt><code>avcintra-class (</code><i>class</i><code>)</code></p>
<dd> Configure the encoder to generate AVC-Intra. Valid values are 50,100 and 200</p>
<dt><code>bluray-compat (</code><i>bluray-compat</i><code>)</code></p>
<dd> Configure the encoder to be compatible with the bluray standard. It is a shorthand for setting &#8220;bluray-compat=1 force-cfr=1&#8221;.</p>
<dt><code>b-bias (</code><i>b-bias</i><code>)</code></p>
<dd> Set the influence on how often B-frames are used.</p>
<dt><code>b-pyramid (</code><i>b-pyramid</i><code>)</code></p>
<dd> Set method for keeping of some B-frames as references. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (</code><i>none</i><code>)</code></p>
<dd> Disabled.</p>
<dt><code>strict (</code><i>strict</i><code>)</code></p>
<dd> Strictly hierarchical pyramid.</p>
<dt><code>normal (</code><i>normal</i><code>)</code></p>
<dd> Non-strict (not Blu-ray compatible).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mixed-refs</code></p>
<dd> Enable the use of one reference per partition, as opposed to one reference per macroblock when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-mixed-refs</code> option.</p>
<dt><code>8x8dct</code></p>
<dd> Enable adaptive spatial transform (high profile 8&#215;8 transform) when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-8x8dct</code> option.</p>
<dt><code>fast-pskip</code></p>
<dd> Enable early <font SIZE="-1">SKIP</font> detection on P-frames when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-fast-pskip</code> option.</p>
<dt><code>aud (</code><i>aud</i><code>)</code></p>
<dd> Enable use of access unit delimiters when set to 1.</p>
<dt><code>mbtree</code></p>
<dd> Enable use macroblock tree ratecontrol when set to 1. When set to 0, it has the same effect as <code>x264</code>&#8216;s <code>&#8211;no-mbtree</code> option.</p>
<dt><code>deblock (</code><i>deblock</i><code>)</code></p>
<dd> Set loop filter parameters, in <i>alpha</i>:<i>beta</i> form.</p>
<dt><code>cplxblur (</code><i>cplxblur</i><code>)</code></p>
<dd> Set fluctuations reduction in <font SIZE="-1">QP</font> (before curve compression).</p>
<dt><code>partitions (</code><i>partitions</i><code>)</code></p>
<dd> Set partitions to consider as a comma-separated list of. Possible values in the list:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>p8x8</code></p>
<dd> 8&#215;8 P-frame partition.</p>
<dt><code>p4x4</code></p>
<dd> 4&#215;4 P-frame partition.</p>
<dt><code>b8x8</code></p>
<dd> 4&#215;4 B-frame partition.</p>
<dt><code>i8x8</code></p>
<dd> 8&#215;8 I-frame partition.</p>
<dt><code>i4x4</code></p>
<dd> 4&#215;4 I-frame partition. (Enabling <code>p4x4</code> requires <code>p8x8</code> to be enabled. Enabling <code>i8x8</code> requires adaptive spatial transform (<code>8x8dct</code> option) to be enabled.)</p>
<dt><code>none (</code><i>none</i><code>)</code></p>
<dd> Do not consider any partitions.</p>
<dt><code>all (</code><i>all</i><code>)</code></p>
<dd> Consider every partition.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>direct-pred (</code><i>direct</i><code>)</code></p>
<dd> Set direct <font SIZE="-1">MV</font> prediction mode. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (</code><i>none</i><code>)</code></p>
<dd> Disable <font SIZE="-1">MV</font> prediction.</p>
<dt><code>spatial (</code><i>spatial</i><code>)</code></p>
<dd> Enable spatial predicting.</p>
<dt><code>temporal (</code><i>temporal</i><code>)</code></p>
<dd> Enable temporal predicting.</p>
<dt><code>auto (</code><i>auto</i><code>)</code></p>
<dd> Automatically decided.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>slice-max-size (</code><i>slice-max-size</i><code>)</code></p>
<dd> Set the limit of the size of each slice in bytes. If not specified but <font SIZE="-1">RTP</font> payload size (<code>ps</code>) is specified, that is used.</p>
<dt><code>stats (</code><i>stats</i><code>)</code></p>
<dd> Set the file name for multi-pass stats.</p>
<dt><code>nal-hrd (</code><i>nal-hrd</i><code>)</code></p>
<dd> Set signal <font SIZE="-1">HRD</font> information (requires <code>vbv-bufsize</code> to be set). Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (</code><i>none</i><code>)</code></p>
<dd> Disable <font SIZE="-1">HRD</font> information signaling.</p>
<dt><code>vbr (</code><i>vbr</i><code>)</code></p>
<dd> Variable bit rate.</p>
<dt><code>cbr (</code><i>cbr</i><code>)</code></p>
<dd> Constant bit rate (not allowed in <font SIZE="-1">MP4</font> container).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>x264opts (N.A.)</code></p>
<dd> Set any x264 option, see <code>x264 &#8211;fullhelp</code> for a list. </p>
<p> Argument is a list of <i>key</i>=<i>value</i> couples separated by &#8220;:&#8221;. In <i>filter</i> and <i>psy-rd</i> options that use &#8220;:&#8221; as a separator themselves, use &#8220;,&#8221; instead. They accept it as well since long ago but this is kept undocumented for some reason. </p>
<p> For example to specify libx264 encoding options with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i foo.mpg -c:v libx264 -x264opts keyint=123:min-keyint=20 -an out.mkv
</pre>
<dt><code>a53cc</code> <i>boolean</i></p>
<dd> Import closed captions (which must be <font SIZE="-1">ATSC</font> compatible format) into output. Only the mpeg2 and h264 decoders provide these. Default is 1 (on).</p>
<dt><code>x264-params (N.A.)</code></p>
<dd> Override the x264 configuration using a :-separated list of key=value parameters. </p>
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
<dt><code>b</code></p>
<dd> Sets target video bitrate.</p>
<dt><code>bf</code></p>
<dd>
<dt><code>g</code></p>
<dd> Set the <font SIZE="-1">GOP</font> size.</p>
<dt><code>keyint_min</code></p>
<dd> Minimum <font SIZE="-1">GOP</font> size.</p>
<dt><code>refs</code></p>
<dd> Number of reference frames each P-frame can use. The range is from <i>1-16</i>.</p>
<dt><code>preset</code></p>
<dd> Set the x265 preset.</p>
<dt><code>tune</code></p>
<dd> Set the x265 tune parameter.</p>
<dt><code>profile</code></p>
<dd> Set profile restrictions.</p>
<dt><code>crf</code></p>
<dd> Set the quality for constant quality mode.</p>
<dt><code>qp</code></p>
<dd> Set constant quantization rate control method parameter.</p>
<dt><code>qmin</code></p>
<dd> Minimum quantizer scale.</p>
<dt><code>qmax</code></p>
<dd> Maximum quantizer scale.</p>
<dt><code>qdiff</code></p>
<dd> Maximum difference between quantizer scales.</p>
<dt><code>qblur</code></p>
<dd> Quantizer curve blur</p>
<dt><code>qcomp</code></p>
<dd> Quantizer curve compression factor</p>
<dt><code>i_qfactor</code></p>
<dd>
<dt><code>b_qfactor</code></p>
<dd>
<dt><code>forced-idr</code></p>
<dd> Normally, when forcing a I-frame type, the encoder can select any type of I-frame. This option forces it to choose an IDR-frame.</p>
<dt><code>x265-params</code></p>
<dd> Set x265 options using a list of <i>key</i>=<i>value</i> couples separated by &#8220;:&#8221;. See <code>x265 &#8211;help</code> for a list of options. </p>
<p> For example to specify libx265 encoding options with <code>-x265-params</code>: </p>
<pre>
        ffmpeg -i input -c:v libx265 -x265-params crf=26:psy-rd=1 output.mp4
</pre>
</dl>
<h3>libxavs2</h3>
<p> xavs2 <font SIZE="-1">AVS2-P2/IEEE1857.4</font> encoder wrapper. </p>
<p> This encoder requires the presence of the libxavs2 headers and library during configuration. You need to explicitly configure the build with <code>&#8211;enable-libxavs2</code>. </p>
<p> The following standard libavcodec options are used:</p>
<dl>
<dt>&bull;</p>
<dd> <code>b</code> / <code>bit_rate</code></p>
<dt>&bull;</p>
<dd> <code>g</code> / <code>gop_size</code></p>
<dt>&bull;</p>
<dd> <code>bf</code> / <code>max_b_frames</code></dl>
<p> The encoder also has its own specific options: </p>
<p> <i>Options</i></p>
<dl>
<dt><code>lcu_row_threads</code></p>
<dd> Set the number of parallel threads for rows from 1 to 8 (default 5).</p>
<dt><code>initial_qp</code></p>
<dd> Set the xavs2 quantization parameter from 1 to 63 (default 34). This is used to set the initial qp for the first frame.</p>
<dt><code>qp</code></p>
<dd> Set the xavs2 quantization parameter from 1 to 63 (default 34). This is used to set the qp value under constant-QP mode.</p>
<dt><code>max_qp</code></p>
<dd> Set the max qp for rate control from 1 to 63 (default 55).</p>
<dt><code>min_qp</code></p>
<dd> Set the min qp for rate control from 1 to 63 (default 20).</p>
<dt><code>speed_level</code></p>
<dd> Set the Speed level from 0 to 9 (default 0). Higher is better but slower.</p>
<dt><code>log_level</code></p>
<dd> Set the log level from -1 to 3 (default 0). -1: none, 0: error, 1: warning, 2: info, 3: debug.</p>
<dt><code>xavs2-params</code></p>
<dd> Set xavs2 options using a list of <i>key</i>=<i>value</i> couples separated by &#8220;:&#8221;. </p>
<p> For example to specify libxavs2 encoding options with <code>-xavs2-params</code>: </p>
<pre>
        ffmpeg -i input -c:v libxavs2 -xavs2-params RdoqLevel=0 output.avs2
</pre>
</dl>
<h3>libxvid</h3>
<p> Xvid <font SIZE="-1">MPEG-4</font> Part 2 encoder wrapper. </p>
<p> This encoder requires the presence of the libxvidcore headers and library during configuration. You need to explicitly configure the build with <tt>&quot;--enable-libxvid --enable-gpl&quot;</tt>. </p>
<p> The native <tt>&quot;mpeg4&quot;</tt> encoder supports the <font SIZE="-1">MPEG-4</font> Part 2 format, so users can encode to this format without this library. </p>
<p> <i>Options</i> </p>
<p> The following options are supported by the libxvid wrapper. Some of the following options are listed but are not documented, and correspond to shared codec options. See <code>the Codec Options chapter</code> for their documentation. The other shared options which are not listed have no effect for the libxvid encoder.</p>
<dl>
<dt><code>b</code></p>
<dd>
<dt><code>g</code></p>
<dd>
<dt><code>qmin</code></p>
<dd>
<dt><code>qmax</code></p>
<dd>
<dt><code>mpeg_quant</code></p>
<dd>
<dt><code>threads</code></p>
<dd>
<dt><code>bf</code></p>
<dd>
<dt><code>b_qfactor</code></p>
<dd>
<dt><code>b_qoffset</code></p>
<dd>
<dt><code>flags</code></p>
<dd> Set specific encoding flags. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mv4</code></p>
<dd> Use four motion vector by macroblock.</p>
<dt><code>aic</code></p>
<dd> Enable high quality <font SIZE="-1">AC</font> prediction.</p>
<dt><code>gray</code></p>
<dd> Only encode grayscale.</p>
<dt><code>gmc</code></p>
<dd> Enable the use of global motion compensation (<font SIZE="-1">GMC</font>).</p>
<dt><code>qpel</code></p>
<dd> Enable quarter-pixel motion compensation.</p>
<dt><code>cgop</code></p>
<dd> Enable closed <font SIZE="-1">GOP.</font></p>
<dt><code>global_header</code></p>
<dd> Place global headers in extradata instead of every keyframe.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>trellis</code></p>
<dd>
<dt><code>me_method</code></p>
<dd> Set motion estimation method. Possible values in decreasing order of speed and increasing order of quality:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>zero</code></p>
<dd> Use no motion estimation (default).</p>
<dt><code>phods</code></p>
<dd>
<dt><code>x1</code></p>
<dd>
<dt><code>log</code></p>
<dd> Enable advanced diamond zonal search for 16&#215;16 blocks and half-pixel refinement for 16&#215;16 blocks. <code>x1</code> and <code>log</code> are aliases for <code>phods</code>.</p>
<dt><code>epzs</code></p>
<dd> Enable all of the things described above, plus advanced diamond zonal search for 8&#215;8 blocks, half-pixel refinement for 8&#215;8 blocks, and motion estimation on chroma planes.</p>
<dt><code>full</code></p>
<dd> Enable all of the things described above, plus extended 16&#215;16 and 8&#215;8 blocks search.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mbd</code></p>
<dd> Set macroblock decision algorithm. Possible values in the increasing order of quality:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>simple</code></p>
<dd> Use macroblock comparing function algorithm (default).</p>
<dt><code>bits</code></p>
<dd> Enable rate distortion-based half pixel and quarter pixel refinement for 16&#215;16 blocks.</p>
<dt><code>rd</code></p>
<dd> Enable all of the things described above, plus rate distortion-based half pixel and quarter pixel refinement for 8&#215;8 blocks, and rate distortion-based search using square pattern.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>lumi_aq</code></p>
<dd> Enable lumi masking adaptive quantization when set to 1. Default is 0 (disabled).</p>
<dt><code>variance_aq</code></p>
<dd> Enable variance adaptive quantization when set to 1. Default is 0 (disabled). </p>
<p> When combined with <code>lumi_aq</code>, the resulting quality will not be better than any of the two specified individually. In other words, the resulting quality will be the worse one of the two effects.</p>
<dt><code>ssim</code></p>
<dd> Set structural similarity (<font SIZE="-1">SSIM</font>) displaying method. Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>off</code></p>
<dd> Disable displaying of <font SIZE="-1">SSIM</font> information.</p>
<dt><code>avg</code></p>
<dd> Output average <font SIZE="-1">SSIM</font> at the end of encoding to stdout. The format of showing the average <font SIZE="-1">SSIM</font> is: </p>
<pre>
        Average SSIM: %f
</pre>
<p> For users who are not familiar with C, <tt>%f</tt> means a float number, or a decimal (e.g. 0.939232).</p>
<dt><code>frame</code></p>
<dd> Output both per-frame <font SIZE="-1">SSIM</font> data during encoding and average <font SIZE="-1">SSIM</font> at the end of encoding to stdout. The format of per-frame information is: </p>
<pre>
               SSIM: avg: %1.3f min: %1.3f max: %1.3f
</pre>
<p> For users who are not familiar with C, <tt>%1</tt>.3f means a float number rounded to 3 digits after the dot (e.g. 0.932).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>ssim_acc</code></p>
<dd> Set <font SIZE="-1">SSIM</font> accuracy. Valid options are integers within the range of 0-4, while 0 gives the most accurate result and 4 computes the fastest.</dl>
<h3>MediaFoundation</h3>
<p> This provides wrappers to encoders (both audio and video) in the MediaFoundation framework. It can access both <font SIZE="-1">SW</font> and <font SIZE="-1">HW</font> encoders. Video encoders can take input in either of nv12 or yuv420p form (some encoders support both, some support only either &#8211; in practice, nv12 is the safer choice, especially among <font SIZE="-1">HW</font> encoders).</p>
<h3>mpeg2</h3>
<p> <font SIZE="-1">MPEG-2</font> video encoder. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>profile</code></p>
<dd> Select the mpeg2 profile to encode:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>422</code></p>
<dd>
<dt><code>high</code></p>
<dd>
<dt><code>ss</code></p>
<dd> Spatially Scalable</p>
<dt><code>snr</code></p>
<dd> <font SIZE="-1">SNR</font> Scalable</p>
<dt><code>main</code></p>
<dd>
<dt><code>simple</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>level</code></p>
<dd> Select the mpeg2 level to encode:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>high</code></p>
<dd>
<dt><code>high1440</code></p>
<dd>
<dt><code>main</code></p>
<dd>
<dt><code>low</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>seq_disp_ext</code> <i>integer</i></p>
<dd> Specifies if the encoder should write a sequence_display_extension to the output.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd>
<dt><code>auto</code></p>
<dd> Decide automatically to write it or not (this is the default) by checking if the data to be written is different from the default or unspecified values.</p>
<dt><code>0</code></p>
<dd>
<dt><code>never</code></p>
<dd> Never write it.</p>
<dt><code>1</code></p>
<dd>
<dt><code>always</code></p>
<dd> Always write it.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>video_format</code> <i>integer</i></p>
<dd> Specifies the video_format written into the sequence display extension indicating the source of the video pictures. The default is <code>unspecified</code>, can be <code>component</code>, <code>pal</code>, <code>ntsc</code>, <code>secam</code> or <code>mac</code>. For maximum compatibility, use <code>component</code>.</p>
<dt><code>a53cc</code> <i>boolean</i></p>
<dd> Import closed captions (which must be <font SIZE="-1">ATSC</font> compatible format) into output. Default is 1 (on).</dl>
<h3>png</h3>
<p> <font SIZE="-1">PNG</font> image encoder. </p>
<p> <i>Private options</i></p>
<dl>
<dt><code>dpi</code> <i>integer</i></p>
<dd> Set physical density of pixels, in dots per inch, unset by default</p>
<dt><code>dpm</code> <i>integer</i></p>
<dd> Set physical density of pixels, in dots per meter, unset by default</dl>
<h3>ProRes</h3>
<p> Apple ProRes encoder. </p>
<p> FFmpeg contains 2 ProRes encoders, the prores-aw and prores-ks encoder. The used encoder can be chosen with the <tt>&quot;-vcodec&quot;</tt> option. </p>
<p> <i>Private Options for prores-ks</i></p>
<dl>
<dt><code>profile</code> <i>integer</i></p>
<dd> Select the ProRes profile to encode</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>proxy</code></p>
<dd>
<dt><code>lt</code></p>
<dd>
<dt><code>standard</code></p>
<dd>
<dt><code>hq</code></p>
<dd>
<dt><code>4444</code></p>
<dd>
<dt><code>4444xq</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>quant_mat</code> <i>integer</i></p>
<dd> Select quantization matrix.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd>
<dt><code>default</code></p>
<dd>
<dt><code>proxy</code></p>
<dd>
<dt><code>lt</code></p>
<dd>
<dt><code>standard</code></p>
<dd>
<dt><code>hq</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> If set to <i>auto</i>, the matrix matching the profile will be picked. If not set, the matrix providing the highest quality, <i>default</i>, will be picked.</dl>
<dt><code>bits_per_mb</code> <i>integer</i></p>
<dd> How many bits to allot for coding one macroblock. Different profiles use between 200 and 2400 bits per macroblock, the maximum is 8000.</p>
<dt><code>mbs_per_slice</code> <i>integer</i></p>
<dd> Number of macroblocks in each slice (1-8); the default value (8) should be good in almost all situations.</p>
<dt><code>vendor</code> <i>string</i></p>
<dd> Override the 4-byte vendor <font SIZE="-1">ID. A</font> custom vendor <font SIZE="-1">ID</font> like <i>apl0</i> would claim the stream was produced by the Apple encoder.</p>
<dt><code>alpha_bits</code> <i>integer</i></p>
<dd> Specify number of bits for alpha component. Possible values are <i>0</i>, <i>8</i> and <i>16</i>. Use <i>0</i> to disable alpha plane coding.</dl>
<p> <i>Speed considerations</i> </p>
<p> In the default mode of operation the encoder has to honor frame constraints (i.e. not produce frames with size bigger than requested) while still making output picture as good as possible. A frame containing a lot of small details is harder to compress and the encoder would spend more time searching for appropriate quantizers for each slice. </p>
<p> Setting a higher <code>bits_per_mb</code> limit will improve the speed. </p>
<p> For the fastest encoding speed set the <code>qscale</code> parameter (4 is the recommended value) and do not set a size constraint.</p>
<h3><font SIZE="-1">QSV</font> encoders</h3>
<p> The family of Intel QuickSync Video encoders (<font SIZE="-1">MPEG-2, H.264, HEVC, JPEG/MJPEG</font> and <font SIZE="-1">VP9</font>) </p>
<p> The ratecontrol method is selected as follows:</p>
<dl>
<dt>&bull;</p>
<dd> When <code>global_quality</code> is specified, a quality-based mode is used. Specifically this means either</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>CQP</i></font><i></i> &#8211; constant quantizer scale, when the <code>qscale</code> codec flag is also set (the <code>-qscale</code> ffmpeg option).</p>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>LA_ICQ</i></font><i></i> &#8211; intelligent constant quality with lookahead, when the <code>look_ahead</code> option is also set.</p>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>ICQ</i></font><i></i> &#8212; intelligent constant quality otherwise.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> Otherwise, a bitrate-based mode is used. For all of those, you should specify at least the desired average bitrate with the <code>b</code> option.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>LA</i></font><i></i> &#8211; <font SIZE="-1">VBR</font> with lookahead, when the <code>look_ahead</code> option is specified.</p>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>VCM</i></font><i></i> &#8211; video conferencing mode, when the <code>vcm</code> option is set.</p>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>CBR</i></font><i></i> &#8211; constant bitrate, when <code>maxrate</code> is specified and equal to the average bitrate.</p>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>VBR</i></font><i></i> &#8211; variable bitrate, when <code>maxrate</code> is specified, but is higher than the average bitrate.</p>
<dt>&#8211;</p>
<dd> <i></i><font SIZE="-1"><i>AVBR</i></font><i></i> &#8211; average <font SIZE="-1">VBR</font> mode, when <code>maxrate</code> is not specified. This mode is further configured by the <code>avbr_accuracy</code> and <code>avbr_convergence</code> options.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Note that depending on your system, a different mode than the one you specified may be selected by the encoder. Set the verbosity level to <i>verbose</i> or higher to see the actual settings used by the <font SIZE="-1">QSV</font> runtime. </p>
<p> Additional libavcodec global options are mapped to <font SIZE="-1">MSDK</font> options as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <code>g/gop_size</code> -&gt; <code>GopPicSize</code></p>
<dt>&bull;</p>
<dd> <code>bf/max_b_frames</code>+1 -&gt; <code>GopRefDist</code></p>
<dt>&bull;</p>
<dd> <code>rc_init_occupancy/rc_initial_buffer_occupancy</code> -&gt; <code>InitialDelayInKB</code></p>
<dt>&bull;</p>
<dd> <code>slices</code> -&gt; <code>NumSlice</code></p>
<dt>&bull;</p>
<dd> <code>refs</code> -&gt; <code>NumRefFrame</code></p>
<dt>&bull;</p>
<dd> <code>b_strategy/b_frame_strategy</code> -&gt; <code>BRefType</code></p>
<dt>&bull;</p>
<dd> <code>cgop/CLOSED_GOP</code> codec flag -&gt; <code>GopOptFlag</code></p>
<dt>&bull;</p>
<dd> For the <i></i><font SIZE="-1"><i>CQP</i></font><i></i> mode, the <code>i_qfactor/i_qoffset</code> and <code>b_qfactor/b_qoffset</code> set the difference between <i></i><font SIZE="-1"><i>QPP</i></font><i></i> and <i></i><font SIZE="-1"><i>QPI</i></font><i></i>, and <i></i><font SIZE="-1"><i>QPP</i></font><i></i> and <i></i><font SIZE="-1"><i>QPB</i></font><i></i> respectively.</p>
<dt>&bull;</p>
<dd> Setting the <code>coder</code> option to the value <i>vlc</i> will make the H.264 encoder use <font SIZE="-1">CAVLC</font> instead of <font SIZE="-1">CABAC.</font></dl>
<h3>snow</h3>
<p> <i>Options</i></p>
<dl>
<dt><code>iterative_dia_size</code></p>
<dd> dia size for the iterative motion estimation</dl>
<h3><font SIZE="-1">VAAPI</font> encoders</h3>
<p> Wrappers for hardware encoders accessible via <font SIZE="-1">VAAPI.</font> </p>
<p> These encoders only accept input in <font SIZE="-1">VAAPI</font> hardware surfaces. If you have input in software frames, use the <code>hwupload</code> filter to upload them to the <font SIZE="-1">GPU.</font> </p>
<p> The following standard libavcodec options are used:</p>
<dl>
<dt>&bull;</p>
<dd> <code>g</code> / <code>gop_size</code></p>
<dt>&bull;</p>
<dd> <code>bf</code> / <code>max_b_frames</code></p>
<dt>&bull;</p>
<dd> <code>profile</code> </p>
<p> If not set, this will be determined automatically from the format of the input frames and the profiles supported by the driver.</p>
<dt>&bull;</p>
<dd> <code>level</code></p>
<dt>&bull;</p>
<dd> <code>b</code> / <code>bit_rate</code></p>
<dt>&bull;</p>
<dd> <code>maxrate</code> / <code>rc_max_rate</code></p>
<dt>&bull;</p>
<dd> <code>bufsize</code> / <code>rc_buffer_size</code></p>
<dt>&bull;</p>
<dd> <code>rc_init_occupancy</code> / <code>rc_initial_buffer_occupancy</code></p>
<dt>&bull;</p>
<dd> <code>compression_level</code> </p>
<p> Speed / quality tradeoff: higher values are faster / worse quality.</p>
<dt>&bull;</p>
<dd> <code>q</code> / <code>global_quality</code> </p>
<p> Size / quality tradeoff: higher values are smaller / worse quality.</p>
<dt>&bull;</p>
<dd> <code>qmin</code></p>
<dt>&bull;</p>
<dd> <code>qmax</code></p>
<dt>&bull;</p>
<dd> <code>i_qfactor</code> / <code>i_quant_factor</code></p>
<dt>&bull;</p>
<dd> <code>i_qoffset</code> / <code>i_quant_offset</code></p>
<dt>&bull;</p>
<dd> <code>b_qfactor</code> / <code>b_quant_factor</code></p>
<dt>&bull;</p>
<dd> <code>b_qoffset</code> / <code>b_quant_offset</code></p>
<dt>&bull;</p>
<dd> <code>slices</code></dl>
<p> All encoders support the following options:</p>
<dl>
<dt><code>low_power</code></p>
<dd> Some drivers/platforms offer a second encoder for some codecs intended to use less power than the default encoder; setting this option will attempt to use that encoder. Note that it may support a reduced feature set, so some other options may not be available in this mode.</p>
<dt><code>idr_interval</code></p>
<dd> Set the number of normal intra frames between full-refresh (<font SIZE="-1">IDR</font>) frames in open-GOP mode. The intra frames are still IRAPs, but will not include global headers and may have non-decodable leading pictures.</p>
<dt><code>b_depth</code></p>
<dd> Set the B-frame reference depth. When set to one (the default), all B-frames will refer only to P- or I-frames. When set to greater values multiple layers of B-frames will be present, frames in each layer only referring to frames in higher layers.</p>
<dt><code>rc_mode</code></p>
<dd> Set the rate control mode to use. A given driver may only support a subset of modes. </p>
<p> Possible modes:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> Choose the mode automatically based on driver support and the other options. This is the default.</p>
<dt><font SIZE="-1"><code>CQP</code></font></p>
<dd> Constant-quality.</p>
<dt><font SIZE="-1"><code>CBR</code></font></p>
<dd> Constant-bitrate.</p>
<dt><font SIZE="-1"><code>VBR</code></font></p>
<dd> Variable-bitrate.</p>
<dt><font SIZE="-1"><code>ICQ</code></font></p>
<dd> Intelligent constant-quality.</p>
<dt><font SIZE="-1"><code>QVBR</code></font></p>
<dd> Quality-defined variable-bitrate.</p>
<dt><font SIZE="-1"><code>AVBR</code></font></p>
<dd> Average variable bitrate.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Each encoder also has its own specific options:</p>
<dl>
<dt><code>h264_vaapi</code></p>
<dd> <code>profile</code> sets the value of <i>profile_idc</i> and the <i>constraint_set*_flag</i>s. <code>level</code> sets the value of <i>level_idc</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>coder</code></p>
<dd> Set entropy encoder (default is <i>cabac</i>). Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ac</code></p>
<dd>
<dt><code>cabac</code></p>
<dd> Use <font SIZE="-1">CABAC.</font></p>
<dt><code>vlc</code></p>
<dd>
<dt><code>cavlc</code></p>
<dd> Use <font SIZE="-1">CAVLC.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>aud</code></p>
<dd> Include access unit delimiters in the stream (not included by default).</p>
<dt><code>sei</code></p>
<dd> Set <font SIZE="-1">SEI</font> message types to include. Some combination of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>identifier</code></p>
<dd> Include a <i>user_data_unregistered</i> message containing information about the encoder.</p>
<dt><code>timing</code></p>
<dd> Include picture timing parameters (<i>buffering_period</i> and <i>pic_timing</i> messages).</p>
<dt><code>recovery_point</code></p>
<dd> Include recovery points where appropriate (<i>recovery_point</i> messages).</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>hevc_vaapi</code></p>
<dd> <code>profile</code> and <code>level</code> set the values of <i>general_profile_idc</i> and <i>general_level_idc</i> respectively.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>aud</code></p>
<dd> Include access unit delimiters in the stream (not included by default).</p>
<dt><code>tier</code></p>
<dd> Set <i>general_tier_flag</i>. This may affect the level chosen for the stream if it is not explicitly specified.</p>
<dt><code>sei</code></p>
<dd> Set <font SIZE="-1">SEI</font> message types to include. Some combination of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>hdr</code></p>
<dd> Include <font SIZE="-1">HDR</font> metadata if the input frames have it (<i>mastering_display_colour_volume</i> and <i>content_light_level</i> messages).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>tiles</code></p>
<dd> Set the number of tiles to encode the input video with, as columns x rows. Larger numbers allow greater parallelism in both encoding and decoding, but may decrease coding efficiency.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mjpeg_vaapi</code></p>
<dd> Only baseline <font SIZE="-1">DCT</font> encoding is supported. The encoder always uses the standard quantisation and huffman tables &#8211; <code>global_quality</code> scales the standard quantisation table (range 1-100). </p>
<p> For <font SIZE="-1">YUV, 4:2:0, 4:2:2</font> and 4:4:4 subsampling modes are supported. <font SIZE="-1">RGB</font> is also supported, and will create an <font SIZE="-1">RGB JPEG.</font></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>jfif</code></p>
<dd> Include <font SIZE="-1">JFIF</font> header in each frame (not included by default).</p>
<dt><code>huffman</code></p>
<dd> Include standard huffman tables (on by default). Turning this off will save a few hundred bytes in each output frame, but may lose compatibility with some <font SIZE="-1">JPEG</font> decoders which don&#8217;t fully handle <font SIZE="-1">MJPEG.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mpeg2_vaapi</code></p>
<dd> <code>profile</code> and <code>level</code> set the value of <i>profile_and_level_indication</i>.</p>
<dt><code>vp8_vaapi</code></p>
<dd> B-frames are not supported. </p>
<p> <code>global_quality</code> sets the <i>q_idx</i> used for non-key frames (range 0-127).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>loop_filter_level</code></p>
<dd>
<dt><code>loop_filter_sharpness</code></p>
<dd> Manually set the loop filter parameters.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>vp9_vaapi</code></p>
<dd> <code>global_quality</code> sets the <i>q_idx</i> used for P-frames (range 0-255).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>loop_filter_level</code></p>
<dd>
<dt><code>loop_filter_sharpness</code></p>
<dd> Manually set the loop filter parameters.</dl>
</dl>
<dl>
<dt>
<dd>
<p> B-frames are supported, but the output stream is always in encode order rather than display order. If B-frames are enabled, it may be necessary to use the <code>vp9_raw_reorder</code> bitstream filter to modify the output stream to display frames in the correct order. </p>
<p> Only normal frames are produced &#8211; the <code>vp9_superframe</code> bitstream filter may be required to produce a stream usable with all decoders.</dl>
</dl>
<h3>vc2</h3>
<p> <font SIZE="-1">SMPTE VC-2</font> (previously <font SIZE="-1">BBC</font> Dirac Pro). This codec was primarily aimed at professional broadcasting but since it supports yuv420, yuv422 and yuv444 at 8 (limited range or full range), 10 or 12 bits, this makes it suitable for other tasks which require low overhead and low compression (like screen recording). </p>
<p> <i>Options</i></p>
<dl>
<dt><code>b</code></p>
<dd> Sets target video bitrate. Usually that&#8217;s around 1:6 of the uncompressed video bitrate (e.g. for 1920&#215;1080 50fps yuv422p10 that&#8217;s around 400Mbps). Higher values (close to the uncompressed bitrate) turn on lossless compression mode.</p>
<dt><code>field_order</code></p>
<dd> Enables field coding when set (e.g. to tt &#8211; top field first) for interlaced inputs. Should increase compression with interlaced content as it splits the fields and encodes each separately.</p>
<dt><code>wavelet_depth</code></p>
<dd> Sets the total amount of wavelet transforms to apply, between 1 and 5 (default). Lower values reduce compression and quality. Less capable decoders may not be able to handle values of <code>wavelet_depth</code> over 3.</p>
<dt><code>wavelet_type</code></p>
<dd> Sets the transform type. Currently only <i>5_3</i> (LeGall) and <i>9_7</i> (Deslauriers-Dubuc) are implemented, with 9_7 being the one with better compression and thus is the default.</p>
<dt><code>slice_width</code></p>
<dd>
<dt><code>slice_height</code></p>
<dd> Sets the slice size for each slice. Larger values result in better compression. For compatibility with other more limited decoders use <code>slice_width</code> of 32 and <code>slice_height</code> of 8.</p>
<dt><code>tolerance</code></p>
<dd> Sets the undershoot tolerance of the rate control system in percent. This is to prevent an expensive search from being run.</p>
<dt><code>qm</code></p>
<dd> Sets the quantization matrix preset to use by default or when <code>wavelet_depth</code> is set to 5</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> <i>default</i> Uses the default quantization matrix from the specifications, extended with values for the fifth level. This provides a good balance between keeping detail and omitting artifacts.</p>
<dt>&#8211;</p>
<dd> <i>flat</i> Use a completely zeroed out quantization matrix. This increases <font SIZE="-1">PSNR</font> but might reduce perception. Use in bogus benchmarks.</p>
<dt>&#8211;</p>
<dd> <i>color</i> Reduces detail but attempts to preserve color at extremely low bitrates.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>SUBTITLES ENCODERS</h2>
<h3>dvdsub</h3>
<p> This codec encodes the bitmap subtitle format that is used in DVDs. Typically they are stored in <font SIZE="-1">VOBSUB</font> file pairs (*.idx + *.sub), and they can also be used in Matroska files. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>palette</code></p>
<dd> Specify the global palette used by the bitmaps. </p>
<p> The format for this option is a string containing 16 24-bits hexadecimal numbers (without 0x prefix) separated by commas, for example <tt>&quot;0d00ee, ee450d, 101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1, 7b2a0e, 0d950c, 0f007b, cf0dec, cfa80c, 7c127b&quot;</tt>.</p>
<dt><code>even_rows_fix</code></p>
<dd> When set to 1, enable a work-around that makes the number of pixel rows even in all subtitles. This fixes a problem with some players that cut off the bottom row if the number is odd. The work-around just adds a fully transparent row if needed. The overhead is low, typically one byte per subtitle on average. </p>
<p> By default, this work-around is disabled.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavcodec/">libavcodec</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
<dt><a href="#lbCO">SUBTITLES ENCODERS</a></p>
<dd>
<dt><a href="#lbCQ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbCR">AUTHORS</a></p>
<dd></dl>
