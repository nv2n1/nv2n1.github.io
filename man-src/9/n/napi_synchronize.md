---
title: "napi_synchronize(9)"
name: "napi_synchronize"
section: "9"
letter: "n"
url: "/docs/linux/man/9-napi_synchronize/"
---

napi_synchronize - wait until NAPI is not running

<h2>Synopsis</h2>

<pre><code>void napi_synchronize(const struct napi_struct *n);</code></pre>

<h2>Arguments</h2>

<i>n</i>
<dl><dd><dd>NAPI context</dl>

<h2>Description</h2>

Wait until NAPI is done being scheduled on this context. Waits till any outstanding processing completes but does not disable future activations.

<h2>Copyright</h2>


