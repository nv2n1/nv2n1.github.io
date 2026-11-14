---
title: "globus_gsi_proxy_handle_get_policy(3)"
name: "globus_gsi_proxy_handle_get_policy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_proxy_handle_get_policy/"
description: "Handle Management –"
---

<h2 class="name">NAME</h2>
<p> Handle Management &#8211; </p>
<p> Create/Destroy/Modify a GSI Proxy Handle.</p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_gsi_proxy_handle_s * <code>globus_gsi_proxy_handle_t</code>&quot;<br />
 <i>GSI Proxy Handle. </i></p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_proxy_handle_init</code> (<code>globus_gsi_proxy_handle_t</code> *handle, <code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs)<br />
 <i>Initialize a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_req</code> (<code>globus_gsi_proxy_handle_t</code> handle, X509_REQ **req)<br />
 <i>Get the certificate request from a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_private_key</code> (<code>globus_gsi_proxy_handle_t</code> handle, EVP_PKEY **proxy_key)<br />
 <i>Get the private key from a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_type</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cert_utils_cert_type_t *type)<br />
 <i>Get Proxy Type. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_type</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cert_utils_cert_type_t type)<br />
 <i>Get Proxy Type. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_policy</code> (<code>globus_gsi_proxy_handle_t</code> handle, const unsigned char *policy_data, int policy_length, int policy_language_NID)<br />
 <i>Set Policy. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_policy</code> (<code>globus_gsi_proxy_handle_t</code> handle, unsigned char **policy_data, int *policy_length, int *policy_NID)<br />
 <i>Get Policy. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_add_extension</code> (<code>globus_gsi_proxy_handle_t</code> handle, X509_EXTENSION *ext)<br />
 <i>Add X.509 Extensions. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_extensions</code> (<code>globus_gsi_proxy_handle_t</code> handle, STACK_OF(X509_EXTENSION)*exts)<br />
 <i>Set X.509 Extensions. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_extensions</code> (<code>globus_gsi_proxy_handle_t</code> handle, STACK_OF(X509_EXTENSION)**exts)<br />
 <i>Get X.509 Extensions. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_pathlen</code> (<code>globus_gsi_proxy_handle_t</code> handle, long pathlen)<br />
 <i>Set Path Length. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_pathlen</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *pathlen)<br />
 <i>Get Path Length. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_time_valid</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *time_valid)<br />
 <i>Get Time Valid. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_time_valid</code> (<code>globus_gsi_proxy_handle_t</code> handle, int time_valid)<br />
 <i>Set Time Valid. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_clear_cert_info</code> (<code>globus_gsi_proxy_handle_t</code> handle)<br />
 <i>Clear Cert Info. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_proxy_cert_info_openssl</code> (<code>globus_gsi_proxy_handle_t</code> handle, PROXY_CERT_INFO_EXTENSION **pci)<br />
 <i>Get Cert Info. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_proxy_cert_info_openssl</code> (<code>globus_gsi_proxy_handle_t</code> handle, PROXY_CERT_INFO_EXTENSION *pci)<br />
 <i>Set Cert Info. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_signing_algorithm</code> (<code>globus_gsi_proxy_handle_t</code> handle, const EVP_MD **signing_algorithm)<br />
 <i>Get Signing Algorithm. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_keybits</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *key_bits)<br />
 <i>Get Key Bits. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_init_prime</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *init_prime)<br />
 <i>Get Init Prime. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_clock_skew_allowable</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *skew)<br />
 <i>Get Clock Skew. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_key_gen_callback</code> (<code>globus_gsi_proxy_handle_t</code> handle, void(**callback)(int, int, void *))<br />
 <i>Get Callback for Creating Keys. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_common_name</code> (<code>globus_gsi_proxy_handle_t</code> handle, char **common_name)<br />
 <i>Get/Set Proxy Common Name. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_is_limited</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_bool_t is_limited)<br />
 <i>Set/Check Proxy Is Limited. </i></p>
<h2>Detailed Description</h2>
<p> Create/Destroy/Modify a GSI Proxy Handle. </p>
<p> Within the Globus GSI Proxy Library, all proxy operations require a handle parameter. Currently, only one proxy operation may be in progress at once per proxy handle. </p>
<p> This section defines operations to create, modify and destroy GSI Proxy handles.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_l_gsi_proxy_handle_s* <code>globus_gsi_proxy_handle_t</code></h3>
<p> GSI Proxy Handle. An GSI Proxy handle is used to associate state with a group of operations. Handles can have immutable <code>attributes</code> associated with them. All proxy <code>operations </code> take a handle pointer as a parameter. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_init()</code>, <code>globus_gsi_proxy_handle_destroy()</code>, <code>Handle Attributes</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_proxy_handle_add_extension (<code>globus_gsi_proxy_handle_t</code>handle, X509_EXTENSION *ext)</h3>
<p> Add X.509 Extensions. Add an X.509 extension to the GSI Proxy handle to be added to certificate </p>
<p> This function adds a X.509 extension to the proxy certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for the proxy to which the extension should be added.<br />
 <i>ext</i> The extension to be added.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the addition was successful, otherwise an error is returned.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_get_extensions()</code> </p>
