---
title: "gss_release_iov_buffer(3)"
name: "gss_release_iov_buffer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gss_release_iov_buffer/"
description: "Heimdal GSS-API functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal GSS-API functions &#8211; </p>
<h3>Functions</h3>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_add_oid_set_member</code> (OM_uint32 *minor_status, const gss_OID member_oid, gss_OID_set *oid_set)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_wrap_iov</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, int conf_req_flag, gss_qop_t qop_req, int *conf_state, gss_iov_buffer_desc *iov, int iov_count)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_unwrap_iov</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, int *conf_state, gss_qop_t *qop_state, gss_iov_buffer_desc *iov, int iov_count)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_wrap_iov_length</code> (OM_uint32 *minor_status, gss_ctx_id_t context_handle, int conf_req_flag, gss_qop_t qop_req, int *conf_state, gss_iov_buffer_desc *iov, int iov_count)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_release_iov_buffer</code> (OM_uint32 *minor_status, gss_iov_buffer_desc *iov, int iov_count)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_canonicalize_name</code> (OM_uint32 *minor_status, gss_const_name_t input_name, const gss_OID mech_type, gss_name_t *output_name)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_display_status</code> (OM_uint32 *minor_status, OM_uint32 status_value, int status_type, const gss_OID mech_type, OM_uint32 *message_context, gss_buffer_t status_string)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_export_name</code> (OM_uint32 *minor_status, gss_const_name_t input_name, gss_buffer_t exported_name)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_import_name</code> (OM_uint32 *minor_status, const gss_buffer_t input_name_buffer, const gss_OID input_name_type, gss_name_t *output_name)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_init_sec_context</code> (OM_uint32 *minor_status, gss_const_cred_id_t initiator_cred_handle, gss_ctx_id_t *context_handle, gss_const_name_t target_name, const gss_OID input_mech_type, OM_uint32 req_flags, OM_uint32 time_req, const gss_channel_bindings_t input_chan_bindings, const gss_buffer_t input_token, gss_OID *actual_mech_type, gss_buffer_t output_token, OM_uint32 *ret_flags, OM_uint32 *time_rec)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_inquire_saslname_for_mech</code> (OM_uint32 *minor_status, const gss_OID desired_mech, gss_buffer_t sasl_mech_name, gss_buffer_t mech_name, gss_buffer_t mech_description)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_inquire_attrs_for_mech</code> (OM_uint32 *minor_status, gss_const_OID mech, gss_OID_set *mech_attr, gss_OID_set *known_mech_attrs)&quot; </p>
<p> GSSAPI_LIB_FUNCTION int<br />
 GSSAPI_LIB_CALL <code>gss_oid_equal</code> (gss_const_OID a, gss_const_OID b)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_release_cred</code> (OM_uint32 *minor_status, gss_cred_id_t *cred_handle)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_release_name</code> (OM_uint32 *minor_status, gss_name_t *input_name)&quot; </p>
<p> GSSAPI_LIB_FUNCTION OM_uint32<br />
 GSSAPI_LIB_CALL <code>gss_wrap</code> (OM_uint32 *minor_status, gss_const_ctx_id_t context_handle, int conf_req_flag, gss_qop_t qop_req, const gss_buffer_t input_message_buffer, int *conf_state, gss_buffer_t output_message_buffer)&quot; </p>
<h3>Variables</h3>
<p> gss_OID_desc GSSAPI_LIB_FUNCTION <code>__gss_c_attr_stream_sizes_oid_desc</code> </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_add_oid_set_member (OM_uint32 *minor_status, const gss_OIDmember_oid, gss_OID_set *oid_set)</h3>
<p> Add a oid to the oid set, function does not make a copy of the oid, so the pointer to member_oid needs to be stable for the whole time oid_set is used. </p>
<p> If there is a duplicate member of the oid, the new member is not added to to the set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code.<br />
 <i>member_oid</i> member to add to the oid set<br />
 <i>oid_set</i> oid set to add the member too</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code, see <code>gss_display_status()</code> about printing the error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_canonicalize_name (OM_uint32 *minor_status, gss_const_name_tinput_name, const gss_OIDmech_type, gss_name_t *output_name)</h3>
<p> gss_canonicalize_name takes a Internal Name (IN) and converts in into a mechanism specific Mechanism Name (MN). </p>
<p> The input name may multiple name, or generic name types. </p>
<p> If the input_name if of the GSS_C_NT_USER_NAME, and the Kerberos mechanism is specified, the resulting MN type is a GSS_KRB5_NT_PRINCIPAL_NAME. </p>
<p> For more information about <code>Internal names and mechanism names</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code.<br />
 <i>input_name</i> name to covert, unchanged by <code>gss_canonicalize_name()</code>.<br />
 <i>mech_type</i> the type to convert Name too.<br />
 <i>output_name</i> the resulting type, release with <code>gss_release_name()</code>, independent of input_name.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code, see <code>gss_display_status()</code> about printing the error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_display_status (OM_uint32 *minor_status, OM_uint32status_value, intstatus_type, const gss_OIDmech_type, OM_uint32 *message_context, gss_buffer_tstatus_string)</h3>
