---
title: "crypto_free_akcipher(9)"
name: "crypto_free_akcipher"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_free_akcipher/"
description: "crypto_free_akcipher – free AKCIPHER tfm handle"
---

<p>crypto_free_akcipher &#8211; free AKCIPHER tfm handle</p>
<h2>Synopsis</h2>
<pre><code>void crypto_free_akcipher(struct crypto_akcipher *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>AKCIPHER tfm handle allocated with <code>crypto_alloc_akcipher</code></dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
