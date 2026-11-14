---
title: "bson_value_copy(3)"
name: "bson_value_copy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_value_copy/"
description: "bson_value_copy() – This function will copy the boxed content in src into dst. dst must be freed with bson_value_destroy() when no longer in use."
---

<h2>NAME</h2>
<p> bson_value_copy() &#8211; This function will copy the boxed content in src into dst. dst must be freed with bson_value_destroy() when no longer in use.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_value_copy(const bson_value_t *src,
                     bson_value_t *dst);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>src</code></p>
<dd> A <code>bson_value_t</code> to copy from.</dl>
<dl>
<dt><code>dst</code></p>
<dd> A <code>bson_value_t</code> to copy into.</dl>
<h2>DESCRIPTION</h2>
<p> This function will copy the boxed content in <code>src</code> into <code>dst</code> \&amp;. <code>dst</code> must be freed with <code><a href="/docs/linux/man/3-bson_value_destroy/">bson_value_destroy</a>(3)</code> when no longer in use. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
