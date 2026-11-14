---
title: "globus_gsi_credential-h(3)"
name: "globus_gsi_credential-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_credential-h/"
description: "globus_gsi_credential.h –"
---

<p>globus_gsi_credential.h &#8211; </p>
<p> Globus GSI Credential Library.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_error_openssl.h&#8217;<br />
 #include &#8216;globus_gsi_cred_constants.h&#8217;<br />
 #include &#8216;globus_gsi_callback.h&#8217;<br />
 #include &#8216;globus_gsi_cert_utils.h&#8217;<br />
 #include &#8216;openssl/x509.h&#8217;<br />
 #include &#8216;openssl/bio.h&#8217;<br />
 #include &#8216;openssl/ssl.h&#8217;<br />
 #include &#8216;globus_error_generic.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_CREDENTIAL_MODULE</code> </p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 globus_l_gsi_cred_handle_s * <code>globus_gsi_cred_handle_t</code>&quot; </p>
<p> typedef struct<br />
 globus_l_gsi_cred_handle_attrs_s * <code>globus_gsi_cred_handle_attrs_t</code>&quot; </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_gsi_cred_handle_init</code> (<code>globus_gsi_cred_handle_t</code> *handle, <code>globus_gsi_cred_handle_attrs_t</code> handle_attrs)<br />
 <i>Initialize a Handle. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_destroy</code> (<code>globus_gsi_cred_handle_t</code> handle)<br />
 <i>Destroy the credential handle. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_copy</code> (<code>globus_gsi_cred_handle_t</code> source, <code>globus_gsi_cred_handle_t</code> *dest)<br />
 <i>Copy a handle. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_init</code> (<code>globus_gsi_cred_handle_attrs_t</code> *handle_attrs)<br />
 <i>Initialize credential handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_destroy</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs)<br />
 <i>Destroy credential handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_copy</code> (<code>globus_gsi_cred_handle_attrs_t</code> source, <code>globus_gsi_cred_handle_attrs_t</code> *dest)<br />
 <i>Copy credential handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_read</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME *desired_subject)<br />
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
 globus_result_t <code>globus_gsi_cred_verify_cert_chain</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, globus_gsi_callback_data_t callback_data)<br />
 <i>Verify credential. </i><br />
 globus_result_t <code>globus_gsi_cred_verify_cert_chain_when</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, globus_gsi_callback_data_t callback_data, time_t check_time)<br />
 <i>Verify credential at a specific time. </i><br />
 globus_result_t <code>globus_gsi_cred_verify</code> (<code>globus_gsi_cred_handle_t</code> handle)<br />
 <i>Verify a credential. </i><br />
 globus_result_t <code>globus_gsi_cred_get_X509_subject_name</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME **subject_name)<br />
 <i>Get credential subject name. </i><br />
 globus_result_t <code>globus_gsi_cred_get_subject_name</code> (<code>globus_gsi_cred_handle_t</code> handle, char **subject_name)<br />
 <i>Get credential subject name. </i><br />
 globus_result_t <code>globus_gsi_cred_get_policies</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK **policies)<br />
 <i>Get certificate chain policies. </i><br />
 globus_result_t <code>globus_gsi_cred_get_policy_languages</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK_OF(ASN1_OBJECT)**languages)<br />
 <i>Get certificate chain policy languages. </i><br />
 globus_result_t <code>globus_gsi_cred_get_X509_issuer_name</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME **issuer_name)<br />
 <i>Get credential issuer name object. </i><br />
 globus_result_t <code>globus_gsi_cred_get_issuer_name</code> (<code>globus_gsi_cred_handle_t</code> handle, char **issuer_name)<br />
 <i>Get issuer name. </i><br />
 globus_result_t <code>globus_gsi_cred_get_X509_identity_name</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME **identity_name)<br />
 <i>Get X.509 identity. </i><br />
 globus_result_t <code>globus_gsi_cred_get_identity_name</code> (<code>globus_gsi_cred_handle_t</code> handle, char **identity_name)<br />
 <i>Get identity name. </i><br />
 globus_result_t <code>globus_gsi_cred_set_cert</code> (<code>globus_gsi_cred_handle_t</code> handle, X509 *cert)<br />
 <i>Set the credential&#8217;s certificate. </i><br />
 globus_result_t <code>globus_gsi_cred_set_key</code> (<code>globus_gsi_cred_handle_t</code> handle, EVP_PKEY *key)<br />
 <i>Set the credential&#8217;s private key. </i><br />
 globus_result_t <code>globus_gsi_cred_set_cert_chain</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK_OF(X509)*cert_chain)<br />
 <i>Set the certificate chain. </i><br />
 globus_result_t <code>globus_gsi_cred_get_cert</code> (<code>globus_gsi_cred_handle_t</code> handle, X509 **cert)<br />
 <i>Get the credential&#8217;s certificate. </i><br />
 globus_result_t <code>globus_gsi_cred_get_key</code> (<code>globus_gsi_cred_handle_t</code> handle, EVP_PKEY **key)<br />
 <i>Get the credential&#8217;s private key. </i><br />
 globus_result_t <code>globus_gsi_cred_get_cert_chain</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK_OF(X509)**cert_chain)<br />
 <i>Get the certificate chain. </i><br />
 globus_result_t <code>globus_gsi_cred_get_handle_attrs</code> (<code>globus_gsi_cred_handle_t</code> handle, <code>globus_gsi_cred_handle_attrs_t</code> *handle_attrs)<br />
 <i>Get the handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_get_lifetime</code> (<code>globus_gsi_cred_handle_t</code> handle, time_t *lifetime)<br />
 <i>Get credential lifetime. </i><br />
 globus_result_t <code>globus_gsi_cred_get_goodtill</code> (<code>globus_gsi_cred_handle_t</code> handle, time_t *goodtill)<br />
 <i>Get credential expiration. </i><br />
 globus_result_t <code>globus_gsi_cred_get_cert_type</code> (<code>globus_gsi_cred_handle_t</code> handle, globus_gsi_cert_utils_cert_type_t *type)<br />
 <i>Get the X.509 certificate type. </i><br />
 globus_result_t <code>globus_gsi_cred_get_key_bits</code> (<code>globus_gsi_cred_handle_t</code> handle, int *key_bits)<br />
 <i>Get credential strength. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_set_search_order</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs, <code>globus_gsi_cred_type_t</code> search_order[])<br />
 <i>Set the search order. </i></p>
<h2>Detailed Description</h2>
<p>Globus GSI Credential Library. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Sam Lang, Sam Meder</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_credential from the source code.</p>
