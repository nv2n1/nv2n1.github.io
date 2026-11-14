---
title: "crypto_shash_update(9)"
name: "crypto_shash_update"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_update/"
description: "crypto_shash_update – add data to message digest for processing"
---

<p>crypto_shash_update &#8211; add data to message digest for processing</p>
<h2>Synopsis</h2>
<pre><code>int crypto_shash_update(struct shash_desc *desc, const u8 *data, unsigned int len);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>operational state handle that is already initialized</dl>
<p> <i>data</i></p>
<dl>
<dd>input data to be added to the message digest</dl>
<p> <i>len</i></p>
<dl>
<dd>length of the input data</dl>
<h2>Description</h2>
<p>Updates the message digest state of the operational state handle.</p>
<h2>Return</h2>
<p>0 if the message digest update was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
