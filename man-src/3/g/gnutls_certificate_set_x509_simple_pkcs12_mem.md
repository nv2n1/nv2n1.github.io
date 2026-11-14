---
title: "gnutls_certificate_set_x509_simple_pkcs12_mem(3)"
name: "gnutls_certificate_set_x509_simple_pkcs12_mem"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_x509_simple_pkcs12_mem/"
description: "gnutls_certificate_set_x509_simple_pkcs12_mem – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_x509_simple_pkcs12_mem &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_x509_simple_pkcs12_mem(gnutls_certificate_credentials_t </code><i>res</i><code>, const gnutls_datum_t * </code><i>p12blob</i><code>, gnutls_x509_crt_fmt_t </code><i>type</i><code>, const char * </code><i>password</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>const gnutls_datum_t * p12blob</p>
<dd> the PKCS<code>12</code> blob.</p>
<dt>gnutls_x509_crt_fmt_t type</p>
<dd> is PEM or DER of the <i>pkcs12file</i> .</p>
<dt>const char * password</p>
<dd> optional password used to decrypt PKCS<code>12</code> file, bags and keys.</dl>
<h2>DESCRIPTION</h2>
<p> This function sets a certificate/private key pair and/or a CRL in the gnutls_certificate_credentials_t structure. This function may be called more than once (in case multiple keys/certificates exist for the server). </p>
<p> Encrypted PKCS<code>12</code> bags and PKCS<code>8</code> private keys are supported. However, only password based security, and the same password for all operations, are supported. </p>
<p> PKCS<code>12</code> file may contain many keys and/or certificates, and this function will try to auto-detect based on the key ID the certificate and key pair to use. If the PKCS<code>12</code> file contain the issuer of the selected certificate, it will be appended to the certificate to form a chain. </p>
<p> If more than one private keys are stored in the PKCS<code>12</code> file, then only one key will be read (and it is undefined which one). </p>
<p> It is believed that the limitations of this function is acceptable for most usage, and that any more flexibility would introduce complexity that would make it harder to use this functionality at all.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success, or a negative error code.</p>
<h2>SINCE</h2>
<p> 2.8.0</p>
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
