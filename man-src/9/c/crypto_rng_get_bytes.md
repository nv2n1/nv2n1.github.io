---
title: "crypto_rng_get_bytes(9)"
name: "crypto_rng_get_bytes"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_rng_get_bytes/"
description: "crypto_rng_get_bytes – get random number"
---

<p>crypto_rng_get_bytes &#8211; get random number</p>
<h2>Synopsis</h2>
<pre><code>int crypto_rng_get_bytes(struct crypto_rng *tfm, u8 *rdata, unsigned int dlen);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<p> <i>rdata</i></p>
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
