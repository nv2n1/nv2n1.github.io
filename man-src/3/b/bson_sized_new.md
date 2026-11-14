---
title: "bson_sized_new(3)"
name: "bson_sized_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_sized_new/"
description: "bson_sized_new() – The bson_sized_new() function shall create a new bson_t on the heap with a preallocated buffer. This is useful if you have a good idea of the size of the resulting document."
---

<h2>NAME</h2>
<p> bson_sized_new() &#8211; The bson_sized_new() function shall create a new bson_t on the heap with a preallocated buffer. This is useful if you have a good idea of the size of the resulting document.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_t *
bson_sized_new (size_t size);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>size</code></p>
<dd> The size to pre-allocate for the underlying buffer.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_sized_new/">bson_sized_new</a>(3)</code> function shall create a new <code>bson_t</code> on the heap with a preallocated buffer. This is useful if you have a good idea of the size of the resulting document. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_t</code> that should be freed with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
