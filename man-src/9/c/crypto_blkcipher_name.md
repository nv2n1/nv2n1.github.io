---
title: "crypto_blkcipher_name(9)"
name: "crypto_blkcipher_name"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_blkcipher_name/"
description: "crypto_blkcipher_name – return the name / cra_name from the cipher handle"
---

<p>crypto_blkcipher_name &#8211; return the name / cra_name from the cipher handle</p>
<h2>Synopsis</h2>
<pre><code>const char *crypto_blkcipher_name(struct crypto_blkcipher *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>tfm</i></p>
<dl>
<dd>
<dd>cipher handle</dl>
<h2>Return</h2>
<p>The character string holding the name of the cipher</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
