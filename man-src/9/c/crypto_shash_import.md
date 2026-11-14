---
title: "crypto_shash_import(9)"
name: "crypto_shash_import"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_import/"
description: "crypto_shash_import – import operational state"
---

<p>crypto_shash_import &#8211; import operational state</p>
<h2>Synopsis</h2>
<pre><code>int crypto_shash_import(struct shash_desc *desc, const void *in);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>reference to the operational state handle the state imported into</dl>
<p> <i>in</i></p>
<dl>
<dd>buffer holding the state</dl>
<h2>Description</h2>
<p>This function imports the hash state into the operational state handle from the input buffer. That buffer should have been generated with the crypto_ahash_export function.</p>
<h2>Return</h2>
<p>0 if the import was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
