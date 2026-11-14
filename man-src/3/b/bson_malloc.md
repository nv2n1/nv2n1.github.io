---
title: "bson_malloc(3)"
name: "bson_malloc"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_malloc/"
description: "bson_malloc() – This is a portable malloc() wrapper."
---

<h2>NAME</h2>
<p> bson_malloc() &#8211; This is a portable malloc() wrapper.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void *
bson_malloc(size_t num_bytes);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>num_bytes</code></p>
<dd> A size_t containing the number of bytes to allocate.</dl>
<h2>DESCRIPTION</h2>
<p> This is a portable <code><a href="/docs/linux/man/3-malloc/">malloc</a>(3)</code> wrapper. </p>
<p> In general, this function will return an allocation at least <code>sizeof(void*)</code> bytes or bigger. </p>
<p> If there was a failure to allocate <code>num_bytes</code> bytes, the process will be aborted. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> This function will abort on failure to allocate memory.</dl>
<h2>RETURNS</h2>
<p> A pointer to a memory region which <code>HAS NOT</code> been zeroed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
