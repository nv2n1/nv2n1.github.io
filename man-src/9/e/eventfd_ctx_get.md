---
title: "eventfd_ctx_get(9)"
name: "eventfd_ctx_get"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_ctx_get/"
---

eventfd_ctx_get - Acquires a reference to the internal eventfd context.

<h2>Synopsis</h2>

<pre><code>struct eventfd_ctx *eventfd_ctx_get(struct eventfd_ctx *ctx);</code></pre>

<h2>Arguments</h2>

<i>ctx</i>
<dl><dd>[in] Pointer to the eventfd context.</dl>

<h2>Return</h2>

<dd>In case of success, returns a pointer to the eventfd context.

<h2>Copyright</h2>


