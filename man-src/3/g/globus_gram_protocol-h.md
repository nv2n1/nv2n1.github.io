---
title: "globus_gram_protocol-h(3)"
name: "globus_gram_protocol-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol-h/"
description: "globus_gram_protocol.h – GRAM Protocol API."
---

<p>globus_gram_protocol.h &#8211; GRAM Protocol API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_io.h&#8217;<br />
 #include &#8216;globus_gram_protocol_constants.h&#8217; </p>
<h3>Typedefs</h3>
<p>typedef unsigned long <code>globus_gram_protocol_handle_t</code><br />
 <i>Unique GRAM protocol identifier. </i><br />
 typedef struct<br />
 globus_gram_protocol_hash_entry_s <code>globus_gram_protocol_extension_t</code>&quot;<br />
 <i>GRAM protocol extension attribute-value pair. </i></p>
<h3>Functions</h3>
<p>int <code>globus_gram_protocol_setup_attr</code> (globus_io_attr_t *attr)<br />
 <i>Create default I/O attribute for GRAM. </i><br />
 globus_bool_t <code>globus_gram_protocol_authorize_self</code> (gss_ctx_id_t context)<br />
 <i>Determine if a GSSAPI context has the same source and target identities. </i><br />
 int <code>globus_gram_protocol_allow_attach</code> (char **url, globus_gram_protocol_callback_t callback, void *callback_arg)<br />
 <i>Create a GRAM protocol service listener. </i><br />
 int <code>globus_gram_protocol_callback_disallow</code> (char *url)<br />
 <i>Stop a GASS protocol listener from handling new requests. </i><br />
 int <code>globus_gram_protocol_post</code> (const char *url, <code>globus_gram_protocol_handle_t</code> *handle, globus_io_attr_t *attr, globus_byte_t *message, globus_size_t message_size, globus_gram_protocol_callback_t callback, void *callback_arg)<br />
 <i>Post a GRAM protocol request to a GRAM server. </i><br />
 int <code>globus_gram_protocol_post_delegation</code> (const char *url, <code>globus_gram_protocol_handle_t</code> *handle, globus_io_attr_t *attr, globus_byte_t *message, globus_size_t message_size, gss_cred_id_t cred_handle, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 req_flags, OM_uint32 time_req, globus_gram_protocol_callback_t callback, void *callback_arg)<br />
 <i>Post a GRAM protocol delegation request to a GRAM server. </i><br />
 int <code>globus_gram_protocol_reply</code> (<code>globus_gram_protocol_handle_t</code> handle, int code, globus_byte_t *message, globus_size_t message_size)<br />
 <i>Reply to a GRAM protocol message. </i><br />
 int <code>globus_gram_protocol_accept_delegation</code> (<code>globus_gram_protocol_handle_t</code> handle, gss_OID_set restriction_oids, gss_buffer_set_t restriction_bufers, OM_uint32 req_flags, OM_uint32 time_req, globus_gram_protocol_delegation_callback_t callback, void *arg)<br />
 <i>Perform the server-side of the GSSAPI delegation handshake to receive a new delegated credential. </i><br />
 int <code>globus_gram_protocol_frame_request</code> (const char *url, const globus_byte_t *msg, globus_size_t msgsize, globus_byte_t **framedmsg, globus_size_t *framedsize)<br />
 <i>Create a HTTP-framed copy of a GRAM request. </i><br />
 int <code>globus_gram_protocol_frame_reply</code> (int code, const globus_byte_t *msg, globus_size_t msgsize, globus_byte_t **framedmsg, globus_size_t *framedsize)<br />
 <i>Create a HTTP-framed copy of a GRAM reply. </i><br />
 int <code>globus_gram_protocol_pack_job_request</code> (int job_state_mask, const char *callback_url, const char *rsl, globus_byte_t **query, globus_size_t *querysize)<br />
 <i>Pack a GRAM Job Request. </i><br />
 int <code>globus_gram_protocol_unpack_job_request</code> (const globus_byte_t *query, globus_size_t querysize, int *job_state_mask, char **callback_url, char **description)<br />
 <i>Unpack a GRAM Job Request. </i><br />
 int <code>globus_gram_protocol_pack_job_request_reply</code> (int status, const char *job_contact, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM reply message. </i><br />
 int <code>globus_gram_protocol_unpack_job_request_reply</code> (const globus_byte_t *reply, globus_size_t replysize, int *status, char **job_contact)<br />
 <i>Unpack a GRAM reply message. </i><br />
 int <code>globus_gram_protocol_pack_job_request_reply_with_extensions</code> (int status, const char *job_contact, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM reply message with extension attributes. </i><br />
 int <code>globus_gram_protocol_unpack_job_request_reply_with_extensions</code> (const globus_byte_t *reply, globus_size_t replysize, int *status, char **job_contact, globus_hashtable_t *extensions)<br />
 <i>Unpack a GRAM reply message, parsing all extensions. </i><br />
 int <code>globus_gram_protocol_pack_status_request</code> (const char *status_request, globus_byte_t **query, globus_size_t *querysize)<br />
 <i>Pack a GRAM query message. </i><br />
 int <code>globus_gram_protocol_unpack_status_request</code> (const globus_byte_t *query, globus_size_t querysize, char **status_requst)<br />
 <i>Unpack a GRAM query message. </i><br />
 int <code>globus_gram_protocol_pack_status_reply</code> (int job_status, int failure_code, int job_failure_code, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM query reply message. </i><br />
 int <code>globus_gram_protocol_pack_status_reply_with_extensions</code> (int job_status, int failure_code, int job_failure_code, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM query reply message with extensions. </i><br />
 int <code>globus_gram_protocol_unpack_status_reply</code> (const globus_byte_t *reply, globus_size_t replysize, int *job_status, int *failure_code, int *job_failure_code)<br />
 <i>Unpack a GRAM query reply. </i><br />
 int <code>globus_gram_protocol_unpack_status_reply_with_extensions</code> (const globus_byte_t *reply, globus_size_t replysize, globus_hashtable_t *extensions)<br />
 <i>Unpack a GRAM query reply with extensions. </i><br />
 int <code>globus_gram_protocol_pack_status_update_message</code> (char *job_contact, int status, int failure_code, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM status update message. </i><br />
 int <code>globus_gram_protocol_unpack_status_update_message</code> (const globus_byte_t *reply, globus_size_t replysize, char **job_contact, int *status, int *failure_code)<br />
 <i>Unpack a GRAM status update message. </i><br />
 int <code>globus_gram_protocol_pack_status_update_message_with_extensions</code> (char *job_contact, int status, int failure_code, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM status update message with extensions. </i><br />
 int <code>globus_gram_protocol_unpack_status_update_message_with_extensions</code> (const globus_byte_t *reply, globus_size_t replysize, globus_hashtable_t *message_hash)<br />
 <i>Unpack a GRAM status update message with extensions. </i><br />
 int <code>globus_gram_protocol_pack_version_request</code> (char **request, size_t *requestsize)<br />
 <i>Pack a GRAM version request message. </i><br />
 void <code>globus_gram_protocol_hash_destroy</code> (globus_hashtable_t *message_hash) </p>
<p> <code>globus_gram_protocol_extension_t</code> * <code>globus_gram_protocol_create_extension</code> (const char *attribute, const char *format,&#8230;) </p>
<p> int <code>globus_gram_protocol_get_sec_context</code> (<code>globus_gram_protocol_handle_t</code> handle, gss_ctx_id_t *context)<br />
 <i>Get a reference to the GSSAPI security context associated with a GRAM protocol handle. </i><br />
 const char * <code>globus_gram_protocol_error_string</code> (int error_code)<br />
 <i>Get a description of a a GRAM error code. </i><br />
 void <code>globus_gram_protocol_error_7_hack_replace_message</code> (const char *message)<br />
 <i>Replace the error message associated with error 7 with a custom message. </i><br />
 void <code>globus_gram_protocol_error_10_hack_replace_message</code> (const char *message)<br />
 <i>Replace the error message associated with error 10 with a custom message. </i></p>
<h2>Detailed Description</h2>
<p>GRAM Protocol API. </p>
<h2>Function Documentation</h2>
<h3><code>globus_gram_protocol_extension_t</code>* globus_gram_protocol_create_extension (const char *attribute, const char *format, &#8230;)</h3>
<p>Create a GRAM5 protocol extension entry </p>
<p> Allocates a new GRAM5 protocol extension entry containing an attribute-value pair. The <i>attribute</i> parameter is copied into the extension, and the <i>format</i> parameter is a printf-style format string used to construct the value of the extension. </p>
<p> The caller is responsible for freeing the extension when done with it. The quoting rules described in <code>GRAM Protocol</code> must be implemented by the caller in the format string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Name of the extension attribute<br />
 <i>format</i> Printf-style format string used along with the varargs to construct the extension&#8217;s value string.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>A</i> new GRAM5 extension structure, or NULL if a malloc error occurred.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gram_protocol from the source code.</p>
