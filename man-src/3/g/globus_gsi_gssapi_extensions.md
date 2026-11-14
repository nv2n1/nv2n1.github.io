---
title: "globus_gsi_gssapi_extensions(3)"
name: "globus_gsi_gssapi_extensions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gssapi_extensions/"
description: "GSSAPI Extensions –"
---

<h2 class="name">NAME</h2>
<p> GSSAPI Extensions &#8211; </p>
<p> extensions</p>
<h3>Modules</h3>
<p> <code>Buffer Set Utilities</code><br />
 <i>Buffer Set Utilities. </i><br />
 <code>Delegation</code><br />
 <i>Delegation Functions. </i></p>
<h3>Functions</h3>
<p> OM_uint32 GSS_CALLCONV <code>gss_export_cred</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, const gss_OID desired_mech, OM_uint32 option_req, gss_buffer_t export_buffer)<br />
 <i>Export a GSSAPI credential. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_import_cred</code> (OM_uint32 *minor_status, gss_cred_id_t *output_cred_handle, const gss_OID desired_mech, OM_uint32 option_req, const gss_buffer_t import_buffer, OM_uint32 time_req, OM_uint32 *time_rec)<br />
 <i>Import a credential. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_inquire_cred_by_oid</code> (OM_uint32 *minor_status, const gss_cred_id_t cred_handle, const gss_OID desired_object, gss_buffer_set_t *data_set)<br />
 <i>Inquire Cred By OID. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_inquire_sec_context_by_oid</code> (OM_uint32 *minor_status, const gss_ctx_id_t context_handle, const gss_OID desired_object, gss_buffer_set_t *data_set)<br />
 <i>Inquire Sec Context by OID. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_set_sec_context_option</code> (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_OID option, const gss_buffer_t value)<br />
 <i>Set Security Context Option. </i></p>
<h2>Detailed Description</h2>
<p> extensions </p>
<p> Experimental GSSAPI routines are defined here. These may change, and we will be looking at adding these to Kerberos as mods, and submitting them to the IETF. </p>
<p> These extensions are more fully documented in GSS-API Extensions</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 GSS_CALLCONV gss_export_cred (OM_uint32 *minor_status, const gss_cred_id_tcred_handle, const gss_OIDdesired_mech, OM_uint32option_req, gss_buffer_texport_buffer)</h3>
<p> Export a GSSAPI credential. Saves the credential so it can be checkpointed and imported by gss_import_cred </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>cred_handle</i><br />
 <i>desired_mech</i> Should either be gss_mech_globus_gssapi_openssl or NULL (in which case gss_mech_globus_gssapi_openssl is assumed).<br />
 <i>option_req</i><br />
 <i>export_buffer</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_import_cred (OM_uint32 *minor_status, gss_cred_id_t *output_cred_handle, const gss_OIDdesired_mech, OM_uint32option_req, const gss_buffer_timport_buffer, OM_uint32time_req, OM_uint32 *time_rec)</h3>
<p> Import a credential. This function will import credentials exported by <code>gss_export_cred()</code>. It is intended to allow a multiple use application to checkpoint delegated credentials. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status returned by this function. This parameter will be 0 upon success.<br />
 <i>output_cred_handle</i> Upon success, this parameter will contain the imported credential. When no longer needed this credential should be freed using <code>gss_release_cred()</code>.<br />
 <i>desired_mech</i> This parameter may be used to specify the desired security mechanism. May be GSS_C_NO_OID.<br />
 <i>option_req</i> This parameter indicates which option_req value was used to produce the import_buffer.<br />
 <i>import_buffer</i> A buffer produced by gss_export_credential().<br />
 <i>time_req</i> The requested period of validity (seconds) for the imported credential. May be NULL.<br />
 <i>time_rec</i> This parameter will contain the received period of validity of the imported credential upon success. May be NULL.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_BAD_MECH</i> Requested security mechanism is unavailable<br />
 <i>GSS_S_DEFECTIVE_TOKEN</i> import_buffer is defective<br />
 <i>GSS_S_FAILURE</i> General failure</dl>
<h3>OM_uint32 GSS_CALLCONV gss_inquire_cred_by_oid (OM_uint32 *minor_status, const gss_cred_id_tcred_handle, const gss_OIDdesired_object, gss_buffer_set_t *data_set)</h3>
<p> Inquire Cred By OID. NOTE: Checks both the cert in the credential and the certs in the cert chain for a valid extension that matches the desired OID. The first one found is used, starting with the endpoint cert, and then searching the cert chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>cred_handle</i><br />
 <i>desired_object</i><br />
 <i>data_set</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h3>OM_uint32 GSS_CALLCONV gss_set_sec_context_option (OM_uint32 *minor_status, gss_ctx_id_t *context_handle, const gss_OIDoption, const gss_buffer_tvalue)</h3>
<p> Set Security Context Option. GSSAPI routine to initiate the sending of a security context See: &lt;draft-ietf-cat-gssv2-cbind-04.txt&gt; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i><br />
 <i>context_handle</i><br />
 <i>option</i><br />
 <i>value</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
