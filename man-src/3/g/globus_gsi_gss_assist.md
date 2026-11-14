---
title: "globus_gsi_gss_assist(3)"
name: "globus_gsi_gss_assist"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gss_assist/"
description: "Utility Functions –"
---

<h2 class="name">NAME</h2>
<p> Utility Functions &#8211; </p>
<p> Utility functions for GSSAPI.</p>
<h3>Defines</h3>
<p> #define <code>GlobusGssAssistFreeDNArray</code>(dn_a) </p>
<p> #define <code>NI_MAXHOST</code> 255 </p>
<h3>Functions</h3>
<p> int <code>globus_gss_assist_gridmap</code> (char *globusidp, char **useridp) </p>
<p> int <code>globus_gss_assist_userok</code> (char *globusid, char *userid) </p>
<p> int <code>globus_gss_assist_map_local_user</code> (char *local_user, char **globusidp) </p>
<p> globus_result_t <code>globus_gss_assist_lookup_all_globusid</code> (char *username, char **dns[], int *dn_count) </p>
<p> globus_result_t <code>globus_gss_assist_map_and_authorize</code> (gss_ctx_id_t context, char *service, char *desired_identity, char *identity_buffer, unsigned int identity_buffer_length) </p>
<h3>Accept Security Context</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_accept_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_t cred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, int *token_status, gss_cred_id_t *delegated_cred_handle, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, int(*gss_assist_send_token)(void *, void *, size_t), void *gss_assist_send_context) </p>
<h3>Accept Security Context Asyncronous</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_accept_sec_context_async</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_cred_id_t cred_handle, char **src_name_char, OM_uint32 *ret_flags, int *user_to_user_flag, void *input_buffer, size_t input_buffer_len, void **output_bufferp, size_t *output_buffer_lenp, gss_cred_id_t *delegated_cred_handle) </p>
<h3>Acquire Credential</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_acquire_cred</code> (OM_uint32 *minor_status, gss_cred_usage_t cred_usage, gss_cred_id_t *output_cred_handle) </p>
<h3>Acquire Credential Extension</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_acquire_cred_ext</code> (OM_uint32 *minor_status, char *desired_name_char, OM_uint32 time_req, const gss_OID_set desired_mechs, gss_cred_usage_t cred_usage, gss_cred_id_t *output_cred_handle, gss_OID_set *actual_mechs, OM_uint32 *time_rec) </p>
<h3>Display Status</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_display_status</code> (FILE *fp, char *comment, OM_uint32 major_status, OM_uint32 minor_status, int token_status) </p>
<h3>Display Status String</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_display_status_str</code> (char **str, char *comment, OM_uint32 major_status, OM_uint32 minor_status, int token_status) </p>
<p> OM_uint32 <code>globus_gss_assist_import_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, int *token_status, int fdp, FILE *fperr) </p>
<h3>Init Security Context</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_init_sec_context</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32 req_flags, OM_uint32 *ret_flags, int *token_status, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, int(*gss_assist_send_token)(void *, void *, size_t), void *gss_assist_send_context) </p>
<h3>Init Security Context Async</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_init_sec_context_async</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t *context_handle, char *target_name_char, OM_uint32 req_flags, OM_uint32 *ret_flags, void *input_buffer, size_t input_buffer_len, void **output_bufferp, size_t *output_buffer_lenp) </p>
<h3>Will Handle Restrictions</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_will_handle_restrictions</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle) </p>
<h3>Get Unwrap</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_get_unwrap</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, char **data, size_t *length, int *token_status, int(*gss_assist_get_token)(void *, void **, size_t *), void *gss_assist_get_context, FILE *fperr) </p>
<h3>Wrap</h3>
<p>&nbsp;<wbr><br />
 OM_uint32 <code>globus_gss_assist_wrap_send</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, char *data, size_t length, int *token_status, int(*gss_assist_send_token)(void *, void *, size_t), void *gss_assist_send_context, FILE *fperr) </p>
