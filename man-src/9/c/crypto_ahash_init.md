---
title: "crypto_ahash_init(9)"
name: "crypto_ahash_init"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_init/"
description: "crypto_ahash_init – (re)initialize message digest handle"
---

<p>crypto_ahash_init &#8211; (re)initialize message digest handle</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ahash_init(struct ahash_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>ahash_request handle that already is initialized with all necessary data using the ahash_request_* API functions</dl>
<h2>Description</h2>
<p>The call (re-)initializes the message digest referenced by the ahash_request handle. Any potentially existing state created by previous operations is discarded.</p>
<h2>Return</h2>
<p>0 if the message digest initialization was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
