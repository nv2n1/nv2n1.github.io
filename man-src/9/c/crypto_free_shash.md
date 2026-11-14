---
title: "crypto_free_shash(9)"
name: "crypto_free_shash"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_free_shash/"
description: "crypto_free_shash – zeroize and free the message digest handle"
---

<p>crypto_free_shash &#8211; zeroize and free the message digest handle</p>
<h2>Synopsis</h2>
<pre><code>void crypto_free_shash(struct crypto_shash *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle to be freed</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
