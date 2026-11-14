---
title: "globus_gsi_cred_get_cert_type(3)"
name: "globus_gsi_cred_get_cert_type"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cred_get_cert_type/"
description: "Credential Operations –"
---

<h2 class="name">NAME</h2>
<p> Credential Operations &#8211; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_cred_read</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME *desired_subject)<br />
 <i>Read a credential. </i><br />
 globus_result_t <code>globus_gsi_cred_read_proxy</code> (<code>globus_gsi_cred_handle_t</code> handle, const char *proxy_filename)<br />
 <i>Read proxy credential. </i><br />
 globus_result_t <code>globus_gsi_cred_read_proxy_bio</code> (<code>globus_gsi_cred_handle_t</code> handle, BIO *bio)<br />
 <i>Read proxy credential from a BIO. </i><br />
 globus_result_t <code>globus_gsi_cred_read_key</code> (<code>globus_gsi_cred_handle_t</code> handle, const char *key_filename, int(*pw_cb)())<br />
 <i>Read a private key. </i><br />
 globus_result_t <code>globus_gsi_cred_read_cert</code> (<code>globus_gsi_cred_handle_t</code> handle, const char *cert_filename)<br />
 <i>Read a certificate chain from a file. </i><br />
 globus_result_t <code>globus_gsi_cred_read_cert_bio</code> (<code>globus_gsi_cred_handle_t</code> handle, BIO *bio)<br />
 <i>Read a certificate chain from a BIO. </i><br />
 globus_result_t <code>globus_gsi_cred_read_cert_buffer</code> (const char *pem_buf, <code>globus_gsi_cred_handle_t</code> *out_handle, X509 **out_cert, STACK_OF(X509)**out_cert_chain, char **out_subject)<br />
 <i>Read certificate chain from a buffer. </i><br />
 globus_result_t <code>globus_gsi_cred_read_pkcs12</code> (<code>globus_gsi_cred_handle_t</code> handle, const char *pkcs12_filename)<br />
 <i>Read certificate and key from a PKCS12 file. </i><br />
 globus_result_t <code>globus_gsi_cred_write</code> (<code>globus_gsi_cred_handle_t</code> handle, BIO *bio)<br />
 <i>Write Credential. </i><br />
 globus_result_t <code>globus_gsi_cred_write_proxy</code> (<code>globus_gsi_cred_handle_t</code> handle, const char *proxy_filename)<br />
 <i>Write a proxy credential. </i><br />
 globus_result_t <code>globus_gsi_cred_get_cert_type</code> (<code>globus_gsi_cred_handle_t</code> handle, globus_gsi_cert_utils_cert_type_t *type)<br />
 <i>Get the X.509 certificate type. </i></p>
<h2>Detailed Description</h2>
<p> Read/Write a GSI Credential Handle. </p>
<p> This section defines operations to read and write GSI Credential handles.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_cred_get_cert_type (<code>globus_gsi_cred_handle_t</code>handle, globus_gsi_cert_utils_cert_type_t *type)</h3>
<p> Get the X.509 certificate type. Determine the type of the given X509 certificate For the list of possible values returned, see globus_gsi_cert_utils_cert_type_t. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate<br />
 <i>type</i> The returned X509 certificate type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_read (<code>globus_gsi_cred_handle_t</code>handle, X509_NAME *desired_subject)</h3>
<p> Read a credential. Read a credential from a filesystem location. The credential to read will be determined by the search order specified in the handle attributes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to set. This credential handle should already be initialized using globus_gsi_cred_handle_init.<br />
 <i>desired_subject</i> The subject to check for when reading in a credential. The desired_subject should be either a exact match of the read cert&#8217;s subject or should just contain the /CN entry. If null, the credential read in is the first match based on the system configuration (paths and environment variables)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no errors occured, otherwise, an error object identifier is returned.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_cred_read_proxy()</code> </p>
