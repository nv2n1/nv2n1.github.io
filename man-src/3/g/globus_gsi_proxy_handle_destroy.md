---
title: "globus_gsi_proxy_handle_destroy(3)"
name: "globus_gsi_proxy_handle_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_proxy_handle_destroy/"
description: "globus_gsi_proxy.h – Globus GSI Proxy API."
---

<h2 class="name">NAME</h2>
<p> globus_gsi_proxy.h &#8211; Globus GSI Proxy API.</p>
<h2>SYNOPSIS</h2>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GSI_PROXY_MODULE</code><br />
 <i>Module descriptor. </i></p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_gsi_proxy_handle_s * <code>globus_gsi_proxy_handle_t</code>&quot;<br />
 <i>GSI Proxy Handle. </i><br />
 typedef struct<br />
 globus_l_gsi_proxy_handle_attrs_s * <code>globus_gsi_proxy_handle_attrs_t</code>&quot;<br />
 <i>Handle Attributes. </i></p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_proxy_handle_init</code> (<code>globus_gsi_proxy_handle_t</code> *handle, <code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs)<br />
 <i>Initialize a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_destroy</code> (<code>globus_gsi_proxy_handle_t</code> handle)<br />
 <i>Destroy a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_req</code> (<code>globus_gsi_proxy_handle_t</code> handle, X509_REQ **req)<br />
 <i>Get the certificate request from a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_req</code> (<code>globus_gsi_proxy_handle_t</code> handle, X509_REQ *req)<br />
 <i>Set Request Set the certificate request in a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_private_key</code> (<code>globus_gsi_proxy_handle_t</code> handle, EVP_PKEY **proxy_key)<br />
 <i>Get the private key from a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_private_key</code> (<code>globus_gsi_proxy_handle_t</code> handle, const EVP_PKEY *proxy_key)<br />
 <i>Set the private key in a GSI Proxy handle. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_type</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cert_utils_cert_type_t *type)<br />
 <i>Get Proxy Type. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_type</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cert_utils_cert_type_t type)<br />
 <i>Get Proxy Type. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_time_valid</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *time_valid)<br />
 <i>Get Time Valid. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_time_valid</code> (<code>globus_gsi_proxy_handle_t</code> handle, int time_valid)<br />
 <i>Set Time Valid. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_policy</code> (<code>globus_gsi_proxy_handle_t</code> handle, const unsigned char *policy_data, int policy_length, int policy_NID)<br />
 <i>Set Policy. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_policy</code> (<code>globus_gsi_proxy_handle_t</code> handle, unsigned char **policy_data, int *policy_length, int *policy_NID)<br />
 <i>Get Policy. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_add_extension</code> (<code>globus_gsi_proxy_handle_t</code> handle, X509_EXTENSION *extension)<br />
 <i>Add X.509 Extensions. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_extensions</code> (<code>globus_gsi_proxy_handle_t</code> handle, STACK_OF(X509_EXTENSION)*extensions)<br />
 <i>Set X.509 Extensions. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_extensions</code> (<code>globus_gsi_proxy_handle_t</code> handle, STACK_OF(X509_EXTENSION)**extension)<br />
 <i>Get X.509 Extensions. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_pathlen</code> (<code>globus_gsi_proxy_handle_t</code> handle, long pathlen)<br />
 <i>Set Path Length. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_pathlen</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *pathlen)<br />
 <i>Get Path Length. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_clear_cert_info</code> (<code>globus_gsi_proxy_handle_t</code> handle)<br />
 <i>Clear Cert Info. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_common_name</code> (<code>globus_gsi_proxy_handle_t</code> handle, char **common_name)<br />
 <i>Get/Set Proxy Common Name. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_set_common_name</code> (<code>globus_gsi_proxy_handle_t</code> handle, const char *common_name) </p>
