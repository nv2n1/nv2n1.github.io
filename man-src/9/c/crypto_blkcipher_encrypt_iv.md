---
title: "crypto_blkcipher_encrypt_iv(9)"
name: "crypto_blkcipher_encrypt_iv"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_blkcipher_encrypt_iv/"
description: "crypto_blkcipher_encrypt_iv – encrypt plaintext with dedicated IV"
---

<p>crypto_blkcipher_encrypt_iv &#8211; encrypt plaintext with dedicated IV</p>
<h2>Synopsis</h2>
<pre><code>int crypto_blkcipher_encrypt_iv(struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>reference to the block cipher handle with meta data</dl>
<p> <i>dst</i></p>
<dl>
<dd>scatter/gather list that is filled by the cipher operation with the ciphertext</dl>
<p> <i>src</i></p>
<dl>
<dd>scatter/gather list that holds the plaintext</dl>
<p> <i>nbytes</i></p>
<dl>
<dd>number of bytes of the plaintext to encrypt.</dl>
<h2>Description</h2>
<p>Encrypt plaintext data with the use of an IV that is solely used for this cipher operation. Any previously set IV is not used. </p>
<p> The blkcipher_desc data structure must be filled by the caller and can reside on the stack. The caller must fill desc as follows: desc.tfm is filled with the block cipher handle; desc.info is filled with the IV to be used for the current operation; desc.flags is filled with either CRYPTO_TFM_REQ_MAY_SLEEP or 0.</p>
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
