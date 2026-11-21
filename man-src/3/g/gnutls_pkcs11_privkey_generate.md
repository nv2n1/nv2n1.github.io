---

title: "gnutls_pkcs11_privkey_generate(3)"
name: "gnutls_pkcs11_privkey_generate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_privkey_generate/"
description: "gnutls_pkcs11_privkey_generate – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_privkey_generate &#8211; API function</p>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_privkey_generate(const char * </code><i>url</i><code>, gnutls_pk_algorithm_t </code><i>pk</i><code>, unsigned int </code><i>bits</i><code>, const char * </code><i>label</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * url</dt>
<dd> a token URL</dd>
<dt>gnutls_pk_algorithm_t pk</dt>
<dd> the public key algorithm</dd>
<dt>unsigned int bits</dt>
<dd> the security bits</dd>
<dt>const char * label</dt>
<dd> a label</dd>
<dt>unsigned int flags</dt>
<dd> should be zero</dd></dl>
<p> This function will generate a private key in the specified by the <i>url</i> token. The private key will be generate within the token and will not be exportable.</p>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
