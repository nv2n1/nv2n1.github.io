---
title: "ablkcipher_request_alloc(9)"
name: "ablkcipher_request_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ablkcipher_request_alloc/"
description: "ablkcipher_request_alloc – allocate request data structure"
---

<p>ablkcipher_request_alloc &#8211; allocate request data structure</p>
<h2>Synopsis</h2>
<pre><code>struct ablkcipher_request *ablkcipher_request_alloc(struct crypto_ablkcipher *tfm, gfp_t gfp);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle to be registered with the request</dl>
<p> <i>gfp</i></p>
<dl>
<dd>memory allocation flag that is handed to kmalloc by the API call.</dl>
<h2>Description</h2>
<p>Allocate the request data structure that must be used with the ablkcipher encrypt and decrypt API calls. During the allocation, the provided ablkcipher handle is registered in the request data structure.</p>
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
