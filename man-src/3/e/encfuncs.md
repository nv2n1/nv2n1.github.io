---
title: "encfuncs(3)"
name: "encfuncs"
section: "3"
letter: "e"
url: "/docs/linux/man/3-encfuncs/"
description: "Functions for Encoding –"
---

<h2 class="name">NAME</h2>
<p> Functions for Encoding &#8211; </p>
<h3>Modules</h3>
<p> <code>Configuration keys for the encoder ctl interface.</code><br />
 <i>Encoder CTL settings. </i></p>
<h3>Macros</h3>
<p> #define <code>OD_SET_QUANT</code> 4000<br />
 <i>Set the quantizer scale. </i><br />
 #define <code>OD_SET_COMPLEXITY</code> 4002<br />
 <i>Configure the encoder&#8217;s computational complexity level. </i><br />
 #define <code>OD_GET_COMPLEXITY</code> 4004<br />
 <i>Get the encoder&#8217;s computational complexity level. </i><br />
 #define <code>OD_SET_ACTIVITY_MASKING</code> 4006<br />
 <i>Whether activity masking should be used or not. </i><br />
 #define <code>OD_SET_QM</code> 4008<br />
 <i>Which quantization matrix to use. </i><br />
 #define <code>OD_SET_DERING</code> 4010<br />
 <i>Whether the bilinear postprocessing filter should be used or not. </i><br />
 #define <code>OD_SET_MC_CHROMA</code> 4100<br />
 <i>Whether the motion compensation search should use the chroma planes in addition to the luma plane. </i><br />
 #define <code>OD_SET_MV_RES_MIN</code> 4102<br />
 <i>Minimum motion vectors resolution for the motion compensation search. </i><br />
 #define <code>OD_SET_MV_LEVEL_MIN</code> 4104<br />
 <i>Minimum motion vectors level for the motion compensation search. </i><br />
 #define <code>OD_SET_MV_LEVEL_MAX</code> 4106<br />
 <i>Maximum motion vectors level for the motion compensation search. </i><br />
 #define <code>OD_SET_MC_SATD</code> 4108<br />
 <i>Whether the SATD metric should be used in motion compensation or not. </i><br />
 #define <code>OD_SET_B_FRAMES</code> 4110<br />
 <i>Number of B frames used by encoder. </i><br />
 #define <code>OD_SET_BITRATE</code> 4112<br />
 <i>Sets the current encoding bitrate. </i><br />
 #define <code>OD_SET_RATE_FLAGS</code> 4114<br />
 <i>Modifies the default bitrate management behavior. </i><br />
 #define <code>OD_SET_RATE_BUFFER</code> 4116<br />
 <i>Sets the size of the bitrate management bit reservoir as a function of number of frames. </i><br />
 #define <code>OD_2PASS_OUT</code> 4118<br />
 <i>Enable pass 1 of two-pass encoding mode and retrieve the first pass metrics. </i><br />
 #define <code>OD_2PASS_IN</code> 4120<br />
 <i>Submits two-pass encoding metric data collected the first encoding pass to the second pass. </i></p>
