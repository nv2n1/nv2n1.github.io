---
title: "crypto_skcipher_decrypt(9)"
name: "crypto_skcipher_decrypt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_skcipher_decrypt/"
description: "crypto_skcipher_decrypt – decrypt ciphertext"
---

<p>crypto_skcipher_decrypt &#8211; decrypt ciphertext</p>
<h2>Synopsis</h2>
<pre><code>int crypto_skcipher_decrypt(struct skcipher_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the skcipher_request handle that holds all information needed to perform the cipher operation</dl>
<h2>Description</h2>
<p>Decrypt ciphertext data using the skcipher_request handle. That data structure and how it is filled with data is discussed with the skcipher_request_* functions.</p>
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
