---
title: "akcipher_request_set_callback(9)"
name: "akcipher_request_set_callback"
section: "9"
letter: "a"
url: "/docs/linux/man/9-akcipher_request_set_callback/"
description: "akcipher_request_set_callback – Sets an asynchronous callback."
---

<p>akcipher_request_set_callback &#8211; Sets an asynchronous callback.</p>
<h2>Synopsis</h2>
<pre><code>void akcipher_request_set_callback(struct akcipher_request *req, u32 flgs, crypto_completion_t cmpl, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request that the callback will be set for</dl>
<p> <i>flgs</i></p>
<dl>
<dd>specify for instance if the operation may backlog</dl>
<p> <i>cmpl</i></p>
<dl>
<dd>callback which will be called</dl>
<p> <i>data</i></p>
<dl>
<dd>private data used by the caller</dl>
<h2>Description</h2>
<p>Callback will be called when an asynchronous operation on a given request is finished.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
