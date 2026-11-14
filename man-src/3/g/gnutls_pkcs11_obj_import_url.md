---
title: "gnutls_pkcs11_obj_import_url(3)"
name: "gnutls_pkcs11_obj_import_url"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_obj_import_url/"
description: "gnutls_pkcs11_obj_import_url – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_obj_import_url &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_obj_import_url(gnutls_pkcs11_obj_t </code><i>obj</i><code>, const char * </code><i>url</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_obj_t obj</p>
<dd> The structure to store the object</p>
<dt>const char * url</p>
<dd> a PKCS 11 url identifying the key</p>
<dt>unsigned int flags</p>
<dd> Or sequence of GNUTLS_PKCS11_OBJ_* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will &quot;import&quot; a PKCS 11 URL identifying an object (e.g. certificate) to the <code>gnutls_pkcs11_obj_t</code> structure. This does not involve any parsing (such as X.509 or OpenPGP) since the <code>gnutls_pkcs11_obj_t</code> is format agnostic. Only data are transferred.</p>
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
