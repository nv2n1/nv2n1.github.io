---
title: "bson_copy_to(3)"
name: "bson_copy_to"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_copy_to/"
description: "bson_copy_to() – The bson_copy_to() function shall initialize dst with a copy of the contents of src."
---

<h2>NAME</h2>
<p> bson_copy_to() &#8211; The bson_copy_to() function shall initialize dst with a copy of the contents of src.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_copy_to(const bson_t *src,
                  bson_t *dst);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>src</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>dst</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_copy_to/">bson_copy_to</a>(3)</code> function shall initialize <code>dst</code> with a copy of the contents of <code>src</code> \&amp;. </p>
<p> <code>dst</code> </p>
<p> <code>MUST</code> be an uninitialized <code>bson_t</code> to avoid leaking memory. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
