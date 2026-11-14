---
title: "globus_gsi_gssapi(3)"
name: "globus_gsi_gssapi"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gssapi/"
description: "Globus GSSAPI –"
---

<h2 class="name">NAME</h2>
<p> Globus GSSAPI &#8211; </p>
<p> GSI Implementation Details.</p>
<h3>Modules</h3>
<p> <code>Constants</code><br />
 <i>Implementation-specific Constants. </i><br />
 <code>Activation</code><br />
 <i>Module Activation. </i><br />
 <code>Request Flags</code><br />
 <i>Request Flags. </i><br />
 <code>Return Flags</code><br />
 <i>Return Flags. </i><br />
 <code>GSSAPI Extensions</code><br />
 <i>extensions </i></p>
<h3>Functions</h3>
<p> OM_uint32 GSS_CALLCONV <code>gss_accept_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle_P, const gss_cred_id_t acceptor_cred_handle, const gss_buffer_t input_token, const gss_channel_bindings_t input_chan_bindings, gss_name_t *src_name_P, gss_OID *mech_type, gss_buffer_t output_token, OM_uint32 *ret_flags, OM_uint32 *time_rec, gss_cred_id_t *delegated_cred_handle_P)<br />
 <i>GSS Accept Security Context. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_acquire_cred</code> (OM_uint32 *minor_status, const gss_name_t desired_name_P, OM_uint32 time_req, const gss_OID_set desired_mechs, gss_cred_usage_t cred_usage, gss_cred_id_t *output_cred_handle_P, gss_OID_set *actual_mechs, OM_uint32 *time_rec)<br />
 <i>Acquire Credential. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_compare_name</code> (OM_uint32 *minor_status, const gss_name_t name1_P, const gss_name_t name2_P, int *name_equal)<br />
 <i>Compare Name. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_delete_sec_context</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle_P, gss_buffer_t output_token)<br />
 <i>Delete Security Context. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_display_name</code> (OM_uint32 *minor_status, const gss_name_t input_name_P, gss_buffer_t output_name, gss_OID *output_name_type)<br />
 <i>Display Name. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_display_status</code> (OM_uint32 *minor_status, OM_uint32 status_value, int status_type, const gss_OID mech_type, OM_uint32 *message_context, gss_buffer_t status_string)<br />
 <i>Display Status</i> </p>
<p> Calls the OpenSSL error print routines to produce a printable message. This may need some work, as the OpenSSL error messages are more of a trace, and my not be the best for the user. Also don&#8217;t take advantage of being called in a loop. &quot;<br />
 OM_uint32 GSS_CALLCONV <code>gss_duplicate_name</code> (OM_uint32 *minor_status, const gss_name_t src_name, gss_name_t *dest_name)<br />
 <i>Duplicate Name. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_export_name</code> (OM_uint32 *minor_status, const gss_name_t input_name_P, gss_buffer_t exported_name)<br />
 <i>Export Name. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_get_mic</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, gss_qop_t qop_req, const gss_buffer_t message_buffer, gss_buffer_t message_token)<br />
 <i>Get MIC</i> </p>
<p> Calculates a cryptographic MIC (message integrity check) over an application message, and returns that MIC in the token. The token and message can then be passed to the peer application which calls <code>gss_verify_mic</code> to verify the MIC. &quot;<br />
 OM_uint32 GSS_CALLCONV <code>gss_sign</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, int qop_req, gss_buffer_t message_buffer, gss_buffer_t message_token)<br />
 <i>Sign. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_import_name</code> (OM_uint32 *minor_status, const gss_buffer_t input_name_buffer, const gss_OID input_name_type, gss_name_t *output_name_P) </p>