<h2>Detailed Description</h2>
<p> Utility functions for GSSAPI.</p>
<h2>Define Documentation</h2>
<h3>#define GlobusGssAssistFreeDNArray(dn_a)</h3>
<p> Free array of distinguished names. Free the contents of a name array created during a successful call to <code>globus_gss_assist_lookup_all_globusid()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dn_a</i> Array of names to free.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>void</i></dl>
<h3>#define NI_MAXHOST 255</h3>
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
<h2>Function Documentation</h2>
<h3>OM_uint32 globus_gss_assist_accept_sec_context (OM_uint32 * minor_status, gss_ctx_id_t * context_handle, const gss_cred_id_t cred_handle, char ** src_name_char, OM_uint32 * ret_flags, int * user_to_user_flag, int * token_status, gss_cred_id_t * delegated_cred_handle, int(*)(void *, void **, size_t *) gss_assist_get_token, void * gss_assist_get_context, int(*)(void *, void *, size_t) gss_assist_send_token, void * gss_assist_send_context)</h3>
<p> This routine accepts a GSSAPI security context and is called by the gram_gatekeeper. It isolates the GSSAPI from the rest of the gram code. </p>
<p> Initialize a gssapi security connection. Used by the server. The context_handle is returned, and there is one for each connection. This routine will take cake of the looping and token processing, using the supplied get_token and send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> gssapi return code<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>src_name_char</i> Pointer to char string repersentation of the client which contacted the server. Maybe NULL if not wanted. Should be freed when done.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted. We will also use this to pass in flags to the globus version of gssapi_ssleay<br />
 <i>user_to_user_flag</i> Pointer to flag to be set if the src_name is the same as our name. (Follwing are particular to this assist routine)<br />
 <i>token_status</i> assist routine get/send token status<br />
 <i>delegated_cred_handle</i> pointer to be set to the credential delegated by the client if delegation occurs during the security handshake<br />
 <i>gss_assist_get_token</i> a get token routine<br />
 <i>gss_assist_get_context</i> first arg for the get token routine<br />
 <i>gss_assist_send_token</i> a send token routine<br />
 <i>gss_assist_send_context</i> first arg for the send token routine</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on sucess Other gss errors on failure.</dl>
<h3>OM_uint32 globus_gss_assist_accept_sec_context_async (OM_uint32 * minor_status, gss_ctx_id_t * context_handle, const gss_cred_id_t cred_handle, char ** src_name_char, OM_uint32 * ret_flags, int * user_to_user_flag, void * input_buffer, size_t input_buffer_len, void ** output_bufferp, size_t * output_buffer_lenp, gss_cred_id_t * delegated_cred_handle)</h3>
<p> This is a asynchronous version of the <code>globus_gss_assist_accept_sec_context()</code> function. Instead of looping itself it passes in and out the read and written buffers and the calling application is responsible for doing the I/O directly. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> gssapi return code<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>src_name_char</i> Pointer to char string repersentation of the client which contacted the server. Maybe NULL if not wanted. Should be freed when done.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted. We will also use this to pass in flags to the globus version of gssapi_ssleay<br />
 <i>user_to_user_flag</i> Pointer to flag to be set if the src_name is the same as our name.<br />
 <i>input_buffer</i> pointer to a buffer received from peer.<br />
 <i>input_buffer_len</i> length of the buffer input_buffer.<br />
 <i>output_bufferp</i> pointer to a pointer which will be filled in with a pointer to a allocated block of memory. If non-NULL the contents of this block should be written to the peer where they will be fed into the gss_assist_init_sec_context_async() function.<br />
 <i>output_buffer_lenp</i> pointer to an integer which will be filled in with the length of the allocated output buffer pointed to by *output_bufferp.<br />
 <i>delegated_cred_handle</i> pointer to be set to the credential delegated by the client if delegation occurs during the security handshake</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on successful completion when this function does not need to be called again.</dl>
<p> GSS_S_CONTINUE_NEEDED when *output_bufferp should be sent to the peer and a new input_buffer read and this function called again. </p>
<p> Other gss errors on failure.</p>
<h3>OM_uint32 globus_gss_assist_acquire_cred (OM_uint32 * minor_status, gss_cred_usage_t cred_usage, gss_cred_id_t * output_cred_handle)</h3>
<p> Called once at the start of the process, to obtain the credentials the process is running under. The </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> pointer for return code<br />
 <i>cred_usage</i> GSS_C_INITIATE, GSS_C_ACCEPT, or GSS_C_BOTH<br />
 <i>output_cred_handle</i> Pointer to the returned handle. This needs to be passed to many gss routines.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on sucess Other GSS return codes</dl>
