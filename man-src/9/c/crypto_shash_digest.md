---
title: "crypto_shash_digest(9)"
name: "crypto_shash_digest"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_digest/"
description: "crypto_shash_digest – calculate message digest for buffer"
---

<p>crypto_shash_digest &#8211; calculate message digest for buffer</p>
<h2>Synopsis</h2>
<pre><code>int crypto_shash_digest(struct shash_desc *desc, const u8 *data, unsigned int len, u8 *out);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>see <code>crypto_shash_final</code></dl>
<p> <i>data</i></p>
<dl>
<dd>see <code>crypto_shash_update</code></dl>
<p> <i>len</i></p>
<dl>
<dd>see <code>crypto_shash_update</code></dl>
<p> <i>out</i></p>
<dl>
<dd>see <code>crypto_shash_final</code></dl>
<h2>Description</h2>
<p>This function is a &#8220;short-hand&#8221; for the function calls of crypto_shash_init, crypto_shash_update and crypto_shash_final. The parameters have the same meaning as discussed for those separate three functions.</p>
<h2>Return</h2>
<p>0 if the message digest creation was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
