---
title: "crypto_free_blkcipher(9)"
name: "crypto_free_blkcipher"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_free_blkcipher/"
description: "crypto_free_blkcipher – zeroize and free the block cipher handle"
---

<p>crypto_free_blkcipher &#8211; zeroize and free the block cipher handle</p>
<h2>Synopsis</h2>
<pre><code>void crypto_free_blkcipher(struct crypto_blkcipher *tfm);</code></pre>
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