<p> Convert a GSS-API status code to text </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code<br />
 <i>status_value</i> status value to convert<br />
 <i>status_type</i> One of: GSS_C_GSS_CODE &#8211; status_value is a GSS status code, GSS_C_MECH_CODE &#8211; status_value is a mechanism status code<br />
 <i>mech_type</i> underlying mechanism. Use GSS_C_NO_OID to obtain the system default.<br />
 <i>message_context</i> state information to extract further messages from the status_value<br />
 <i>status_string</i> the allocated text representation. Release with gss_release_buffer()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_export_name (OM_uint32 *minor_status, gss_const_name_tinput_name, gss_buffer_texported_name)</h3>
<p> Convert a GGS-API name from internal form to contiguous string. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>gss_import_name()</code>, <code>Internal names and mechanism names</code>.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code<br />
 <i>input_name</i> input name in internal name form<br />
 <i>exported_name</i> output name in contiguos string form</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code, see <code>gss_display_status()</code> about printing the error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_import_name (OM_uint32 *minor_status, const gss_buffer_tinput_name_buffer, const gss_OIDinput_name_type, gss_name_t *output_name)</h3>
<p> Convert a GGS-API name from contiguous string to internal form. </p>
<p> Type of name and their format:</p>
<dl>
<dt>&bull;</p>
<dd> GSS_C_NO_OID</p>
<dt>&bull;</p>
<dd> GSS_C_NT_USER_NAME</p>
<dt>&bull;</p>
<dd> GSS_C_NT_HOSTBASED_SERVICE</p>
<dt>&bull;</p>
<dd> GSS_C_NT_EXPORT_NAME</p>
<dt>&bull;</p>
<dd> GSS_C_NT_ANONYMOUS</p>
<dt>&bull;</p>
<dd> GSS_KRB5_NT_PRINCIPAL_NAME</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>gss_export_name()</code>, <code>Internal names and mechanism names</code>.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code<br />
 <i>input_name_buffer</i> import name buffer<br />
 <i>input_name_type</i> type of the import name buffer<br />
 <i>output_name</i> the resulting type, release with <code>gss_release_name()</code>, independent of input_name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code, see <code>gss_display_status()</code> about printing the error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_init_sec_context (OM_uint32 *minor_status, gss_const_cred_id_tinitiator_cred_handle, gss_ctx_id_t *context_handle, gss_const_name_ttarget_name, const gss_OIDinput_mech_type, OM_uint32req_flags, OM_uint32time_req, const gss_channel_bindings_tinput_chan_bindings, const gss_buffer_tinput_token, gss_OID *actual_mech_type, gss_buffer_toutput_token, OM_uint32 *ret_flags, OM_uint32 *time_rec)</h3>
<p> As the initiator build a context with an acceptor. </p>
<p> Returns in the major</p>
<dl>
<dt>&bull;</p>
<dd> GSS_S_COMPLETE &#8211; if the context if build</p>
<dt>&bull;</p>
<dd> GSS_S_CONTINUE_NEEDED &#8211; if the caller needs to continue another round of gss_i nit_sec_context</p>
<dt>&bull;</p>
<dd> error code &#8211; any other error code</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code.<br />
 <i>initiator_cred_handle</i> the credential to use when building the context, if GSS_C_NO_CREDENTIAL is passed, the default credential for the mechanism will be used.<br />
 <i>context_handle</i> a pointer to a context handle, will be returned as long as there is not an error.<br />
 <i>target_name</i> the target name of acceptor, created using <code>gss_import_name()</code>. The name is can be of any name types the mechanism supports, check supported name types with gss_inquire_names_for_mech().<br />
 <i>input_mech_type</i> mechanism type to use, if GSS_C_NO_OID is used, Kerberos (GSS_KRB5_MECHANISM) will be tried. Other available mechanism are listed in the <code>GSS-API mechanisms</code> section.<br />
 <i>req_flags</i> flags using when building the context, see <code>Context creation flags</code><br />
 <i>time_req</i> time requested this context should be valid in seconds, common used value is GSS_C_INDEFINITE<br />
 <i>input_chan_bindings</i> Channel bindings used, if not exepected otherwise, used GSS_C_NO_CHANNEL_BINDINGS<br />
 <i>input_token</i> input token sent from the acceptor, for the initial packet the buffer of { NULL, 0 } should be used.<br />
 <i>actual_mech_type</i> the actual mech used, MUST NOT be freed since it pointing to static memory.<br />
 <i>output_token</i> if there is an output token, regardless of complete, continue_needed, or error it should be sent to the acceptor<br />
 <i>ret_flags</i> return what flags was negotitated, caller should check if they are accetable. For example, if GSS_C_MUTUAL_FLAG was negotiated with the acceptor or not.<br />
 <i>time_rec</i> amount of time this context is valid for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code, see <code>gss_display_status()</code> about printing the error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_inquire_attrs_for_mech (OM_uint32 *minor_status, gss_const_OIDmech, gss_OID_set *mech_attr, gss_OID_set *known_mech_attrs)</h3>
