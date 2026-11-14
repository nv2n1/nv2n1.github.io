---
title: "crypto_shash_final(9)"
name: "crypto_shash_final"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_final/"
description: "crypto_shash_final – calculate message digest"
---

<p>crypto_shash_final &#8211; calculate message digest</p>
<h2>Synopsis</h2>
<pre><code>int crypto_shash_final(struct shash_desc *desc, u8 *out);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>operational state handle that is already filled with data</dl>
<p> <i>out</i></p>
<dl>
<dd>output buffer filled with the message digest</dl>
<h2>Description</h2>
<p>Finalize the message digest operation and create the message digest based on all data added to the cipher handle. The message digest is placed into the output buffer. The caller must ensure that the output buffer is large enough by using crypto_shash_digestsize.</p>
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
