---
title: "globus_gss_assist_import_sec_context(3)"
name: "globus_gss_assist_import_sec_context"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_import_sec_context/"
description: "Security Context Management –"
---

<h2 class="name">NAME</h2>
<p> Security Context Management &#8211; </p>
<p> Security Context Creation and Use.</p>
<h3>Functions</h3>
<p> OM_uint32 <code>globus_gss_assist_accept_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_t cred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, int *token_status, gss_cred_id_t *delegated_cred_handle, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, int(*gss_assist_send_token)(void *, void *, size_t), void *gss_assist_send_context)<br />
 <i>Accept a Security Context. </i><br />
 OM_uint32 <code>globus_gss_assist_accept_sec_context_async</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_t cred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, void *input_buffer, size_t input_buffer_len, void **output_bufferp, size_t *output_buffer_lenp, gss_cred_id_t *delegated_cred_handle)<br />
 <i>Accept a Security Context Without Blocking. </i><br />
 OM_uint32 <code>globus_gss_assist_export_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, int fdp, FILE *fperr) </p>
<p> OM_uint32 <code>globus_gss_assist_import_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, int fdp, FILE *fperr) </p>
<p> OM_uint32 <code>globus_gss_assist_init_sec_context</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32 req_flags, OM_uint32 *ret_flags, int *token_status, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, int(*gss_assist_send_token)(void *, void *, size_t), void *gss_assist_send_context) </p>
<p> OM_uint32 <code>globus_gss_assist_init_sec_context_async</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32 req_flags, OM_uint32 *ret_flags, void *input_buffer, size_t input_buffer_len, void **output_bufferp, size_t *output_buffer_lenp) </p>
<p> OM_uint32 <code>globus_gss_assist_will_handle_restrictions</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle) </p>
<p> OM_uint32 <code>globus_gss_assist_get_unwrap</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, char **data, size_t *length, int *token_status, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, FILE *fperr)<br />
 <i>Get Unwrap. </i></p>
<h2>Detailed Description</h2>
<p> Security Context Creation and Use. </p>
<p> The functions in this section are used to create security contexts and send and receive messages sent over them. They use the functions provided by <code>Token Transport</code> or user-supplied functions to communicate security tokens over the context, looping over continue results from the GSSAPI as needed.</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 globus_gss_assist_accept_sec_context (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_tcred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, int *token_status, gss_cred_id_t *delegated_cred_handle, int(*)(void *, void **, size_t *)gss_assist_get_token, void *gss_assist_get_context, int(*)(void *, void *, size_t)gss_assist_send_token, void *gss_assist_send_context)</h3>
<p> Accept a Security Context. This routine accepts a GSSAPI security context and is called by the gram_gatekeeper. It isolates the GSSAPI from the rest of the gram code. </p>
<p> Initialize a GSSAPI security connection. Used by the server. The context_handle is returned, and there is one for each connection. This routine will take cake of the looping and token processing, using the supplied get_token and send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>src_name_char</i> Pointer to char string representation of the client which contacted the server. Maybe NULL if not wanted. Should be freed when done.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted. We will also use this to pass in flags to the globus version of GSSAPI<br />
 <i>user_to_user_flag</i> Pointer to flag to be set if the src_name is the same as our name. (Following are particular to this assist routine)<br />
 <i>token_status</i> assist routine get/send token status<br />
 <i>delegated_cred_handle</i> pointer to be set to the credential delegated by the client if delegation occurs during the security handshake<br />
 <i>gss_assist_get_token</i> a get token routine<br />
 <i>gss_assist_get_context</i> first arg for the get token routine<br />
 <i>gss_assist_send_token</i> a send token routine<br />
 <i>gss_assist_send_context</i> first arg for the send token routine</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on success Other GSSAPI errors on failure.</dl>
<h3>OM_uint32 globus_gss_assist_accept_sec_context_async (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_tcred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, void *input_buffer, size_tinput_buffer_len, void **output_bufferp, size_t *output_buffer_lenp, gss_cred_id_t *delegated_cred_handle)</h3>
<p> Accept a Security Context Without Blocking. This is a asynchronous version of the <code>globus_gss_assist_accept_sec_context()</code> function. Instead of looping itself it passes in and out the read and written buffers and the calling application is responsible for doing the I/O directly. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>src_name_char</i> Pointer to char string representation of the client which contacted the server. Maybe NULL if not wanted. Should be freed when done.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted. We will also use this to pass in flags to the Globus version of GSSAPI<br />
 <i>user_to_user_flag</i> Pointer to flag to be set if the src_name is the same as our name.<br />
 <i>input_buffer</i> pointer to a buffer received from peer.<br />
 <i>input_buffer_len</i> length of the buffer input_buffer.<br />
 <i>output_bufferp</i> pointer to a pointer which will be filled in with a pointer to a allocated block of memory. If non-NULL the contents of this block should be written to the peer where they will be fed into the <code>globus_gss_assist_init_sec_context_async()</code> function.<br />
 <i>output_buffer_lenp</i> pointer to an integer which will be filled in with the length of the allocated output buffer pointed to by *output_bufferp.<br />
 <i>delegated_cred_handle</i> pointer to be set to the credential delegated by the client if delegation occurs during the security handshake</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on successful completion when this function does not need to be called again.</dl>
