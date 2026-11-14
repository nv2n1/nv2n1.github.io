---
title: "decfuncs(3)"
name: "decfuncs"
section: "3"
letter: "d"
url: "/docs/linux/man/3-decfuncs/"
description: "Functions for Decoding –"
---

<h2 class="name">NAME</h2>
<p> Functions for Decoding &#8211; </p>
<h3>Modules</h3>
<p> <code>Configuration keys for the decoder ctl interface.</code><br />
 <i>Decoder CTL settings. </i></p>
<h3>Functions for decoding</h3>
<p> You must link to libdaalaadec if you use any of the functions in this section.<br />
 int <code>daala_decode_header_in</code> (<code>daala_info</code> *info, <code>daala_comment</code> *dc, <code>daala_setup_info</code> **ds, const <code>daala_packet</code> *dp)<br />
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
<h2>Function Documentation</h2>
<h3>int daala_decode_header_in (<code>daala_info</code> *info, <code>daala_comment</code> *dc, <code>daala_setup_info</code> **ds, const <code>daala_packet</code> *dp)</h3>
<p> Parses the header packets from an Ogg Daala stream. To use this function:</p>
<dl>
<dt>&bull;</p>
<dd> Initialize a <code>daala_info</code> structure using daala_info_init().</p>
<dt>&bull;</p>
<dd> Initialize a <code>daala_comment</code> structure using <code>daala_comment_init()</code>.</p>
<dt>&bull;</p>
<dd> Initialize a daala_setup_info pointer to NULL.</p>
<dt>&bull;</p>
<dd> Call this function three times, passing in pointers to the same <code>daala_info</code>, <code>daala_comment</code>, and daala_setup_info pointer each time, and the three successive header packets.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>info</i> The <code>daala_info</code> structure to fill in. This must have been previously initialized with daala_info_init(). The application may begin using the contents of this structure after the first header is decoded, though it must continue to be passed in unmodified on all subsequent calls.<br />
 <i>dc</i> The <code>daala_comment</code> structure to fill in. This must have been previously initialized with <code>daala_comment_init()</code>. The application may immediately begin using the contents of this structure after the second header is decoded, though it must continue to be passed in on all subsequent calls. Users should free the returned data with <code>daala_comment_clear()</code>.<br />
 <i>ds</i> A pointer to a daala_setup_info pointer to fill in. The contents of this pointer must be initialized to NULL on the first call, and the returned value must continue to be passed in on all subsequent calls.<br />
 <i>dp</i> The current header packet to process.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A positive value indicates that a Daala header was successfully processed and indicates the remaining number of headers to be read.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>0</i> The last header was processed and the next packet will contain video.<br />
 <i>OD_EFAULT</i> One of <i>info</i>, <i>dc</i>, or <i>ds</i> was NULL, or there was a memory allocation failure.<br />
 <i>OD_EBADHEADER</i> <i>op</i> was NULL, the packet was not the next header packet in the expected sequence, or the format fo the header data was invalid.<br />
 <i>OD_EVERSION</i> The packet data was a Daala header, but for a bitstream version not decodable with this version of libdaaladec.<br />
 <i>OD_ENOTFORMAT</i> The packet was not a Daala header.</dl>
<h3><code>daala_dec_ctx</code>* daala_decode_create (const <code>daala_info</code> *info, const <code>daala_setup_info</code> *setup)</h3>
<p> Allocates a decoder instance. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>info</i> A <code>daala_info</code> struct filled via <code>daala_decode_header_in()</code>.<br />
 <i>setup</i> A <code>daala_setup_info</code> handle returned via <code>daala_decode_header_in()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The initialized <code>daala_dec_ctx</code> handle.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>NULL</i> If the decoding parameters were invalid.</dl>
<h3>void daala_setup_free (<code>daala_setup_info</code> *setup)</h3>
<p> Releases all storage used for the decoder setup information. This should be called after you no longer want to create any decoders for a stream whose headers you have parsed with <code>daala_decode_header_in()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>setup</i> The setup information to free. This can safely be NULL.</dl>
<h3>int daala_decode_ctl (<code>daala_dec_ctx</code> *dec, intreq, void *buf, size_tbuf_sz)</h3>
<p> Decoder control function. This is used to provide advanced control of the decoding process. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dec</i> A <code>daala_dec_ctx</code> handle.<br />
 <i>req</i> The control code to process. See <code>the list of available control codes</code> for details.<br />
 <i>buf</i> The parameters for this control code.<br />
 <i>buf_sz</i> The size of the parameter buffer.</dl>
<h3>void daala_decode_free (<code>daala_dec_ctx</code> *dec)</h3>
<p> Frees an allocated decoder instance. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dec</i> A <code>daala_dec_ctx</code> handle.</dl>
<h3>int daala_decode_packet_in (<code>daala_dec_ctx</code> *dec, const <code>daala_packet</code> *dp)</h3>
<p> Retrieves decoded video data frames. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dec</i> A <code>daala_dec_ctx</code> handle.</dl>
<h3>int daala_decode_img_out (<code>daala_dec_ctx</code> *dec, <code>daala_image</code> *img)</h3>
<p> Outputs the next available decoded image frame. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>img</i> A buffer to receive the decoded image data.<br />
 <i>dp</i> An incoming Daala packet.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A positive value 1 means an output image was available and was placed in <i>img</i>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>1</i> An decoded image was available and was placed in <i>img</i>.<br />
 <i>0</i> No image was available, so the contents of <i>img</i> were left unchanged.<br />
 <i>OD_EFAULT</i> One of <i>dec</i> or <i>img</i> was NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for daala from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
