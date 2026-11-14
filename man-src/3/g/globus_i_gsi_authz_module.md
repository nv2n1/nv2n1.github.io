---
title: "globus_i_gsi_authz_module(3)"
name: "globus_i_gsi_authz_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_gsi_authz_module/"
description: "globus_gsi_authz.h – GSI Authorization API."
---

<h2 class="name">NAME</h2>
<p> globus_gsi_authz.h &#8211; GSI Authorization API.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common.h&#8217;<br />
 #include &#8216;gssapi.h&#8217; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_authz_handle_init</code> (globus_gsi_authz_handle_t *handle, const char *service_name, const gss_ctx_id_t context, globus_gsi_authz_cb_t callback, void *callback_arg)<br />
 <i>Initialize an authorization handle. </i><br />
 globus_result_t <code>globus_gsi_authorize</code> (globus_gsi_authz_handle_t handle, const void *action, const void *object, globus_gsi_authz_cb_t callback, void *callback_arg)<br />
 <i>Start the authorization decision-making process. </i><br />
 globus_result_t <code>globus_gsi_cancel_authz</code> (globus_gsi_authz_handle_t handle)<br />
 <i>Cancel Authorization. </i><br />
 globus_result_t <code>globus_gsi_authz_handle_destroy</code> (globus_gsi_authz_handle_t handle, globus_gsi_authz_cb_t callback, void *callback_arg)<br />
 <i>Destroy an authz handle. </i><br />
 globus_result_t <code>globus_gsi_authz_get_authorization_identity</code> (globus_gsi_authz_handle_t handle, char **identity_ptr, globus_gsi_authz_cb_t callback, void *callback_arg)<br />
 <i>Query for authorization identity. </i></p>
<h3>Variables</h3>
<p> globus_module_descriptor_t <code>globus_i_gsi_authz_module</code> </p>
<h2>Detailed Description</h2>
<p> GSI Authorization API. </p>
<h2>Variable Documentation</h2>
<h3>globus_module_descriptor_t globus_i_gsi_authz_module</h3>
<p> Module descriptor static initializer</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_authz from the source code. </p>
<h2>Index</h2>
