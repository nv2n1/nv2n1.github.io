---
title: "crypto_skcipher_reqtfm(9)"
name: "crypto_skcipher_reqtfm"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_skcipher_reqtfm/"
description: "crypto_skcipher_reqtfm – obtain cipher handle from request"
---

<p>crypto_skcipher_reqtfm &#8211; obtain cipher handle from request</p>
<h2>Synopsis</h2>
<pre><code>struct crypto_skcipher *crypto_skcipher_reqtfm(struct skcipher_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>skcipher_request out of which the cipher handle is to be obtained</dl>
<h2>Description</h2>
<p>Return the crypto_skcipher handle when furnishing an skcipher_request data structure.</p>
<h2>Return</h2>
<p>crypto_skcipher handle</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
