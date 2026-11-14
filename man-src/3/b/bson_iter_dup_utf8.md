---
title: "bson_iter_dup_utf8(3)"
name: "bson_iter_dup_utf8"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_dup_utf8/"
description: "bson_iter_dup_utf8() – This function is similar to bson_iter_utf8() except that it calls bson_strndup() on the result."
---

<h2>NAME</h2>
<p> bson_iter_dup_utf8() &#8211; This function is similar to bson_iter_utf8() except that it calls bson_strndup() on the result.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_iter_dup_utf8(const bson_iter_t *iter,
                   uint32_t *length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>length</code></p>
<dd> An optional location for the length of the UTF-8 encoded string.</dl>
<h2>DESCRIPTION</h2>
<p> This function is similar to <code><a href="/docs/linux/man/3-bson_iter_utf8/">bson_iter_utf8</a>(3)</code> except that it calls <code><a href="/docs/linux/man/3-bson_strndup/">bson_strndup</a>(3)</code> on the result. </p>
<h2>RETURNS</h2>
<p> A newly allocated string that should be freed with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
