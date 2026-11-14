---
title: "crypto_cipher_decrypt_one(9)"
name: "crypto_cipher_decrypt_one"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_cipher_decrypt_one/"
description: "crypto_cipher_decrypt_one – decrypt one block of ciphertext"
---

<p>crypto_cipher_decrypt_one &#8211; decrypt one block of ciphertext</p>
<h2>Synopsis</h2>
<pre><code>void crypto_cipher_decrypt_one(struct crypto_cipher *tfm, u8 *dst, const u8 *src);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>dst</i></p>
<dl>
<dd>points to the buffer that will be filled with the plaintext</dl>
<p> <i>src</i></p>
<dl>
<dd>buffer holding the ciphertext to be decrypted</dl>
<h2>Description</h2>
<p>Invoke the decryption operation of one block. The caller must ensure that the plaintext and ciphertext buffers are at least one block in size.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
