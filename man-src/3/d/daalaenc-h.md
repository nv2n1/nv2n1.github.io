---
title: "daalaenc-h(3)"
name: "daalaenc-h"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daalaenc-h/"
description: "daala/daalaenc.h –"
---

<p>daala/daalaenc.h &#8211; </p>
<p> The libdaala C encoding API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;codec.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>_daala_daalaenc_H</code> (1) </p>
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
 <i>Submits two-pass encoding metric data collected the first encoding pass to the second pass. </i> </p>
<p> <code>OD_SET_RATE_FLAGS flags</code><br />
 These are the flags available for use with <code>OD_SET_RATE_FLAGS</code>. </p>
<p> #define <code>OD_RATECTL_DROP_FRAMES</code> (0x1)<br />
 <i>Drop frames to keep within bitrate buffer constraints. </i><br />
 #define <code>OD_RATECTL_CAP_OVERFLOW</code> (0x2)<br />
 <i>Ignore bitrate buffer overflows. </i><br />
 #define <code>OD_RATECTL_CAP_UNDERFLOW</code> (0x4)<br />
 <i>Ignore bitrate buffer underflows. </i></p>
<h3>Typedefs</h3>
<p><code>Encoder state</code><br />
 The following data structure is opaque, and its contents are not publicly defined by this API. </p>
<p> Referring to its internals directly is unsupported, and may break without warning. </p>
<p> typedef struct <code>daala_enc_ctx</code> <code>daala_enc_ctx</code><br />
 <i>The encoder context. </i></p>
<h3>Functions</h3>
<p><code>Functions for encoding</code><br />
 You must link to libdaalabase and libdaalaenc if you use any of the functions in this section. </p>
<p> The functions are listed in the order they are used in a typical encode. The basic steps are:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Fill in a <code>daala_info</code> structure with details on the format of the video you wish to encode.</p>
<dt>&bull;</p>
<dd>Allocate a <code>daala_enc_ctx</code> handle with daala_encode_alloc().</p>
<dt>&bull;</p>
<dd>Perform any additional encoder configuration required with <code>daala_encode_ctl()</code>.</p>
<dt>&bull;</p>
<dd>Repeatedly call daala_encode_flusheader() to retrieve all the header packets.</p>
<dt>&bull;</p>
<dd>For each uncompressed frame:</p>
<dt> &bull;</p>
<dd>Submit the compressed frame via <code>daala_encode_img_in()</code>.</p>
<dt> &bull;</p>
<dd>Repeatedly call <code>daala_encode_packet_out()</code> to retrieve any video data packets that are ready.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Call <code>daala_comment_clear()</code> to release all comments allocated.</p>
<dt>&bull;</p>
<dd>Call <code>daala_encode_free()</code> to release all encoder memory.</dl>
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
<p>The libdaala C encoding API. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define OD_RATECTL_DROP_FRAMES (0x1)</h3>
<p>Drop frames to keep within bitrate buffer constraints. This can have a severe impact on quality, but is the only way to ensure that bitrate targets are met at low rates during sudden bursts of activity. It is enabled by default.</p>
<h3>#define OD_RATECTL_CAP_OVERFLOW (0x2)</h3>
<p>Ignore bitrate buffer overflows. If the encoder uses so few bits that the reservoir of available bits overflows, ignore the excess. The encoder will not try to use these extra bits in future frames. At high rates this may cause the result to be undersized, but allows a client to play the stream using a finite buffer; it should normally be enabled, which is the default.</p>
<h3>#define OD_RATECTL_CAP_UNDERFLOW (0x4)</h3>
<p>Ignore bitrate buffer underflows. If the encoder uses so many bits that the reservoir of available bits underflows, ignore the deficit. The encoder will not try to make up these extra bits in future frames. At low rates this may cause the result to be oversized; it should normally be disabled, which is the default.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>daala_enc_ctx</code> <code>daala_enc_ctx</code></h3>
<p>The encoder context.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for daala from the source code.</p>
