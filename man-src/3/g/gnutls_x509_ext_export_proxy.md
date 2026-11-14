---
title: "gnutls_x509_ext_export_proxy(3)"
name: "gnutls_x509_ext_export_proxy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_ext_export_proxy/"
description: "gnutls_x509_ext_export_proxy – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_ext_export_proxy &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_ext_export_proxy(int </code><i>pathLenConstraint</i><code>, const char * </code><i>policyLanguage</i><code>, const char * </code><i>policy</i><code>, size_t </code><i>sizeof_policy</i><code>, gnutls_datum_t * </code><i>ext</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int pathLenConstraint</p>
<dd> non-negative error codes indicate maximum length of path, and negative error codes indicate that the pathLenConstraints field should not be present.</p>
<dt>const char * policyLanguage</p>
<dd> OID describing the language of <i>policy</i> .</p>
<dt>const char * policy</p>
<dd> uint8_t byte array with policy language, can be <code>NULL</code></p>
<dt>size_t sizeof_policy</p>
<dd> size of <i>policy</i> .</p>
<dt>gnutls_datum_t * ext</p>
<dd> The DER-encoded extension data; must be freed using <code>gnutls_free()</code>.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the parameters provided to a proxyCertInfo extension. </p>
<p> The <i>ext</i> data will be allocated using <code>gnutls_malloc()</code>.</p>
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
