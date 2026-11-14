---
title: "globus_gsi_callback_data_t(3)"
name: "globus_gsi_callback_data_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_callback_data_t/"
description: "Callback Data Functions –"
---

<h2 class="name">NAME</h2>
<p> Callback Data Functions &#8211; </p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_gsi_callback_data_s * <code>globus_gsi_callback_data_t</code>&quot; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_callback_data_init</code> (<code>globus_gsi_callback_data_t</code> *callback_data)<br />
 <i>Initialize a callback data structure. </i><br />
 globus_result_t <code>globus_gsi_callback_data_destroy</code> (<code>globus_gsi_callback_data_t</code> callback_data)<br />
 <i>Initialize a callback data structure. </i><br />
 globus_result_t <code>globus_gsi_callback_data_copy</code> (<code>globus_gsi_callback_data_t</code> source, <code>globus_gsi_callback_data_t</code> *dest)<br />
 <i>Copy a callback data structure. </i><br />
 globus_result_t <code>globus_gsi_callback_get_cert_depth</code> (<code>globus_gsi_callback_data_t</code> callback_data, int *cert_depth)<br />
 <i>Getting the certificate chain depth. </i><br />
 globus_result_t <code>globus_gsi_callback_set_cert_depth</code> (<code>globus_gsi_callback_data_t</code> callback_data, int cert_depth)<br />
 <i>Set the certificate chain depth. </i><br />
 globus_result_t <code>globus_gsi_callback_get_proxy_depth</code> (<code>globus_gsi_callback_data_t</code> callback_data, int *proxy_depth)<br />
 <i>Get the &#8216;proxy chain&#8217; depth. </i><br />
 globus_result_t <code>globus_gsi_callback_set_proxy_depth</code> (<code>globus_gsi_callback_data_t</code> callback_data, int proxy_depth)<br />
 <i>Set the &#8216;proxy chain&#8217; depth. </i><br />
 globus_result_t <code>globus_gsi_callback_get_cert_type</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_gsi_cert_utils_cert_type_t *cert_type)<br />
 <i>Get the certificate type. </i><br />
 globus_result_t <code>globus_gsi_callback_set_cert_type</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_gsi_cert_utils_cert_type_t cert_type)<br />
 <i>Set the certificate type. </i><br />
 globus_result_t <code>globus_gsi_callback_get_cert_chain</code> (<code>globus_gsi_callback_data_t</code> callback_data, STACK_OF(X509)**cert_chain)<br />
 <i>Get the certificate chain. </i><br />
 globus_result_t <code>globus_gsi_callback_set_cert_chain</code> (<code>globus_gsi_callback_data_t</code> callback_data, STACK_OF(X509)*cert_chain)<br />
 <i>Set the certificate chain. </i><br />
 globus_result_t <code>globus_gsi_callback_get_multiple_limited_proxy_ok</code> (<code>globus_gsi_callback_data_t</code> callback_data, int *multiple_limited_proxy_ok)<br />
 <i>Get the limited proxy handling setting. </i><br />
 globus_result_t <code>globus_gsi_callback_set_multiple_limited_proxy_ok</code> (<code>globus_gsi_callback_data_t</code> callback_data, int multiple_limited_proxy_ok)<br />
 <i>Set the limited proxy handling setting. </i><br />
 globus_result_t <code>globus_gsi_callback_get_extension_oids</code> (<code>globus_gsi_callback_data_t</code> callback_data, void **extension_oids)<br />
 <i>Get X.509 extension OIDs. </i><br />
 globus_result_t <code>globus_gsi_callback_set_extension_oids</code> (<code>globus_gsi_callback_data_t</code> callback_data, void *extension_oids)<br />
 <i>Set X.509 extension OIDs. </i><br />
 globus_result_t <code>globus_gsi_callback_get_cert_dir</code> (<code>globus_gsi_callback_data_t</code> callback_data, char **cert_dir)<br />
 <i>Get the trusted certificate directory. </i><br />
 globus_result_t <code>globus_gsi_callback_set_cert_dir</code> (<code>globus_gsi_callback_data_t</code> callback_data, char *cert_dir)<br />
 <i>Set the trusted certificate directory. </i><br />
 globus_result_t <code>globus_gsi_callback_get_extension_cb</code> (<code>globus_gsi_callback_data_t</code> callback_data, <code>globus_gsi_extension_callback_t</code> *extension_cb)<br />
 <i>Get the unknown X.509 extension callback. </i><br />
 globus_result_t <code>globus_gsi_callback_set_extension_cb</code> (<code>globus_gsi_callback_data_t</code> callback_data, <code>globus_gsi_extension_callback_t</code> extension_cb) </p>
