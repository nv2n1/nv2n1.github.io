---
title: "gnutls_x509_aki_set_cert_issuer(3)"
name: "gnutls_x509_aki_set_cert_issuer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_aki_set_cert_issuer/"
description: "gnutls_x509_aki_set_cert_issuer – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_aki_set_cert_issuer &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_aki_set_cert_issuer(gnutls_x509_aki_t </code><i>aki</i><code>, unsigned int </code><i>san_type</i><code>, const gnutls_datum_t * </code><i>san</i><code>, const char * </code><i>othername_oid</i><code>, const gnutls_datum_t * </code><i>serial</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_aki_t aki</p>
<dd> The authority key ID structure</p>
<dt>unsigned int san_type</p>
<dd> the type of the name (of <code>gnutls_subject_alt_names_t</code>), may be null</p>
<dt>const gnutls_datum_t * san</p>
<dd> The alternative name data</p>
<dt>const char * othername_oid</p>
<dd> The object identifier if <i>san_type</i> is <code>GNUTLS_SAN_OTHERNAME</code></p>
<dt>const gnutls_datum_t * serial</p>
<dd> The authorityCertSerialNumber number (may be null)</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the authorityCertIssuer name and the authorityCertSerialNumber to be stored in the <i>aki</i> structure. When storing multiple names, the serial should be set on the first call, and subsequent calls should use a <code>NULL</code> serial.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
