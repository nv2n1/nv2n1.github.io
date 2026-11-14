---
title: "napi_enable(9)"
name: "napi_enable"
section: "9"
letter: "n"
url: "/docs/linux/man/9-napi_enable/"
---

napi_enable - enable NAPI scheduling

<h2>Synopsis</h2>

<pre><code>void napi_enable(struct napi_struct *n);</code></pre>

<h2>Arguments</h2>

<i>n</i>
<dl><dd><dd>NAPI context</dl>

<h2>Description</h2>

Resume NAPI from being scheduled on this context. Must be paired with napi_disable.

<h2>Copyright</h2>


