---
title: "ahash_request_set_crypt(9)"
name: "ahash_request_set_crypt"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ahash_request_set_crypt/"
description: "ahash_request_set_crypt – set data buffers"
---

<p>ahash_request_set_crypt &#8211; set data buffers</p>
<h2>Synopsis</h2>
<pre><code>void ahash_request_set_crypt(struct ahash_request *req, struct scatterlist *src, u8 *result, unsigned int nbytes);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>ahash_request handle to be updated</dl>
<p> <i>src</i></p>
<dl>
<dd>source scatter/gather list</dl>
<p> <i>result</i></p>
<dl>
<dd>buffer that is filled with the message digest &#8212; the caller must ensure that the buffer has sufficient space by, for example, calling <code>crypto_ahash_digestsize</code></dl>
<p> <i>nbytes</i></p>
<dl>
<dd>number of bytes to process from the source scatter/gather list</dl>
<h2>Description</h2>
<p>By using this call, the caller references the source scatter/gather list. The source scatter/gather list points to the data the message digest is to be calculated for.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
