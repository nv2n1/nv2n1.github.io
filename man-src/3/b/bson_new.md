---
title: "bson_new(3)"
name: "bson_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_new/"
description: "bson_new() – The bson_new() function shall create a new bson_t structure on the heap. It should be freed with bson_destroy() when it is no longer in use."
---

<h2>NAME</h2>
<p> bson_new() &#8211; The bson_new() function shall create a new bson_t structure on the heap. It should be freed with bson_destroy() when it is no longer in use.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bson_t *
bson_new(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_new/">bson_new</a>(3)</code> function shall create a new <code>bson_t</code> structure on the heap. It should be freed with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> when it is no longer in use. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_t</code> that should be freed with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
