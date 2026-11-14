---
title: "bson_copy(3)"
name: "bson_copy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_copy/"
description: "bson_copy() – The bson_copy() function shall copy the contents of a bson document into a new bson_t."
---

<h2>NAME</h2>
<p> bson_copy() &#8211; The bson_copy() function shall copy the contents of a bson document into a new bson_t.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bson_t *
bson_copy(const bson_t *bson);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_copy/">bson_copy</a>(3)</code> function shall copy the contents of a bson document into a new <code>bson_t</code> \&amp;. </p>
<p> The resulting <code>bson_t</code> should be freed with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_t</code> that should be freed with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
