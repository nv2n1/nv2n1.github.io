---
title: "skcipher_request_alloc(9)"
name: "skcipher_request_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skcipher_request_alloc/"
description: "skcipher_request_alloc – allocate request data structure"
---

<p>skcipher_request_alloc &#8211; allocate request data structure</p>
<h2>Synopsis</h2>
<pre><code>struct skcipher_request *skcipher_request_alloc(struct crypto_skcipher *tfm, gfp_t gfp);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle to be registered with the request</dl>
<p> <i>gfp</i></p>
<dl>
<dd>memory allocation flag that is handed to kmalloc by the API call.</dl>
<h2>Description</h2>
<p>Allocate the request data structure that must be used with the skcipher encrypt and decrypt API calls. During the allocation, the provided skcipher handle is registered in the request data structure.</p>
<h2>Return</h2>
<p>allocated request handle in case of success, or NULL if out of memory</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