<p> <code>globus_gsi_proxy_handle_set_extensions()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_clear_cert_info (<code>globus_gsi_proxy_handle_t</code>handle)</h3>
<p> Clear Cert Info. Clear the proxy cert info extension stored in the GSI Proxy handle. </p>
<p> This function clears proxy cert info extension related setting in the GSI Proxy handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for which to clear the proxy cert info extension.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle is valid, otherwise an error is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_clock_skew_allowable (<code>globus_gsi_proxy_handle_t</code>handle, int *skew)</h3>
<p> Get Clock Skew. Get the clock skew of the proxy handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to get the clock skew of<br />
 <i>skew</i> The resulting clock skew</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case an error object identifier (in the form of a globus_result_t) is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_common_name (<code>globus_gsi_proxy_handle_t</code>handle, char **common_name)</h3>
<p> Get/Set Proxy Common Name. Get the proxy common name stored in the GSI Proxy handle. </p>
<p> This function retrieves the proxy common name from the GSI Proxy handle. The common name only impacts draft compliant proxies. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle from which to get the proxy common name.<br />
 <i>common_name</i> Contains the proxy common name upon successful return. If the handle does not contain a common name, this parameter will be NULL upon return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS upon success GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE if handle is invalid</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_extensions (<code>globus_gsi_proxy_handle_t</code>handle, STACK_OF(X509_EXTENSION)**exts)</h3>
<p> Get X.509 Extensions. Get the X.509 extensions from a GSI Proxy handle </p>
<p> This function returns the X.509 extensions from the proxy certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for the proxy from which the extensions should be retrieved.<br />
 <i>exts</i> The variable to hold the extensions. The caller is responsible for freeing the extensions with sk_X509_EXTENSION_free() when they are done with them.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the retrieval was successful, otherwise an error is returned.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_add_extension()</code> </p>
<p> <code>globus_gsi_proxy_handle_set_extensions()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_init_prime (<code>globus_gsi_proxy_handle_t</code>handle, int *init_prime)</h3>
<p> Get Init Prime. Get the init prime of the proxy handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to get the init prime used in generating the key pair<br />
 <i>init_prime</i> The resulting init prime</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case an error object identifier (in the form of a globus_result_t) is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_key_gen_callback (<code>globus_gsi_proxy_handle_t</code>handle, void(**)(int, int, void *)callback)</h3>
<p> Get Callback for Creating Keys. Get the callback for creating the public/private key pair </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The proxy handle to get the callback from<br />
 <i>callback</i> Parameter used for returning the callback</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_keybits (<code>globus_gsi_proxy_handle_t</code>handle, int *key_bits)</h3>
<p> Get Key Bits. Get the key bits used for the pub/private key pair of the proxy </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The proxy handle to get the key bits of<br />
 <i>key_bits</i> key bits of the proxy handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_pathlen (<code>globus_gsi_proxy_handle_t</code>handle, int *pathlen)</h3>
<p> Get Path Length. Get the path length from the GSI Proxy handle. </p>
<p> This function gets the path length that is being used in the proxy cert info extension. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be interrogated.<br />
 <i>pathlen</i> The maximum allowable path length</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle is valid, otherwise an error is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_set_pathlen()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_policy (<code>globus_gsi_proxy_handle_t</code>handle, unsigned char **policy_data, int *policy_length, int *policy_NID)</h3>
<p> Get Policy. Get the policy from the GSI Proxy handle. </p>
<p> This function gets the policy that is being used in the proxy cert info extension. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be interrogated.<br />
 <i>policy_data</i> The policy data.<br />
 <i>policy_length</i> The length of the returned policy<br />
 <i>policy_NID</i> The NID of the policy language.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle is valid, otherwise an error is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_set_policy()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_private_key (<code>globus_gsi_proxy_handle_t</code>handle, EVP_PKEY **proxy_key)</h3>
<p> Get the private key from a GSI Proxy handle. </p>
<pre>
Copies the private key associated with the proxy handle to the
value pointed to by the proxy_key parameter.
</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle from which to get the private key<br />
 <i>proxy_key</i> Parameter used to return the key. It is the users responsibility to free the returned key by calling EVP_PKEY_free().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_set_private_key()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_proxy_cert_info_openssl (<code>globus_gsi_proxy_handle_t</code>handle, PROXY_CERT_INFO_EXTENSION **pci)</h3>
<p> Get Cert Info. Get the proxy cert info extension stored in the GSI Proxy handle. </p>
<p> This function retrieves the proxy cert info extension from the GSI Proxy handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle from which to get the proxy cert info extension.<br />
 <i>pci</i> Contains the proxy cert info extension upon successful return. If the handle does not contain a pci extension, this parameter will be NULL upon return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS upon success GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE if handle is invalid GLOBUS_GSI_PROXY_ERROR_WITH_PROXYCERTINFO if the pci pointer is invalid or if the get failed.</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_req (<code>globus_gsi_proxy_handle_t</code>handle, X509_REQ **req)</h3>
