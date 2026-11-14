---
title: "gnutls_x509_crt_verify(3)"
name: "gnutls_x509_crt_verify"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_verify/"
description: "gnutls_x509_crt_verify – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_verify &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_verify(gnutls_x509_crt_t </code><i>cert</i><code>, const gnutls_x509_crt_t * </code><i>CA_list</i><code>, int </code><i>CA_list_length</i><code>, unsigned int </code><i>flags</i><code>, unsigned int * </code><i>verify</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> is the certificate to be verified</p>
<dt>const gnutls_x509_crt_t * CA_list</p>
<dd> is one certificate that is considered to be trusted one</p>
<dt>int CA_list_length</p>
<dd> holds the number of CA certificate in CA_list</p>
<dt>unsigned int flags</p>
<dd> Flags that may be used to change the verification algorithm. Use OR of the gnutls_certificate_verify_flags enumerations.</p>
<dt>unsigned int * verify</p>
<dd> will hold the certificate verification output.</dl>
<h2>DESCRIPTION</h2>
<p> This function will try to verify the given certificate and return its status. Note that a verification error does not imply a negative return status. In that case the <i>verify</i> status is set.</p>
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
