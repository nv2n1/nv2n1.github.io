---
title: "crypto_free_skcipher(9)"
name: "crypto_free_skcipher"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_free_skcipher/"
description: "crypto_free_skcipher – zeroize and free cipher handle"
---

<p>crypto_free_skcipher &#8211; zeroize and free cipher handle</p>
<h2>Synopsis</h2>
<pre><code>void crypto_free_skcipher(struct crypto_skcipher *tfm);</code></pre>
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
