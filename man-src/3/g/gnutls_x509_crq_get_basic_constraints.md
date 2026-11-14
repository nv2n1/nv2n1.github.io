---
title: "gnutls_x509_crq_get_basic_constraints(3)"
name: "gnutls_x509_crq_get_basic_constraints"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_basic_constraints/"
description: "gnutls_x509_crq_get_basic_constraints – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_get_basic_constraints &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_basic_constraints(gnutls_x509_crq_t </code><i>crq</i><code>, unsigned int * </code><i>critical</i><code>, unsigned int * </code><i>ca</i><code>, int * </code><i>pathlen</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>unsigned int * critical</p>
<dd> will be non-zero if the extension is marked as critical</p>
<dt>unsigned int * ca</p>
<dd> pointer to output integer indicating CA status, may be NULL, value is 1 if the certificate CA flag is set, 0 otherwise.</p>
<dt>int * pathlen</p>
<dd> pointer to output integer indicating path length (may be NULL), non-negative error codes indicate a present pathLenConstraint field and the actual value, -1 indicate that the field is absent.</dl>
<h2>DESCRIPTION</h2>
<p> This function will read the certificate&#8217;s basic constraints, and return the certificates CA status. It reads the basicConstraints X.509 extension (2.5.29.19).</p>
<h2>RETURNS</h2>
<p> If the certificate is a CA a positive value will be returned, or (0) if the certificate does not have CA flag set. A negative error code may be returned in case of errors. If the certificate does not contain the basicConstraints extension <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
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
