---
title: "bson_iter_key(3)"
name: "bson_iter_key"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_key/"
description: "bson_iter_key() – Fetches the key for the current element observed by iter."
---

<h2>NAME</h2>
<p> bson_iter_key() &#8211; Fetches the key for the current element observed by iter.</p>
<h2>SYNOPSIS</h2>
<pre><code>
const char *
bson_iter_key(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the key for the current element observed by <code>iter</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A string which should not be modified or freed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
