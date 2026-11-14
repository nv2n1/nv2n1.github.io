---
title: "gnutls_pkcs11_copy_secret_key(3)"
name: "gnutls_pkcs11_copy_secret_key"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_copy_secret_key/"
description: "gnutls_pkcs11_copy_secret_key – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_copy_secret_key &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_copy_secret_key(const char * </code><i>token_url</i><code>, gnutls_datum_t * </code><i>key</i><code>, const char * </code><i>label</i><code>, unsigned int </code><i>key_usage</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * token_url</p>
<dd> A PKCS <code>11</code> URL specifying a token</p>
<dt>gnutls_datum_t * key</p>
<dd> The raw key</p>
<dt>const char * label</p>
<dd> A name to be used for the stored data</p>
<dt>unsigned int key_usage</p>
<dd> One of GNUTLS_KEY_*</p>
<dt>unsigned int flags</p>
<dd> One of GNUTLS_PKCS11_OBJ_FLAG_*</dl>
<h2>DESCRIPTION</h2>
<p> This function will copy a raw secret (symmetric) key into a PKCS <code>11</code> token specified by a URL. The key can be marked as sensitive or not.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
