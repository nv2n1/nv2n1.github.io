---
title: "gnutls_certificate_get_issuer(3)"
name: "gnutls_certificate_get_issuer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_get_issuer/"
description: "gnutls_certificate_get_issuer – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_get_issuer &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_get_issuer(gnutls_certificate_credentials_t </code><i>sc</i><code>, gnutls_x509_crt_t </code><i>cert</i><code>, gnutls_x509_crt_t * </code><i>issuer</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t sc</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>gnutls_x509_crt_t cert</p>
<dd> is the certificate to find issuer for</p>
<dt>gnutls_x509_crt_t * issuer</p>
<dd> Will hold the issuer if any. Should be treated as constant.</p>
<dt>unsigned int flags</p>
<dd> Use zero or <code>GNUTLS_TL_GET_COPY</code></dl>
<h2>DESCRIPTION</h2>
<p> This function will return the issuer of a given certificate. As with <code>gnutls_x509_trust_list_get_issuer()</code> this function requires the <code>GNUTLS_TL_GET_COPY</code> flag in order to operate with PKCS <code>11</code> trust lists. In that case the issuer must be freed using <code>gnutls_x509_crt_deinit()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
