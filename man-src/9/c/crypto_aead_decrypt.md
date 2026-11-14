---
title: "crypto_aead_decrypt(9)"
name: "crypto_aead_decrypt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_aead_decrypt/"
description: "crypto_aead_decrypt – decrypt ciphertext"
---

<p>crypto_aead_decrypt &#8211; decrypt ciphertext</p>
<h2>Synopsis</h2>
<pre><code>int crypto_aead_decrypt(struct aead_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the ablkcipher_request handle that holds all information needed to perform the cipher operation</dl>
<h2>Description</h2>
<p>Decrypt ciphertext data using the aead_request handle. That data structure and how it is filled with data is discussed with the aead_request_* functions. </p>
<p> IMPORTANT NOTE The caller must concatenate the ciphertext followed by the authentication data / tag. That authentication data / tag must have the size defined by the crypto_aead_setauthsize invocation.</p>
<h2>Return</h2>
<p>0 if the cipher operation was successful; -EBADMSG: The AEAD cipher operation performs the authentication of the data during the decryption operation. Therefore, the function returns this error if the authentication of the ciphertext was unsuccessful (i.e. the integrity of the ciphertext or the associated data was violated); &lt; 0 if an error occurred.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