<h3>Functions for encoding</h3>
<p> You must link to libdaalabase and libdaalaenc if you use any of the functions in this section. </p>
<p> The functions are listed in the order they are used in a typical encode. The basic steps are:</p>
<dl>
<dt>&bull;</p>
<dd> Fill in a <code>daala_info</code> structure with details on the format of the video you wish to encode.</p>
<dt>&bull;</p>
<dd> Allocate a <code>daala_enc_ctx</code> handle with daala_encode_alloc().</p>
<dt>&bull;</p>
<dd> Perform any additional encoder configuration required with <code>daala_encode_ctl()</code>.</p>
<dt>&bull;</p>
<dd> Repeatedly call daala_encode_flusheader() to retrieve all the header packets.</p>
<dt>&bull;</p>
<dd> For each uncompressed frame:</p>
<dt> &bull;</p>
<dd> Submit the compressed frame via <code>daala_encode_img_in()</code>.</p>
<dt> &bull;</p>
<dd> Repeatedly call <code>daala_encode_packet_out()</code> to retrieve any video data packets that are ready.</dl>
<dl>
<dt>&bull;</p>
<dd> Call <code>daala_comment_clear()</code> to release all comments allocated.</p>
<dt>&bull;</p>
<dd> Call <code>daala_encode_free()</code> to release all encoder memory.</dl>
<p> <code>daala_enc_ctx</code> * <code>daala_encode_create</code> (const <code>daala_info</code> *info)<br />
 <i>Allocates and initializes an encoder instance. </i><br />
 int <code>daala_encode_ctl</code> (<code>daala_enc_ctx</code> *enc, int req, void *buf, size_t buf_sz)<br />
 <i>Encoder control function. </i><br />
 int <code>daala_encode_flush_header</code> (<code>daala_enc_ctx</code> *enc, <code>daala_comment</code> *comments, <code>daala_packet</code> *dp)<br />
 <i>Outputs the next header packet. </i><br />
 int <code>daala_encode_img_in</code> (<code>daala_enc_ctx</code> *enc, <code>daala_image</code> *img, int duration)<br />
 <i>Submits an uncompressed frame to the encoder. </i><br />
 int <code>daala_encode_packet_out</code> (<code>daala_enc_ctx</code> *enc, int last, <code>daala_packet</code> *dp)<br />
 <i>Retrieves encoded video data packets. </i><br />
 void <code>daala_encode_free</code> (<code>daala_enc_ctx</code> *enc)<br />
 <i>Frees an allocated encoder instance. </i></p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define OD_SET_QUANT 4000</h3>
<p> Set the quantizer scale. The passed buffer is interpreted as containing a single int. The valid range is 0-511.</p>
<h3>#define OD_SET_COMPLEXITY 4002</h3>
<p> Configure the encoder&#8217;s computational complexity level. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>OD_GET_COMPLEXITY</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: The new encoder complexity level. Values must lie in the range 0&#8230;10, inclusive, with higher values requiring more CPU but generally producing better quality at a given bitrate.</dl>
<h3>#define OD_GET_COMPLEXITY 4004</h3>
<p> Get the encoder&#8217;s computational complexity level. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>OD_SET_COMPLEXITY</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: Returns a value in the range 0&#8230;10, inclusive. Higher values indicate higher CPU requirements, but generally producing better quality at a given bitrate.</dl>
<h3>#define OD_SET_ACTIVITY_MASKING 4006</h3>
<p> Whether activity masking should be used or not. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: 0 to disable the use of activity masking, a non-zero value otherwise (the default).</dl>
<h3>#define OD_SET_QM 4008</h3>
<p> Which quantization matrix to use. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: 0 =&gt; flat quantization matrix, 1 =&gt; HVS (the default).</dl>
<h3>#define OD_SET_DERING 4010</h3>
<p> Whether the bilinear postprocessing filter should be used or not. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: 0 to disable the bilinear postprocessing filter, a non-zero value otherwise (the default).</dl>
<h3>#define OD_SET_MC_CHROMA 4100</h3>
<p> Whether the motion compensation search should use the chroma planes in addition to the luma plane. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: 0 to disable the use of the chroma planes, a non-zero value otherwise (the default).</dl>
<h3>#define OD_SET_MV_RES_MIN 4102</h3>
<p> Minimum motion vectors resolution for the motion compensation search. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: 0 =&gt; 1/8 pel (default), 1 =&gt; 1/4 pel, 2 =&gt; 1/2 pel</dl>
<h3>#define OD_SET_MV_LEVEL_MIN 4104</h3>
<p> Minimum motion vectors level for the motion compensation search. If this level is greater than the maximum level, the maximum level will be used instead. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: level between 0 and 4 Default: 0</dl>
<h3>#define OD_SET_MV_LEVEL_MAX 4106</h3>
<p> Maximum motion vectors level for the motion compensation search. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: level between 0 and 4 Default: 4</dl>
<h3>#define OD_SET_MC_SATD 4108</h3>
<p> Whether the SATD metric should be used in motion compensation or not. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: 0 to disable the use of SATD (the default), a non-zero value otherwise.</dl>
<h3>#define OD_SET_B_FRAMES 4110</h3>
<p> Number of B frames used by encoder. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>_buf</i> int: The number of B frames. Values must lie in the range 0&#8230;OD_MAX_B_FRAMES, inclusive.</dl>
<h3>#define OD_SET_BITRATE 4112</h3>
<p> Sets the current encoding bitrate. Once a bitrate is set, the encoder must use a rate-controlled mode for all future frames (this restriction may be relaxed in a future version). Due to the buffer delay, the exact bitrate of each section of the encode is not guaranteed. The encoder may have already used more bits than allowed for the frames it has encoded, expecting to make them up in future frames, or it may have used fewer, holding the excess in reserve. The exact transition between two bitrates is not well-defined by this API, but may be affected by flags set with <code>OD_SET_RATE_FLAGS</code>. After a number of frames equal to the buffer delay, one may expect further output to average at the target bitrate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> long: The new target bitrate, in bits per second.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>OD_SUCCESS</i> Success.<br />
 <i>OD_EFAULT</i> <i>enc</i> or <i>buf</i> is NULL.<br />
 <i>OD_EINVAL</i> The target bitrate was not positive. A future version of this library may allow passing 0 to disabled rate-controlled mode and return to a quality-based mode, in which case this function will not return an error for that value.<br />
 <i>OD_EIMPL</i> Not supported by this implementation.</dl>
