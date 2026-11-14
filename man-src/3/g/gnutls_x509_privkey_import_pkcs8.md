---
title: "gnutls_x509_privkey_import_pkcs8(3)"
name: "gnutls_x509_privkey_import_pkcs8"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_privkey_import_pkcs8/"
description: "gnutls_x509_privkey_import_pkcs8 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_privkey_import_pkcs8 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_privkey_import_pkcs8(gnutls_x509_privkey_t </code><i>key</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, const char * </code><i>password</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_privkey_t key</p>
<dd> The structure to store the parsed key</p>
<dt>const gnutls_datum_t * data</p>
<dd> The DER or PEM encoded key.</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> One of DER or PEM</p>
<dt>const char * password</p>
<dd> the password to decrypt the key (if it is encrypted).</p>
<dt>unsigned int flags</p>
<dd> 0 if encrypted or GNUTLS_PKCS_PLAIN if not encrypted.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given DER or PEM encoded PKCS8 2.0 encrypted key to the native gnutls_x509_privkey_t format. The output will be stored in <i>key</i> . Both RSA and DSA keys can be imported, and flags can only be used to indicate an unencrypted key. </p>
<p> The <i>password</i> can be either ASCII or UTF-8 in the default PBES2 encryption schemas, or ASCII for the PKCS12 schemas. </p>
<p> If the Certificate is PEM encoded it should have a header of &quot;ENCRYPTED PRIVATE KEY&quot;, or &quot;PRIVATE KEY&quot;. You only need to specify the flags if the key is DER encoded, since in that case the encryption status cannot be auto-detected. </p>
<p> If the <code>GNUTLS_PKCS_PLAIN</code> flag is specified and the supplied data are encrypted then <code>GNUTLS_E_DECRYPTION_FAILED</code> is returned.</p>
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
