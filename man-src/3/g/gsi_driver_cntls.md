---
title: "gsi_driver_cntls(3)"
name: "gsi_driver_cntls"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsi_driver_cntls/"
description: "Attributes and Cntls –"
---

<h2 class="name">NAME</h2>
<p> Attributes and Cntls &#8211; </p>
<p> GSI driver specific attrs and cntls.</p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_gsi_cmd_t</code> { <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, <code>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS</code>, <code>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS</code>, <code>GLOBUS_XIO_GSI_SET_PROXY_MODE</code>, <code>GLOBUS_XIO_GSI_GET_PROXY_MODE</code>, <code>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE</code>, <code>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE</code>, <code>GLOBUS_XIO_GSI_SET_DELEGATION_MODE</code>, <code>GLOBUS_XIO_GSI_GET_DELEGATION_MODE</code>, <code>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE</code>, <code>GLOBUS_XIO_GSI_SET_ANON</code>, <code>GLOBUS_XIO_GSI_SET_WRAP_MODE</code>, <code>GLOBUS_XIO_GSI_GET_WRAP_MODE</code>, <code>GLOBUS_XIO_GSI_SET_BUFFER_SIZE</code>, <code>GLOBUS_XIO_GSI_GET_BUFFER_SIZE</code>, <code>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_GET_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_SET_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_GET_CONTEXT</code>, <code>GLOBUS_XIO_GSI_GET_DELEGATED_CRED</code>, <code>GLOBUS_XIO_GSI_GET_PEER_NAME</code>, <code>GLOBUS_XIO_GSI_GET_LOCAL_NAME</code>, <code>GLOBUS_XIO_GSI_INIT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_ACCEPT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_CREDENTIAL, gss_cred_id_t credential) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_SET_CREDENTIAL, gss_cred_id_t credential) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_CREDENTIAL, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_GET_CREDENTIAL, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS, OM_uint32 req_flags) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS, OM_uint32 *req_flags) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_PROXY_MODE, <code>globus_xio_gsi_proxy_mode_t</code> proxy_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_PROXY_MODE, <code>globus_xio_gsi_proxy_mode_t</code> *proxy_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE, <code>globus_xio_gsi_authorization_mode_t</code> authz_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE, <code>globus_xio_gsi_authorization_mode_t</code> *authz_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_DELEGATION_MODE, <code>globus_xio_gsi_delegation_mode_t</code> delegation_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_DELEGATION_MODE, <code>globus_xio_gsi_delegation_mode_t</code> *delegation_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE, globus_bool_t ssl_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_ANON, globus_bool_t anon_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_WRAP_MODE, globus_boolean_t wrap_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_WRAP_MODE, globus_boolean_t *wrap_mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_BUFFER_SIZE, globus_size_t buffer_size) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_BUFFER_SIZE, globus_size_t *buffer_size) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL, <code>globus_xio_gsi_protection_level_t</code> protection_level) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL, <code>globus_xio_gsi_protection_level_t</code> *protection_level) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_GET_TARGET_NAME, gss_name_t *target_name) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_SET_TARGET_NAME, gss_name_t target_name) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_GET_CONTEXT, gss_ctx_id_t *context) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_GET_DELEGATED_CRED, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_GET_PEER_NAME, gss_name_t *peer_name) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_GET_LOCAL_NAME, gss_name_t *local_name) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_INIT_DELEGATION, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_init_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_ACCEPT_DELEGATION, gss_cred_id_t *credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_accept_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_GSI_FORCE_SERVER_MODE, globus_bool_t server_mode) </p>
<h2>Detailed Description</h2>
<p> GSI driver specific attrs and cntls. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_gsi_cmd_t</code></h3>
<p> doxygen varargs filter stuff GSI driver specific cntls </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_GSI_SET_CREDENTIAL </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_CREDENTIAL </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_PROXY_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_PROXY_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_DELEGATION_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_DELEGATION_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_ANON </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_WRAP_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_WRAP_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_BUFFER_SIZE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_BUFFER_SIZE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_TARGET_NAME </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_SET_TARGET_NAME </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_CONTEXT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_DELEGATED_CRED </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_PEER_NAME </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_GET_LOCAL_NAME </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_INIT_DELEGATION </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_ACCEPT_DELEGATION </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_GSI_FORCE_SERVER_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_CREDENTIAL, gss_cred_id_t credential)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the credential to be used. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The credential to set. The credential structure needs to remain valid for the lifetime of any xio datastructure it is used by.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> If this is called with the handle_cntl, there must be no outstanding operations on the handle.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_SET_CREDENTIAL, gss_cred_id_t credential)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the credential to be used. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The credential to set. The credential structure needs to remain valid for the lifetime of any xio datastructure it is used by.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> If this is called with the handle_cntl, there must be no outstanding operations on the handle.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_CREDENTIAL, gss_cred_id_t * credential)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the credential to be used. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The credential that is currently set. This will only return a credential if a credential was explicitly set prior to this call. It will not return any credential automatically acquired during context initizalization.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_GET_CREDENTIAL, gss_cred_id_t * credential)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the credential to be used. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The credential that is currently set. This will only return a credential if a credential was explicitly set prior to this call. It will not return any credential automatically acquired during context initizalization.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS, OM_uint32 req_flags)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the GSSAPI req_flags to be used. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>req_flags</i> The req_flags to set</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS, OM_uint32 * req_flags)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the GSSAPI req_flags to be used. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>req_flags</i> The req flags currently in effect</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_PROXY_MODE, <code>globus_xio_gsi_proxy_mode_t</code> proxy_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the proxy mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proxy_mode</i> The proxy mode to set</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Changing the proxy mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_PROXY_MODE, <code>globus_xio_gsi_proxy_mode_t</code> * proxy_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the proxy mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proxy_mode</i> The proxy mode that is currently in effect</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Changing the proxy mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE, <code>globus_xio_gsi_authorization_mode_t</code> authz_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the authorization mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>authz_mode</i> The authorization mode to set</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE, <code>globus_xio_gsi_authorization_mode_t</code> * authz_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the authorization mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>authz_mode</i> The authorization mode that is currently in effect</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_DELEGATION_MODE, <code>globus_xio_gsi_delegation_mode_t</code> delegation_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the delegation mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>delegation_mode</i> The delegation mode to use</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Changing the delegation mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_DELEGATION_MODE, <code>globus_xio_gsi_delegation_mode_t</code> * delegation_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the delegation mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>delegation_mode</i> The delegation mode currently in effect</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE, globus_bool_t ssl_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Make the on the wire protocol SSL compatible. This implies no wrapping of security tokens and no delegation </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ssl_mode</i> The ssl compatibility mode to use</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Changing the ssl compatibility mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_ANON, globus_bool_t anon_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Do anonymous authentication. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>anon_mode</i> The ssl compatibility mode to use</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Changing the ssl compatibility mode changes the req_flags and the wrapping mode</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_WRAP_MODE, globus_boolean_t wrap_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the wrapping mode </p>
<p> This mode determines whether tokens will be wrapped with a Globus IO style header or not. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>wrap_mode</i> The wrapping mode to use</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_WRAP_MODE, globus_boolean_t * wrap_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the wrapping mode </p>
<p> This mode determines whether tokens will be wrapped with a Globus IO style header or not. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>wrap_mode</i> The wrapping mode currently in use.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_BUFFER_SIZE, globus_size_t buffer_size)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the read buffer size </p>
<p> The read buffer is used for buffering wrapped data, is initialized with a default size of 128K and scaled dynamically to always be able to fit whole tokens. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buffer_size</i> The size of the read buffer</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_BUFFER_SIZE, globus_size_t * buffer_size)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the read buffer size </p>
<p> The read buffer is used for buffering wrapped data, is initialized with a default size of 128K and scaled dynamically to always be able to fit whole tokens. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buffer_size</i> The size of the read buffer</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL, <code>globus_xio_gsi_protection_level_t</code> protection_level)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the protection level. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>protection_level</i> The protection level to set</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Changing the proxy mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL, <code>globus_xio_gsi_protection_level_t</code> * protection_level)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the protection level. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>protection_level</i> The current protection level</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_GET_TARGET_NAME, gss_name_t * target_name)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the expected peer name. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>target_name</i> The expected peer name</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_SET_TARGET_NAME, gss_name_t target_name)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the expected peer name. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>target_name</i> The expected peer name</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_GET_CONTEXT, gss_ctx_id_t * context)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the GSS context. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The GSS context</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_GET_DELEGATED_CRED, gss_cred_id_t * credential)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the delegated credential. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The delegated credential</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_GET_PEER_NAME, gss_name_t * peer_name)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the name of the peer. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>peer_name</i> The GSS name of the peer.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_GET_LOCAL_NAME, gss_name_t * local_name)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the GSS name associated with the local credentials. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>local_name</i> The GSS name of the local credentials</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_INIT_DELEGATION, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Initialize delegation-at-any-time process. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The GSS credential to delegate<br />
 <i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The lifetime of the delegated credential</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_init_callback_t</code> callback, void * callback_arg)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Initialize non-blocking delegation-at-any-time process. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The GSS credential to delegate<br />
 <i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The lifetime of the delegated credential<br />
 <i>callback</i> The callback to call when the operation completes<br />
 <i>callback_arg</i> The arguments to pass to the callback</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_ACCEPT_DELEGATION, gss_cred_id_t * credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Accept delegation-at-any-time process. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The delegated GSS credential<br />
 <i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The requested lifetime of the delegated credential</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_accept_callback_t</code> callback, void * callback_arg)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Accept non-blocking delegation-at-any-time process. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The lifetime of the delegated credential<br />
 <i>callback</i> The callback to call when the operation completes<br />
 <i>callback_arg</i> The arguments to pass to the callback</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_GSI_FORCE_SERVER_MODE, globus_bool_t server_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Force the server mode setting. This explicitly sets the directionality of context establishment and delegation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server_mode</i> The server mode.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio gsi driver from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbBN">Author</a></p>
<dd></dl>
