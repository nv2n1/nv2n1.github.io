---
title: "gnutls_pkcs11_get_raw_issuer(3)"
name: "gnutls_pkcs11_get_raw_issuer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_get_raw_issuer/"
description: "gnutls_pkcs11_get_raw_issuer – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_get_raw_issuer &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_get_raw_issuer(const char * </code><i>url</i><code>, gnutls_x509_crt_t </code><i>cert</i><code>, gnutls_datum_t * </code><i>issuer</i><code>, gnutls_x509_crt_fmt_t </code><i>fmt</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * url</p>
<dd> A PKCS 11 url identifying a token</p>
<dt>gnutls_x509_crt_t cert</p>
<dd> is the certificate to find issuer for</p>
<dt>gnutls_datum_t * issuer</p>
<dd> Will hold the issuer if any in an allocated buffer.</p>
<dt>gnutls_x509_crt_fmt_t fmt</p>
<dd> The format of the exported issuer.</p>
<dt>unsigned int flags</p>
<dd> Use zero or flags from <code>GNUTLS_PKCS11_OBJ_FLAG</code>.</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the issuer of a given certificate, if it is stored in the token. By default only marked as trusted issuers are retuned. If any issuer should be returned specify <code>GNUTLS_PKCS11_OBJ_FLAG_RETRIEVE_ANY</code> in <i>flags</i> .</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.2.7</p>
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
