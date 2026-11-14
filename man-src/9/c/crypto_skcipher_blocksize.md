---
title: "crypto_skcipher_blocksize(9)"
name: "crypto_skcipher_blocksize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_skcipher_blocksize/"
description: "crypto_skcipher_blocksize – obtain block size of cipher"
---

<p>crypto_skcipher_blocksize &#8211; obtain block size of cipher</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_skcipher_blocksize(struct crypto_skcipher *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The block size for the skcipher referenced with the cipher handle is returned. The caller may use that information to allocate appropriate memory for the data returned by the encryption or decryption operation</p>
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
