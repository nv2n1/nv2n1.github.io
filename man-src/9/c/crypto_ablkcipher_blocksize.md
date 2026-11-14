---
title: "crypto_ablkcipher_blocksize(9)"
name: "crypto_ablkcipher_blocksize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ablkcipher_blocksize/"
description: "crypto_ablkcipher_blocksize – obtain block size of cipher"
---

<p>crypto_ablkcipher_blocksize &#8211; obtain block size of cipher</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_ablkcipher_blocksize(struct crypto_ablkcipher *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The block size for the ablkcipher referenced with the cipher handle is returned. The caller may use that information to allocate appropriate memory for the data returned by the encryption or decryption operation</p>
<h2>Return</h2>
<p>block size of cipher</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
