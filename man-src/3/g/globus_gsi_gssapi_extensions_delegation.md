---
title: "globus_gsi_gssapi_extensions_delegation(3)"
name: "globus_gsi_gssapi_extensions_delegation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gssapi_extensions_delegation/"
description: "Delegation –"
---

<h2 class="name">NAME</h2>
<p> Delegation &#8211; </p>
<p> Delegation Functions.</p>
<h3>Functions</h3>
<p> OM_uint32 GSS_CALLCONV <code>gss_accept_delegation</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, const gss_OID_set extension_oids, const gss_buffer_set_t extension_buffers, const gss_buffer_t input_token, OM_uint32 req_flags, OM_uint32 time_req, OM_uint32 *time_rec, gss_cred_id_t *delegated_cred_handle, gss_OID *mech_type, gss_buffer_t output_token)<br />
 <i>Accept a delegated credential. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_init_delegation</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, const gss_cred_id_t cred_handle, const gss_OID desired_mech, const gss_OID_set extension_oids, const gss_buffer_set_t extension_buffers, const gss_buffer_t input_token, OM_uint32 req_flags, OM_uint32 time_req, gss_buffer_t output_token)<br />
 <i>Initiate Delegation. </i></p>
<h2>Detailed Description</h2>
<p> Delegation Functions. </p>
<p> Functions in this section allow delegation to occur outside of the context initiation handshake.</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 GSS_CALLCONV gss_accept_delegation (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, const gss_OID_setextension_oids, const gss_buffer_set_textension_buffers, const gss_buffer_tinput_token, OM_uint32req_flags, OM_uint32time_req, OM_uint32 *time_rec, gss_cred_id_t *delegated_cred_handle, gss_OID *mech_type, gss_buffer_toutput_token)</h3>
<p> Accept a delegated credential. This functions drives the accepting side of the credential delegation process. It is expected to be called in tandem with the gss_init_delegation function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status returned by this function. This parameter will be 0 upon success.<br />
 <i>context_handle</i> The security context over which the credential is delegated.<br />
 <i>extension_oids</i> A set of extension OIDs corresponding to buffers in the extension_buffers parameter below. May be GSS_C_NO_BUFFER_SET. Currently not used.<br />
 <i>extension_buffers</i> A set of extension buffers corresponding to OIDs in the extension_oids parameter above. May be GSS_C_NO_BUFFER_SET. Currently not used.<br />
 <i>input_token</i> The token that was produced by a prior call to gss_init_delegation.<br />
 <i>req_flags</i> Flags that modify the behavior of the function. Currently only GSS_C_GLOBUS_SSL_COMPATIBLE is checked for. This flag results in tokens that aren&#8217;t wrapped.<br />
 <i>time_req</i> The requested period of validity (seconds) of the delegated credential. Currently a NO-OP.<br />
 <i>time_rec</i> This parameter will contain the received period of validity of the delegated credential upon success. May be NULL.<br />
 <i>delegated_cred_handle</i> This parameter will contain the delegated credential upon success.<br />
 <i>mech_type</i> Returns the security mechanism upon success. Currently not implemented. May be NULL.<br />
 <i>output_token</i> A token that should be passed to gss_init_delegation if the return value is GSS_S_CONTINUE_NEEDED.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Successful completion<br />
 <i>GSS_S_CONTINUE_NEEDED</i> The function needs to be called again.<br />
 <i>GSS_S_FAILURE</i> Failure</dl>
<h3>OM_uint32 GSS_CALLCONV gss_init_delegation (OM_uint32 *minor_status, const gss_ctx_id_tcontext_handle, const gss_cred_id_tcred_handle, const gss_OIDdesired_mech, const gss_OID_setextension_oids, const gss_buffer_set_textension_buffers, const gss_buffer_tinput_token, OM_uint32req_flags, OM_uint32time_req, gss_buffer_toutput_token)</h3>
<p> Initiate Delegation. This functions drives the initiating side of the credential delegation process. It is expected to be called in tandem with the gss_accept_delegation function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status returned by this function. This parameter will be 0 upon success.<br />
 <i>context_handle</i> The security context over which the credential is delegated.<br />
 <i>cred_handle</i> The credential to be delegated. May be GSS_C_NO_CREDENTIAL in which case the credential associated with the security context is used.<br />
 <i>desired_mech</i> The desired security mechanism. Currently not used. May be GSS_C_NO_OID.<br />
 <i>extension_oids</i> A set of extension OIDs corresponding to buffers in the extension_buffers parameter below. The extensions specified will be added to the delegated credential. May be GSS_C_NO_BUFFER_SET.<br />
 <i>extension_buffers</i> A set of extension buffers corresponding to OIDs in the extension_oids parameter above. May be GSS_C_NO_BUFFER_SET.<br />
 <i>input_token</i> The token that was produced by a prior call to gss_accept_delegation. This parameter will be ignored the first time this function is called.<br />
 <i>req_flags</i> Flags that modify the behavior of the function. Currently only GSS_C_GLOBUS_SSL_COMPATIBLE and GSS_C_GLOBUS_LIMITED_DELEG_PROXY_FLAG are checked for. The GSS_C_GLOBUS_SSL_COMPATIBLE flag results in tokens that aren&#8217;t wrapped and GSS_C_GLOBUS_LIMITED_DELEG_PROXY_FLAG causes the delegated proxy to be limited (requires that no extensions are specified.<br />
 <i>time_req</i> The requested period of validity (seconds) of the delegated credential. Passing a time_req of 0 cause the delegated credential to have the same lifetime as the credential that issued it.<br />
 <i>output_token</i> A token that should be passed to gss_accept_delegation if the return value is GSS_S_CONTINUE_NEEDED.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_CONTINUE_NEEDED</i> This function needs to be called again.<br />
 <i>GSS_S_FAILURE</i> upon failure</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
