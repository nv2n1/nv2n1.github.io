---
title: "crypto_ablkcipher_setkey(9)"
name: "crypto_ablkcipher_setkey"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ablkcipher_setkey/"
description: "crypto_ablkcipher_setkey – set key for cipher"
---

<p>crypto_ablkcipher_setkey &#8211; set key for cipher</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ablkcipher_setkey(struct crypto_ablkcipher *tfm, const u8 *key, unsigned int keylen);</code></pre>
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
<p>The caller provided key is set for the ablkcipher referenced by the cipher handle. </p>
<p> Note, the key length determines the cipher type. Many block ciphers implement different cipher modes depending on the key size, such as AES-128 vs AES-192 vs. AES-256. When providing a 16 byte key for an AES cipher handle, AES-128 is performed.</p>
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
