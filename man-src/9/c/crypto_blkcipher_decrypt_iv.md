---
title: "crypto_blkcipher_decrypt_iv(9)"
name: "crypto_blkcipher_decrypt_iv"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_blkcipher_decrypt_iv/"
description: "crypto_blkcipher_decrypt_iv – decrypt ciphertext with dedicated IV"
---

<p>crypto_blkcipher_decrypt_iv &#8211; decrypt ciphertext with dedicated IV</p>
<h2>Synopsis</h2>
<pre><code>int crypto_blkcipher_decrypt_iv(struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>reference to the block cipher handle with meta data</dl>
<p> <i>dst</i></p>
<dl>
<dd>scatter/gather list that is filled by the cipher operation with the plaintext</dl>
<p> <i>src</i></p>
<dl>
<dd>scatter/gather list that holds the ciphertext</dl>
<p> <i>nbytes</i></p>
<dl>
<dd>number of bytes of the ciphertext to decrypt.</dl>
<h2>Description</h2>
<p>Decrypt ciphertext data with the use of an IV that is solely used for this cipher operation. Any previously set IV is not used. </p>
<p> The blkcipher_desc data structure must be filled by the caller as documented for the crypto_blkcipher_encrypt_iv call above.</p>
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
