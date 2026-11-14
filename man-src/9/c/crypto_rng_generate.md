---
title: "crypto_rng_generate(9)"
name: "crypto_rng_generate"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_rng_generate/"
description: "crypto_rng_generate – get random number"
---

<p>crypto_rng_generate &#8211; get random number</p>
<h2>Synopsis</h2>
<pre><code>int crypto_rng_generate(struct crypto_rng *tfm, const u8 *src, unsigned int slen, u8 *dst, unsigned int dlen);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>src</i></p>
<dl>
<dd>Input buffer holding additional data, may be NULL</dl>
<p> <i>slen</i></p>
<dl>
<dd>Length of additional data</dl>
<p> <i>dst</i></p>
<dl>
<dd>output buffer holding the random numbers</dl>
<p> <i>dlen</i></p>
<dl>
<dd>length of the output buffer</dl>
<h2>Description</h2>
<p>This function fills the caller-allocated buffer with random numbers using the random number generator referenced by the cipher handle.</p>
<h2>Return</h2>
<p>0 function was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
