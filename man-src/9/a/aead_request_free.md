---
title: "aead_request_free(9)"
name: "aead_request_free"
section: "9"
letter: "a"
url: "/docs/linux/man/9-aead_request_free/"
description: "aead_request_free – zeroize and free request data structure"
---

<p>aead_request_free &#8211; zeroize and free request data structure</p>
<h2>Synopsis</h2>
<pre><code>void aead_request_free(struct aead_request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request data structure cipher handle to be freed</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