<p> Get the certificate request from a GSI Proxy handle. </p>
<pre>
Copies the certificate request associated with the proxy handle to
the req parameter.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle from which to get the certificate request<br />
 <i>req</i> Parameter used to return the request. It is the users responsibility to free the returned request.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_set_req()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_signing_algorithm (<code>globus_gsi_proxy_handle_t</code>handle, const EVP_MD **signing_algorithm)</h3>
<p> Get Signing Algorithm. Get the signing algorithm used to sign the proxy cert request </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The proxy handle containing the type of signing algorithm used<br />
 <i>signing_algorithm</i> signing algorithm of the proxy handle</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_time_valid (<code>globus_gsi_proxy_handle_t</code>handle, int *time_valid)</h3>
<p> Get Time Valid. Get the validity time of the proxy </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The proxy handle to get the expiration date of<br />
 <i>time_valid</i> expiration date of the proxy handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_get_type (<code>globus_gsi_proxy_handle_t</code>handle, globus_gsi_cert_utils_cert_type_t *type)</h3>
<p> Get Proxy Type. Determine the type of proxy that will be generated when using this handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle from which to get the type<br />
 <i>type</i> Parameter used to return the type.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_set_type()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_init (<code>globus_gsi_proxy_handle_t</code> *handle, <code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs)</h3>
<p> Initialize a GSI Proxy handle. Initialize a proxy handle which can be used in subsequent operations. The handle may only be used in one sequence of operations at a time. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the handle to be initialized. If the handle is originally NULL, space is allocated for it. Otherwise, the current values of the handle are overwritten.<br />
 <i>handle_attrs</i> Initial attributes to be used to create this handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_destroy()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_extensions (<code>globus_gsi_proxy_handle_t</code>handle, STACK_OF(X509_EXTENSION)*exts)</h3>
<p> Set X.509 Extensions. Set the X.509 extensions from a GSI Proxy handle </p>
<p> This function sets the X.509 extensions for a proxy certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for the proxy from which the extension should be set.<br />
 <i>exts</i> The extensions to be set. Can be NULL to clear extensions.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the addition was successful, otherwise an error is returned.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_add_extension()</code> </p>
<p> <code>globus_gsi_proxy_handle_get_extensions()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_is_limited (<code>globus_gsi_proxy_handle_t</code>handle, globus_bool_tis_limited)</h3>
<p> Set/Check Proxy Is Limited. Set the limited proxy flag on the proxy handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the proxy handle<br />
 <i>is_limited</i> boolean value to set on the proxy handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_pathlen (<code>globus_gsi_proxy_handle_t</code>handle, longpathlen)</h3>
<p> Set Path Length. Set the path length to be used in the GSI Proxy handle. </p>
<p> This function sets the path length to be used in the proxy cert info extension. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be modified.<br />
 <i>pathlen</i> The maximum allowable path length</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle is valid, otherwise an error is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_get_pathlen()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_policy (<code>globus_gsi_proxy_handle_t</code>handle, const unsigned char *policy_data, intpolicy_length, intpolicy_language_NID)</h3>
<p> Set Policy. Set the policy to be used in the GSI Proxy handle. </p>
<p> This function sets the policy to be used in the proxy cert info extension. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be modified.<br />
 <i>policy_data</i> The policy data.<br />
 <i>policy_length</i> The length of the policy data<br />
 <i>policy_language_NID</i> The NID of the policy language.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle and its associated fields are valid otherwise an error is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_get_policy()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_proxy_cert_info_openssl (<code>globus_gsi_proxy_handle_t</code>handle, PROXY_CERT_INFO_EXTENSION *pci)</h3>
<p> Set Cert Info. Set the proxy cert info extension stored in the GSI Proxy handle. </p>
<p> This function sets the proxy cert info extension in the GSI Proxy handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for which to set the proxy cert info extension.<br />
 <i>pci</i> The proxy cert info extension to set.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE</i> Handle is invalid<br />
 <i>GLOBUS_GSI_PROXY_ERROR_WITH_PROXYCERTINFO</i> pci pointer is invalid or if the set failed.</dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_time_valid (<code>globus_gsi_proxy_handle_t</code>handle, inttime_valid)</h3>
<p> Set Time Valid. Set the validity time of the proxy </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The proxy handle to set the expiration date for<br />
 <i>time_valid</i> desired expiration date of the proxy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_type (<code>globus_gsi_proxy_handle_t</code>handle, globus_gsi_cert_utils_cert_type_ttype)</h3>
<p> Get Proxy Type. Set the type of proxy that will be generated when using this handle. Note that this will have no effect when generating a proxy from a proxy. In that case the generated proxy will inherit the type of the parent. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for which to set the type<br />
 <i>type</i> Parameter used to pass the type.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_set_type()</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_proxy_core from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbBG">Author</a></p>
<dd></dl>