<h3>OM_uint32 globus_gss_assist_acquire_cred_ext (OM_uint32 * minor_status, char * desired_name_char, OM_uint32 time_req, const gss_OID_set desired_mechs, gss_cred_usage_t cred_usage, gss_cred_id_t * output_cred_handle, gss_OID_set * actual_mechs, OM_uint32 * time_rec)</h3>
<p> Called once at the start of the process, to obtain the credentials the process is running under. All the parameters of the gss_acquire_cred, except the desired_name is a string of the form: [type:]name. This will be imported with the type. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on sucess Other GSS return codes</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> globus_gsi_gss_acquire_cred</dl>
<h3>OM_uint32 globus_gss_assist_display_status (FILE * fp, char * comment, OM_uint32 major_status, OM_uint32 minor_status, int token_status)</h3>
<p> Display the messages for the major and minor status on the file pointed at by fp. Takes care of the overloaded major_status if there was a problem with the get_token or send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>fp</i> a file pointer<br />
 <i>comment</i> String to print out before other error messages.<br />
 <i>major_status</i> The major status to display<br />
 <i>minor_status</i> The minor status to display<br />
 <i>token_status</i> token status to display</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0</dl>
<h3>OM_uint32 globus_gss_assist_display_status_str (char ** str, char * comment, OM_uint32 major_status, OM_uint32 minor_status, int token_status)</h3>
<p> Display the messages for the major and minor status and return a string with the messages. Takes care of the overloaded major_status if there was a problem with the get_token or send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>str</i> pointer to char * for returned string. Must be freed<br />
 <i>comment</i> String to print out before other error messages.<br />
 <i>major_status</i> The major status to display<br />
 <i>minor_status</i> The minor status to display<br />
 <i>token_status</i> token status to display</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0</dl>
<h3>int globus_gss_assist_gridmap (char * globusidp, char ** useridp)</h3>
<p> Look up the default mapping for a Grid identity in a gridmap file. The <code>globus_gss_assist_gridmap()</code> function parses the default gridmap file and modifies its <i>useridp</i> parameter to point to a copy of the string containing the default local identity that the grid identity is mapped to. If successful, the caller is responsible for freeing the string pointed to by <i>useridp</i>. </p>
<p> By default, <i></i><code>globus_gss_assist_gridmap()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globusidp</i> The GSSAPI name string of the identity who requested authorization<br />
 <i>useridp</i> A pointer to a string to be set to the default user ID for the local system. No validation is done to check that such a user exists.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_gss_assist_gridmap()</code> returns 0 and modifies the the string pointed to by the <i>useridp</i> parameter. If an error occurs, a non-zero value is returned and the value pointed to by <i>useridp</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>1</i> Error</dl>
<h3>int globus_gss_assist_userok (char * globusid, char * userid)</h3>
<p> Gridmap entry existence check. The <i></i><code>globus_gss_assist_userok()</code> function parses the default gridmap file and checks whether any mapping exists for the grid identity passed as the <i>globusid</i> parameter and the local user identity passed as the @ userid parameter. </p>
<p> By default, <i></i><code>globus_gss_assist_userok()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globusid</i> The GSSAPI name string of the identity who requested authorization<br />
 <i>userid</i> The local account name that access is sought for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> If <i></i><code>globus_gss_assist_userok()</code> is able to find a mapping between <i>globusid</i> and <i>userid</i>, it returns 0; otherwise it returns 1.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>1</i> Error</dl>
<h3>int globus_gss_assist_map_local_user (char * local_user, char ** globusidp)</h3>
<p> Look up the default Grid identity associated with a local user name. The <i></i><code>globus_gss_assist_map_local_user()</code> function parses the gridmap file to determine a if the user name passed as the <i>local_user</i> parameter is the default local user for a Grid ID in the gridmap file. If so, it modifies <i>globusidp</i> to point to a copy of that ID. Otherwise, it searches the gridmap file for a Grid ID that has a non-default mapping for <i>local_user</i> and modifies <i>globusidp</i> to point to a copy of that ID. If successful, the caller is responsible for freeing the string pointed to by the <i>globusidp</i> pointer. </p>
<p> By default, <i></i><code>globus_gss_assist_map_local_user()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>local_user</i> The local username to find a Grid ID for<br />
 <i>globusidp</i> A Grid ID that maps from the local_user.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <i></i><code>globus_gss_assist_map_local_user()</code> returns 0 and modifies <i>globusidp</i> to point to a Grid ID that maps to <i>local_user</i>; otherwise, <i></i><code>globus_gss_assist_map_local_user()</code> returns 1 and the value pointed to by <i>globusidp</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>1</i> Error</dl>