<p> globus_result_t <code>globus_gsi_proxy_is_limited</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_bool_t *is_limited) </p>
<p> globus_result_t <code>globus_gsi_proxy_handle_set_is_limited</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_bool_t is_limited)<br />
 <i>Set/Check Proxy Is Limited. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_signing_algorithm</code> (<code>globus_gsi_proxy_handle_t</code> handle, const EVP_MD **algorithm)<br />
 <i>Get Signing Algorithm. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_keybits</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *key_bits)<br />
 <i>Get Key Bits. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_init_prime</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *init_prime)<br />
 <i>Get Init Prime. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_clock_skew_allowable</code> (<code>globus_gsi_proxy_handle_t</code> handle, int *skew)<br />
 <i>Get Clock Skew. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_get_key_gen_callback</code> (<code>globus_gsi_proxy_handle_t</code> handle, void(**callback)(int, int, void *))<br />
 <i>Get Callback for Creating Keys. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_init</code> (<code>globus_gsi_proxy_handle_attrs_t</code> *handle_attrs)<br />
 <i>Initialize Attributes. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_destroy</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs)<br />
 <i>Destroy attributes. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_copy</code> (<code>globus_gsi_proxy_handle_attrs_t</code> a, <code>globus_gsi_proxy_handle_attrs_t</code> *b)<br />
 <i>Copy Attributes. </i><br />
 globus_result_t <code>globus_gsi_proxy_create_req</code> (<code>globus_gsi_proxy_handle_t</code> handle, BIO *output_bio)<br />
 <i>Create a proxy credential request. </i><br />
 globus_result_t <code>globus_gsi_proxy_inquire_req</code> (<code>globus_gsi_proxy_handle_t</code> handle, BIO *input_bio)<br />
 <i>Inquire a proxy credential request. </i><br />
 globus_result_t <code>globus_gsi_proxy_sign_req</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cred_handle_t issuer_credential, BIO *output_bio)<br />
 <i>Sign a proxy certificate request. </i><br />
 globus_result_t <code>globus_gsi_proxy_resign_cert</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cred_handle_t issuer_credential, globus_gsi_cred_handle_t peer_credential, globus_gsi_cred_handle_t *resigned_credential)<br />
 <i>Resign an existing certificate into a proxy. </i><br />
 globus_result_t <code>globus_gsi_proxy_assemble_cred</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cred_handle_t *proxy_credential, BIO *input_bio)<br />
 <i>Assemble a proxy credential. </i><br />
 globus_result_t <code>globus_gsi_proxy_create_signed</code> (<code>globus_gsi_proxy_handle_t</code> handle, globus_gsi_cred_handle_t issuer, globus_gsi_cred_handle_t *proxy_credential)<br />
 <i>Create Signed Proxy Certificate. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_keybits</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int bits)<br />
 <i>Set Key Bits. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_keybits</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int *bits)<br />
 <i>Get Key Bits. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_init_prime</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int prime)<br />
 <i>Set Initial Prime Number. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_init_prime</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int *prime)<br />
 <i>Get Initial Prime Number. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_signing_algorithm</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, const EVP_MD *algorithm)<br />
 <i>Set Signing Algorithm. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_signing_algorithm</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, const EVP_MD **algorithm)<br />
 <i>Get Signing Algorithm. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_clock_skew_allowable</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle, int skew)<br />
 <i>Set Clock Skew Allowable. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_clock_skew_allowable</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle, int *skew)<br />
 <i>Get Clock Skew Allowable. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_key_gen_callback</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle, void(**callback)(int, int, void *))<br />
 <i>Get Key Gen Callback. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_key_gen_callback</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle, void(*callback)(int, int, void *))<br />
 <i>Set Key Gen Callback. </i></p>
<h2>Detailed Description</h2>
<p> Globus GSI Proxy API. </p>
<p> Globus GSI Proxy API</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_proxy_handle_destroy (<code>globus_gsi_proxy_handle_t</code>handle)</h3>
<p> Destroy a GSI Proxy handle. </p>
<pre>
Free the memory used by a GSI proxy handle.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be destroyed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_init()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_common_name (<code>globus_gsi_proxy_handle_t</code>handle, const char *common_name)</h3>
<p> Set the proxy common name stored in the GSI Proxy handle. </p>
<p> This function sets the proxy common name in the GSI Proxy handle. Note that the common name is only used for draft compliant proxies. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for which to set the proxy common name.<br />
 <i>common_name</i> The proxy common name to set.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS upon success GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE if handle is invalid</dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_private_key (<code>globus_gsi_proxy_handle_t</code>handle, const EVP_PKEY *proxy_key)</h3>
<p> Set the private key in a GSI Proxy handle. </p>
<pre>
Copies the private key pointed to by proxy_key to the 
handle.
</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for which to set the private key<br />
 <i>proxy_key</i> Parameter used to pass the key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_get_private_key()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_set_req (<code>globus_gsi_proxy_handle_t</code>handle, X509_REQ *req)</h3>
<p> Set Request Set the certificate request in a GSI Proxy handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle for which to set the certificate request<br />
 <i>req</i> Request to be copied to handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_get_req()</code></dl>
<h3>globus_result_t globus_gsi_proxy_is_limited (<code>globus_gsi_proxy_handle_t</code>handle, globus_bool_t *is_limited)</h3>
<p> Check to see the proxy is a limited proxy </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the proxy handle to check<br />
 <i>is_limited</i> boolean value to set depending on the type of proxy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_proxy_core from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
