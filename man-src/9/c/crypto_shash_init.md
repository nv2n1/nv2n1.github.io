---
title: "crypto_shash_init(9)"
name: "crypto_shash_init"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_shash_init/"
description: "crypto_shash_init – (re)initialize message digest"
---

<p>crypto_shash_init &#8211; (re)initialize message digest</p>
<h2>Synopsis</h2>
<pre><code>int crypto_shash_init(struct shash_desc *desc);</code></pre>
<h2>Arguments</h2>
<p><i>desc</i></p>
<dl>
<dd>
<dd>operational state handle that is already filled</dl>
<h2>Description</h2>
<p>The call (re-)initializes the message digest referenced by the operational state handle. Any potentially existing state created by previous operations is discarded.</p>
<h2>Return</h2>
<p>0 if the message digest initialization was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
