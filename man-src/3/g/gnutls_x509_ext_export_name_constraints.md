---
title: "gnutls_x509_ext_export_name_constraints(3)"
name: "gnutls_x509_ext_export_name_constraints"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_ext_export_name_constraints/"
description: "gnutls_x509_ext_export_name_constraints – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_ext_export_name_constraints &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_ext_export_name_constraints(gnutls_x509_name_constraints_t </code><i>nc</i><code>, gnutls_datum_t * </code><i>ext</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_name_constraints_t nc</p>
<dd> The nameconstraints structure</p>
<dt>gnutls_datum_t * ext</p>
<dd> The DER-encoded extension data; must be freed using <code>gnutls_free()</code>.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the provided name constraints structure to a DER-encoded PKIX NameConstraints (2.5.29.30) extension. The output data in<br />
&nbsp;<wbr><i>ext</i>&nbsp;<wbr>will be allocated usin&nbsp;<wbr><code>gnutls_malloc()</code>.</p>
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
