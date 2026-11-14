---
title: "crypto_aead_reqsize(9)"
name: "crypto_aead_reqsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_aead_reqsize/"
description: "crypto_aead_reqsize – obtain size of the request data structure"
---

<p>crypto_aead_reqsize &#8211; obtain size of the request data structure</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_aead_reqsize(struct crypto_aead *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Return</h2>
<p>number of bytes</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
