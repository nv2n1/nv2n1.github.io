---
title: "gnutls_x509_crt_list_import_pkcs11(3)"
name: "gnutls_x509_crt_list_import_pkcs11"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_list_import_pkcs11/"
description: "gnutls_x509_crt_list_import_pkcs11 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_list_import_pkcs11 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_list_import_pkcs11(gnutls_x509_crt_t * </code><i>certs</i><code>, unsigned int </code><i>cert_max</i><code>, gnutls_pkcs11_obj_t * const </code><i>objs</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t * certs</dt>
<dd> A list of certificates of type <code>gnutls_x509_crt_t</code></dd>
<dt>unsigned int cert_max</dt>
<dd> The maximum size of the list</dd>
<dt>gnutls_pkcs11_obj_t * const objs</dt>
<dd> A list of PKCS 11 objects</dd>
<dt>unsigned int flags</dt>
<dd> 0 for now</dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will import a PKCS 11 certificate list to a list of <code>gnutls_x509_crt_t</code> structure. These must not be initialized.</p>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
<h2>Index</h2>
