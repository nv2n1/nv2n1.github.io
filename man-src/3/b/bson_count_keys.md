---
title: "bson_count_keys(3)"
name: "bson_count_keys"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_count_keys/"
description: "bson_count_keys() – The bson_count_keys() function shall count the number of elements within bson."
---

<h2>NAME</h2>
<p> bson_count_keys() &#8211; The bson_count_keys() function shall count the number of elements within bson.</p>
<h2>SYNOPSIS</h2>
<pre><code>
uint32_t
bson_count_keys(const bson_t *bson);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_count_keys/">bson_count_keys</a>(3)</code> function shall count the number of elements within <code>bson</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A positive integer or zero. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
