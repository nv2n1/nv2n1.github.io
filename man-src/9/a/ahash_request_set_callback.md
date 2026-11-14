---
title: "ahash_request_set_callback(9)"
name: "ahash_request_set_callback"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ahash_request_set_callback/"
description: "ahash_request_set_callback – set asynchronous callback function"
---

<p>ahash_request_set_callback &#8211; set asynchronous callback function</p>
<h2>Synopsis</h2>
<pre><code>void ahash_request_set_callback(struct ahash_request *req, u32 flags, crypto_completion_t compl, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request handle</dl>
<p> <i>flags</i></p>
<dl>
<dd>specify zero or an ORing of the flags CRYPTO_TFM_REQ_MAY_BACKLOG the request queue may back log and increase the wait queue beyond the initial maximum size; CRYPTO_TFM_REQ_MAY_SLEEP the request processing may sleep</dl>
<p> <i>compl</i></p>
<dl>
<dd>callback function pointer to be registered with the request handle</dl>
<p> <i>data</i></p>
<dl>
<dd>The data pointer refers to memory that is not used by the kernel crypto API, but provided to the callback function for it to use. Here, the caller can provide a reference to memory the callback function can operate on. As the callback function is invoked asynchronously to the related functionality, it may need to access data structures of the related functionality which can be referenced using this pointer. The callback function can access the memory via the &#8220;data&#8221; field in the crypto_async_request data structure provided to the callback function.</dl>
<h2>Description</h2>
<p>This function allows setting the callback function that is triggered once the cipher operation completes. </p>
<p> The callback function is registered with the ahash_request handle and must comply with the following template </p>
<p> void callback_function(struct crypto_async_request *req, int error)</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
