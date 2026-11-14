---
title: "request_resource_conflict(9)"
name: "request_resource_conflict"
section: "9"
letter: "r"
url: "/docs/linux/man/9-request_resource_conflict/"
---

request_resource_conflict - request and reserve an I/O or memory resource

<h2>Synopsis</h2>

<pre><code>struct resource *request_resource_conflict(struct resource *root, struct resource *new);</code></pre>

<h2>Arguments</h2>

<i>root</i>
<dl><dd><dd>root resource descriptor</dl>
 

 <i>new</i>
<dl><dd>resource descriptor desired by caller</dl>

<h2>Description</h2>

Returns 0 for success, conflict resource on error.

<h2>Copyright</h2>


