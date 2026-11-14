---
title: "gnutls_x509_crt_list_verify(3)"
name: "gnutls_x509_crt_list_verify"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_list_verify/"
description: "gnutls_x509_crt_list_verify – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_list_verify &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_list_verify(const gnutls_x509_crt_t * </code><i>cert_list</i><code>, int </code><i>cert_list_length</i><code>, const gnutls_x509_crt_t * </code><i>CA_list</i><code>, int </code><i>CA_list_length</i><code>, const gnutls_x509_crl_t * </code><i>CRL_list</i><code>, int </code><i>CRL_list_length</i><code>, unsigned int </code><i>flags</i><code>, unsigned int * </code><i>verify</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const gnutls_x509_crt_t * cert_list</p>
<dd> is the certificate list to be verified</p>
<dt>int cert_list_length</p>
<dd> holds the number of certificate in cert_list</p>
<dt>const gnutls_x509_crt_t * CA_list</p>
<dd> is the CA list which will be used in verification</p>
<dt>int CA_list_length</p>
<dd> holds the number of CA certificate in CA_list</p>
<dt>const gnutls_x509_crl_t * CRL_list</p>
<dd> holds a list of CRLs.</p>
<dt>int CRL_list_length</p>
<dd> the length of CRL list.</p>
<dt>unsigned int flags</p>
<dd> Flags that may be used to change the verification algorithm. Use OR of the gnutls_certificate_verify_flags enumerations.</p>
<dt>unsigned int * verify</p>
<dd> will hold the certificate verification output.</dl>
<h2>DESCRIPTION</h2>
<p> This function will try to verify the given certificate list and return its status. If no flags are specified (0), this function will use the basicConstraints (2.5.29.19) PKIX extension. This means that only a certificate authority is allowed to sign a certificate. </p>
<p> You must also check the peer&#8217;s name in order to check if the verified certificate belongs to the actual peer. </p>
<p> The certificate verification output will be put in <i>verify</i> and will be one or more of the gnutls_certificate_status_t enumerated elements bitwise or&#8217;d. For a more detailed verification status use <code>gnutls_x509_crt_verify()</code> per list element.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
