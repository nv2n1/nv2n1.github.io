---
title: "bson_concat(3)"
name: "bson_concat"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_concat/"
description: "bson_concat() – The bson_concat() function shall append the contents of src to dst."
---

<h2>NAME</h2>
<p> bson_concat() &#8211; The bson_concat() function shall append the contents of src to dst.</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_concat (bson_t       *dst,
             const bson_t *src);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>dst</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>src</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_concat/">bson_concat</a>(3)</code> function shall append the contents of <code>src</code> to <code>dst</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>dst</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
