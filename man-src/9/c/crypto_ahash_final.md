---
title: "crypto_ahash_final(9)"
name: "crypto_ahash_final"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_final/"
description: "crypto_ahash_final – calculate message digest"
---

<p>crypto_ahash_final &#8211; calculate message digest</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ahash_final(struct ahash_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the ahash_request handle that holds all information needed to perform the cipher operation</dl>
<h2>Description</h2>
<p>Finalize the message digest operation and create the message digest based on all data added to the cipher handle. The message digest is placed into the output buffer registered with the ahash_request handle.</p>
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
