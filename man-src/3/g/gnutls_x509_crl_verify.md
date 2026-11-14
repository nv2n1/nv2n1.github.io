---
title: "gnutls_x509_crl_verify(3)"
name: "gnutls_x509_crl_verify"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_verify/"
description: "gnutls_x509_crl_verify – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_verify &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_verify(gnutls_x509_crl_t </code><i>crl</i><code>, const gnutls_x509_crt_t * </code><i>trusted_cas</i><code>, int </code><i>tcas_size</i><code>, unsigned int </code><i>flags</i><code>, unsigned int * </code><i>verify</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> is the crl to be verified</p>
<dt>const gnutls_x509_crt_t * trusted_cas</p>
<dd> is a certificate list that is considered to be trusted one</p>
<dt>int tcas_size</p>
<dd> holds the number of CA certificates in CA_list</p>
<dt>unsigned int flags</p>
<dd> Flags that may be used to change the verification algorithm. Use OR of the gnutls_certificate_verify_flags enumerations.</p>
<dt>unsigned int * verify</p>
<dd> will hold the crl verification output.</dl>
<h2>DESCRIPTION</h2>
<p> This function will try to verify the given crl and return its verification status. See <code>gnutls_x509_crt_list_verify()</code> for a detailed description of return values. Note that since GnuTLS 3.1.4 this function includes the time checks. </p>
<p> Note that value in <i>verify</i> is set only when the return value of this function is success (i.e, failure to trust a CRL a certificate does not imply a negative return value).</p>
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
