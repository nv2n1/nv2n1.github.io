---
title: "eventfd_ctx_fdget(9)"
name: "eventfd_ctx_fdget"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_ctx_fdget/"
---

eventfd_ctx_fdget - Acquires a reference to the internal eventfd context.

<h2>Synopsis</h2>

<pre><code>struct eventfd_ctx *eventfd_ctx_fdget(int fd);</code></pre>

<h2>Arguments</h2>

<i>fd</i>
<dl><dd>[in] Eventfd file descriptor.</dl>

<h2>Description</h2>

<dd>Returns a pointer to the internal eventfd context, otherwise the error pointers returned by the following functions: 

 eventfd_fget

<h2>Copyright</h2>


