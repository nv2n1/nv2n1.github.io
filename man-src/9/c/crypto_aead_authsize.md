---
title: "crypto_aead_authsize(9)"
name: "crypto_aead_authsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_aead_authsize/"
description: "crypto_aead_authsize – obtain maximum authentication data size"
---

<p>crypto_aead_authsize &#8211; obtain maximum authentication data size</p>
<h2>Synopsis</h2>
<pre><code>unsigned int crypto_aead_authsize(struct crypto_aead *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Description</h2>
<p>The maximum size of the authentication data for the AEAD cipher referenced by the AEAD cipher handle is returned. The authentication data size may be zero if the cipher implements a hard-coded maximum. </p>
<p> The authentication data may also be known as &#8220;tag value&#8221;.</p>
<h2>Return</h2>
<p>authentication data size / tag size in bytes</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
