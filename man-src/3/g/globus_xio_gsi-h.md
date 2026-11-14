---
title: "globus_xio_gsi-h(3)"
name: "globus_xio_gsi-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_gsi-h/"
description: "globus_xio_gsi.h – XIO GSI Driver."
---

<p>globus_xio_gsi.h &#8211; XIO GSI Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;gssapi.h&#8217;<br />
 #include &#8216;globus_common.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>globus_xio_gsi_attr_cntl</code> globus_xio_attr_cntl </p>
<h3>Typedefs</h3>
<p>typedef void(* <code>globus_xio_gsi_delegation_init_callback_t</code> )(globus_result_t result, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_gsi_delegation_accept_callback_t</code> )(globus_result_t result, gss_cred_id_t delegated_cred, OM_uint32 time_rec, void *user_arg) </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_gsi_error_t</code> { <code>GLOBUS_XIO_GSI_ERROR_INVALID_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_ERROR_WRAP_GSSAPI</code>, <code>GLOBUS_XIO_GSI_ERROR_EMPTY_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_ERROR_EMPTY_HOST_NAME</code>, <code>GLOBUS_XIO_GSI_AUTHORIZATION_FAILED</code>, <code>GLOBUS_XIO_GSI_ERROR_TOKEN_TOO_BIG</code> } </p>
<p> enum <code>globus_xio_gsi_cmd_t</code> { <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, <code>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS</code>, <code>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS</code>, <code>GLOBUS_XIO_GSI_SET_PROXY_MODE</code>, <code>GLOBUS_XIO_GSI_GET_PROXY_MODE</code>, <code>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE</code>, <code>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE</code>, <code>GLOBUS_XIO_GSI_SET_DELEGATION_MODE</code>, <code>GLOBUS_XIO_GSI_GET_DELEGATION_MODE</code>, <code>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE</code>, <code>GLOBUS_XIO_GSI_SET_ANON</code>, <code>GLOBUS_XIO_GSI_SET_WRAP_MODE</code>, <code>GLOBUS_XIO_GSI_GET_WRAP_MODE</code>, <code>GLOBUS_XIO_GSI_SET_BUFFER_SIZE</code>, <code>GLOBUS_XIO_GSI_GET_BUFFER_SIZE</code>, <code>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_GET_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_SET_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_GET_CONTEXT</code>, <code>GLOBUS_XIO_GSI_GET_DELEGATED_CRED</code>, <code>GLOBUS_XIO_GSI_GET_PEER_NAME</code>, <code>GLOBUS_XIO_GSI_GET_LOCAL_NAME</code>, <code>GLOBUS_XIO_GSI_INIT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_ACCEPT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code>, <code>GLOBUS_XIO_GSI_SET_ALLOW_MISSING_SIGNING_POLICY</code>, <code>GLOBUS_XIO_GSI_GET_ALLOW_MISSING_SIGNING_POLICY</code> } </p>
<p> enum <code>globus_xio_gsi_protection_level_t</code> { <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_NONE</code>, <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_INTEGRITY</code>, <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_PRIVACY</code> } </p>
<p> enum <code>globus_xio_gsi_delegation_mode_t</code> { <code>GLOBUS_XIO_GSI_DELEGATION_MODE_NONE</code>, <code>GLOBUS_XIO_GSI_DELEGATION_MODE_LIMITED</code>, <code>GLOBUS_XIO_GSI_DELEGATION_MODE_FULL</code> } </p>
<p> enum <code>globus_xio_gsi_proxy_mode_t</code> { <code>GLOBUS_XIO_GSI_PROXY_MODE_FULL</code>, <code>GLOBUS_XIO_GSI_PROXY_MODE_LIMITED</code>, <code>GLOBUS_XIO_GSI_PROXY_MODE_MANY</code> } </p>
<p> enum <code>globus_xio_gsi_authorization_mode_t</code> { <code>GLOBUS_XIO_GSI_NO_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_SELF_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_HOST_AUTHORIZATION</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, gss_cred_id_t credential) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, gss_cred_id_t credential) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS</code>, OM_uint32 req_flags) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS</code>, OM_uint32 *req_flags) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_PROXY_MODE</code>, <code>globus_xio_gsi_proxy_mode_t</code> proxy_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_PROXY_MODE</code>, <code>globus_xio_gsi_proxy_mode_t</code> *proxy_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE</code>, <code>globus_xio_gsi_authorization_mode_t</code> authz_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE</code>, <code>globus_xio_gsi_authorization_mode_t</code> *authz_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_DELEGATION_MODE</code>, <code>globus_xio_gsi_delegation_mode_t</code> delegation_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_DELEGATION_MODE</code>, <code>globus_xio_gsi_delegation_mode_t</code> *delegation_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE</code>, globus_bool_t ssl_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_ANON</code>, globus_bool_t anon_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_WRAP_MODE</code>, globus_bool_t wrap_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_WRAP_MODE</code>, globus_bool_t *wrap_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_BUFFER_SIZE</code>, globus_size_t buffer_size) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_BUFFER_SIZE</code>, globus_size_t *buffer_size) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL</code>, <code>globus_xio_gsi_protection_level_t</code> protection_level) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL</code>, <code>globus_xio_gsi_protection_level_t</code> *protection_level) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_TARGET_NAME</code>, gss_name_t *target_name) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_TARGET_NAME</code>, gss_name_t target_name) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_CONTEXT</code>, gss_ctx_id_t *context) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_DELEGATED_CRED</code>, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_PEER_NAME</code>, gss_name_t *peer_name) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_LOCAL_NAME</code>, gss_name_t *local_name) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_INIT_DELEGATION</code>, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION</code>, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_init_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_ACCEPT_DELEGATION</code>, gss_cred_id_t *credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION</code>, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_accept_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code>, globus_bool_t server_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_ALLOW_MISSING_SIGNING_POLICY</code>, globus_bool_t allow) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_ALLOW_MISSING_SIGNING_POLICY</code>, globus_bool_t *allow) </p>
<h2>Detailed Description</h2>
<p>XIO GSI Driver. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Sam Meder</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define globus_xio_gsi_attr_cntl globus_xio_attr_cntl</h3>
<p>doxygen varargs filter stuff</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio_gsi_driver from the source code.</p>
