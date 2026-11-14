---
title: "eventfd_ctx_put(9)"
name: "eventfd_ctx_put"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_ctx_put/"
description: "eventfd_ctx_put – Releases a reference to the internal eventfd context."
---

<p>eventfd_ctx_put &#8211; Releases a reference to the internal eventfd context.</p>
<h2>Synopsis</h2>
<pre><code>void eventfd_ctx_put(struct eventfd_ctx *ctx);</code></pre>
<h2>Arguments</h2>
<p><i>ctx</i></p>
<dl>
<dd>[in] Pointer to eventfd context.</dl>
<h2>Description</h2>
<dd>The eventfd context reference must have been previously acquired either with <code>eventfd_ctx_get</code> or <code>eventfd_ctx_fdget</code>.</p>
<h2>Copyright</h2>
