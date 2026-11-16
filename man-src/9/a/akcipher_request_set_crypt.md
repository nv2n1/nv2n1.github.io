---
title: "akcipher_request_set_crypt(9)"
name: "akcipher_request_set_crypt"
section: "9"
letter: "a"
url: "/docs/linux/man/9-akcipher_request_set_crypt/"
description: "akcipher_request_set_crypt – Sets request parameters"
---

<p>akcipher_request_set_crypt &#8211; Sets request parameters</p>
<h2>Synopsis</h2>
<pre><code>void akcipher_request_set_crypt(struct akcipher_request *req, struct scatterlist *src, struct scatterlist *dst, unsigned int src_len, unsigned int dst_len);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
</dd><dd>public key request</dd></dl>
<p> <i>src</i></p>
<dl>
<dd>ptr to input scatter list</dd></dl>
<p> <i>dst</i></p>
<dl>
<dd>ptr to output scatter list</dd></dl>
<p> <i>src_len</i></p>
<dl>
<dd>size of the src input scatter list to be processed</dd></dl>
<p> <i>dst_len</i></p>
<dl>
<dd>size of the dst output scatter list</dd></dl>
<h2>Description</h2>
<p>Sets parameters required by crypto operation</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
