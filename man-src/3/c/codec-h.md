---
title: "codec-h(3)"
name: "codec-h"
section: "3"
letter: "c"
url: "/docs/linux/man/3-codec-h/"
description: "daala/codec.h – The shared libdaala C API."
---

<p>daala/codec.h &#8211; The shared libdaala C API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;daala_integer.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>daala_image_plane</code><br />
 <i>Representation of a single component within an image or frame. </i><br />
 struct <code>daala_image</code><br />
 <i>Representation of an image or video frame. </i><br />
 struct <code>daala_plane_info</code><br />
 <i>Subsampling factors for a plane as a power of 2. </i><br />
 struct <code>daala_info</code><br />
 <i>Configuration parameters for a codec instance. </i><br />
 struct <code>daala_packet</code> </p>
<p> struct <code>daala_comment</code><br />
 <i>The comment information. </i></p>
<h3>Macros</h3>
<p>#define <code>_daala_codec_H</code> (1) </p>
<p> #define <code>OD_GNUC_PREREQ</code>(maj, min, pat) (0) </p>
<p> #define <code>OD_WARN_UNUSED_RESULT</code> </p>
<p> #define <code>OD_ARG_NONNULL</code>(x) </p>
<p> #define <code>OD_NPLANES_MAX</code> (4)<br />
 <i>The maximum number of color planes allowed in a single frame. </i> </p>
<p> <code>Error codes</code> </p>
<p> #define <code>OD_SUCCESS</code> (0)<br />
 <i>No error occurred. </i><br />
 #define <code>OD_EFAULT</code> (-1)<br />
 <i>An invalid pointer was provided. </i><br />
 #define <code>OD_EINVAL</code> (-10)<br />
 <i>An invalid argument was provided. </i><br />
 #define <code>OD_EBADHEADER</code> (-20)<br />
 <i>The contents of the header were incomplete, invalid, or unexpected. </i><br />
 #define <code>OD_ENOTFORMAT</code> (-21)<br />
 <i>The header does not belong to a Daala stream. </i><br />
 #define <code>OD_EVERSION</code> (-22)<br />
 <i>The bitstream version is too high. </i><br />
 #define <code>OD_EIMPL</code> (-23)<br />
 <i>The specified function is not implemented. </i><br />
 #define <code>OD_EBADPACKET</code> (-24)<br />
 <i>There were errors in the video data packet. </i> </p>
<p> <code>Colorspaces</code><br />
 The currently defined color space tags. </p>
<p> #define <code>OD_CS_UNSPECIFIED</code> (0)<br />
 <i>The color space was not specified at the encoder. </i><br />
 #define <code>OD_CS_ITU_REC_470M</code> (1)<br />
 <i>A Y&#8217;CbCr color space designed for NTSC content. </i><br />
 #define <code>OD_CS_ITU_REC_470BG</code> (2)<br />
 <i>A Y&#8217;CbCr color space designed for PAL/SECAM content. </i><br />
 #define <code>OD_CS_ITU_REC_790</code> (3)<br />
 <i>A Y&#8217;CbCr color space designed for HD content. </i><br />
 #define <code>OD_CS_YCgCo</code> (4)<br />
 <i>A Y&#8217;CgCo color space designed for sRGB content. </i><br />
 #define <code>OD_CS_NSPACES</code> (5)<br />
 <i>The total number of currently defined color spaces. </i> </p>
<p> <code>Bit Depths</code><br />
 The three video bit depths currently supported by Daala. </p>
<p> #define <code>OD_BITDEPTH_MODE_8</code> (1)<br />
 <i>8-bit mode. </i><br />
 #define <code>OD_BITDEPTH_MODE_10</code> (2)<br />
 <i>10-bit mode. </i><br />
 #define <code>OD_BITDEPTH_MODE_12</code> (3)<br />
 <i>12-bit mode. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>daala_image_plane</code> <code>daala_image_plane</code> </p>
<p> typedef struct <code>daala_image</code> <code>daala_image</code> </p>
<p> typedef struct <code>daala_plane_info</code> <code>daala_plane_info</code> </p>
<p> typedef struct <code>daala_info</code> <code>daala_info</code> </p>
<p> typedef struct <code>daala_comment</code> <code>daala_comment</code> </p>
<h3>Functions</h3>
<p>const char * <code>daala_version_string</code> (void) </p>
<p> int <code>daala_log_init</code> (void)<br />
 <i>Initialize the logging module. </i><br />
 void <code>daala_info_init</code> (<code>daala_info</code> *info) </p>
<p> void <code>daala_info_clear</code> (<code>daala_info</code> *info) </p>
<p> void <code>daala_comment_init</code> (<code>daala_comment</code> *dc)<br />
 <i>Initializes a </i><code>daala_comment</code> section.<br />
 void <code>daala_comment_clear</code> (<code>daala_comment</code> *dc)<br />
 <i>Free resources allocated for metadata. </i><br />
 int64_t <code>daala_granule_basetime</code> (void *encdec, int64_t granpos) </p>