<p> globus_result_t <code>globus_gsi_callback_get_error</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_result_t *error)<br />
 <i>Get error status. </i><br />
 globus_result_t <code>globus_gsi_callback_set_error</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_result_t error)<br />
 <i>Set error status. </i><br />
 globus_result_t <code>globus_gsi_callback_get_check_policy_for_self_signed_certs</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_bool_t *check)<br />
 <i>Get the self-signed policy checking flag. </i><br />
 globus_result_t <code>globus_gsi_callback_set_check_policy_for_self_signed_certs</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_bool_t check)<br />
 <i>Set the self-signed policy checking flag. </i><br />
 globus_result_t <code>globus_gsi_callback_get_allow_missing_signing_policy</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_bool_t *allow)<br />
 <i>Get the &#8216;allow missing signing policy&#8217; flag. </i><br />
 globus_result_t <code>globus_gsi_callback_set_allow_missing_signing_policy</code> (<code>globus_gsi_callback_data_t</code> callback_data, globus_bool_t allow)<br />
 <i>Set the &#8216;allow missing signing policy&#8217; flag. </i></p>
<h2>Detailed Description</h2>
<p> Functions that deal with the data structure that contains state associated with the path validation callback.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_l_gsi_callback_data_s* <code>globus_gsi_callback_data_t</code></h3>
<p> Callback data typedef</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_callback_data_copy (<code>globus_gsi_callback_data_t</code>source, <code>globus_gsi_callback_data_t</code> *dest)</h3>
<p> Copy a callback data structure. This function copies a globus_gsi_callback_data_t. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>source</i> The structure to be copied<br />
 <i>dest</i> The destination of the copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_data_destroy (<code>globus_gsi_callback_data_t</code>callback_data)</h3>
<p> Initialize a callback data structure. This function destroys a globus_gsi_callback_data_t. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The structure to be destroyed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_data_init (<code>globus_gsi_callback_data_t</code> *callback_data)</h3>
<p> Initialize a callback data structure. This function initializes a globus_gsi_callback_data_t. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> Reference to the structure to be initialized</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_allow_missing_signing_policy (<code>globus_gsi_callback_data_t</code>callback_data, globus_bool_t *allow)</h3>
<p> Get the &#8216;allow missing signing policy&#8217; flag. This function gets the value of the &#8216;allow missing signing policy&#8217; flag in the callback data. If this is TRUE then the CA signing policy need not be present. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the error from<br />
 <i>allow</i> Contains the value of the flag upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>Since:</code></p>
<dl>
<dt>
<dd> Globus Toolkit 5.2.0</dl>
<h3>globus_result_t globus_gsi_callback_get_cert_chain (<code>globus_gsi_callback_data_t</code>callback_data, STACK_OF(X509)**cert_chain)</h3>
<p> Get the certificate chain. This function returns the certificate chain associated with the callback data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to retrieve the certificate chain from.<br />
 <i>cert_chain</i> Contains the certificate chain upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_cert_depth (<code>globus_gsi_callback_data_t</code>callback_data, int *cert_depth)</h3>
<p> Getting the certificate chain depth. This function returns the certificate chain depth. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to retrieve the depth from<br />
 <i>cert_depth</i> The returned certificate chain depth</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_cert_dir (<code>globus_gsi_callback_data_t</code>callback_data, char **cert_dir)</h3>
<p> Get the trusted certificate directory. This function gets the trusted certificate directory from the callback data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the trusted certificates directory from.<br />
 <i>cert_dir</i> Contains the path to the trusted certificate directory upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_cert_type (<code>globus_gsi_callback_data_t</code>callback_data, globus_gsi_cert_utils_cert_type_t *cert_type)</h3>
<p> Get the certificate type. This function returns the certificate type of the certificate currently being processed </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to retrieve the certificate type from<br />
 <i>cert_type</i> Variable containing the certificate type on return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_check_policy_for_self_signed_certs (<code>globus_gsi_callback_data_t</code>callback_data, globus_bool_t *check)</h3>
<p> Get the self-signed policy checking flag. This function gets the value of the &#8216;check policy for self-signed certificates flag&#8217; in the callback data. If this is set than the CA signing policy for a self-signed certificate must include a policy line that allows it to sign itself. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the error from<br />
 <i>check</i> Contains the value of the flag upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>Since:</code></p>
<dl>
<dt>
<dd> Globus Toolkit 4.2.1</dl>
<h3>globus_result_t globus_gsi_callback_get_error (<code>globus_gsi_callback_data_t</code>callback_data, globus_result_t *error)</h3>
<p> Get error status. This function gets the error status stored in the callback data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the error from<br />
 <i>error</i> Contains the error upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_extension_cb (<code>globus_gsi_callback_data_t</code>callback_data, <code>globus_gsi_extension_callback_t</code> *extension_cb)</h3>
<p> Get the unknown X.509 extension callback. This function gets the callback that is called for unknown X.509 extensions </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the callback information from<br />
 <i>extension_cb</i> Contains the extension callback upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_extension_oids (<code>globus_gsi_callback_data_t</code>callback_data, void **extension_oids)</h3>
<p> Get X.509 extension OIDs. This function gets a list of X.509 extension OIDs that may be used by the extensions callback to allow or disallow certain extensions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the array of extension OIDs from.<br />
 <i>extension_oids</i> Contains the list of extension OIDs upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_multiple_limited_proxy_ok (<code>globus_gsi_callback_data_t</code>callback_data, int *multiple_limited_proxy_ok)</h3>
