---
title: "globus_gss_assist_wrap_send(3)"
name: "globus_gss_assist_wrap_send"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_wrap_send/"
description: "globus_gss_assist.h – GSS Assist Header."
---

<h2 class="name">NAME</h2>
<p> globus_gss_assist.h &#8211; GSS Assist Header.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;gssapi.h&#8217;<br />
 #include &lt;stdio.h&gt;<br />
 #include &lt;stdlib.h&gt;<br />
 #include &#8216;globus_gss_assist_constants.h&#8217; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GSI_GSS_ASSIST_MODULE</code> </p>
<p> #define <code>GlobusGssAssistFreeDNArray</code>(dn_a)<br />
 <i>Free array of distinguished names. </i></p>
<h3>Functions</h3>
<p> int <code>globus_gss_assist_token_get_fd</code> (void *arg, void **bufp, size_t *sizep)<br />
 <i>Get token from a FILE *. </i><br />
 int <code>globus_gss_assist_token_send_fd</code> (void *arg, void *buf, size_t size)<br />
 <i>Send token via a FILE *. </i><br />
 int <code>globus_gss_assist_token_send_fd_ex</code> (void *arg, void *buf, size_t size)<br />
 <i>Send a token to a FILE *. </i><br />
 int <code>globus_gss_assist_token_send_fd_without_length</code> (void *arg, void *buf, size_t size)<br />
 <i>Send token to a FILE *. </i><br />
 OM_uint32 <code>globus_gss_assist_acquire_cred</code> (OM_uint32 *, gss_cred_usage_t, gss_cred_id_t *) </p>
<p> OM_uint32 <code>globus_gss_assist_acquire_cred_ext</code> (OM_uint32 *, char *, OM_uint32, const gss_OID_set, gss_cred_usage_t, gss_cred_id_t *, gss_OID_set *, OM_uint32 *) </p>
<p> OM_uint32 <code>globus_gss_assist_accept_sec_context</code> (OM_uint32 *, gss_ctx_id_t *, const gss_cred_id_t, char **, OM_uint32 *, int *, int *, gss_cred_id_t *, int(*get_token)(void *, void **, size_t *), void *get_context, int(*send_token)(void *, void *, size_t), void *send_context)<br />
 <i>Accept a Security Context. </i><br />
 OM_uint32 <code>globus_gss_assist_accept_sec_context_async</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_t cred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, void *input_buffer, size_t input_buffer_len, void **output_bufferp, size_t *output_buffer_lenp, gss_cred_id_t *delegated_cred_handle)<br />
 <i>Accept a Security Context Without Blocking. </i><br />
 OM_uint32 <code>globus_gss_assist_init_sec_context</code> (OM_uint32 *, const gss_cred_id_t, gss_ctx_id_t *, char *, OM_uint32, OM_uint32 *, int *, int(*get_token)(void *, void **, size_t *), void *get_arg, int(*send_token)(void *, void *, size_t), void *send_arg) </p>
<p> OM_uint32 <code>globus_gss_assist_init_sec_context_async</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32 req_flags, OM_uint32 *ret_flags, void *input_buffer, size_t input_buffer_len, void **output_bufferp, size_t *output_buffer_lenp) </p>
<p> OM_uint32 <code>globus_gss_assist_display_status</code> (FILE *, char *, OM_uint32, OM_uint32, int) </p>
<p> OM_uint32 <code>globus_gss_assist_display_status_str</code> (char **, char *, OM_uint32, OM_uint32, int) </p>
<p> OM_uint32 <code>globus_gss_assist_wrap_send</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, char *data, size_t length, int *token_status, int(*gss_assist_send_token)(void *, void *, size_t), void *gss_assist_send_context, FILE *fperr)<br />
 <i>Wrap. </i><br />
 OM_uint32 <code>globus_gss_assist_get_unwrap</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, char **data, size_t *length, int *token_status, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, FILE *fperr)<br />
 <i>Get Unwrap. </i><br />
 OM_uint32 <code>globus_gss_assist_will_handle_restrictions</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle) </p>
<p> OM_uint32 <code>globus_gss_assist_export_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, int fdp, FILE *fperr) </p>
<p> OM_uint32 <code>globus_gss_assist_import_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, int fdp, FILE *fperr) </p>
<p> globus_result_t <code>globus_gss_assist_authorization_host_name</code> (char *hostname, gss_name_t *authorization_hostname) </p>
<p> int <code>globus_gss_assist_gridmap</code> (char *globusidp, char **useridp)<br />
 <i>Look up the default mapping for a Grid identity in a gridmap file. </i><br />
 int <code>globus_gss_assist_userok</code> (char *globusid, char *userid)<br />
 <i>Gridmap entry existence check. </i><br />
 int <code>globus_gss_assist_map_local_user</code> (char *local_user, char **globusidp)<br />
 <i>Look up the default Grid identity associated with a local user name. </i><br />
 globus_result_t <code>globus_gss_assist_lookup_all_globusid</code> (char *username, char **dns[], int *dn_count)<br />
 <i>Look up all Grid IDs associated with a local user ID. </i><br />
 globus_result_t <code>globus_gss_assist_map_and_authorize</code> (gss_ctx_id_t context, char *service, char *desired_identity, char *identity_buffer, unsigned int identity_buffer_length)<br />
 <i>Authorize the peer of a security context to use a service. </i><br />
 globus_result_t <code>globus_gss_assist_map_and_authorize_sharing</code> (char *shared_user_certificate, gss_ctx_id_t context, char *desired_identity, char *identity_buffer, unsigned int identity_buffer_length)<br />
 <i>Authorize a particular credential for shared access. </i></p>
<h2>Detailed Description</h2>
<p> GSS Assist Header. </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gss_assist_authorization_host_name (char *hostname, gss_name_t *authorization_hostname)</h3>
<p> Create a GSS Name structure from the given hostname. This function tries to resolve the given host name string to the canonical DNS name for the host. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>hostname</i> The host name or numerical address to be resolved and transform into a GSS Name<br />
 <i>authorization_hostname</i> The resulting GSS Name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS on successful completion, a error object otherwise</dl>
<h3>OM_uint32 globus_gss_assist_wrap_send (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, char *data, size_tlength, int *token_status, int(*)(void *, void *, size_t)gss_assist_send_token, void *gss_assist_send_context, FILE *fperr)</h3>
<p> Wrap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. If the call was successful, the minor status is equal to GLOBUS_SUCCESS. Otherwise, it is an error object ID for which globus_error_get() and globus_object_free() can be used to get and destroy it.<br />
 <i>context_handle</i> the context.<br />
 <i>data</i> pointer to application data to wrap and send<br />
 <i>length</i> length of the <i>data</i> array<br />
 <i>token_status</i> assist routine get/send token status<br />
 <i>gss_assist_send_token</i> a send_token routine<br />
 <i>gss_assist_send_context</i> first arg for the send_token<br />
 <i>fperr</i> file handle to write error message to.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on success Other GSSAPI errors on failure.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> gss_wrap()</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
