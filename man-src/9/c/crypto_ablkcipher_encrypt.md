---
title: "crypto_ablkcipher_encrypt(9)"
name: "crypto_ablkcipher_encrypt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ablkcipher_encrypt/"
description: "crypto_ablkcipher_encrypt – encrypt plaintext"
---

<p>crypto_ablkcipher_encrypt &#8211; encrypt plaintext</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ablkcipher_encrypt(struct ablkcipher_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the ablkcipher_request handle that holds all information needed to perform the cipher operation</dl>
<h2>Description</h2>
<p>Encrypt plaintext data using the ablkcipher_request handle. That data structure and how it is filled with data is discussed with the ablkcipher_request_* functions.</p>
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
