---
title: "globus_gsi_authz(3)"
name: "globus_gsi_authz"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_authz/"
description: "GSI Authorization API –"
---

<h2 class="name">NAME</h2>
<p> GSI Authorization API &#8211; </p>
<p> Authorization Callouts.</p>
<h3>Modules</h3>
<p> <code>GSI Credential Constants</code> </p>
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
<h2>Detailed Description</h2>
<p> Authorization Callouts. </p>
<p> The GSI Authorization API provides an interface for making generic authorization decisions using dynamically-loaded authorization modules. The API documentation is divided into the following sections: </p>
<dl>
<dt>&bull;</p>
<dd> <code>GSI Authorization API</code></p>
<dt>&bull;</p>
<dd> <code>GSI Credential Constants</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_authorize (globus_gsi_authz_handle_thandle, const void *action, const void *object, globus_gsi_authz_cb_tcallback, void *callback_arg)</h3>
<p> Start the authorization decision-making process. Processes an authorization decision by calling the GLOBUS_GSI_AUTHORIZE_ASYNC function named in the authorization configuration file. The parameters to this function are passed to the authorization callout. Once the authorization decision is made, the callback function will be called, with the result and the callback_arg passed to it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Pointer to an authorization handle<br />
 <i>action</i> Action to authorize<br />
 <i>object</i> Object that the action pertains to.<br />
 <i>callback</i> Callback function to call when authorization completes<br />
 <i>callback_arg</i> Argument to callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if successful, or a Globus error object on failure.</dl>
<h3>globus_result_t globus_gsi_authz_get_authorization_identity (globus_gsi_authz_handle_thandle, char **identity_ptr, globus_gsi_authz_cb_tcallback, void *callback_arg)</h3>
<p> Query for authorization identity. Query for authorization identity by calling the GLOBUS_GSI_GET_AUTHORIZATION_IDENTITY callout. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle that is to be used for the identity check.<br />
 <i>identity_ptr</i> The authorization identity determined by the authorization handle. This is must be freed by the caller. If the value is NULL (and this function returned GLOBUS_SUCCESS), the caller should use the authenticated identity.<br />
 <i>callback</i> Callback function to call when identity is determined.<br />
 <i>callback_arg</i> Argument to callback function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_authz_handle_destroy (globus_gsi_authz_handle_thandle, globus_gsi_authz_cb_tcallback, void *callback_arg)</h3>
<p> Destroy an authz handle. Initialize an authorization handle by calling the GLOBUS_GSI_AUTHZ_HANDLE_DESTROY function named in the authorization configuration file. Once the initialization is complete, the callback function is called, with the result and the callback_arg passed to it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle that is to be destroyed<br />
 <i>callback</i> Callback function to call when handle is destroyed<br />
 <i>callback_arg</i> Argument to callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_authz_handle_init (globus_gsi_authz_handle_t *handle, const char *service_name, const gss_ctx_id_tcontext, globus_gsi_authz_cb_tcallback, void *callback_arg)</h3>
<p> Initialize an authorization handle. Initialize an authorization handle by calling the GLOBUS_GSI_AUTHZ_HANDLE_INIT function named in the authorization configuration file. The parameters to this function are passed to the authorization callout. Once the initialization is complete, the callback function is called, with the result and the callback_arg passed to it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Pointer to the handle that is to be initialized<br />
 <i>service_name</i> Service to authorize access to<br />
 <i>context</i> Security context used to contact the service<br />
 <i>callback</i> Callback function to call when authz handle init completes<br />
 <i>callback_arg</i> Argument to callback function</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>The</i> <code>globus_gsi_authz_handle_init()</code> function returns GLOBUS_SUCCESS if successful, or a Globus error object on failure</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_authz_handle_destroy()</code></dl>
<h3>globus_result_t globus_gsi_cancel_authz (globus_gsi_authz_handle_thandle)</h3>
<p> Cancel Authorization. Cancel an authorization decision by calling the GLOBUS_GSI_AUTHZ_CANCEL function named in the authorization configuration file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The authorization handle to cancel</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_authz from the source code. </p>
<h2>Index</h2>
