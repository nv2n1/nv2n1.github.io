---
title: "crypto_aead_encrypt(9)"
name: "crypto_aead_encrypt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_aead_encrypt/"
description: "crypto_aead_encrypt – encrypt plaintext"
---

<p>crypto_aead_encrypt &#8211; encrypt plaintext</p>
<h2>Synopsis</h2>
<pre><code>int crypto_aead_encrypt(struct aead_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the aead_request handle that holds all information needed to perform the cipher operation</dl>
<h2>Description</h2>
<p>Encrypt plaintext data using the aead_request handle. That data structure and how it is filled with data is discussed with the aead_request_* functions. </p>
<p> IMPORTANT NOTE The encryption operation creates the authentication data / tag. That data is concatenated with the created ciphertext. The ciphertext memory size is therefore the given number of block cipher blocks + the size defined by the crypto_aead_setauthsize invocation. The caller must ensure that sufficient memory is available for the ciphertext and the authentication tag.</p>
<h2>Return</h2>
<p>0 if the cipher operation was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