<p> double <code>daala_granule_time</code> (void *encdec, int64_t granpos)<br />
 <i>Converts a granule position to an absolute time in seconds. </i><br />
 int <code>daala_packet_isheader</code> (<code>daala_packet</code> *dpkt)<br />
 <i>Determines whether a Daala packet is a header or not. </i><br />
 int <code>daala_packet_iskeyframe</code> (<code>daala_packet</code> *dpkt)<br />
 <i>Determines whether a Daala packet is a key frame or not. </i></p>
<h2>Detailed Description</h2>
<p>The shared libdaala C API. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define OD_SUCCESS (0)</h3>
<p>No error occurred.</p>
<h3>#define OD_EFAULT (-1)</h3>
<p>An invalid pointer was provided.</p>
<h3>#define OD_EINVAL (-10)</h3>
<p>An invalid argument was provided.</p>
<h3>#define OD_EBADHEADER (-20)</h3>
<p>The contents of the header were incomplete, invalid, or unexpected.</p>
<h3>#define OD_ENOTFORMAT (-21)</h3>
<p>The header does not belong to a Daala stream.</p>
<h3>#define OD_EVERSION (-22)</h3>
<p>The bitstream version is too high.</p>
<h3>#define OD_EIMPL (-23)</h3>
<p>The specified function is not implemented.</p>
<h3>#define OD_EBADPACKET (-24)</h3>
<p>There were errors in the video data packet.</p>
<h3>#define OD_CS_UNSPECIFIED (0)</h3>
<p>The color space was not specified at the encoder. It may be conveyed by an external means.</p>
<h3>#define OD_CS_ITU_REC_470BG (2)</h3>
<p>A Y&#8217;CbCr color space designed for PAL/SECAM content.</p>
<h3>#define OD_CS_ITU_REC_790 (3)</h3>
<p>A Y&#8217;CbCr color space designed for HD content.</p>
<h3>#define OD_CS_YCgCo (4)</h3>
<p>A Y&#8217;CgCo color space designed for sRGB content.</p>
<h3>#define OD_CS_NSPACES (5)</h3>
<p>The total number of currently defined color spaces.</p>
<h3>#define OD_NPLANES_MAX (4)</h3>
<p>The maximum number of color planes allowed in a single frame.</p>
<h3>#define OD_BITDEPTH_MODE_8 (1)</h3>
<p>8-bit mode.</p>
<h3>#define OD_BITDEPTH_MODE_10 (2)</h3>
<p>10-bit mode.</p>
<h3>#define OD_BITDEPTH_MODE_12 (3)</h3>
<p>12-bit mode.</p>
<h2>Function Documentation</h2>
<h3>int daala_log_init (void)</h3>
<p>Initialize the logging module. This should be called once before invoking any other Daala functions if logging support is enabled and you want to use it. Otherwise no logging messages will be printed. </p>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> Success. This function always succeeds. It only returns a value for convenience (e.g., for use in a static initializer).</dl>
<h3>void daala_comment_init (<code>daala_comment</code> *dc)</h3>
<p>Initializes a <code>daala_comment</code> section. Users should free the returned data with <code>daala_comment_clear()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dc</i> A <code>daala_comment</code> structure.</dl>
<h3>void daala_comment_clear (<code>daala_comment</code> *dc)</h3>
<p>Free resources allocated for metadata. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dc</i> A <code>daala_comment</code> structure.</dl>
<h3>double daala_granule_time (void *encdec, int64_tgranpos)</h3>
<p>Converts a granule position to an absolute time in seconds. The granule position is interpreted in the context of a given <code>daala_enc_ctx</code> or <code>daala_dec_ctx</code> handle (either will suffice). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>encdec</i> A previously allocated <code>daala_enc_ctx</code> or <code>daala_dec_ctx</code> handle.<br />
 <i>granpos</i> The granule position to convert.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The absolute time in seconds corresponding to <i>granpos</i>. This is the &#8216;end time&#8217; for the frame, or the latest time it should be displayed. It is not the presentation time.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>-1</i> The given granule position was invalid (i.e. negative).</dl>
<h3>int daala_packet_isheader (<code>daala_packet</code> *dpkt)</h3>
<p>Determines whether a Daala packet is a header or not. This function does no verification beyond checking the packet type bit, so it should not be used for bitstream identification. Use daala_decode_headerin() for that. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dpkt</i> A <code>daala_packet</code> structure.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>1</i> The packet is a header packet.<br />
 <i>0</i> The packet is a video data packet.</dl>
<h3>int daala_packet_iskeyframe (<code>daala_packet</code> *dpkt)</h3>
<p>Determines whether a Daala packet is a key frame or not. This function does no verfication beyond checking the packet type and key frame bits, so it should not be used for bitstream identification. Feed the packet to an actual decoder for that. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dpkt</i> A <code>daala_packet</code> structure.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>1</i> The packet contains a key frame.<br />
 <i>0</i> The packet contains a delta frame.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for daala from the source code.</p>
