---
title: "hx509_context_free(3)"
name: "hx509_context_free"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_context_free/"
description: "hx509 library –"
---

<h2 class="name">NAME</h2>
<p> hx509 library &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_context_init</code> (hx509_context *context) </p>
<p> void <code>hx509_context_free</code> (hx509_context *context) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void hx509_context_free (hx509_context *context)</h3>
<p> Free the context allocated by <code>hx509_context_init()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> context to be freed.</dl>
<h3>int hx509_context_init (hx509_context *context)</h3>
<p> Creates a hx509 context that most functions in the library uses. The context is only allowed to be used by one thread at each moment. Free the context with <code>hx509_context_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Returns a pointer to new hx509 context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