<p> Get the limited proxy handling setting. This function gets the value of the limited proxy handling setting. This setting determines whether path validation will accept limited proxies that have been further delegated, i.e. certificate chains with a limited proxy followed by further proxies. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the limited proxy setting from<br />
 <i>multiple_limited_proxy_ok</i> Contains the value of the setting upon successful return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_proxy_depth (<code>globus_gsi_callback_data_t</code>callback_data, int *proxy_depth)</h3>
<p> Get the &#8216;proxy chain&#8217; depth. This function returns the number of proxies in the certificate chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to retrieve the depth from<br />
 <i>proxy_depth</i> The returned &#8216;proxy chain&#8217; depth</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_allow_missing_signing_policy (<code>globus_gsi_callback_data_t</code>callback_data, globus_bool_tallow)</h3>
<p> Set the &#8216;allow missing signing policy&#8217; flag. This function sets the value of the &#8216;allow missing signing policy&#8217; flag in the callback data. If this is TRUE then the CA signing policy need not be present. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the error on<br />
 <i>allow</i> New value of the flag</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>Since:</code></p>
<dl>
<dt>
<dd> Globus Toolkit 5.2.0</dl>
<h3>globus_result_t globus_gsi_callback_set_cert_chain (<code>globus_gsi_callback_data_t</code>callback_data, STACK_OF(X509)*cert_chain)</h3>
<p> Set the certificate chain. This function sets the certificate chain associated with the callback data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the certificate chain on<br />
 <i>cert_chain</i> The certificate chain</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_cert_depth (<code>globus_gsi_callback_data_t</code>callback_data, intcert_depth)</h3>
<p> Set the certificate chain depth. This function sets the certificate chain depth </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to retrieve the depth from<br />
 <i>cert_depth</i> The certificate chain depth</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_cert_dir (<code>globus_gsi_callback_data_t</code>callback_data, char *cert_dir)</h3>
<p> Set the trusted certificate directory. This function sets the trusted certificate directory on the callback data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the trusted certificates directory on.<br />
 <i>cert_dir</i> The path to the trusted certificate directory</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_cert_type (<code>globus_gsi_callback_data_t</code>callback_data, globus_gsi_cert_utils_cert_type_tcert_type)</h3>
<p> Set the certificate type. This function sets the certificate type of the certificate currently being processed </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the certificate type on<br />
 <i>cert_type</i> The certificate type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_check_policy_for_self_signed_certs (<code>globus_gsi_callback_data_t</code>callback_data, globus_bool_tcheck)</h3>
<p> Set the self-signed policy checking flag. This function sets the value of the &#8216;check policy for self-signed certificates flag&#8217; in the callback data. If this is set than the CA signing policy for a self-signed certificate must include a policy line that allows it to sign itself. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the error on<br />
 <i>check</i> New value of the flag</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>Since:</code></p>
<dl>
<dt>
<dd> Globus Toolkit 4.2.1</dl>
<h3>globus_result_t globus_gsi_callback_set_error (<code>globus_gsi_callback_data_t</code>callback_data, globus_result_terror)</h3>
<p> Set error status. This function sets the error status stored in the callback data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the error on<br />
 <i>error</i> The error</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_extension_cb (<code>globus_gsi_callback_data_t</code>callback_data, <code>globus_gsi_extension_callback_t</code>extension_cb)</h3>
<p> Set the unknown X.509 extension callback </p>
<p> This function sets the callback that is called for unknown X.509 extensions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the callback information on<br />
 <i>extension_cb</i> The extension callback</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_extension_oids (<code>globus_gsi_callback_data_t</code>callback_data, void *extension_oids)</h3>
<p> Set X.509 extension OIDs. This function sets a list of X.509 extension OIDs that may be used by the extensions callback to allow or disallow certain extensions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to get the array of extension OIDs from.<br />
 <i>extension_oids</i> The list of extension OIDs</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_multiple_limited_proxy_ok (<code>globus_gsi_callback_data_t</code>callback_data, intmultiple_limited_proxy_ok)</h3>
<p> Set the limited proxy handling setting. This function sets the value of the limited proxy handling setting. This setting determines whether path validation will accept limited proxies that have been further delegated, i.e. certificate chains with a limited proxy followed by further proxies. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to set the limited proxy setting on<br />
 <i>multiple_limited_proxy_ok</i> The value of the setting</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_set_proxy_depth (<code>globus_gsi_callback_data_t</code>callback_data, intproxy_depth)</h3>
<p> Set the &#8216;proxy chain&#8217; depth. This function sets the number of proxies in the certificate chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_data</i> The globus_gsi_callback_data_t to retrieve the depth from<br />
 <i>proxy_depth</i> The &#8216;proxy chain&#8217; depth</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_callback from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbBH">Author</a></p>
<dd></dl>
