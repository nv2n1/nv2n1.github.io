---
title: "gnutls_x509_trust_list_verify_crt2(3)"
name: "gnutls_x509_trust_list_verify_crt2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_verify_crt2/"
description: "gnutls_x509_trust_list_verify_crt2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_verify_crt2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_verify_crt2(gnutls_x509_trust_list_t </code><i>list</i><code>, gnutls_x509_crt_t * </code><i>cert_list</i><code>, unsigned int </code><i>cert_list_size</i><code>, gnutls_typed_vdata_st * </code><i>data</i><code>, unsigned int </code><i>elements</i><code>, unsigned int </code><i>flags</i><code>, unsigned int * </code><i>voutput</i><code>, gnutls_verify_output_function </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>gnutls_x509_crt_t * cert_list</p>
<dd> is the certificate list to be verified</p>
<dt>unsigned int cert_list_size</p>
<dd> is the certificate list size</p>
<dt>gnutls_typed_vdata_st * data</p>
<dd> an array of typed data</p>
<dt>unsigned int elements</p>
<dd> the number of data elements</p>
<dt>unsigned int flags</p>
<dd> Flags that may be used to change the verification algorithm. Use OR of the gnutls_certificate_verify_flags enumerations.</p>
<dt>unsigned int * voutput</p>
<dd> will hold the certificate verification output.</p>
<dt>gnutls_verify_output_function func</p>
<dd> If non-null will be called on each chain element verification with the output.</dl>
<h2>DESCRIPTION</h2>
<p> This function will try to verify the given certificate and return its status. The <i>verify</i> parameter will hold an OR&#8217;ed sequence of <code>gnutls_certificate_status_t</code> flags. </p>
<p> Additionally a certificate verification profile can be specified from the ones in <code>gnutls_certificate_verification_profiles_t</code> by ORing the result of <code>GNUTLS_PROFILE_TO_VFLAGS()</code> to the verification flags. </p>
<p> The acceptable <i>data</i> types are <code>GNUTLS_DT_DNS_HOSTNAME</code> and <code>GNUTLS_DT_KEY_PURPOSE_OID</code>. The former accepts as data a null-terminated hostname, and the latter a null-terminated object identifier (e.g., <code>GNUTLS_KP_TLS_WWW_SERVER</code>). If a DNS hostname is provided then this function will compare the hostname in the certificate against the given. If names do not match the <code>GNUTLS_CERT_UNEXPECTED_OWNER</code> status flag will be set. If a key purpose OID is provided and the end-certificate contains the extended key usage PKIX extension, it will be required to be have the provided key purpose or be marked for any purpose, otherwise verification will fail with <code>GNUTLS_CERT_SIGNER_CONSTRAINTS_FAILURE</code> status.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value. Note that verification failure will not result to an error code, only <i>voutput</i> will be updated.</p>
<h2>SINCE</h2>
<p> 3.3.8</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
