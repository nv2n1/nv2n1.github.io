---
title: "bson_string_append_c(3)"
name: "bson_string_append_c"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_append_c/"
description: "bson_string_append_c() – Appends c to the string builder string."
---

<h2>NAME</h2>
<p> bson_string_append_c() &#8211; Appends c to the string builder string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_string_append_c(bson_string_t *string,
                          char str);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></p>
<dd> A <code>bson_string_t</code> \&amp;.</dl>
<dl>
<dt><code>str</code></p>
<dd> An ASCII char.</dl>
<h2>DESCRIPTION</h2>
<p> Appends <code>c</code> to the string builder <code>string</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