<p> OM_uint32 GSS_CALLCONV <code>gss_init_sec_context</code> (OM_uint32 *minor_status, const gss_cred_id_t initiator_cred_handle, gss_ctx_id_t *context_handle_P, const gss_name_t target_name, const gss_OID mech_type, OM_uint32 req_flags, OM_uint32 time_req, const gss_channel_bindings_t input_chan_bindings, const gss_buffer_t input_token, gss_OID *actual_mech_type, gss_buffer_t output_token, OM_uint32 *ret_flags, OM_uint32 *time_rec)<br />
 <i>Init Sec Context. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_inquire_context</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle_P, gss_name_t *src_name_P, gss_name_t *targ_name_P, OM_uint32 *lifetime_rec, gss_OID *mech_type, OM_uint32 *ctx_flags, int *locally_initiated, int *open)<br />
 <i>Inquire Context. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_context_time</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, OM_uint32 *time_rec)<br />
 <i>Context Time. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_inquire_cred</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle_P, gss_name_t *name, OM_uint32 *lifetime, gss_cred_usage_t *cred_usage, gss_OID_set *mechanisms)<br />
 <i>Inquire Cred. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_add_oid_set_member</code> (OM_uint32 *minor_status, const gss_OID member_oid, gss_OID_set *oid_set)<br />
 <i>Add OID Set Member. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_create_empty_oid_set</code> (OM_uint32 *minor_status, gss_OID_set *oid_set)<br />
 <i>Create Empty OID Set</i> </p>
<p> Creates an object identifier set containing no object identifiers, to which members may be subsequently added using the GSS_Add_OID_set_member() routine. These routines are intended to be used to construct sets of mechanism object identifiers, for input to GSS_Acquire_cred(). &quot;<br />
 OM_uint32 GSS_CALLCONV <code>gss_indicate_mechs</code> (OM_uint32 *minor_status, gss_OID_set *mech_set)<br />
 <i>Indicate Mechs. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_release_oid_set</code> (OM_uint32 *minor_status, gss_OID_set *mech_set)<br />
 <i>Release OID Set. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_test_oid_set_member</code> (OM_uint32 *minor_status, const gss_OID member, const gss_OID_set set, int *present)<br />
 <i>Test OID Set Member. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_release_buffer</code> (OM_uint32 *minor_status, gss_buffer_t buffer)<br />
 <i>Release Buffer. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_release_cred</code> (OM_uint32 *minor_status, gss_cred_id_t *cred_handle_P)<br />
 <i>Release Credential. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_release_name</code> (OM_uint32 *minor_status, gss_name_t *name_P)<br />
 <i>GSS Release Name. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_unwrap</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, const gss_buffer_t input_message_buffer, gss_buffer_t output_message_buffer, int *conf_state, gss_qop_t *qop_state)<br />
 <i>Unwrap. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_unseal</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, gss_buffer_t input_message_buffer, gss_buffer_t output_message_buffer, int *conf_state, int *qop_state)<br />
 <i>Unseal. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_verify_mic</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, const gss_buffer_t message_buffer, const gss_buffer_t token_buffer, gss_qop_t *qop_state)<br />
 <i>Verify MIC. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_verify</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, gss_buffer_t message_buffer, gss_buffer_t token_buffer, int *qop_state)<br />
 <i>Verify. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_wrap_size_limit</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, int conf_req_flag, gss_qop_t qop_req, OM_uint32 req_output_size, OM_uint32 *max_input_size)<br />
 <i>Wrap Size Limit. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_wrap</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, int conf_req_flag, gss_qop_t qop_req, const gss_buffer_t input_message_buffer, int *conf_state, gss_buffer_t output_message_buffer)<br />
 <i>Wrap. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_seal</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, int conf_req_flag, int qop_req, gss_buffer_t input_message_buffer, int *conf_state, gss_buffer_t output_message_buffer)<br />
 <i>Seal. </i></p>
