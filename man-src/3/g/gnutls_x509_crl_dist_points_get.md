---
title: "gnutls_x509_crl_dist_points_get(3)"
name: "gnutls_x509_crl_dist_points_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_dist_points_get/"
description: "gnutls_x509_crl_dist_points_get – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_dist_points_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_dist_points_get(gnutls_x509_crl_dist_points_t </code><i>cdp</i><code>, unsigned int </code><i>seq</i><code>, unsigned int * </code><i>type</i><code>, gnutls_datum_t * </code><i>san</i><code>, unsigned int * </code><i>reasons</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_dist_points_t cdp</p>
<dd> The CRL distribution points structure</p>
<dt>unsigned int seq</p>
<dd> specifies the sequence number of the distribution point (0 for the first one, 1 for the second etc.)</p>
<dt>unsigned int * type</p>
<dd> The name type of the corresponding name (gnutls_x509_subject_alt_name_t)</p>
<dt>gnutls_datum_t * san</p>
<dd> The distribution point names (to be treated as constant)</p>
<dt>unsigned int * reasons</p>
<dd> Revocation reasons. An ORed sequence of flags from <code>gnutls_x509_crl_reason_flags_t</code>.</dl>
<h2>DESCRIPTION</h2>
<p> This function retrieves the individual CRL distribution points (2.5.29.31), contained in provided structure.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the index is out of bounds, otherwise a negative error value.</p>
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
