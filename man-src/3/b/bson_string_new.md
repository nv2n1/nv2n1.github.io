---
title: "bson_string_new(3)"
name: "bson_string_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_new/"
description: "bson_string_new() – Creates a new string builder, which uses power-of-two growth of buffers. Use the various bson_string_append*() functions to append to the string."
---

<h2>NAME</h2>
<p> bson_string_new() &#8211; Creates a new string builder, which uses power-of-two growth of buffers. Use the various bson_string_append*() functions to append to the string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bson_string_t *
bson_string_new(const char *str);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></p>
<dd> A string to be copied or NULL.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new string builder, which uses power-of-two growth of buffers. Use the various bson_string_append*() functions to append to the string. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_string_t that should be freed with bson_string_free() when no longer in use. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
