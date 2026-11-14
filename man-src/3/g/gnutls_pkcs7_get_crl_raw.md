---
title: "gnutls_pkcs7_get_crl_raw(3)"
name: "gnutls_pkcs7_get_crl_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs7_get_crl_raw/"
description: "gnutls_pkcs7_get_crl_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs7_get_crl_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_pkcs7_get_crl_raw(gnutls_pkcs7_t </code><i>pkcs7</i><code>, int </code><i>indx</i><code>, void * </code><i>crl</i><code>, size_t * </code><i>crl_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs7_t pkcs7</p>
<dd> should contain a <code>gnutls_pkcs7_t</code> structure</p>
<dt>int indx</p>
<dd> contains the index of the crl to extract</p>
<dt>void * crl</p>
<dd> the contents of the crl will be copied there (may be null)</p>
<dt>size_t * crl_size</p>
<dd> should hold the size of the crl</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a crl of the PKCS7 or RFC2630 crl set.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value. If the provided buffer is not long enough, then <i>crl_size</i> is updated and <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> is returned. After the last crl has been read <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
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
