---
title: "bson_free(3)"
name: "bson_free"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_free/"
description: "bson_free() – This function shall free the memory supplied by mem. This should be used by functions that require you free the result with bson_free()."
---

<h2>NAME</h2>
<p> bson_free() &#8211; This function shall free the memory supplied by mem. This should be used by functions that require you free the result with bson_free().</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_free(void *mem);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>mem</code></p>
<dd> A memory region.</dl>
<h2>DESCRIPTION</h2>
<p> This function shall free the memory supplied by <code>mem</code> \&amp;. This should be used by functions that require you free the result with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
