---
title: "bson_iter_value(3)"
name: "bson_iter_value"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_value/"
description: "bson_iter_value() – Fetches the value for the currently observed type as a boxed type. This allows passing around the value without knowing the type at runtime."
---

<h2>NAME</h2>
<p> bson_iter_value() &#8211; Fetches the value for the currently observed type as a boxed type. This allows passing around the value without knowing the type at runtime.</p>
<h2>SYNOPSIS</h2>
<pre><code>
const bson_value_t *
bson_iter_value(bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the value for the currently observed type as a boxed type. This allows passing around the value without knowing the type at runtime. </p>
<h2>RETURNS</h2>
<p> A <code>bson_value_t</code> that should not be modified or freed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