<h3>#define OD_SET_RATE_FLAGS 4114</h3>
<p> Modifies the default bitrate management behavior. Use to allow or disallow frame dropping, and to enable or disable capping bit reservoir overflows and underflows. See <code>the list of available flags</code>. The flags are set by default to <code>OD_RATECTL_DROP_FRAMES</code>|<code>OD_RATECTL_CAP_OVERFLOW</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> int: Any combination of <code>the available flags</code>:</p>
<dl>
<dt>&bull;</p>
<dd> <code>OD_RATECTL_DROP_FRAMES</code>: Enable frame dropping.</p>
<dt>&bull;</p>
<dd> <code>OD_RATECTL_CAP_OVERFLOW</code>: Don&#8217;t bank excess bits for later use.</p>
<dt>&bull;</p>
<dd> <code>OD_RATECTL_CAP_UNDERFLOW</code>: Don&#8217;t try to make up shortfalls later.</dl>
</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>OD_SUCCESS</i> Success.<br />
 <i>OD_EFAULT</i> <i>enc</i> or <i>buf</i> is NULL.<br />
 <i>OD_EINVAL</i> <i>buf_sz</i> is not sizeof(int) or rate control is not enabled.<br />
 <i>OD_EIMPL</i> Not supported by this implementation in the current encoding mode.</dl>
<h3>#define OD_SET_RATE_BUFFER 4116</h3>
<p> Sets the size of the bitrate management bit reservoir as a function of number of frames. The reservoir size affects how quickly bitrate management reacts to instantaneous changes in the video complexity. Larger reservoirs react more slowly, and provide better overall quality, but require more buffering by a client, adding more latency to live streams. By default, libdaala sets the reservoir to the maximum distance between keyframes, subject to a minimum and maximum limit. This call may be used to increase or decrease the reservoir, increasing or decreasing the allowed temporary variance in bitrate. An implementation may impose some limits on the size of a reservoir it can handle, in which case the actual reservoir size may not be exactly what was requested. The actual value set will be returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> int: Requested size of the reservoir measured in frames.<br />
 <i>buf</i> int: The actual size of the reservoir set.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>OD_EFAULT</i> <i>enc</i> or <i>buf</i> is NULL.<br />
 <i>OD_EINVAL</i> <i>buf_sz</i> is not sizeof(int), or rate control is not enabled. The buffer has an implementation defined minimum and maximum size and the value in buf will be adjusted to match the actual value set.<br />
 <i>OD_EIMPL</i> Not supported by this implementation in the current encoding mode.</dl>
