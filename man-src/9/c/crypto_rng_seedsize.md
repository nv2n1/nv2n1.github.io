---
title: "crypto_rng_seedsize(9)"
name: "crypto_rng_seedsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_rng_seedsize/"
description: "crypto_rng_seedsize – obtain seed size of RNG"
---

<p>crypto_rng_seedsize &#8211; obtain seed size of RNG</p>
<h2>Synopsis</h2>
<pre><code>int crypto_rng_seedsize(struct crypto_rng *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The function returns the seed size for the random number generator referenced by the cipher handle. This value may be zero if the random number generator does not implement or require a reseeding. For example, the SP800-90A DRBGs implement an automated reseeding after reaching a pre-defined threshold.</p>
<h2>Return</h2>
<p>seed size for the random number generator</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
