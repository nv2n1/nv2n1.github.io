---
title: "gnutls_x509_privkey_sign_data(3)"
name: "gnutls_x509_privkey_sign_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_privkey_sign_data/"
description: "gnutls_x509_privkey_sign_data – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_privkey_sign_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_x509_privkey_sign_data(gnutls_x509_privkey_t </code><i>key</i><code>, gnutls_digest_algorithm_t </code><i>digest</i><code>, unsigned int </code><i>flags</i><code>, const gnutls_datum_t * </code><i>data</i><code>, void * </code><i>signature</i><code>, size_t * </code><i>signature_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_privkey_t key</p>
<dd> Holds the key</p>
<dt>gnutls_digest_algorithm_t digest</p>
<dd> should be MD5 or SHA1</p>
<dt>unsigned int flags</p>
<dd> should be 0 for now</p>
<dt>const gnutls_datum_t * data</p>
<dd> holds the data to be signed</p>
<dt>void * signature</p>
<dd> will contain the signature</p>
<dt>size_t * signature_size</p>
<dd> holds the size of signature (and will be replaced by the new size)</dl>
<h2>DESCRIPTION</h2>
<p> This function will sign the given data using a signature algorithm supported by the private key. Signature algorithms are always used together with a hash functions. Different hash functions may be used for the RSA algorithm, but only SHA-1 for the DSA keys. </p>
<p> If the buffer provided is not long enough to hold the output, then * <i>signature_size</i> is updated and <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> will be returned. </p>
<p> Use <code>gnutls_x509_crt_get_preferred_hash_algorithm()</code> to determine the hash algorithm.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>DEPRECATED</h2>
<p> Use <code>gnutls_privkey_sign_data()</code>.</p>
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
