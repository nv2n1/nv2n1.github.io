---
title: "eventfd_ctx_fileget(9)"
name: "eventfd_ctx_fileget"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_ctx_fileget/"
---

eventfd_ctx_fileget - Acquires a reference to the internal eventfd context.

<h2>Synopsis</h2>

<pre><code>struct eventfd_ctx *eventfd_ctx_fileget(struct file *file);</code></pre>

<h2>Arguments</h2>

<i>file</i>
<dl><dd>[in] Eventfd file pointer.</dl>

<h2>Description</h2>

<dd>Returns a pointer to the internal eventfd context, otherwise the error pointer: 

 -EINVAL : The <i>fd</i> file descriptor is not an eventfd file.

<h2>Copyright</h2>


