---
title: "crypto_ahash_finup(9)"
name: "crypto_ahash_finup"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_finup/"
description: "crypto_ahash_finup – update and finalize message digest"
---

<p>crypto_ahash_finup &#8211; update and finalize message digest</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ahash_finup(struct ahash_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the ahash_request handle that holds all information needed to perform the cipher operation</dl>
<h2>Description</h2>
<p>This function is a &#8220;short-hand&#8221; for the function calls of crypto_ahash_update and crypto_shash_final. The parameters have the same meaning as discussed for those separate functions.</p>
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
