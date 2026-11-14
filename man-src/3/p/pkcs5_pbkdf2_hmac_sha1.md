---
title: "pkcs5_pbkdf2_hmac_sha1(3)"
name: "pkcs5_pbkdf2_hmac_sha1"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pkcs5_pbkdf2_hmac_sha1/"
description: "hcrypto miscellaneous functions –"
---

<p>hcrypto miscellaneous functions &#8211; </p>
<h3>Functions</h3>
<p>int <code>PKCS5_PBKDF2_HMAC_SHA1</code> (const void *password, size_t password_len, const void *salt, size_t salt_len, unsigned long iter, size_t keylen, void *key) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int PKCS5_PBKDF2_HMAC_SHA1 (const void *password, size_tpassword_len, const void *salt, size_tsalt_len, unsigned longiter, size_tkeylen, void *key)</h3>
<p>As descriped in PKCS5, convert a password, salt, and iteration counter into a crypto key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>password</i> Password.<br />
 <i>password_len</i> Length of password.<br />
 <i>salt</i> Salt<br />
 <i>salt_len</i> Length of salt.<br />
 <i>iter</i> iteration counter.<br />
 <i>keylen</i> the output key length.<br />
 <i>key</i> the output key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, non 1 on failure.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
