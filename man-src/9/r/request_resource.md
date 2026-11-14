---
title: "request_resource(9)"
name: "request_resource"
section: "9"
letter: "r"
url: "/docs/linux/man/9-request_resource/"
---

request_resource - request and reserve an I/O or memory resource

<h2>Synopsis</h2>

<pre><code>int request_resource(struct resource *root, struct resource *new);</code></pre>

<h2>Arguments</h2>

<i>root</i>
<dl><dd><dd>root resource descriptor</dl>
 

 <i>new</i>
<dl><dd>resource descriptor desired by caller</dl>

<h2>Description</h2>

Returns 0 for success, negative error code on error.

<h2>Copyright</h2>


