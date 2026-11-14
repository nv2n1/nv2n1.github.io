---
title: "bson_string_free(3)"
name: "bson_string_free"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_free/"
description: "bson_string_free() – Frees the bson_string_t structure and optionally the string itself."
---

<h2>NAME</h2>
<p> bson_string_free() &#8211; Frees the bson_string_t structure and optionally the string itself.</p>
<h2>SYNOPSIS</h2>
<pre>
char *
bson_string_free (bson_string_t *string,
                  bool           free_segment);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></p>
<dd> A <code>bson_string_t</code> \&amp;.</dl>
<dl>
<dt><code>free_segment</code></p>
<dd> A bool indicating if <code>str-&gt;str</code> should be returned.</dl>
<h2>DESCRIPTION</h2>
<p> Frees the bson_string_t structure and optionally the string itself. </p>
<h2>RETURNS</h2>
<p> <code>str-&gt;str</code> if <code>free_segment</code> is true, otherwise NULL. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
