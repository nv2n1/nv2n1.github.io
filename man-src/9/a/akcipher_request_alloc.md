---
title: "akcipher_request_alloc(9)"
name: "akcipher_request_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-akcipher_request_alloc/"
description: "akcipher_request_alloc – allocates public key request"
---

<p>akcipher_request_alloc &#8211; allocates public key request</p>
<h2>Synopsis</h2>
<pre><code>struct akcipher_request *akcipher_request_alloc(struct crypto_akcipher *tfm, gfp_t gfp);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>AKCIPHER tfm handle allocated with <code>crypto_alloc_akcipher</code></dl>
<p> <i>gfp</i></p>
<dl>
<dd>allocation flags</dl>
<h2>Return</h2>
<p>allocated handle in case of success or NULL in case of an error.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
