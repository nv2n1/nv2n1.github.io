---
title: "globus_gsi_cert_utils_make_time(3)"
name: "globus_gsi_cert_utils_make_time"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cert_utils_make_time/"
description: "Globus GSI Certificate Handling Utilities –"
---

<h2 class="name">NAME</h2>
<p> Globus GSI Certificate Handling Utilities &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<p> <code>Cert Utils Constants</code> </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_cert_utils_make_time</code> (const ASN1_UTCTIME *ctm, time_t *newtime)<br />
 <i>Convert ASN1_UTCTIME to time_t. </i><br />
 globus_result_t <code>globus_gsi_cert_utils_get_cert_type</code> (X509 *cert, <code>globus_gsi_cert_utils_cert_type_t</code> *type)<br />
 <i>Get the X509 certificate type. </i><br />
 globus_result_t <code>globus_gsi_cert_utils_get_x509_name</code> (const char *subject_string, int length, X509_NAME *x509_name)<br />
 <i>Get the certificate name. </i><br />
 globus_result_t <code>globus_gsi_cert_utils_get_base_name</code> (X509_NAME *subject, STACK_OF(X509)*cert_chain)<br />
 <i>Get the base certificate name from a certificate chain. </i><br />
 globus_result_t <code>globus_gsi_cert_utils_get_eec</code> (STACK_OF(X509)*cert_chain, X509 **eec)<br />
 <i>Get the end-entity certificate from a certificate chain. </i><br />
 globus_result_t <code>globus_gsi_cert_utils_get_identity_cert</code> (STACK_OF(X509)*cert_chain, X509 **identity_cert)<br />
 <i>Get the identity certificate from a certificate chain. </i></p>
<h2>Detailed Description</h2>
<p> The Globus GSI Certificate Handling Utilities library. This library contains helper functions for dealing with certificates. </p>
<dl>
<dt>&bull;</p>
<dd> <code>Activation</code></p>
<dt>&bull;</p>
<dd> <code>Globus GSI Certificate Handling Utilities</code></p>
<dt>&bull;</p>
<dd> <code>Cert Utils Constants</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_cert_utils_get_base_name (X509_NAME *subject, STACK_OF(X509)*cert_chain)</h3>
<p> Get the base certificate name from a certificate chain. Get the base name of a proxy certificate. Given an X509 name, strip off the proxy related /CN components to get the base name of the certificate&#8217;s subject </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>subject</i> Pointer to an X509_NAME object which gets stripped<br />
 <i>cert_chain</i> The certificate chain used to detect the number of CNs to strip. This is done by figuring out the number of proxies in the chain.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_cert_utils_get_cert_type (X509 *cert, <code>globus_gsi_cert_utils_cert_type_t</code> *type)</h3>
<p> Get the X509 certificate type. Determine the type of the given X509 certificate For the list of possible values returned, see globus_gsi_cert_utils_cert_type_t. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cert</i> The X509 certificate<br />
 <i>type</i> The returned X509 certificate type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cert_utils_get_eec (STACK_OF(X509)*cert_chain, X509 **eec)</h3>
<p> Get the end-entity certificate from a certificate chain. Get the end-entity certificate associated with a certificate chain </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cert_chain</i> Certificate chain to inspect.<br />
 <i>eec</i> Pointer to be set to the EEC value from within the cert chain. Must freed by the caller.</dl>
<h3>globus_result_t globus_gsi_cert_utils_get_identity_cert (STACK_OF(X509)*cert_chain, X509 **identity_cert)</h3>
<p> Get the identity certificate from a certificate chain. Get the identity-providing certificate associated with a certificate chain. This may be an independent proxy or a end-entity certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cert_chain</i> Certificate chain to inspect.<br />
 <i>identity_cert</i> Pointer to be set to the certificate value from within the cert chain. Must freed by the caller.</dl>
<h3>globus_result_t globus_gsi_cert_utils_get_x509_name (const char *subject_string, intlength, X509_NAME *x509_name)</h3>
<p> Get the certificate name. Get the X509_NAME from a subject string. OpenSSL doesn&#8217;t provide this function, probably because it shouldn&#8217;t be used. If you are getting an X509_NAME from just a string, its impossible to verify its integrity. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>subject_string</i> The subject in the format: &#8216;/O=Grid/OU=&#8230;&#8217;<br />
 <i>length</i> The length of the subject string<br />
 <i>x509_name</i> The resulting X509_NAME object</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<h3>globus_result_t globus_gsi_cert_utils_make_time (const ASN1_UTCTIME *ctm, time_t *newtime)</h3>
<p> Convert ASN1_UTCTIME to time_t. Convert a ASN1_UTCTIME structure to a time_t </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctm</i> The ASN1_UTCTIME to convert<br />
 <i>newtime</i> The converted time</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_cert_utils from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
