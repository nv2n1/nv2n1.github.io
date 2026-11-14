---
title: "crypto_ahash_setkey(9)"
name: "crypto_ahash_setkey"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_setkey/"
description: "crypto_ahash_setkey – set key for cipher handle"
---

<p>crypto_ahash_setkey &#8211; set key for cipher handle</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ahash_setkey(struct crypto_ahash *tfm, const u8 *key, unsigned int keylen);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>key</i></p>
<dl>
<dd>buffer holding the key</dl>
<p> <i>keylen</i></p>
<dl>
<dd>length of the key in bytes</dl>
<h2>Description</h2>
<p>The caller provided key is set for the ahash cipher. The cipher handle must point to a keyed hash in order for this function to succeed.</p>
<h2>Return</h2>
<p>0 if the setting of the key was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
