---
title: "aead_request_set_ad(9)"
name: "aead_request_set_ad"
section: "9"
letter: "a"
url: "/docs/linux/man/9-aead_request_set_ad/"
description: "aead_request_set_ad – set associated data information"
---

<p>aead_request_set_ad &#8211; set associated data information</p>
<h2>Synopsis</h2>
<pre><code>void aead_request_set_ad(struct aead_request *req, unsigned int assoclen);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request handle</dl>
<p> <i>assoclen</i></p>
<dl>
<dd>number of bytes in associated data</dl>
<h2>Description</h2>
<p>Setting the AD information. This function sets the length of the associated data.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
