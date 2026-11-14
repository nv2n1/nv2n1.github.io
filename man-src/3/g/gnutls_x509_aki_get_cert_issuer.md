---
title: "gnutls_x509_aki_get_cert_issuer(3)"
name: "gnutls_x509_aki_get_cert_issuer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_aki_get_cert_issuer/"
description: "gnutls_x509_aki_get_cert_issuer – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_aki_get_cert_issuer &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_aki_get_cert_issuer(gnutls_x509_aki_t </code><i>aki</i><code>, unsigned int </code><i>seq</i><code>, unsigned int * </code><i>san_type</i><code>, gnutls_datum_t * </code><i>san</i><code>, gnutls_datum_t * </code><i>othername_oid</i><code>, gnutls_datum_t * </code><i>serial</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_aki_t aki</p>
<dd> The authority key ID structure</p>
<dt>unsigned int seq</p>
<dd> The index of the name to get</p>
<dt>unsigned int * san_type</p>
<dd> Will hold the type of the name (of <code>gnutls_subject_alt_names_t</code>)</p>
<dt>gnutls_datum_t * san</p>
<dd> The alternative name data</p>
<dt>gnutls_datum_t * othername_oid</p>
<dd> The object identifier if <i>san_type</i> is <code>GNUTLS_SAN_OTHERNAME</code></p>
<dt>gnutls_datum_t * serial</p>
<dd> The authorityCertSerialNumber number</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a specific authorityCertIssuer name as stored in the <i>aki</i> structure, as well as the authorityCertSerialNumber. All the returned values should be treated as constant, and may be set to <code>NULL</code> when are not required.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the index is out of bounds, otherwise a negative error value.</p>
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
