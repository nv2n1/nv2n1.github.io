---
title: "crypto_rng_reset(9)"
name: "crypto_rng_reset"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_rng_reset/"
description: "crypto_rng_reset – re-initialize the RNG"
---

<p>crypto_rng_reset &#8211; re-initialize the RNG</p>
<h2>Synopsis</h2>
<pre><code>int crypto_rng_reset(struct crypto_rng *tfm, const u8 *seed, unsigned int slen);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>seed</i></p>
<dl>
<dd>seed input data</dl>
<p> <i>slen</i></p>
<dl>
<dd>length of the seed input data</dl>
<h2>Description</h2>
<p>The reset function completely re-initializes the random number generator referenced by the cipher handle by clearing the current state. The new state is initialized with the caller provided seed or automatically, depending on the random number generator type (the ANSI X9.31 RNG requires caller-provided seed, the SP800-90A DRBGs perform an automatic seeding). The seed is provided as a parameter to this function call. The provided seed should have the length of the seed size defined for the random number generator as defined by crypto_rng_seedsize.</p>
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