<p> globus_gsi_cred_read_cert_and_key()</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function always searches for the desired credential. If you don&#8217;t want to perform a search, then don&#8217;t use this function. The search goes in the order of the handle attributes&#8217; search order.</dl>
<h3>globus_result_t globus_gsi_cred_read_cert (<code>globus_gsi_cred_handle_t</code>handle, const char *cert_filename)</h3>
<p> Read a certificate chain from a file. Read a cert from a file. Cert should be in PEM format. Will also read additional certificates as chain if present. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to set based on the certificate that is read<br />
 <i>cert_filename</i> the filename of the certificate to read</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_read_cert_bio (<code>globus_gsi_cred_handle_t</code>handle, BIO *bio)</h3>
<p> Read a certificate chain from a BIO. Read a cert from a BIO. Cert should be in PEM format. Will also read additional certificates as chain if present. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to set based on the certificate that is read<br />
 <i>bio</i> the bio to read the certificate from</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_read_cert_buffer (const char *pem_buf, <code>globus_gsi_cred_handle_t</code> *out_handle, X509 **out_cert, STACK_OF(X509)**out_cert_chain, char **out_subject)</h3>
<p> Read certificate chain from a buffer. Read a cert from a buffer. Cert should be in PEM format. Will also read additional certificates as chain if present. Any parameter besides pem_buf may be NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>pem_buf</i> The buffer containing the PEM formatted cert and chain.<br />
 <i>out_handle</i> The handle to initialize and set cert on.<br />
 <i>out_cert</i> The X509 certificate. This should be freed with X509_free().<br />
 <i>out_cert_chain</i> The X509 certificate chain. This should be freed with sk_X509_free().<br />
 <i>out_subject</i> The identity name of the cert. This should be freed with OPENSSL_free().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_read_key (<code>globus_gsi_cred_handle_t</code>handle, const char *key_filename, int(*)()pw_cb)</h3>
<p> Read a private key. Read a key from a PEM file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to set based on the key that is read<br />
 <i>key_filename</i> the filename of the key to read<br />
 <i>pw_cb</i> the callback for obtaining a password for decrypting the key.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_read_pkcs12 (<code>globus_gsi_cred_handle_t</code>handle, const char *pkcs12_filename)</h3>
<p> Read certificate and key from a PKCS12 file. Read a cert and key from a file. The file should be in PKCS12 format. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to populate with the read credential<br />
 <i>pkcs12_filename</i> the filename containing the credential to read</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_read_proxy (<code>globus_gsi_cred_handle_t</code>handle, const char *proxy_filename)</h3>
<p> Read proxy credential. Read a proxy from a PEM file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to set based on the proxy credential read from the file<br />
 <i>proxy_filename</i> The file containing the proxy credential</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_read_proxy_bio (<code>globus_gsi_cred_handle_t</code>handle, BIO *bio)</h3>
<p> Read proxy credential from a BIO. Read a Proxy Credential from a BIO stream and set the credential handle to represent the read credential. The values read from the stream, in order, will be the signed certificate, the private key, and the certificate chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to set. The credential should handle be initialized (i.e. not NULL).<br />
 <i>bio</i> The stream to read the credential from</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case an error object is returned</dl>
<h3>globus_result_t globus_gsi_cred_write (<code>globus_gsi_cred_handle_t</code>handle, BIO *bio)</h3>
<p> Write Credential. Write out a credential to a BIO. The credential parameters written, in order, are the signed certificate, the RSA private key, and the certificate chain (a set of X509 certificates). the credential is written out in PEM format. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential to write out<br />
 <i>bio</i> The BIO stream to write out to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case an error object ID is returned.</dl>
<h3>globus_result_t globus_gsi_cred_write_proxy (<code>globus_gsi_cred_handle_t</code>handle, const char *proxy_filename)</h3>
<p> Write a proxy credential. Write out a credential to a file. The credential parameters written, in order, are the signed certificate, the RSA private key, and the certificate chain (a set of X509 certificates). the credential is written out in PEM format. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential to write out<br />
 <i>proxy_filename</i> The file to write out to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case an error object ID is returned.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_credential from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">Author</a></p>
<dd></dl>
