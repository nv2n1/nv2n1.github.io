---
title: "gnutls_ocsp_req_add_cert(3)"
name: "gnutls_ocsp_req_add_cert"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_req_add_cert/"
description: "gnutls_ocsp_req_add_cert – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_req_add_cert &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_req_add_cert(gnutls_ocsp_req_t </code><i>req</i><code>, gnutls_digest_algorithm_t </code><i>digest</i><code>, gnutls_x509_crt_t </code><i>issuer</i><code>, gnutls_x509_crt_t </code><i>cert</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_req_t req</p>
<dd> should contain a <code>gnutls_ocsp_req_t</code> structure</p>
<dt>gnutls_digest_algorithm_t digest</p>
<dd> hash algorithm, a <code>gnutls_digest_algorithm_t</code> value</p>
<dt>gnutls_x509_crt_t issuer</p>
<dd> issuer of <i>subject</i> certificate</p>
<dt>gnutls_x509_crt_t cert</p>
<dd> certificate to request status for</dl>
<h2>DESCRIPTION</h2>
<p> This function will add another request to the OCSP request for a particular certificate. The issuer name hash, issuer key hash, and serial number fields is populated as follows. The issuer name and the serial number is taken from <i>cert</i> . The issuer key is taken from <i>issuer</i> . The hashed values will be hashed using the <i>digest</i> algorithm, normally <code>GNUTLS_DIG_SHA1</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
