---
title: "struct_aead_request(9)"
name: "struct_aead_request"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_aead_request/"
description: "struct_aead_request – AEAD request"
---

<p>struct_aead_request &#8211; AEAD request</p>
<h2>Synopsis</h2>
<pre><code>struct aead_request {
    struct crypto_async_request base;
    unsigned int assoclen;
    unsigned int cryptlen;
    u8 *iv;
    struct scatterlist *src;
    struct scatterlist *dst;
    void *__ctx[];
};</code></pre>
<h2>Members</h2>
<p>base</p>
<dl>
<dd>Common attributes for async crypto requests</dl>
<p> assoclen</p>
<dl>
<dd>Length in bytes of associated data for authentication</dl>
<p> cryptlen</p>
<dl>
<dd>Length of data to be encrypted or decrypted</dl>
<p> iv</p>
<dl>
<dd>Initialisation vector</dl>
<p> src</p>
<dl>
<dd>Source data</dl>
<p> dst</p>
<dl>
<dd>Destination data</dl>
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
