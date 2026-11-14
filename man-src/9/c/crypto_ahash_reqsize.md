---
title: "crypto_ahash_reqsize(9)"
name: "crypto_ahash_reqsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_reqsize/"
description: "crypto_ahash_reqsize – obtain size of the request data structure"
---

<p>crypto_ahash_reqsize &#8211; obtain size of the request data structure</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_ahash_reqsize(struct crypto_ahash *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>Return the size of the ahash state size. With the crypto_ahash_export function, the caller can export the state into a buffer whose size is defined with this function.</p>
<h2>Return</h2>
<p>size of the ahash state</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
