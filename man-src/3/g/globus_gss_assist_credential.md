---
title: "globus_gss_assist_credential(3)"
name: "globus_gss_assist_credential"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_credential/"
description: "Credential Management –"
---

<h2 class="name">NAME</h2>
<p> Credential Management &#8211; </p>
<p> Acquire Credential.</p>
<h3>Functions</h3>
<p> OM_uint32 <code>globus_gss_assist_acquire_cred</code> (OM_uint32 *minor_status, gss_cred_usage_t cred_usage, gss_cred_id_t *output_cred_handle) </p>
<p> OM_uint32 <code>globus_gss_assist_acquire_cred_ext</code> (OM_uint32 *minor_status, char *desired_name_char, OM_uint32 time_req, const gss_OID_set desired_mechs, gss_cred_usage_t cred_usage, gss_cred_id_t *output_cred_handle, gss_OID_set *actual_mechs, OM_uint32 *time_rec) </p>
<h2>Detailed Description</h2>
<p> Acquire Credential. </p>
<p> The functions in this section are used to acquire security credentials.</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 globus_gss_assist_acquire_cred (OM_uint32 *minor_status, gss_cred_usage_tcred_usage, gss_cred_id_t *output_cred_handle)</h3>
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
<dd> GSS_S_COMPLETE on success Other GSSAPI return codes</dl>
<h3>OM_uint32 globus_gss_assist_acquire_cred_ext (OM_uint32 *minor_status, char *desired_name_char, OM_uint32time_req, const gss_OID_setdesired_mechs, gss_cred_usage_tcred_usage, gss_cred_id_t *output_cred_handle, gss_OID_set *actual_mechs, OM_uint32 *time_rec)</h3>
<p> Called once at the start of the process, to obtain the credentials the process is running under. All the parameters of the gss_acquire_cred(), except the desired_name is a string of the form: [type:]name. This will be imported with the type. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GSS_S_COMPLETE on success Other GSSPI return codes</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_gss_acquire_cred</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