<h2>Detailed Description</h2>
<p> GSI Implementation Details. </p>
<p> The Globus GSI GSSAPI is an implementation of GSS API C Bindings using OpenSSL. This API documentation is intended to explain implementation-specific behavior of this GSSAPI implementation, as well as GSSAPI extensions. </p>
<p> The API documentation is divided into sections covering:</p>
<dl>
<dt>&bull;</p>
<dd> <code>Globus GSSAPI</code></p>
<dt>&bull;</p>
<dd> <code>Activation</code></p>
<dt>&bull;</p>
<dd> <code>Constants</code></p>
<dt>&bull;</p>
<dd> <code>Request Flags</code></p>
<dt>&bull;</p>
<dd> <code>Return Flags</code></p>
<dt>&bull;</p>
<dd> <code>GSSAPI Extensions</code></p>
<dt>&bull;</p>
<dd> <code>Delegation</code></dl>
<h2>Function Documentation</h2>
<h3>OM_uint32 GSS_CALLCONV gss_accept_sec_context (OM_uint32 *minor_status, gss_ctx_id_t *context_handle_P, const gss_cred_id_tacceptor_cred_handle, const gss_buffer_tinput_token, const gss_channel_bindings_tinput_chan_bindings, gss_name_t *src_name_P, gss_OID *mech_type, gss_buffer_toutput_token, OM_uint32 *ret_flags, OM_uint32 *time_rec, gss_cred_id_t *delegated_cred_handle_P)</h3>
<p> GSS Accept Security Context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle_P</i><br />
 <i>acceptor_cred_handle</i><br />
 <i>input_token</i><br />
 <i>input_chan_bindings</i><br />
 <i>src_name_P</i><br />
 <i>mech_type</i><br />
 <i>output_token</i><br />
 <i>ret_flags</i> Also used as req_flags for other functions<br />
 <i>time_rec</i><br />
 <i>delegated_cred_handle_P</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_acquire_cred (OM_uint32 *minor_status, const gss_name_tdesired_name_P, OM_uint32time_req, const gss_OID_setdesired_mechs, gss_cred_usage_tcred_usage, gss_cred_id_t *output_cred_handle_P, gss_OID_set *actual_mechs, OM_uint32 *time_rec)</h3>
<p> Acquire Credential. GSSAPI routine to acquire the local credential. See the latest IETF draft/RFC on the GSSAPI C bindings. </p>
<p> Gets the local credentials. The proxy_init_cred does most of the work of setting up the SSL_ctx, getting the user&#8217;s cert, key, etc. </p>
<p> The globusid will be obtained from the certificate. (Minus and /CN=proxy entries.) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> Mechanism specific status code. In this implementation, the minor_status is a cast from a globus_result_t value, which is either GLOBUS_SUCCESS or a globus error object ID if an error occurred.<br />
 <i>desired_name_P</i> Name of principle whose credentials should be acquired This parameter maps to the desired subject of the cert to be acquired as the credential. Possible values are:</p>
<dl>
<dt>&bull;</p>
<dd> For a service cert: <i>service name</i>@<i>fqdn</i></p>
<dt>&bull;</p>
<dd> For a host cert: <i>fqdn</i></p>
<dt>&bull;</p>
<dd> For a proxy cert: <i>subject name</i></p>
<dt>&bull;</p>
<dd> For a user cert: <i>subject name</i> This parameter can be NULL, in which case the cert is chosen using a default search order of: host, proxy, user, service</dl>
<p> <i>time_req</i> Number of seconds that credentials should remain valid. This value can be GSS_C_INDEFINITE for an unlimited lifetime. NOTE: in the current implementation, this parameter is ignored, since you can&#8217;t change the expiration of a signed cert.<br />
 <i>desired_mechs</i><br />
 <i>cred_usage</i><br />
 <i>output_cred_handle_P</i><br />
 <i>actual_mechs</i><br />
 <i>time_rec</i></dl>
