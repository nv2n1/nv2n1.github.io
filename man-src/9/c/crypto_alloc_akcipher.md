---
title: "crypto_alloc_akcipher(9)"
name: "crypto_alloc_akcipher"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_alloc_akcipher/"
description: "crypto_alloc_akcipher – allocate AKCIPHER tfm handle"
---

<p>crypto_alloc_akcipher &#8211; allocate AKCIPHER tfm handle</p>
<h2>Synopsis</h2>
<pre><code>struct crypto_akcipher *crypto_alloc_akcipher(const char *alg_name, u32 type, u32 mask);</code></pre>
<h2>Arguments</h2>
<p><i>alg_name</i></p>
<dl>
<dd>
<dd>is the cra_name / name or cra_driver_name / driver name of the public key algorithm e.g. &#8220;rsa&#8221;</dl>
<p> <i>type</i></p>
<dl>
<dd>specifies the type of the algorithm</dl>
<p> <i>mask</i></p>
<dl>
<dd>specifies the mask for the algorithm</dl>
<h2>Description</h2>
<p>Allocate a handle for public key algorithm. The returned struct crypto_akcipher is the handle that is required for any subsequent API invocation for the public key operations.</p>
<h2>Return</h2>
<p>allocated handle in case of success; <code>IS_ERR</code> is true in case of an error, <code>PTR_ERR</code> returns the error code.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
