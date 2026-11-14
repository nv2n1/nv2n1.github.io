---
title: "gnutls_certificate_set_x509_key_mem2(3)"
name: "gnutls_certificate_set_x509_key_mem2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_x509_key_mem2/"
description: "gnutls_certificate_set_x509_key_mem2 – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_x509_key_mem2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_x509_key_mem2(gnutls_certificate_credentials_t </code><i>res</i><code>, const gnutls_datum_t * </code><i>cert</i><code>, const gnutls_datum_t * </code><i>key</i><code>, gnutls_x509_crt_fmt_t </code><i>type</i><code>, const char * </code><i>pass</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>const gnutls_datum_t * cert</p>
<dd> contains a certificate list (path) for the specified private key</p>
<dt>const gnutls_datum_t * key</p>
<dd> is the private key, or <code>NULL</code></p>
<dt>gnutls_x509_crt_fmt_t type</p>
<dd> is PEM or DER</p>
<dt>const char * pass</p>
<dd> is the key&#8217;s password</p>
<dt>unsigned int flags</p>
<dd> an ORed sequence of gnutls_pkcs_encrypt_flags_t</dl>
<h2>DESCRIPTION</h2>
<p> This function sets a certificate/private key pair in the gnutls_certificate_credentials_t structure. This function may be called more than once, in case multiple keys/certificates exist for the server. </p>
<p> Note that the keyUsage (2.5.29.15) PKIX extension in X.509 certificates is supported. This means that certificates intended for signing cannot be used for ciphersuites that require encryption. </p>
<p> If the certificate and the private key are given in PEM encoding then the strings that hold their values must be null terminated. </p>
<p> The <i>key</i> may be <code>NULL</code> if you are using a sign callback, see <code>gnutls_sign_callback_set()</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success, or a negative error code.</p>
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