<h3>#define OD_2PASS_OUT 4118</h3>
<p> Enable pass 1 of two-pass encoding mode and retrieve the first pass metrics. Pass 1 mode must be enabled before the first frame is encoded, and a target bitrate must have already been specified to the encoder. Although this does not have to be the exact rate that will be used in the second pass, closer values may produce better results. The first call returns the size of the two-pass header data, along with some placeholder content, and sets the encoder into pass 1 mode implicitly. This call sets the encoder to pass 1 mode implicitly. Then, a subsequent call must be made after each call to <code>daala_encode_img_in()</code> to retrieve the metrics for that frame. An additional, final call must be made to retrieve the summary data, containing such information as the total number of frames, etc. This must be stored in place of the placeholder data that was returned in the first call, before the frame metrics data. All of this data must be presented back to the encoder during pass 2 using <code>OD_2PASS_IN</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>&lt;tt&gt;char</i> *buf: Returns a pointer to internal storage containing the two pass metrics data. This storage is only valid until the next call, or until the encoder context is freed, and must be copied by the application.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>&gt;=0</i> The number of bytes of metric data available in the returned buffer.<br />
 <i>OD_EFAULT</i> <i>enc</i> or <i>buf</i> is NULL.<br />
 <i>OD_EINVAL</i> <i>buf_sz</i> is not sizeof(char *), no target bitrate has been set, or the first call was made after the first frame was submitted for encoding.<br />
 <i>OD_EIMPL</i> Not supported by this implementation.</dl>
<h3>#define OD_2PASS_IN 4120</h3>
<p> Submits two-pass encoding metric data collected the first encoding pass to the second pass. The first call must be made before the first frame is encoded, and a target bitrate must have already been specified to the encoder. It sets the encoder to pass 2 mode implicitly; this cannot be disabled. The encoder may require reading data from some or all of the frames in advance, depending on, e.g., the reservoir size used in the second pass. You must call this function repeatedly before each frame to provide data until either a) it fails to consume all of the data presented or b) all of the pass 1 data has been consumed. In the first case, you must save the remaining data to be presented after the next frame. You can call this function with a NULL argument to get an upper bound on the number of bytes that will be required before the next frame. </p>
<p> When pass 2 is first enabled, the default bit reservoir is set to the entire file; this gives maximum flexibility but can lead to very high peak rates. You can subsequently set it to another value with <code>OD_SET_RATE_BUFFER</code> (e.g., to set it to the keyframe interval for non-live streaming), however, you may then need to provide more data before the next frame. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> char[]: A buffer containing the data returned by <code>OD_2PASS_OUT</code> in pass 1. You may pass NULL for <i>buf</i> to return an upper bound on the number of additional bytes needed before the next frame. The summary data returned at the end of pass 1 must be at the head of the buffer on the first call with a non-NULL <i>buf</i>, and the placeholder data returned at the start of pass 1 should be omitted. After each call you should advance this buffer by the number of bytes consumed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>&gt;0</i> The number of bytes of metric data required/consumed.<br />
 <i>0</i> No more data is required before the next frame.<br />
 <i>OD_EFAULT</i> <i>enc</i> is NULL.<br />
 <i>OD_EINVAL</i> No target bitrate has been set, or the first call was made after the first frame was submitted for encoding.<br />
 <i>OD_ENOTFORMAT</i> The data did not appear to be pass 1 from a compatible implementation of this library.<br />
 <i>OD_EBADHEADER</i> The data was invalid; this may be returned when attempting to read an aborted pass 1 file that still has the placeholder data in place of the summary data.<br />
 <i>OD_EIMPL</i> Not supported by this implementation.</dl>
