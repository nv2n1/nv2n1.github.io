---
title: "gnutls_pkcs11_obj_export2(3)"
name: "gnutls_pkcs11_obj_export2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_obj_export2/"
description: "gnutls_pkcs11_obj_export2 – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_obj_export2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_obj_export2(gnutls_pkcs11_obj_t </code><i>obj</i><code>, gnutls_datum_t * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_obj_t obj</p>
<dd> Holds the object</p>
<dt>gnutls_datum_t * out</p>
<dd> will contain the object data</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the PKCS11 object data. It is normal for data to be inaccesible and in that case <code>GNUTLS_E_INVALID_REQUEST</code> will be returned. </p>
<p> The output buffer is allocated using <code>gnutls_malloc()</code>.</p>
<h2>RETURNS</h2>
<p> In case of failure a negative error code will be returned, and <code>GNUTLS_E_SUCCESS</code> (0) on success.</p>
<h2>SINCE</h2>
<p> 3.1.3</p>
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
