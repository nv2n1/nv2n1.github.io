---
title: "globus_gsi_callback_x509_verify_cert(3)"
name: "globus_gsi_callback_x509_verify_cert"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_callback_x509_verify_cert/"
description: "Callback Functions –"
---

<p>Callback Functions &#8211; </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_gsi_callback_get_X509_STORE_callback_data_index</code> (int *index)<br />
 <i>Get callback data index from X509_STORE. </i><br />
 globus_result_t <code>globus_gsi_callback_get_SSL_callback_data_index</code> (int *index)<br />
 <i>Get callback data index from SSL structure. </i><br />
 int <code>globus_gsi_callback_X509_verify_cert</code> (X509_STORE_CTX *context, void *arg)<br />
 <i>Certificate verify wrapper. </i><br />
 int <code>globus_gsi_callback_create_proxy_callback</code> (int preverify_ok, X509_STORE_CTX *x509_context)<br />
 <i>Independent path validation callback. </i><br />
 int <code>globus_gsi_callback_handshake_callback</code> (int preverify_ok, X509_STORE_CTX *x509_context)<br />
 <i>SSL path validation callback. </i><br />
 int <code>globus_gsi_callback_check_issued</code> (X509_STORE_CTX *context, X509 *cert, X509 *issuer)<br />
 <i>OpenSSL X509_check_issued() wrapper. </i></p>
<h2>Detailed Description</h2>
<p>Functions that plug into various plug points in the OpenSSL path validation mechanism. These functions add CRL checking, X509 Extension handling and proxy validation.</p>
<h2>Function Documentation</h2>
<h3>int globus_gsi_callback_check_issued (X509_STORE_CTX *context, X509 *cert, X509 *issuer)</h3>
<p>OpenSSL X509_check_issued() wrapper. This function wraps the OpenSSL X509_check_issued() call and catches the error caused by the fact that a proxy certificate issuer may not have to have the correct KeyUsage fields set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The validation state object.<br />
 <i>cert</i> The certificate to check<br />
 <i>issuer</i> The issuer certificate to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success 0 on failure</dl>
<h3>int globus_gsi_callback_create_proxy_callback (intpreverify_ok, X509_STORE_CTX *x509_context)</h3>
<p>Independent path validation callback. This function provides a path validation callback for validation outside of a SSL session. It should be used in X509_STORE_set_verify_cb_func(). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>preverify_ok</i> Communicates the result of default validation steps performed by OpenSSL<br />
 <i>x509_context</i> The validation state object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success 0 on failure</dl>
<h3>globus_result_t globus_gsi_callback_get_SSL_callback_data_index (int *index)</h3>
<p>Get callback data index from SSL structure. Retrieve or create the index for our callback data structure in the SSL structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Will contain the index upon return</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_callback_get_X509_STORE_callback_data_index (int *index)</h3>
<p>Get callback data index from X509_STORE. Retrieve or create the index for our callback data structure in the X509_STORE. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Will contain the index upon return</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>int globus_gsi_callback_handshake_callback (intpreverify_ok, X509_STORE_CTX *x509_context)</h3>
<p>SSL path validation callback. This function provides a path validation callback for the validation part of establishing a SSL session. It handles proxy certificates, X509 Extensions and CRL checking. It should be used in SSL_CTX_set_verify(). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>preverify_ok</i> Communicates the result of default validation steps performed by OpenSSL<br />
 <i>x509_context</i> The validation state object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success 0 on failure</dl>
<h3>int globus_gsi_callback_X509_verify_cert (X509_STORE_CTX *context, void *arg)</h3>
<p>Certificate verify wrapper. This function wraps the OpenSSL certificate verification callback for the purpose of a replacing the standard issuer check with one that deals with proxy certificates. Should be used with SSL_CTX_set_cert_verify_callback() </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The X509_STORE_CTX for which to register the callback.<br />
 <i>arg</i> Arguments to the callback. Currently ignored.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success 0 on failure</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_callback from the source code.</p>
