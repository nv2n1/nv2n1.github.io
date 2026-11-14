---
title: "gnutls_x509_crt_get_preferred_hash_algorithm(3)"
name: "gnutls_x509_crt_get_preferred_hash_algorithm"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_preferred_hash_algorithm/"
description: "gnutls_x509_crt_get_preferred_hash_algorithm – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_preferred_hash_algorithm &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_preferred_hash_algorithm(gnutls_x509_crt_t </code><i>crt</i><code>, gnutls_digest_algorithm_t * </code><i>hash</i><code>, unsigned int * </code><i>mand</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> Holds the certificate</p>
<dt>gnutls_digest_algorithm_t * hash</p>
<dd> The result of the call with the hash algorithm used for signature</p>
<dt>unsigned int * mand</p>
<dd> If non-zero it means that the algorithm MUST use this hash. May be NULL.</dl>
<h2>DESCRIPTION</h2>
<p> This function will read the certifcate and return the appropriate digest algorithm to use for signing with this certificate. Some certificates (i.e. DSA might not be able to sign without the preferred algorithm).</p>
<h2>DEPRECATED</h2>
<p> Please use <code>gnutls_pubkey_get_preferred_hash_algorithm()</code>.</p>
<h2>RETURNS</h2>
<p> the 0 if the hash algorithm is found. A negative error code is returned on error.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
