---
title: "bson_zero_free(3)"
name: "bson_zero_free"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_zero_free/"
description: "bson_zero_free() – This function behaves like bson_free() except that it zeroes the memory first. This can be useful if you are storing passwords or other similarly important data. Note that if it ..."
---

<h2>NAME</h2>
<p> bson_zero_free() &#8211; This function behaves like bson_free() except that it zeroes the memory first. This can be useful if you are storing passwords or other similarly important data. Note that if it truly is important, you probably want a page protected with mlock() as well to prevent it swapping to disk.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_zero_free(void *mem,
                    size_t size);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>mem</code></p>
<dd> A memory region.</dl>
<dl>
<dt><code>size</code></p>
<dd> The size of <code>mem</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> This function behaves like <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> except that it zeroes the memory first. This can be useful if you are storing passwords or other similarly important data. Note that if it truly is important, you probably want a page protected with <code><a href="/docs/linux/man/3-mlock/">mlock</a>(3)</code> as well to prevent it swapping to disk. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
