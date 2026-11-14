---
title: "crypto_ahash_reqtfm(9)"
name: "crypto_ahash_reqtfm"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_reqtfm/"
description: "crypto_ahash_reqtfm – obtain cipher handle from request"
---

<p>crypto_ahash_reqtfm &#8211; obtain cipher handle from request</p>
<h2>Synopsis</h2>
<pre><code>struct crypto_ahash *crypto_ahash_reqtfm(struct ahash_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>asynchronous request handle that contains the reference to the ahash cipher handle</dl>
<h2>Description</h2>
<p>Return the ahash cipher handle that is registered with the asynchronous request handle ahash_request.</p>
<h2>Return</h2>
<p>ahash cipher handle</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
