---
title: "gnutls_x509_crt_set_authority_info_access(3)"
name: "gnutls_x509_crt_set_authority_info_access"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_authority_info_access/"
description: "gnutls_x509_crt_set_authority_info_access – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_set_authority_info_access &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_set_authority_info_access(gnutls_x509_crt_t </code><i>crt</i><code>, int </code><i>what</i><code>, gnutls_datum_t * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> Holds the certificate</p>
<dt>int what</p>
<dd> what data to get, a <code>gnutls_info_access_what_t</code> type.</p>
<dt>gnutls_datum_t * data</p>
<dd> output data to be freed with <code>gnutls_free()</code>.</dl>
<h2>DESCRIPTION</h2>
<p> This function sets the Authority Information Access (AIA) extension, see RFC 5280 section 4.2.2.1 for more information. </p>
<p> The type of data stored in <i>data</i> is specified via <i>what</i> which should be <code>gnutls_info_access_what_t</code> values. </p>
<p> If <i>what</i> is <code>GNUTLS_IA_OCSP_URI</code>, <i>data</i> will hold the OCSP URI. If <i>what</i> is <code>GNUTLS_IA_CAISSUERS_URI</code>, <i>data</i> will hold the caIssuers URI.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
