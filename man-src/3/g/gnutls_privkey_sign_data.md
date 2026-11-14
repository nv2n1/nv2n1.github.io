---
title: "gnutls_privkey_sign_data(3)"
name: "gnutls_privkey_sign_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_sign_data/"
description: "gnutls_privkey_sign_data – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_sign_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_sign_data(gnutls_privkey_t </code><i>signer</i><code>, gnutls_digest_algorithm_t </code><i>hash</i><code>, unsigned int </code><i>flags</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_datum_t * </code><i>signature</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t signer</p>
<dd> Holds the key</p>
<dt>gnutls_digest_algorithm_t hash</p>
<dd> should be a digest algorithm</p>
<dt>unsigned int flags</p>
<dd> Zero or one of <code>gnutls_privkey_flags_t</code></p>
<dt>const gnutls_datum_t * data</p>
<dd> holds the data to be signed</p>
<dt>gnutls_datum_t * signature</p>
<dd> will contain the signature allocate with <code>gnutls_malloc()</code></dl>
<h2>DESCRIPTION</h2>
<p> This function will sign the given data using a signature algorithm supported by the private key. Signature algorithms are always used together with a hash functions. Different hash functions may be used for the RSA algorithm, but only the SHA family for the DSA keys. </p>
<p> You may use <code>gnutls_pubkey_get_preferred_hash_algorithm()</code> to determine the hash algorithm.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
