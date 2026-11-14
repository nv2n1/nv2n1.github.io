---
title: "crypto_akcipher_encrypt(9)"
name: "crypto_akcipher_encrypt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_akcipher_encrypt/"
description: "crypto_akcipher_encrypt – Invoke public key encrypt operation"
---

<p>crypto_akcipher_encrypt &#8211; Invoke public key encrypt operation</p>
<h2>Synopsis</h2>
<pre><code>int crypto_akcipher_encrypt(struct akcipher_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>asymmetric key request</dl>
<h2>Description</h2>
<p>Function invokes the specific public key encrypt operation for a given public key algorithm</p>
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
