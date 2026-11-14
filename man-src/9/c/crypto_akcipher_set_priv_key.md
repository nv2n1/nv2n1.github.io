---
title: "crypto_akcipher_set_priv_key(9)"
name: "crypto_akcipher_set_priv_key"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_akcipher_set_priv_key/"
description: "crypto_akcipher_set_priv_key – Invoke set private key operation"
---

<p>crypto_akcipher_set_priv_key &#8211; Invoke set private key operation</p>
<h2>Synopsis</h2>
<pre><code>int crypto_akcipher_set_priv_key(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>tfm handle</dl>
<p> <i>key</i></p>
<dl>
<dd>BER encoded private key</dl>
<p> <i>keylen</i></p>
<dl>
<dd>length of the key</dl>
<h2>Description</h2>
<p>Function invokes the algorithm specific set key function, which knows how to decode and interpret the encoded key</p>
<h2>Return</h2>
<p>zero on success; error code in case of error</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