<p> List support attributes for a mech and/or all mechanisms. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code<br />
 <i>mech</i> given together with mech_attr will return the list of attributes for mechanism, can optionally be GSS_C_NO_OID.<br />
 <i>mech_attr</i> see mech parameter, can optionally be NULL, release with gss_release_oid_set().<br />
 <i>known_mech_attrs</i> all attributes for mechanisms supported, release with gss_release_oid_set().</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_inquire_saslname_for_mech (OM_uint32 *minor_status, const gss_OIDdesired_mech, gss_buffer_tsasl_mech_name, gss_buffer_tmech_name, gss_buffer_tmech_description)</h3>
<p> Returns different protocol names and description of the mechanism. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code<br />
 <i>desired_mech</i> mech list query<br />
 <i>sasl_mech_name</i> SASL GS2 protocol name<br />
 <i>mech_name</i> gssapi protocol name<br />
 <i>mech_description</i> description of gssapi mech</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> returns GSS_S_COMPLETE or a error code.</dl>
<h3>GSSAPI_LIB_FUNCTION int GSSAPI_LIB_CALL gss_oid_equal (gss_const_OIDa, gss_const_OIDb)</h3>
<p> Compare two GSS-API OIDs with each other. </p>
<p> GSS_C_NO_OID matches nothing, not even it-self. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>a</i> first oid to compare<br />
 <i>b</i> second oid to compare</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> non-zero when both oid are the same OID, zero when they are not the same.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_release_cred (OM_uint32 *minor_status, gss_cred_id_t *cred_handle)</h3>
<p> Release a credentials </p>
<p> Its ok to release the GSS_C_NO_CREDENTIAL/NULL credential, it will return a GSS_S_COMPLETE error code. On return cred_handle is set ot GSS_C_NO_CREDENTIAL. </p>
<p> Example: </p>
<pre><code>
*gss_cred_id_t cred = GSS_C_NO_CREDENTIAL;
*major = gss_release_cred(&amp;minor, &amp;cred);
*
</code></pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status return code, mech specific<br />
 <i>cred_handle</i> a pointer to the credential too release</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an gssapi error code</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_release_iov_buffer (OM_uint32 *minor_status, gss_iov_buffer_desc *iov, intiov_count)</h3>
<p> Free all buffer allocated by <code>gss_wrap_iov()</code> or <code>gss_unwrap_iov()</code> by looking at the GSS_IOV_BUFFER_FLAG_ALLOCATED flag.</p>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_release_name (OM_uint32 *minor_status, gss_name_t *input_name)</h3>
<p> Free a name </p>
<p> import_name can point to NULL or be NULL, or a pointer to a gss_name_t structure. If it was a pointer to gss_name_t, the pointer will be set to NULL on success and failure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code<br />
 <i>input_name</i> name to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a gss_error code, see <code>gss_display_status()</code> about printing the error code.</dl>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_unwrap_iov (OM_uint32 *minor_status, gss_ctx_id_tcontext_handle, int *conf_state, gss_qop_t *qop_state, gss_iov_buffer_desc *iov, intiov_count)</h3>
<p> Decrypt or verifies the signature on the data.</p>
<h3>GSSAPI_LIB_FUNCTION OM_uint32 GSSAPI_LIB_CALL gss_wrap (OM_uint32 *minor_status, gss_const_ctx_id_tcontext_handle, intconf_req_flag, gss_qop_tqop_req, const gss_buffer_tinput_message_buffer, int *conf_state, gss_buffer_toutput_message_buffer)</h3>
<p> Wrap a message using either confidentiality (encryption + signature) or sealing (signature). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> minor status code.<br />
 <i>context_handle</i> context handle.<br />
 <i>conf_req_flag</i> if non zero, confidentiality is requestd.<br />
 <i>qop_req</i> type of protection needed, in most cases it GSS_C_QOP_DEFAULT should be passed in.<br />
 <i>input_message_buffer</i> messages to wrap<br />
 <i>conf_state</i> returns non zero if confidentiality was honoured.<br />
 <i>output_message_buffer</i> the resulting buffer, release with gss_release_buffer().</p>
