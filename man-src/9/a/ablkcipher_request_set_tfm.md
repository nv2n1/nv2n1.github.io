---
title: "ablkcipher_request_set_tfm(9)"
name: "ablkcipher_request_set_tfm"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ablkcipher_request_set_tfm/"
description: "ablkcipher_request_set_tfm – update cipher handle reference in request"
---

<p>ablkcipher_request_set_tfm &#8211; update cipher handle reference in request</p>
<h2>Synopsis</h2>
<pre><code>void ablkcipher_request_set_tfm(struct ablkcipher_request *req, struct crypto_ablkcipher *tfm);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request handle to be modified</dl>
<p> <i>tfm</i></p>
<dl>
<dd>cipher handle that shall be added to the request handle</dl>
<h2>Description</h2>
<p>Allow the caller to replace the existing ablkcipher handle in the request data structure with a different one.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
