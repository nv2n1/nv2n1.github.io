---
title: "crypto_has_cipher(9)"
name: "crypto_has_cipher"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_has_cipher/"
description: "crypto_has_cipher – Search for the availability of a single block cipher"
---

<p>crypto_has_cipher &#8211; Search for the availability of a single block cipher</p>
<h2>Synopsis</h2>
<pre><code>int crypto_has_cipher(const char *alg_name, u32 type, u32 mask);</code></pre>
<h2>Arguments</h2>
<p><i>alg_name</i></p>
<dl>
<dd>
<dd>is the cra_name / name or cra_driver_name / driver name of the single block cipher</dl>
<p> <i>type</i></p>
<dl>
<dd>specifies the type of the cipher</dl>
<p> <i>mask</i></p>
<dl>
<dd>specifies the mask for the cipher</dl>
<h2>Return</h2>
<p>true when the single block cipher is known to the kernel crypto API; false otherwise</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
