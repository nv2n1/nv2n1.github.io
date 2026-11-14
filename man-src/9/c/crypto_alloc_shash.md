---
title: "crypto_alloc_shash(9)"
name: "crypto_alloc_shash"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_alloc_shash/"
description: "crypto_alloc_shash – allocate message digest handle"
---

<p>crypto_alloc_shash &#8211; allocate message digest handle</p>
<h2>Synopsis</h2>
<pre><code>struct crypto_shash *crypto_alloc_shash(const char *alg_name, u32 type, u32 mask);</code></pre>
<h2>Arguments</h2>
<p><i>alg_name</i></p>
<dl>
<dd>
<dd>is the cra_name / name or cra_driver_name / driver name of the message digest cipher</dl>
<p> <i>type</i></p>
<dl>
<dd>specifies the type of the cipher</dl>
<p> <i>mask</i></p>
<dl>
<dd>specifies the mask for the cipher</dl>
<h2>Description</h2>
<p>Allocate a cipher handle for a message digest. The returned struct crypto_shash is the cipher handle that is required for any subsequent API invocation for that message digest.</p>
<h2>Return</h2>
<p>allocated cipher handle in case of success; <code>IS_ERR</code> is true in case of an error, <code>PTR_ERR</code> returns the error code.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
