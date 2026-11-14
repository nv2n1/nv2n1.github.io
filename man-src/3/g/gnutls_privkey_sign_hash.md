---
title: "gnutls_privkey_sign_hash(3)"
name: "gnutls_privkey_sign_hash"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_sign_hash/"
description: "gnutls_privkey_sign_hash – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_sign_hash &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_sign_hash(gnutls_privkey_t </code><i>signer</i><code>, gnutls_digest_algorithm_t </code><i>hash_algo</i><code>, unsigned int </code><i>flags</i><code>, const gnutls_datum_t * </code><i>hash_data</i><code>, gnutls_datum_t * </code><i>signature</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t signer</p>
<dd> Holds the signer&#8217;s key</p>
<dt>gnutls_digest_algorithm_t hash_algo</p>
<dd> The hash algorithm used</p>
<dt>unsigned int flags</p>
<dd> Zero or one of <code>gnutls_privkey_flags_t</code></p>
<dt>const gnutls_datum_t * hash_data</p>
<dd> holds the data to be signed</p>
<dt>gnutls_datum_t * signature</p>
<dd> will contain newly allocated signature</dl>
<h2>DESCRIPTION</h2>
<p> This function will sign the given hashed data using a signature algorithm supported by the private key. Signature algorithms are always used together with a hash functions. Different hash functions may be used for the RSA algorithm, but only SHA-XXX for the DSA keys. </p>
<p> You may use <code>gnutls_pubkey_get_preferred_hash_algorithm()</code> to determine the hash algorithm. </p>
<p> Note that if <code>GNUTLS_PRIVKEY_SIGN_FLAG_TLS1_RSA</code> flag is specified this function will ignore <i>hash_algo</i> and perform a raw PKCS1 signature.</p>
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
