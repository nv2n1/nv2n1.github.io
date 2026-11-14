---
title: "ipc_rcu_alloc(9)"
name: "ipc_rcu_alloc"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_rcu_alloc/"
---

ipc_rcu_alloc - allocate ipc and rcu space

<h2>Synopsis</h2>

<pre><code>void *ipc_rcu_alloc(int size);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>size desired</dl>

<h2>Description</h2>

Allocate memory for the rcu header structure + the object. Returns the pointer to the object or NULL upon failure.

<h2>Copyright</h2>


