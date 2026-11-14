---
title: "bson_equal(3)"
name: "bson_equal"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_equal/"
description: "bson_equal() – The bson_equal() function shall return true if both documents are equal."
---

<h2>NAME</h2>
<p> bson_equal() &#8211; The bson_equal() function shall return true if both documents are equal.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_equal(const bson_t *bson,
                const bson_t *other);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>other</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_equal/">bson_equal</a>(3)</code> function shall return true if both documents are equal. </p>
<h2>RETURNS</h2>
<p> true if both documents are equal. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
