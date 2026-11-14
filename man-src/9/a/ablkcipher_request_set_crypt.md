---
title: "ablkcipher_request_set_crypt(9)"
name: "ablkcipher_request_set_crypt"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ablkcipher_request_set_crypt/"
description: "ablkcipher_request_set_crypt – set data buffers"
---

<p>ablkcipher_request_set_crypt &#8211; set data buffers</p>
<h2>Synopsis</h2>
<pre><code>void ablkcipher_request_set_crypt(struct ablkcipher_request *req, struct scatterlist *src, struct scatterlist *dst, unsigned int nbytes, void *iv);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request handle</dl>
<p> <i>src</i></p>
<dl>
<dd>source scatter / gather list</dl>
<p> <i>dst</i></p>
<dl>
<dd>destination scatter / gather list</dl>
<p> <i>nbytes</i></p>
<dl>
<dd>number of bytes to process from <i>src</i></dl>
<p> <i>iv</i></p>
<dl>
<dd>IV for the cipher operation which must comply with the IV size defined by crypto_ablkcipher_ivsize</dl>
<h2>Description</h2>
<p>This function allows setting of the source data and destination data scatter / gather lists. </p>
<p> For encryption, the source is treated as the plaintext and the destination is the ciphertext. For a decryption operation, the use is reversed &#8211; the source is the ciphertext and the destination is the plaintext.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
