---
title: "bson_value_destroy(3)"
name: "bson_value_destroy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_value_destroy/"
description: "bson_value_destroy() – Releases any resources associated with value."
---

<h2>NAME</h2>
<p> bson_value_destroy() &#8211; Releases any resources associated with value.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_value_destroy(bson_value_t *value);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>value</code></p>
<dd> A <code>bson_value_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Releases any resources associated with <code>value</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
