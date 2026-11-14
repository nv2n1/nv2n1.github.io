---
title: "crypto_blkcipher_set_iv(9)"
name: "crypto_blkcipher_set_iv"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_blkcipher_set_iv/"
description: "crypto_blkcipher_set_iv – set IV for cipher"
---

<p>crypto_blkcipher_set_iv &#8211; set IV for cipher</p>
<h2>Synopsis</h2>
<pre><code>void crypto_blkcipher_set_iv(struct crypto_blkcipher *tfm, const u8 *src, unsigned int len);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>src</i></p>
<dl>
<dd>buffer holding the IV</dl>
<p> <i>len</i></p>
<dl>
<dd>length of the IV in bytes</dl>
<h2>Description</h2>
<p>The caller provided IV is set for the block cipher referenced by the cipher handle.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
