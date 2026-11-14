---
title: "crypto_blkcipher_get_iv(9)"
name: "crypto_blkcipher_get_iv"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_blkcipher_get_iv/"
description: "crypto_blkcipher_get_iv – obtain IV from cipher"
---

<p>crypto_blkcipher_get_iv &#8211; obtain IV from cipher</p>
<h2>Synopsis</h2>
<pre><code>void crypto_blkcipher_get_iv(struct crypto_blkcipher *tfm, u8 *dst, unsigned int len);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>dst</i></p>
<dl>
<dd>buffer filled with the IV</dl>
<p> <i>len</i></p>
<dl>
<dd>length of the buffer dst</dl>
<h2>Description</h2>
<p>The caller can obtain the IV set for the block cipher referenced by the cipher handle and store it into the user-provided buffer. If the buffer has an insufficient space, the IV is truncated to fit the buffer.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
