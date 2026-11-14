---
title: "crypto_akcipher_maxsize(9)"
name: "crypto_akcipher_maxsize"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_akcipher_maxsize/"
description: "crypto_akcipher_maxsize – Get len for output buffer"
---

<p>crypto_akcipher_maxsize &#8211; Get len for output buffer</p>
<h2>Synopsis</h2>
<pre><code>int crypto_akcipher_maxsize(struct crypto_akcipher *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>AKCIPHER tfm handle allocated with <code>crypto_alloc_akcipher</code></dl>
<h2>Description</h2>
<p>Function returns the dest buffer size required for a given key</p>
<h2>Return</h2>
<p>minimum len for output buffer or error code in key hasn&#8217;t been set</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
