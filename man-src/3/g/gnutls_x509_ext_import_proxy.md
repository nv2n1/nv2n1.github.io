---
title: "gnutls_x509_ext_import_proxy(3)"
name: "gnutls_x509_ext_import_proxy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_ext_import_proxy/"
description: "gnutls_x509_ext_import_proxy – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_ext_import_proxy &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_ext_import_proxy(const gnutls_datum_t * </code><i>ext</i><code>, int * </code><i>pathlen</i><code>, char ** </code><i>policyLanguage</i><code>, char ** </code><i>policy</i><code>, size_t * </code><i>sizeof_policy</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const gnutls_datum_t * ext</p>
<dd> the DER encoded extension data</p>
<dt>int * pathlen</p>
<dd> pointer to output integer indicating path length (may be NULL), non-negative error codes indicate a present pCPathLenConstraint field and the actual value, -1 indicate that the field is absent.</p>
<dt>char ** policyLanguage</p>
<dd> output variable with OID of policy language</p>
<dt>char ** policy</p>
<dd> output variable with policy data</p>
<dt>size_t * sizeof_policy</p>
<dd> output variable size of policy data</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the information from a proxy certificate extension. It reads the ProxyCertInfo X.509 extension (1.3.6.1.5.5.7.1.14). The <i>policyLanguage</i> and <i>policy</i> values must be deinitialized using <code>gnutls_free()</code> after use.</p>
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
