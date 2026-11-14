---
title: "crypto_rng_alg(9)"
name: "crypto_rng_alg"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_rng_alg/"
description: "crypto_rng_alg – obtain name of RNG"
---

<p>crypto_rng_alg &#8211; obtain name of RNG</p>
<h2>Synopsis</h2>
<pre><code>struct rng_alg *crypto_rng_alg(struct crypto_rng *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>Return the generic name (cra_name) of the initialized random number generator</p>
<h2>Return</h2>
<p>generic name string</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
