---
title: "struct_akcipher_request(9)"
name: "struct_akcipher_request"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_akcipher_request/"
description: "struct_akcipher_request – public key request"
---

<p>struct_akcipher_request &#8211; public key request</p>
<h2>Synopsis</h2>
<pre><code>struct akcipher_request {
    struct crypto_async_request base;
    struct scatterlist *src;
    struct scatterlist *dst;
    unsigned int src_len;
    unsigned int dst_len;
    void *__ctx[];
};</code></pre>
<h2>Members</h2>
<p>base</p>
<dl>
<dd>Common attributes for async crypto requests</dl>
<p> src</p>
<dl>
<dd>Source data</dl>
<p> dst</p>
<dl>
<dd>Destination data</dl>
<p> src_len</p>
<dl>
<dd>Size of the input buffer</dl>
<p> dst_len</p>
<dl>
<dd>Size of the output buffer. It needs to be at least as big as the expected result depending on the operation After operation it will be updated with the actual size of the result. In case of error where the dst sgl size was insufficient, it will be updated to the size required for the operation.</dl>
<p> __ctx[]</p>
<dl>
<dd>Start of private context data</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
