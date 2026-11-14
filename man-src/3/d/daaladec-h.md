---
title: "daaladec-h(3)"
name: "daaladec-h"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daaladec-h/"
description: "daala/daaladec.h –"
---

<p>daala/daaladec.h &#8211; </p>
<p> The libdaala C decoding API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;codec.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>od_acct_symbol</code> </p>
<p> struct <code>od_accounting_dict</code><br />
 <i>Dictionary for translating strings into id. </i><br />
 struct <code>od_accounting</code> </p>
<h3>Macros</h3>
<p>#define <code>_daala_daaladec_H</code> (1) </p>
<p> #define <code>OD_DECCTL_SET_BSIZE_BUFFER</code> (7001) </p>
<p> #define <code>OD_DECCTL_SET_FLAGS_BUFFER</code> (7003) </p>
<p> #define <code>OD_DECCTL_SET_MV_BUFFER</code> (7005) </p>
<p> #define <code>OD_DECCTL_SET_MC_IMG</code> (7007)<br />
 <i>Copy the motion compensated reference into a user supplied </i><code>daala_image</code>.<br />
 #define <code>OD_DECCTL_GET_ACCOUNTING</code> (7009) </p>
<p> #define <code>OD_DECCTL_SET_ACCOUNTING_ENABLED</code> (7011) </p>
<p> #define <code>OD_DECCTL_SET_DERING_BUFFER</code> (7013) </p>
<p> #define <code>OD_ACCT_FRAME</code> (10) </p>
<p> #define <code>OD_ACCT_MV</code> (11) </p>
<p> #define <code>MAX_SYMBOL_TYPES</code> (256) </p>
<h3>Typedefs</h3>
<p><code>Decoder state</code><br />
 The following data structures are opaque, and their contents are not publicly defined by this API. </p>
<p> Referring to their internals directly is unsupported, and may break without warning. </p>
<p> typedef struct <code>daala_dec_ctx</code> <code>daala_dec_ctx</code><br />
 <i>The decoder context. </i><br />
 typedef struct <code>daala_setup_info</code> <code>daala_setup_info</code><br />
 <i>Setup information. </i></p>
<h3>Functions</h3>
<p><code>Functions for decoding</code><br />
 You must link to libdaalaadec if you use any of the functions in this section. </p>
<p> int <code>daala_decode_header_in</code> (<code>daala_info</code> *info, <code>daala_comment</code> *dc, <code>daala_setup_info</code> **ds, const <code>daala_packet</code> *dp)<br />
 <i>Parses the header packets from an Ogg Daala stream. </i><br />
 <code>daala_dec_ctx</code> * <code>daala_decode_create</code> (const <code>daala_info</code> *info, const <code>daala_setup_info</code> *setup)<br />
 <i>Allocates a decoder instance. </i><br />
 void <code>daala_setup_free</code> (<code>daala_setup_info</code> *setup)<br />
 <i>Releases all storage used for the decoder setup information. </i><br />
 int <code>daala_decode_ctl</code> (<code>daala_dec_ctx</code> *dec, int req, void *buf, size_t buf_sz)<br />
 <i>Decoder control function. </i><br />
 void <code>daala_decode_free</code> (<code>daala_dec_ctx</code> *dec)<br />
 <i>Frees an allocated decoder instance. </i><br />
 int <code>daala_decode_packet_in</code> (<code>daala_dec_ctx</code> *dec, const <code>daala_packet</code> *dp)<br />
 <i>Retrieves decoded video data frames. </i><br />
 int <code>daala_decode_img_out</code> (<code>daala_dec_ctx</code> *dec, <code>daala_image</code> *img)<br />
 <i>Outputs the next available decoded image frame. </i></p>
<h2>Detailed Description</h2>
<p>The libdaala C decoding API. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define OD_DECCTL_SET_MC_IMG (7007)</h3>
<p>Copy the motion compensated reference into a user supplied <code>daala_image</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>&lt;tt&gt;daala_image*&lt;/tt&gt;,:</i> Pointer to the user supplied <code>daala_image</code>. Image must be allocated by the caller, and must be the same format as the decoder output images.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>daala_dec_ctx</code> <code>daala_dec_ctx</code></h3>
<p>The decoder context.</p>
<h3>typedef struct <code>daala_setup_info</code> <code>daala_setup_info</code></h3>
<p>Setup information. This contains auxiliary information decoded from the setup header by <code>daala_decode_header_in()</code> to be passed to <code>daala_decode_create()</code>. It can be re-used to initialize any number of decoders, and can be freed via <code>daala_setup_free()</code> at any time.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for daala from the source code.</p>