<h3>globus_result_t globus_gss_assist_lookup_all_globusid (char * username, char ** dns[], int * dn_count)</h3>
<p> Look up all Grid IDs associated with a local user ID. The <i></i><code>globus_gss_assist_lookup_all_globusid()</code> function parses a gridmap file and finds all Grid IDs that map to a local user ID. The <i>dns</i> parameter is modified to point to an array of Grid ID strings from the gridmap file, and the <i>dn_count</i> parameter is modified to point to the number of Grid ID strings in the array. The caller is responsible for freeing the array using the macro <i></i><code>GlobusGssAssistFreeDNArray()</code>. </p>
<p> By default, <i></i><code>globus_gss_assist_lookup_all_globusid()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>username</i> The local username to look up in the gridmap file.<br />
 <i>dns</i> A pointer to an array of strings. This function modifies this to point to a newly allocated array of strings. The caller must use the macro <i></i><code>GlobusGssAssistFreeDNArray()</code> to free this memory.<br />
 <i>dn_count</i> A pointer to an integer that is modified to contain the number of entries in the array returned via the <i>dns</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <i></i><code>globus_gss_assist_lookup_all_globusid()</code> returns GLOBUS_SUCCESS and modifies its <i>dns</i> and <i>dn_count</i> parameters as described above. If an error occurs, <i></i><code>globus_gss_assist_lookup_all_globusid()</code> returns a globus_result_t that can be resolved to an error object and the values pointed to by <i>dns</i> and <i>dn_count</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_ARGUMENTS</i> Error with arguments<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_GRIDMAP</i> Invalid path to gridmap<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_ERRNO</i> System error</dl>
<h3>globus_result_t globus_gss_assist_map_and_authorize (gss_ctx_id_t context, char * service, char * desired_identity, char * identity_buffer, unsigned int identity_buffer_length)</h3>
<p> Authorize the peer of a security context to use a service. The <code>globus_gss_assist_map_and_authorize()</code> function attempts to authorize the peer of a security context to use a particular service. If the <i>desired_identity</i> parameter is non-NULL, the authorization will succeed only if the peer is authorized for that identity. Otherwise, any valid authorized local user name will be used. If authorized, the local user name will be copied to the string pointed to by the <i>identity_buffer</i> parameter, which must be at least as long as the value passed as the <i>identity_buffer_length</i> parameter. </p>
<p> If authorization callouts are defined in the callout configuration file, <i></i><code>globus_gss_assist_map_and_authorize()</code> will invoke both the GLOBUS_GENERIC_MAPPING_TYPE callout and the GLOBUS_GENERIC_AUTHZ_TYPE callout; otherwise the default gridmap file will be used for mapping and no service-specific authorization will be done. </p>
<p> If <i></i><code>globus_gss_assist_map_and_authorize()</code> uses a gridmap file, it first looks for a file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Security context to inspect for peer identity information.<br />
 <i>service</i> A NULL-terminated string containing the name of the service that an authorization decision is being made for.<br />
 <i>desired_identity</i> Optional. If non-NULL, perform an authorization to act as the local user named by this NULL-terminated string.<br />
 <i>identity_buffer</i> A pointer to a string buffer into which will be copied the local user name that the peer of the context is authorized to act as.<br />
 <i>identity_buffer_length</i> Length of the <i>identity_buffer</i> array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <i></i><code>globus_gss_assist_map_and_authorize()</code> returns GLOBUS_SUCCESS and copies the authorized local identity to the <i>identity_buffer</i> parameter. If an error occurs, <i></i><code>globus_gss_assist_map_and_authorize()</code> returns a globus_result_t that can be resolved to an error object.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_CALLOUT_CONFIG</i> Invalid authorization configuration file<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE</i> Hash table operation failed.<br />
 <i>GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR</i> The callout itself returned a error.<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_DL</i> Dynamic library operation failed.<br />
 <i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</i> Out of memory<br />
 <i>GLOBUS_GSI_GSS_ASSIST_GSSAPI_ERROR</i> A GSSAPI function returned an error<br />
 <i>GLOBUS_GSI_GSS_ASSIST_GRIDMAP_LOOKUP_FAILED</i> Gridmap lookup failure<br />
 <i>GLOBUS_GSI_GSS_ASSIST_BUFFER_TOO_SMALL</i> Caller provided insufficient buffer space for local identity</dl>
