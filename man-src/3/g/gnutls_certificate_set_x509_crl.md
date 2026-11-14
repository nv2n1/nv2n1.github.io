---
title: "gnutls_certificate_set_x509_crl(3)"
name: "gnutls_certificate_set_x509_crl"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_x509_crl/"
description: "gnutls_certificate_set_x509_crl – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_x509_crl &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_x509_crl(gnutls_certificate_credentials_t </code><i>res</i><code>, gnutls_x509_crl_t * </code><i>crl_list</i><code>, int </code><i>crl_list_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>gnutls_x509_crl_t * crl_list</p>
<dd> is a list of trusted CRLs. They should have been verified before.</p>
<dt>int crl_list_size</p>
<dd> holds the size of the crl_list</dl>
<h2>DESCRIPTION</h2>
<p> This function adds the trusted CRLs in order to verify client or server certificates. In case of a client this is not required to be called if the certificates are not verified using <code>gnutls_certificate_verify_peers2()</code>. This function may be called multiple times.</p>
<h2>RETURNS</h2>
<p> number of CRLs processed, or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
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
