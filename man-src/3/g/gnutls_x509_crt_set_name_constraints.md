---
title: "gnutls_x509_crt_set_name_constraints(3)"
name: "gnutls_x509_crt_set_name_constraints"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_name_constraints/"
description: "gnutls_x509_crt_set_name_constraints – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_set_name_constraints &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_set_name_constraints(gnutls_x509_crt_t </code><i>crt</i><code>, gnutls_x509_name_constraints_t </code><i>nc</i><code>, unsigned int </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> The certificate structure</p>
<dt>gnutls_x509_name_constraints_t nc</p>
<dd> The nameconstraints structure</p>
<dt>unsigned int critical</p>
<dd> whether this extension will be critical</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the provided name constraints to the certificate extension list. This extension is always marked as critical.</p>
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
