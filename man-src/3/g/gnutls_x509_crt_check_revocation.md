---
title: "gnutls_x509_crt_check_revocation(3)"
name: "gnutls_x509_crt_check_revocation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_check_revocation/"
description: "gnutls_x509_crt_check_revocation – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_check_revocation &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_check_revocation(gnutls_x509_crt_t </code><i>cert</i><code>, const gnutls_x509_crl_t * </code><i>crl_list</i><code>, int </code><i>crl_list_length</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>const gnutls_x509_crl_t * crl_list</p>
<dd> should contain a list of gnutls_x509_crl_t structures</p>
<dt>int crl_list_length</p>
<dd> the length of the crl_list</dl>
<h2>DESCRIPTION</h2>
<p> This function will return check if the given certificate is revoked. It is assumed that the CRLs have been verified before.</p>
<h2>RETURNS</h2>
<p> 0 if the certificate is NOT revoked, and 1 if it is. A negative error code is returned on error.</p>
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
