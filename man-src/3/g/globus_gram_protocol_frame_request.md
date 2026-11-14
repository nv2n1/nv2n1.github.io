---
title: "globus_gram_protocol_frame_request(3)"
name: "globus_gram_protocol_frame_request"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_frame_request/"
description: "Message Framing –"
---

<h2 class="name">NAME</h2>
<p> Message Framing &#8211; </p>
<p> Message Framing.</p>
<h3>Functions</h3>
<p> int <code>globus_gram_protocol_frame_request</code> (const char *url, const globus_byte_t *msg, globus_size_t msgsize, globus_byte_t **framedmsg, globus_size_t *framedsize)<br />
 <i>Create a HTTP-framed copy of a GRAM request. </i><br />
 int <code>globus_gram_protocol_frame_reply</code> (int code, const globus_byte_t *msg, globus_size_t msgsize, globus_byte_t **framedmsg, globus_size_t *framedsize)<br />
 <i>Create a HTTP-framed copy of a GRAM reply. </i></p>
<h2>Detailed Description</h2>
<p> Message Framing. </p>
<p> The functions in this section frame a GRAM request, query, or reply message with HTTP headers compatible with the GRAM2 protocol parsers in GT2 GT3, and GT4. </p>
<p> These functions should be used when an application wants to control the way that the GRAM Protocol messages are sent, while still using the standard message formatting and framing routines. An alternative set of functions in the <code>Message I/O</code> section of the manual combine message framing with callback-driven I/O.</p>
<h2>Function Documentation</h2>
<h3>int globus_gram_protocol_frame_reply (intcode, const globus_byte_t *msg, globus_size_tmsgsize, globus_byte_t **framedmsg, globus_size_t *framedsize)</h3>
<p> Create a HTTP-framed copy of a GRAM reply. The <code>globus_gram_protocol_frame_reply()</code> function adds HTTP 1.1 framing around the input message. The framed message includes HTTP headers relating the the status of the operation being replied to and the length of the message content. The framed message is returned by modifying <i>framedmsg</i> to point to a newly allocated string. The integer pointed to by the <i>framedsize</i> parameter is set to the length of this message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>code</i> The HTTP response code to send along with this reply.<br />
 <i>msg</i> A string containing the reply message content to be framed.<br />
 <i>msgsize</i> The length of the string pointed to by <i>msg</i>.<br />
 <i>framedmsg</i> An output parameter which will be set to a copy of the <i>msg</i> string with an HTTP reply frame around it.<br />
 <i>framedsize</i> An output parameter which will be set to the length of the framed reply string pointed to by <i>framedmsg</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_frame_reply()</code> will return GLOBUS_SUCCESS and the <i>framedmsg</i> and <i>framedsize</i> parameters will be modified to point to the new framed message string and its length respectively. When this occurs, the caller is responsible for freeing the string pointed to by <i>framedmsg</i>. If an error occurs, its value will returned and the <i>framedmsg</i> and <i>framedsize</i> parameters will be uninitialized.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success</dl>
<h3>int globus_gram_protocol_frame_request (const char *url, const globus_byte_t *msg, globus_size_tmsgsize, globus_byte_t **framedmsg, globus_size_t *framedsize)</h3>
<p> Create a HTTP-framed copy of a GRAM request. The <code>globus_gram_protocol_frame_request()</code> function adds HTTP 1.1 framing around the input message. The framed message includes HTTP headers relating the the destination URL and the length of the message content. The framed message is returned by modifying <i>framedmsg</i> to point to a newly allocated string. The integer pointed to by the <i>framedsize</i> parameter is set to the length of this message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> The URL of the GRAM resource to contact. This is parsed and used to generate the HTTP POST operation destination and the Host HTTP header.<br />
 <i>msg</i> A string containing the message content to be framed.<br />
 <i>msgsize</i> The length of the string pointed to by <i>msg</i><br />
 <i>framedmsg</i> An output parameter which will be set to a copy of the <i>msg</i> string with an HTTP frame around it.<br />
 <i>framedsize</i> An output parameter which will be set to the length of the framed message.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_frame_request()</code> will return GLOBUS_SUCCESS and the <i>framedmsg</i> and <i>framedsize</i> parameters will be modified to point to the new framed message string and its length respectively. When this occurs, the caller is responsible for freeing the string pointed to by <i>framedmsg</i>. If an error occurs, its value will returned and the <i>framedmsg</i> and <i>framedsize</i> parameters will be uninitialized.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_protocol from the source code. </p>
<h2>Index</h2>
