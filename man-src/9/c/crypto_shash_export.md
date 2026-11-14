---
title: "crypto_shash_export(9)"
name: "crypto_shash_export"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_export/"
description: "crypto_shash_export – extract operational state for message digest"
---

<p>crypto_shash_export &#8211; extract operational state for message digest</p>
<h2>Synopsis</h2>
<pre><code>int crypto_shash_export(struct shash_desc *desc, void *out);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>reference to the operational state handle whose state is exported</dl>
<p> <i>out</i></p>
<dl>
<dd>output buffer of sufficient size that can hold the hash state</dl>
<h2>Description</h2>
<p>This function exports the hash state of the operational state handle into the caller-allocated output buffer out which must have sufficient size (e.g. by calling crypto_shash_descsize).</p>
<h2>Return</h2>
<p>0 if the export creation was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
