---
title: "sk_wmem_alloc_get(9)"
name: "sk_wmem_alloc_get"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_wmem_alloc_get/"
---

sk_wmem_alloc_get - returns write allocations

<h2>Synopsis</h2>

<pre><code>int sk_wmem_alloc_get(const struct sock *sk);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>socket</dl>

<h2>Description</h2>

Returns sk_wmem_alloc minus initial offset of one

<h2>Copyright</h2>


