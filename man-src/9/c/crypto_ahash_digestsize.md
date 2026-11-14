---
title: "crypto_ahash_digestsize(9)"
name: "crypto_ahash_digestsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_digestsize/"
description: "crypto_ahash_digestsize – obtain message digest size"
---

<p>crypto_ahash_digestsize &#8211; obtain message digest size</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_ahash_digestsize(struct crypto_ahash *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The size for the message digest created by the message digest cipher referenced with the cipher handle is returned.</p>
<h2>Return</h2>
<p>message digest size of cipher</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
