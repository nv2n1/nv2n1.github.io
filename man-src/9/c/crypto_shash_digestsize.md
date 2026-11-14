---
title: "crypto_shash_digestsize(9)"
name: "crypto_shash_digestsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_digestsize/"
description: "crypto_shash_digestsize – obtain message digest size"
---

<p>crypto_shash_digestsize &#8211; obtain message digest size</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_shash_digestsize(struct crypto_shash *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The size for the message digest created by the message digest cipher referenced with the cipher handle is returned.</p>
<h2>Return</h2>
<p>digest size of cipher</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
