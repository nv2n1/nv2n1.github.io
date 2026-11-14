---
title: "crypto_blkcipher_decrypt(9)"
name: "crypto_blkcipher_decrypt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_blkcipher_decrypt/"
description: "crypto_blkcipher_decrypt – decrypt ciphertext"
---

<p>crypto_blkcipher_decrypt &#8211; decrypt ciphertext</p>
<h2>Synopsis</h2>
<pre><code>int crypto_blkcipher_decrypt(struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes);</code></pre>
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
<p>Decrypt ciphertext data using the IV set by the caller with a preceding call of crypto_blkcipher_set_iv. </p>
<p> The blkcipher_desc data structure must be filled by the caller as documented for the crypto_blkcipher_encrypt call above.</p>
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
