---
title: "gnutls_pubkey_import_pkcs11_url(3)"
name: "gnutls_pubkey_import_pkcs11_url"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pubkey_import_pkcs11_url/"
description: "gnutls_pubkey_import_pkcs11_url – API function"
---

<h2>NAME</h2>
<p> gnutls_pubkey_import_pkcs11_url &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_pubkey_import_pkcs11_url(gnutls_pubkey_t </code><i>key</i><code>, const char * </code><i>url</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pubkey_t key</p>
<dd> A key of type <code>gnutls_pubkey_t</code></p>
<dt>const char * url</p>
<dd> A PKCS 11 url</p>
<dt>unsigned int flags</p>
<dd> One of GNUTLS_PKCS11_OBJ_* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will import a PKCS 11 certificate to a <code>gnutls_pubkey_t</code> structure.</p>
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