<p> GSS_S_CONTINUE_NEEDED when *output_bufferp should be sent to the peer and a new input_buffer read and this function called again. </p>
<p> Other GSSAPI errors on failure.</p>
<h3>OM_uint32 globus_gss_assist_export_sec_context (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, intfdp, FILE *fperr)</h3>
<p> Export the security context from a file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. This is a Globus Error code (or GLOBUS_SUCCESS) cast to a OM_uint32 pointer. If an error has occurred, the resulting error (from calling globus_error_get on this variable) needs to be freed by the caller<br />
 <i>context_handle</i> The context to export<br />
 <i>token_status</i> Errors that occurred while reading from the file<br />
 <i>fdp</i> the file descriptor pointing to a file containing the security context<br />
 <i>fperr</i> FILE * to write error messages</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the major status</dl>
<h3>OM_uint32 globus_gss_assist_get_unwrap (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, char **data, size_t *length, int *token_status, int(*)(void *, void **, size_t *)gss_assist_get_token, void *gss_assist_get_context, FILE *fperr)</h3>
<p> Get Unwrap. Gets a token using the specific tokenizing functions, and performs the GSS unwrap of that token </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> gss_unwrap</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code,</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> gss_unwrap</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context_handle</i> the context<br />
 <i>data</i> pointer to be set to the unwrapped application data. This must be freed by the caller.<br />
 <i>length</i> pointer to be set to the length of the <i>data</i> byte array.<br />
 <i>token_status</i> assist routine get/send token status<br />
 <i>gss_assist_get_token</i> a detokenizing routine<br />
 <i>gss_assist_get_context</i> first arg for above routine<br />
 <i>fperr</i> error stream to print to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on sucess Other gss errors on failure.</dl>
<h3>OM_uint32 globus_gss_assist_import_sec_context (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, intfdp, FILE *fperr)</h3>
<p> Import the security context from a file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. This is a Globus Error code (or GLOBUS_SUCCESS) cast to a OM_uint32 pointer. If an error has occurred, the resulting error (from calling globus_error_get on this variable) needs to be freed by the caller<br />
 <i>context_handle</i> The imported context<br />
 <i>token_status</i> Errors that occurred while reading from the file<br />
 <i>fdp</i> the file descriptor pointing to a file containing the security context<br />
 <i>fperr</i> FILE * to write error messages</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the major status</dl>
<h3>OM_uint32 globus_gss_assist_init_sec_context (OM_uint32 *minor_status, const gss_cred_id_tcred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32req_flags, OM_uint32 *ret_flags, int *token_status, int(*)(void *, void **, size_t *)gss_assist_get_token, void *gss_assist_get_context, int(*)(void *, void *, size_t)gss_assist_send_token, void *gss_assist_send_context)</h3>
<p> Initialize a GSSAPI security connection. Used by the client. The context_handle is returned, and there is one for each connection. This routine will take cake of the looping and token processing, using the supplied get_token and send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. The new minor_status is a globus_result_t cast to an OM_uint32. If the call was successful, the minor status is equivalent to GLOBUS_SUCCESS. Otherwise, it is a globus error object ID that can be passed to globus_error_get to get the error object. The error object needs to be freed with globus_object_free.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>target_name_char</i> char string representation of the server to be contacted.<br />
 <i>req_flags</i> request flags, such as GSS_C_DELEG_FLAG for delegation and the GSS_C_MUTUAL_FLAG for mutual authentication.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted.</dl>
<p> The following are particular to this assist routine: </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>token_status</i> the assist routine&#8217;s get/send token status<br />
 <i>gss_assist_get_token</i> function pointer for getting the token<br />
 <i>gss_assist_get_context</i> first argument passed to the gss_assist_get_token function<br />
 <i>gss_assist_send_token</i> function pointer for setting the token<br />
 <i>gss_assist_send_context</i> first argument passed to the gss_assist_set_token function pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The major status</dl>
<h3>OM_uint32 globus_gss_assist_init_sec_context_async (OM_uint32 *minor_status, const gss_cred_id_tcred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32req_flags, OM_uint32 *ret_flags, void *input_buffer, size_tinput_buffer_len, void **output_bufferp, size_t *output_buffer_lenp)</h3>
<p> This is a asynchronous version of the <code>globus_gss_assist_init_sec_context()</code> function. Instead of looping itself it passes in and out the read and written buffers and the calling application is responsible for doing the I/O directly. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. The new minor status is a globus_result_t cast to a OM_uint32. If an error occurred (GSS_ERROR(major_status)) the minor_status is a globus error object id. The error object can be obtained via globus_error_get and should be destroyed with globus_object_free when no longer needed. If no error occurred, the minor status is equal to GLOBUS_SUCCESS.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>target_name_char</i> char string representation of the server to be contacted.<br />
 <i>req_flags</i> request flags, such as GSS_C_DELEG_FLAG for delegation and the GSS_C_MUTUAL_FLAG for mutual authentication.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted.<br />
 <i>input_buffer</i> pointer to a buffer received from peer. Should be NULL on first call.<br />
 <i>input_buffer_len</i> length of the buffer input_buffer. Should be zero on first call.<br />
 <i>output_bufferp</i> pointer to a pointer which will be filled in with a pointer to a allocated block of memory. If non-NULL the contents of this block should be written to the peer where they will be fed into the gss_assist_init_sec_context_async() function.<br />
 <i>output_buffer_lenp</i> pointer to an integer which will be filled in with the length of the allocated output buffer pointed to by *output_bufferp.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on successful completion when this function does not need to be called again.</dl>
<p> GSS_S_CONTINUE_NEEDED when *output_bufferp should be sent to the peer and a new input_buffer read and this function called again. </p>
<p> Other gss errors on failure.</p>
<h3>OM_uint32 globus_gss_assist_will_handle_restrictions (OM_uint32 *minor_status, gss_ctx_id_t *context_handle)</h3>
<p> Sets the context to handle restrictions </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> the resulting minor status from setting the context handle<br />
 <i>context_handle</i> the context handle to set the minor status of</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the major status from setting the context</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
