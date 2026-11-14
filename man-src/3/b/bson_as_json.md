---
title: "bson_as_json(3)"
name: "bson_as_json"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_as_json/"
description: "bson_as_json() – The bson_as_json() function shall encode bson as a JSON encoded UTF-8 string."
---

<h2>NAME</h2>
<p> bson_as_json() &#8211; The bson_as_json() function shall encode bson as a JSON encoded UTF-8 string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_as_json(const bson_t *bson,
             size_t *length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>length</code></p>
<dd> An optional location for the length of the resulting string.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_as_json/">bson_as_json</a>(3)</code> function shall encode <code>bson</code> as a JSON encoded UTF-8 string. </p>
<p> The caller is responsible for freeing the resulting UTF-8 encoded string by calling <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> with the result. </p>
<p> If non-NULL, <code>length</code> will be set to the length of the result in bytes. </p>
<h2>RETURNS</h2>
<p> If successful, a newly allocated UTF-8 encoded string and <code>length</code> is set. </p>
<p> Upon failure, NULL is returned. </p>
<h2>EXAMPLE</h2>
<pre><code>
char *str = bson_as_json(doc, NULL);
printf("%s
", str);
bson_free(str);
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