<h3>OM_uint32 globus_gss_assist_import_sec_context (OM_uint32 * minor_status, gss_ctx_id_t * context_handle, int * token_status, int fdp, FILE * fperr)</h3>
<p> Import the security context from a file. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. This is a Globus Error code (or GLOBUS_SUCCESS) cast to a OM_uint32 pointer. If an erro has occurred, the resulting error (from calling globus_error_get on this variable) needs to be freed by the caller<br />
 <i>context_handle</i> The imported context<br />
 <i>token_status</i> Errors that occurred while reading from the file<br />
 <i>fdp</i> the file descriptor pointing to a file containing the security context<br />
 <i>fperr</i> FILE * to write error messages</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the major status</dl>
<h3>OM_uint32 globus_gss_assist_init_sec_context (OM_uint32 * minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t * context_handle, char * target_name_char, OM_uint32 req_flags, OM_uint32 * ret_flags, int * token_status, int(*)(void *, void **, size_t *) gss_assist_get_token, void * gss_assist_get_context, int(*)(void *, void *, size_t) gss_assist_send_token, void * gss_assist_send_context)</h3>
<p> Initialize a gssapi security connection. Used by the client. The context_handle is returned, and there is one for each connection. This routine will take cake of the looping and token processing, using the supplied get_token and send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. The new minor_status is a globus_result_t cast to an OM_uint32. If the call was successful, the minor status is equivalant to GLOBUS_SUCCESS. Otherwise, it is a globus error object ID that can be passed to globus_error_get to get the error object. The error object needs to be freed with globus_object_free.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>target_name_char</i> char string repersentation of the server to be contacted.<br />
 <i>req_flags</i> request flags, such as GSS_C_DELEG_FLAG for delegation and the GSS_C_MUTUAL_FLAG for mutual authentication.<br />
 <i>ret_flags</i> Pointer to which services are available after the connection is established. Maybe NULL if not wanted.</dl>
<p> The Follwing are particular to this assist routine: </p>
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
<h3>OM_uint32 globus_gss_assist_init_sec_context_async (OM_uint32 * minor_status, const gss_cred_id_t cred_handle, gss_ctx_id_t * context_handle, char * target_name_char, OM_uint32 req_flags, OM_uint32 * ret_flags, void * input_buffer, size_t input_buffer_len, void ** output_bufferp, size_t * output_buffer_lenp)</h3>
<p> This is a asynchronous version of the <code>globus_gss_assist_init_sec_context()</code> function. Instead of looping itself it passes in and out the read and written buffers and the calling application is responsible for doing the I/O directly. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code. The new minor status is a globus_result_t cast to a OM_uint32. If an error occurred (GSS_ERROR(major_status)) the minor_status is a globus error object id. The error object can be obtained via globus_error_get and should be destroyed with globus_object_free when no longer needed. If no error occurred, the minor status is equal to GLOBUS_SUCCESS.<br />
 <i>cred_handle</i> the cred handle obtained by acquire_cred.<br />
 <i>context_handle</i> pointer to returned context.<br />
 <i>target_name_char</i> char string repersentation of the server to be contacted.<br />
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
<h3>OM_uint32 globus_gss_assist_will_handle_restrictions (OM_uint32 * minor_status, gss_ctx_id_t * context_handle)</h3>
<p> Sets the context to handle restrictions. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> the resulting minor status from setting the context handle<br />
 <i>context_handle</i> the context handle to set the minor status of</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the major status from setting the context</dl>
<h3>OM_uint32 globus_gss_assist_get_unwrap (OM_uint32 * minor_status, const gss_ctx_id_t context_handle, char ** data, size_t * length, int * token_status, int(*)(void *, void **, size_t *) gss_assist_get_token, void * gss_assist_get_context, FILE * fperr)</h3>
<p> Gets a token using the specific tokenizing functions, and performs the GSS unwrap of that token. <code>See also:</code></p>
<dl>
<dt>
<dd> gss_unwrap</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> GSSAPI return code,</dl>
<p> <code>See also:</code></p>
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
<h3>OM_uint32 globus_gss_assist_wrap_send (OM_uint32 * minor_status, const gss_ctx_id_t context_handle, char * data, size_t length, int * token_status, int(*)(void *, void *, size_t) gss_assist_send_token, void * gss_assist_send_context, FILE * fperr)<code>Parameters:</code></h3>
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
<dd> GSS_S_COMPLETE on sucess Other gss errors on failure.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> gss_wrap()</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus gss assist from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBL">Author</a></p>
<dd></dl>
