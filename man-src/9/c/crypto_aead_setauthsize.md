---
title: "crypto_aead_setauthsize(9)"
name: "crypto_aead_setauthsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_aead_setauthsize/"
description: "crypto_aead_setauthsize – set authentication data size"
---

<p>crypto_aead_setauthsize &#8211; set authentication data size</p>
<h2>Synopsis</h2>
<pre><code>int crypto_aead_setauthsize(struct crypto_aead *tfm, unsigned int authsize);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>authsize</i></p>
<dl>
<dd>size of the authentication data / tag in bytes</dl>
<h2>Description</h2>
<p>Set the authentication data size / tag size. AEAD requires an authentication tag (or MAC) in addition to the associated data.</p>
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
