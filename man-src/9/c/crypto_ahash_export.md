---
title: "crypto_ahash_export(9)"
name: "crypto_ahash_export"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crypto_ahash_export/"
description: "crypto_ahash_export – extract current message digest state"
---

<p>crypto_ahash_export &#8211; extract current message digest state</p>
<h2>Synopsis</h2>
<pre><code>int crypto_ahash_export(struct ahash_request *req, void *out);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>reference to the ahash_request handle whose state is exported</dl>
<p> <i>out</i></p>
<dl>
<dd>output buffer of sufficient size that can hold the hash state</dl>
<h2>Description</h2>
<p>This function exports the hash state of the ahash_request handle into the caller-allocated output buffer out which must have sufficient size (e.g. by calling crypto_ahash_reqsize).</p>
<h2>Return</h2>
<p>0 if the export was successful; &lt; 0 if an error occurred</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
