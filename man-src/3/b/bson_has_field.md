---
title: "bson_has_field(3)"
name: "bson_has_field"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_has_field/"
description: "bson_has_field() – Checks to see if key contains an element named key. This also accepts \"dotkey\" notation such as \"a.b.c.d\"."
---

<h2>NAME</h2>
<p> bson_has_field() &#8211; Checks to see if key contains an element named key. This also accepts &quot;dotkey&quot; notation such as &quot;a.b.c.d&quot;.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_has_field(const bson_t *bson,
                    const char *key);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> A string containing the name of the field to check for.</dl>
<h2>DESCRIPTION</h2>
<p> Checks to see if key contains an element named <code>key</code> \&amp;. This also accepts &quot;dotkey&quot; notation such as &quot;a.b.c.d&quot;. </p>
<h2>RETURNS</h2>
<p> true if <code>key</code> was found within <code>bson</code> ; otherwise false. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
