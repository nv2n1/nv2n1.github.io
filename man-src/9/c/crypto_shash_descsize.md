---
title: "crypto_shash_descsize(9)"
name: "crypto_shash_descsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_descsize/"
description: "crypto_shash_descsize – obtain the operational state size"
---

<p>crypto_shash_descsize &#8211; obtain the operational state size</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_shash_descsize(struct crypto_shash *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The size of the operational state the cipher needs during operation is returned for the hash referenced with the cipher handle. This size is required to calculate the memory requirements to allow the caller allocating sufficient memory for operational state. </p>
<p> The operational state is defined with struct shash_desc where the size of that data structure is to be calculated as sizeof(struct shash_desc) + crypto_shash_descsize(alg)</p>
<h2>Return</h2>
<p>size of the operational state</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
