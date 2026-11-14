---
title: "bson_iter_symbol(3)"
name: "bson_iter_symbol"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_symbol/"
description: "bson_iter_symbol() – The symbol element type is DEPRECATED in the bson specification at http://bsonspec.org."
---

<h2>NAME</h2>
<p> bson_iter_symbol() &#8211; The symbol element type is DEPRECATED in the bson specification at <a rel="nofollow" href="http://bsonspec.org.">http://bsonspec.org.</a></p>
<h2>SYNOPSIS</h2>
<pre><code>
const char *
bson_iter_symbol(const bson_iter_t *iter,
                 uint32_t *length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>length</code></p>
<dd> A uint32_t.</dl>
<h2>DESCRIPTION</h2>
<p> The symbol element type is <code>DEPRECATED</code> in the bson specification at <a rel="nofollow" href="http://bsonspec.org.">http://bsonspec.org.</a> </p>
<p> The <code><a href="/docs/linux/man/3-bson_iter_symbol/">bson_iter_symbol</a>(3)</code> function shall return the contents of a BSON_TYPE_SYMBOL element. </p>
<p> if non-NULL, <code>length</code> will be set to the length of the resulting string. </p>
<h2>RETURNS</h2>
<p> The symbol and <code>length</code> is set. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
