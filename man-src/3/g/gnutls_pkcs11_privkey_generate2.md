---
title: "gnutls_pkcs11_privkey_generate2(3)"
name: "gnutls_pkcs11_privkey_generate2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_privkey_generate2/"
description: "gnutls_pkcs11_privkey_generate2 – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_privkey_generate2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_privkey_generate2(const char * </code><i>url</i><code>, gnutls_pk_algorithm_t </code><i>pk</i><code>, unsigned int </code><i>bits</i><code>, const char * </code><i>label</i><code>, gnutls_x509_crt_fmt_t </code><i>fmt</i><code>, gnutls_datum_t * </code><i>pubkey</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * url</p>
<dd> a token URL</p>
<dt>gnutls_pk_algorithm_t pk</p>
<dd> the public key algorithm</p>
<dt>unsigned int bits</p>
<dd> the security bits</p>
<dt>const char * label</p>
<dd> a label</p>
<dt>gnutls_x509_crt_fmt_t fmt</p>
<dd> the format of output params. PEM or DER</p>
<dt>gnutls_datum_t * pubkey</p>
<dd> will hold the public key (may be <code>NULL</code>)</p>
<dt>unsigned int flags</p>
<dd> zero or an OR&#8217;ed sequence of <code>GNUTLS_PKCS11_OBJ_FLAGs</code></dl>
<h2>DESCRIPTION</h2>
<p> This function will generate a private key in the specified by the <i>url</i> token. The private key will be generate within the token and will not be exportable. This function will store the DER-encoded public key in the SubjectPublicKeyInfo format in <i>pubkey</i> . The <i>pubkey</i> should be deinitialized using <code>gnutls_free()</code>. </p>
<p> Note that when generating an elliptic curve key, the curve can be substituted in the place of the bits parameter using the <code>GNUTLS_CURVE_TO_BITS()</code> macro.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.1.5</p>
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
