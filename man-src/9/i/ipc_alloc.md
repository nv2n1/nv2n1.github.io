---
title: "ipc_alloc(9)"
name: "ipc_alloc"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_alloc/"
---

ipc_alloc - allocate ipc space

<h2>Synopsis</h2>

<pre><code>void *ipc_alloc(int size);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>size desired</dl>

<h2>Description</h2>

Allocate memory from the appropriate pools and return a pointer to it. NULL is returned if the allocation fails

<h2>Copyright</h2>


