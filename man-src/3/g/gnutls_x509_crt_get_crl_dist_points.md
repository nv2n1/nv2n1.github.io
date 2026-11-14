---
title: "gnutls_x509_crt_get_crl_dist_points(3)"
name: "gnutls_x509_crt_get_crl_dist_points"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_crl_dist_points/"
description: "gnutls_x509_crt_get_crl_dist_points – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_crl_dist_points &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_crl_dist_points(gnutls_x509_crt_t </code><i>cert</i><code>, unsigned int </code><i>seq</i><code>, void * </code><i>san</i><code>, size_t * </code><i>san_size</i><code>, unsigned int * </code><i>reason_flags</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>unsigned int seq</p>
<dd> specifies the sequence number of the distribution point (0 for the first one, 1 for the second etc.)</p>
<dt>void * san</p>
<dd> is the place where the distribution point will be copied to</p>
<dt>size_t * san_size</p>
<dd> holds the size of ret.</p>
<dt>unsigned int * reason_flags</p>
<dd> Revocation reasons. An ORed sequence of flags from <code>gnutls_x509_crl_reason_flags_t</code>.</p>
<dt>unsigned int * critical</p>
<dd> will be non-zero if the extension is marked as critical (may be null)</dl>
<h2>DESCRIPTION</h2>
<p> This function retrieves the CRL distribution points (2.5.29.31), contained in the given certificate in the X509v3 Certificate Extensions.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> and updates <i>ret_size</i> if<br />
&nbsp;<wbr><i>ret_size</i>&nbsp;<wbr>is not enough to hold the distribution point, or the type of the distribution point if everything was ok. The type is one of the enumerated <code>gnutls_x509_subject_alt_name_t</code>. If the certificate does not have an Alternative name with the specified sequence number then <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned.</p>
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