<h2>Function Documentation</h2>
<h3><code>daala_enc_ctx</code>* daala_encode_create (const <code>daala_info</code> *info)</h3>
<p> Allocates and initializes an encoder instance. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>info</i> A <code>daala_info</code> struct filled with the desired encoding parameters.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The initialized <code>daala_enc_ctx</code> handle.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>NULL</i> if the encoding parameters were invalid.</dl>
<h3>int daala_encode_ctl (<code>daala_enc_ctx</code> *enc, intreq, void *buf, size_tbuf_sz)</h3>
<p> Encoder control function. This is used to provide advanced control of the encoding process. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>enc</i> A <code>daala_enc_ctx</code> handle.<br />
 <i>req</i> The control code to process. See <code>the list of available control codes</code> for details.<br />
 <i>buf</i> The parameters for this control code.<br />
 <i>buf_sz</i> The size of the parameter buffer.</dl>
<h3>int daala_encode_flush_header (<code>daala_enc_ctx</code> *enc, <code>daala_comment</code> *comments, <code>daala_packet</code> *dp)</h3>
<p> Outputs the next header packet. This should be called repeatedly after encoder initialization until it return 0 to get all of the header packets, in order, before encoding actual video data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>enc</i> A <code>daala_enc_ctx</code> handle.<br />
 <i>comments</i> The metadata to place in the comment header, when it is encoded. Users should free the returned data with <code>daala_comment_clear()</code>.<br />
 <i>dp</i> A <code>daala_packet</code> structure to fill. All of the elements of this structure will be set, including a pointer to the header data. The memory for the header data is owned by libdaala.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A positive value indicates that a header packet was successfully produced.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>0</i> No packet was produced, and no more header packets remain.<br />
 <i>OD_EFAULT</i> <i>enc</i>, <i>comments</i> or <i>op</i> was NULL.</dl>
<h3>int daala_encode_img_in (<code>daala_enc_ctx</code> *enc, <code>daala_image</code> *img, intduration)</h3>
<p> Submits an uncompressed frame to the encoder. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>enc</i> A <code>daala_enc_ctx</code> handle.<br />
 <i>img</i> A buffer of image data to encode.<br />
 <i>duration</i> The duration to display the frame for, in timebase units. If a non-zero frame duration was specified in the header, then this parameter is ignored.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>0</i> Success.<br />
 <i>OD_EFAULT</i> <i>enc</i> or <i>img</i> was NULL.<br />
 <i>OD_EINVAL</i> The image size does not match the frame size the encoder was initialized with, or encoding has already completed.</dl>
<h3>int daala_encode_packet_out (<code>daala_enc_ctx</code> *enc, intlast, <code>daala_packet</code> *dp)</h3>
<p> Retrieves encoded video data packets. This should be called repeatedly after each frame is submitted to flush any encoded packets, until it returns 0. The encoder will not buffer these packets as subsequent frames are compressed, so a failure to do so will result in lost video data. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Current the encoder operates in a one-frame-in, one-packet-out manner. However, this may be changed in the future.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>enc</i> A <code>daala_enc_ctx</code> handle. This ensures that a proper EOS flag is set on the last packet.<br />
 <i>dp</i> A <code>daala_packet</code> structure to fill. All of the elements of this structure will be set, including a pointer to the video data. The memory for the video data is owned by libdaala.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A positive value indicates that a video data packet was successfully produced.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>0</i> No packet was produced, and no more encoded video data remains.<br />
 <i>OD_EFAULT</i> <i>enc</i> or <i>op</i> was NULL.</dl>
<h3>void daala_encode_free (<code>daala_enc_ctx</code> *enc)</h3>
<p> Frees an allocated encoder instance. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>enc</i> A <code>daala_enc_ctx</code> handle.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for daala from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBF">Author</a></p>
<dd></dl>
