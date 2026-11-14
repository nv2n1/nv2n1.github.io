---
title: "crypto_akcipher_verify(9)"
name: "crypto_akcipher_verify"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_akcipher_verify/"
description: "crypto_akcipher_verify – Invoke public key verify operation"
---

<p>crypto_akcipher_verify &#8211; Invoke public key verify operation</p>
<h2>Synopsis</h2>
<pre><code>int crypto_akcipher_verify(struct akcipher_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>asymmetric key request</dl>
<h2>Description</h2>
<p>Function invokes the specific public key verify operation for a given public key algorithm</p>
<h2>Return</h2>
<p>zero on success; error code in case of error</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
