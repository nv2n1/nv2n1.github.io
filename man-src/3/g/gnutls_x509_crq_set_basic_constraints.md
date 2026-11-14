---
title: "gnutls_x509_crq_set_basic_constraints(3)"
name: "gnutls_x509_crq_set_basic_constraints"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_set_basic_constraints/"
description: "gnutls_x509_crq_set_basic_constraints – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_set_basic_constraints &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_set_basic_constraints(gnutls_x509_crq_t </code><i>crq</i><code>, unsigned int </code><i>ca</i><code>, int </code><i>pathLenConstraint</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> a certificate request of type <code>gnutls_x509_crq_t</code></p>
<dt>unsigned int ca</p>
<dd> <a href="/docs/linux/man/1-true/">true</a>(1) or false(0) depending on the Certificate authority status.</p>
<dt>int pathLenConstraint</p>
<dd> non-negative error codes indicate maximum length of path, and negative error codes indicate that the pathLenConstraints field should not be present.</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the basicConstraints certificate extension.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.8.0</p>
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
