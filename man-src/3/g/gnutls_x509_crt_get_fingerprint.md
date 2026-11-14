---
title: "gnutls_x509_crt_get_fingerprint(3)"
name: "gnutls_x509_crt_get_fingerprint"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_fingerprint/"
description: "gnutls_x509_crt_get_fingerprint – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_fingerprint &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_fingerprint(gnutls_x509_crt_t </code><i>cert</i><code>, gnutls_digest_algorithm_t </code><i>algo</i><code>, void * </code><i>buf</i><code>, size_t * </code><i>buf_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>gnutls_digest_algorithm_t algo</p>
<dd> is a digest algorithm</p>
<dt>void * buf</p>
<dd> a pointer to a structure to hold the fingerprint (may be null)</p>
<dt>size_t * buf_size</p>
<dd> initially holds the size of <i>buf</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will calculate and copy the certificate&#8217;s fingerprint in the provided buffer. The fingerprint is a hash of the DER-encoded data of the certificate. </p>
<p> If the buffer is null then only the size will be filled.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if the provided buffer is not long enough, and in that case the *buf_size will be updated with the required size. On success 0 is returned.</p>
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
