---
title: "crypto_aead_ivsize(9)"
name: "crypto_aead_ivsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_aead_ivsize/"
description: "crypto_aead_ivsize – obtain IV size"
---

<p>crypto_aead_ivsize &#8211; obtain IV size</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_aead_ivsize(struct crypto_aead *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The size of the IV for the aead referenced by the cipher handle is returned. This IV size may be zero if the cipher does not need an IV.</p>
<h2>Return</h2>
<p>IV size in bytes</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
