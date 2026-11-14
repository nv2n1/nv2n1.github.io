---
title: "crypto_shash_blocksize(9)"
name: "crypto_shash_blocksize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_blocksize/"
description: "crypto_shash_blocksize – obtain block size for cipher"
---

<p>crypto_shash_blocksize &#8211; obtain block size for cipher</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_shash_blocksize(struct crypto_shash *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The block size for the message digest cipher referenced with the cipher handle is returned.</p>
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