<h3>OM_uint32 GSS_CALLCONV gss_add_oid_set_member (OM_uint32 *minor_status, const gss_OIDmember_oid, gss_OID_set *oid_set)</h3>
<p> Add OID Set Member. Adds an Object Identifier to an Object Identifier set. This routine is intended for use in conjunction with GSS_Create_empty_OID_set() when constructing a set of mechanism OIDs for input to GSS_Acquire_cred(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>member_oid</i><br />
 <i>oid_set</i></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Operation failed</dl>
<h3>OM_uint32 GSS_CALLCONV gss_compare_name (OM_uint32 *minor_status, const gss_name_tname1_P, const gss_name_tname2_P, int *name_equal)</h3>
<p> Compare Name. Compare two names. GSSAPI names in this implementation are pointers to X.509 names. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> currently is always set to GLOBUS_SUCCESS<br />
 <i>name1_P</i><br />
 <i>name2_P</i><br />
 <i>name_equal</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> currently always returns GSS_S_COMPLETE</dl>
<h3>OM_uint32 GSS_CALLCONV gss_context_time (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, OM_uint32 *time_rec)</h3>
<p> Context Time. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>time_rec</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_create_empty_oid_set (OM_uint32 *minor_status, gss_OID_set *oid_set)</h3>
<p> Create Empty OID Set </p>
<p> Creates an object identifier set containing no object identifiers, to which members may be subsequently added using the GSS_Add_OID_set_member() routine. These routines are intended to be used to construct sets of mechanism object identifiers, for input to GSS_Acquire_cred(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>oid_set</i></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Operation failed</dl>
<h3>OM_uint32 GSS_CALLCONV gss_delete_sec_context (OM_uint32 *minor_status, gss_ctx_id_t *context_handle_P, gss_buffer_toutput_token)</h3>
<p> Delete Security Context. Delete the GSS Security Context </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status result &#8211; this is a globus_result_t cast to a OM_uint32.<br />
 <i>context_handle_P</i> The context handle to be deleted<br />
 <i>output_token</i> A token created upon destroying the context. If non-empty, this should be sent to the peer of the context to indicate that the context is closed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function always returns GSS_S_COMPLETE</dl>
<h3>OM_uint32 GSS_CALLCONV gss_display_name (OM_uint32 *minor_status, const gss_name_tinput_name_P, gss_buffer_toutput_name, gss_OID *output_name_type)</h3>
<p> Display Name. Produces a single line version of the internal X.509 name </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>input_name_P</i><br />
 <i>output_name</i><br />
 <i>output_name_type</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_display_status (OM_uint32 *minor_status, OM_uint32status_value, intstatus_type, const gss_OIDmech_type, OM_uint32 *message_context, gss_buffer_tstatus_string)</h3>
<p> Display Status </p>
<p> Calls the OpenSSL error print routines to produce a printable message. This may need some work, as the OpenSSL error messages are more of a trace, and my not be the best for the user. Also don&#8217;t take advantage of being called in a loop. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>status_value</i><br />
 <i>status_type</i><br />
 <i>mech_type</i><br />
 <i>message_context</i><br />
 <i>status_string</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_duplicate_name (OM_uint32 *minor_status, const gss_name_tsrc_name, gss_name_t *dest_name)</h3>
<p> Duplicate Name. Copy a GSSAPI name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>src_name</i><br />
 <i>dest_name</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_export_name (OM_uint32 *minor_status, const gss_name_tinput_name_P, gss_buffer_texported_name)</h3>
<p> Export Name. Produces a mechanism-independent exported name object. See section 3.2 of RFC 2743.</p>
<h3>OM_uint32 GSS_CALLCONV gss_get_mic (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, gss_qop_tqop_req, const gss_buffer_tmessage_buffer, gss_buffer_tmessage_token)</h3>
<p> Get MIC </p>
<p> Calculates a cryptographic MIC (message integrity check) over an application message, and returns that MIC in the token. The token and message can then be passed to the peer application which calls <code>gss_verify_mic</code> to verify the MIC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>qop_req</i><br />
 <i>message_buffer</i><br />
 <i>message_token</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_import_name (OM_uint32 *minor_status, const gss_buffer_tinput_name_buffer, const gss_OIDinput_name_type, gss_name_t *output_name_P)</h3>
<p> Import a name into a gss_name_t </p>
<p> Creates a new gss_name_t which contains a mechanism-specific representation of the input name. GSSAPI OpenSSL implements the following name types, based on the input_name_type OID: </p>
<dl>
<dt>&bull;</p>
<dd> GSS_C_NT_ANONYMOUS (input_name_buffer is ignored)</p>
<dt>&bull;</p>
<dd> GSS_C_NT_HOSTBASED_SERVICE (input_name_buffer contains a string &#8216;service@FQN&#8217; which will match /CN=service/FQDN)</p>
<dt>&bull;</p>
<dd> GSS_C_NT_EXPORT_NAME (input_name_buffer contains a string with the X509_oneline representation of a name) like &#8216;/X=Y/Z=A&#8230;&#8217;)</p>
<dt>&bull;</p>
<dd> GSS_C_NO_OID or GSS_C_NT_USER_NAME (input_name_buffer contains an X.500 name formatted like &#8216;/X=Y/Z=A&#8230;&#8217;)</p>
<dt>&bull;</p>
<dd> GLOBUS_GSS_C_NT_HOST_IP (input_name_buffer contains a string &#8216;FQDN/ip-address&#8217; which will match names with the FQDN or the IP address)</p>
<dt>&bull;</p>
<dd> GLOBUS_SSS_C_NT_X509 (input buffer is an X509 struct from OpenSSL)</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> Minor status<br />
 <i>input_name_buffer</i> Input name buffer which is interpreted based on the <i>input_name_type</i><br />
 <i>input_name_type</i> OID of the name<br />
 <i>output_name_P</i> New gss_name_t value containing the name</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> indicates that a valid name representation is output in output_name and described by the type value in output_name_type.<br />
 <i>GSS_S_BAD_NAMETYPE</i> indicates that the input_name_type is unsupported by the applicable underlying GSS-API mechanism(s), so the import operation could not be completed.<br />
 <i>GSS_S_BAD_NAME</i> indicates that the provided input_name_string is ill-formed in terms of the input_name_type, so the import operation could not be completed.<br />
 <i>GSS_S_BAD_MECH</i> indicates that the input presented for import was an exported name object and that its enclosed mechanism type was not recognized or was unsupported by the GSS-API implementation.<br />
 <i>GSS_S_FAILURE</i> indicates that the requested operation could not be performed for reasons unspecified at the GSS-API level.</dl>
<h3>OM_uint32 GSS_CALLCONV gss_indicate_mechs (OM_uint32 *minor_status, gss_OID_set *mech_set)</h3>
<p> Indicate Mechs. Passes back the mech set of available mechs. We only have one for now. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>mech_set</i></dl>
<h3>OM_uint32 GSS_CALLCONV gss_inquire_context (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle_P, gss_name_t *src_name_P, gss_name_t *targ_name_P, OM_uint32 *lifetime_rec, gss_OID *mech_type, OM_uint32 *ctx_flags, int *locally_initiated, int *open)</h3>
<p> Inquire Context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle_P</i><br />
 <i>src_name_P</i><br />
 <i>targ_name_P</i><br />
 <i>lifetime_rec</i><br />
 <i>mech_type</i><br />
 <i>ctx_flags</i><br />
 <i>locally_initiated</i><br />
 <i>open</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_inquire_cred (OM_uint32 *minor_status, const gss_cred_id_tcred_handle_P, gss_name_t *name, OM_uint32 *lifetime, gss_cred_usage_t *cred_usage, gss_OID_set *mechanisms)</h3>
<p> Inquire Cred. We will also allow the return of the proxy file name, if the minor_status is set to a value of 57056 0xdee0 This is done since there is no way to pass back the delegated credential file name. </p>
<p> When 57056 is seen, this will cause a new copy of this credential to be written, and it is the user&#8217;s responsibility to free the file when done. The name will be a pointer to a char * of the file name which must be freeed. The minor_status will be set to 57057 0xdee1 to indicate this. </p>
<p> DEE &#8211; this is a kludge, till the GSSAPI get a better way to return the name. </p>
<p> If the minor status is not changed from 57056 to 57057 assume it is not this gssapi, and a gss name was returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>cred_handle_P</i><br />
 <i>name</i><br />
 <i>lifetime</i><br />
 <i>cred_usage</i><br />
 <i>mechanisms</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_release_buffer (OM_uint32 *minor_status, gss_buffer_tbuffer)</h3>
<p> Release Buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>buffer</i></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success</dl>
<h3>OM_uint32 GSS_CALLCONV gss_release_cred (OM_uint32 *minor_status, gss_cred_id_t *cred_handle_P)</h3>
<p> Release Credential. Release the GSSAPI credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status result &#8211; this is a globus_result_t cast to a OM_uint32. To access the globus error object use: globus_error_get((globus_result_t) *minor_status)<br />
 <i>cred_handle_P</i> The gss cred handle to be released</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success</dl>
<h3>OM_uint32 GSS_CALLCONV gss_release_name (OM_uint32 *minor_status, gss_name_t *name_P)</h3>
<p> GSS Release Name. Release the GSS Name </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status result &#8211; this is a globus_result_t cast to a (OM_uint32 *).<br />
 <i>name_P</i> The GSSAPI name to be released</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Failure</dl>
<h3>OM_uint32 GSS_CALLCONV gss_release_oid_set (OM_uint32 *minor_status, gss_OID_set *mech_set)</h3>
<p> Release OID Set. Release the OID set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>mech_set</i></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success</dl>
<h3>OM_uint32 GSS_CALLCONV gss_seal (OM_uint32 *minor_status, gss_ctx_id_tcontext_handle, intconf_req_flag, intqop_req, gss_buffer_tinput_message_buffer, int *conf_state, gss_buffer_toutput_message_buffer)</h3>
<p> Seal. Obsolete variant of gss_wrap for V1 compatibility </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>conf_req_flag</i><br />
 <i>qop_req</i><br />
 <i>input_message_buffer</i><br />
 <i>conf_state</i><br />
 <i>output_message_buffer</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_sign (OM_uint32 *minor_status, gss_ctx_id_tcontext_handle, intqop_req, gss_buffer_tmessage_buffer, gss_buffer_tmessage_token)</h3>
<p> Sign. Deprecated. Does the same thing as gss_get_mic for V1 compatibility. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>qop_req</i><br />
 <i>message_buffer</i><br />
 <i>message_token</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_test_oid_set_member (OM_uint32 *minor_status, const gss_OIDmember, const gss_OID_setset, int *present)</h3>
<p> Test OID Set Member. Interrogates an Object Identifier set to determine whether a specified Object Identifier is a member. This routine is intended to be used with OID sets returned by GSS_Indicate_mechs(), GSS_Acquire_cred(), and GSS_Inquire_cred(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>member</i><br />
 <i>set</i><br />
 <i>present</i></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Operation failed</dl>
<h3>OM_uint32 GSS_CALLCONV gss_unseal (OM_uint32 *minor_status, gss_ctx_id_tcontext_handle, gss_buffer_tinput_message_buffer, gss_buffer_toutput_message_buffer, int *conf_state, int *qop_state)</h3>
<p> Unseal. Obsolete variant of gss_wrap for V1 compatibility allow for non 32 bit integer in qop_state. </p>
<p> Return the data from the wrapped buffer. There may also be errors, such as integrity errors. Since we can not communicate directly with our peer, we can not do everything SSL could, i.e. return a token for example. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>input_message_buffer</i><br />
 <i>output_message_buffer</i><br />
 <i>conf_state</i><br />
 <i>qop_state</i></dl>
<h3>OM_uint32 GSS_CALLCONV gss_unwrap (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, const gss_buffer_tinput_message_buffer, gss_buffer_toutput_message_buffer, int *conf_state, gss_qop_t *qop_state)</h3>
<p> Unwrap. GSSAPI routine to unwrap a buffer which may have been received and wraped by wrap.c </p>
<p> Return the data from the wrapped buffer. There may also be errors, such as integrity errors. Since we can not communicate directly with our peer, we can not do everything SSL could, i.e. return a token for example. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>input_message_buffer</i><br />
 <i>output_message_buffer</i><br />
 <i>conf_state</i><br />
 <i>qop_state</i></dl>
<h3>OM_uint32 GSS_CALLCONV gss_verify (OM_uint32 *minor_status, gss_ctx_id_tcontext_handle, gss_buffer_tmessage_buffer, gss_buffer_ttoken_buffer, int *qop_state)</h3>
<p> Verify. Obsolete variant of gss_verify for V1 compatibility Check a MIC of the date </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>message_buffer</i><br />
 <i>token_buffer</i><br />
 <i>qop_state</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_verify_mic (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, const gss_buffer_tmessage_buffer, const gss_buffer_ttoken_buffer, gss_qop_t *qop_state)</h3>
<p> Verify MIC. Check a MIC of the data </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>message_buffer</i><br />
 <i>token_buffer</i><br />
 <i>qop_state</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_wrap (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, intconf_req_flag, gss_qop_tqop_req, const gss_buffer_tinput_message_buffer, int *conf_state, gss_buffer_toutput_message_buffer)</h3>
<p> Wrap. Wrap a message for integrity and protection. We do this using the SSLv3 routines, by writing to the SSL bio, and pulling off the buffer from the back of the write BIO. But we can&#8217;t do everything SSL might want, such as control messages, or segment the messages here, since we are forced to using the GSSAPI tokens, and can not communicate directly with our peer. So there maybe some failures which would work with true SSL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>conf_req_flag</i><br />
 <i>qop_req</i><br />
 <i>input_message_buffer</i><br />
 <i>conf_state</i><br />
 <i>output_message_buffer</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_wrap_size_limit (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, intconf_req_flag, gss_qop_tqop_req, OM_uint32req_output_size, OM_uint32 *max_input_size)</h3>
<p> Wrap Size Limit. GSSAPI routine to take a buffer, calculate a MIC which is returned as a token. We will use the SSL protocol here. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>conf_req_flag</i><br />
 <i>qop_req</i><br />
 <i>req_output_size</i><br />
 <i>max_input_size</i></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
