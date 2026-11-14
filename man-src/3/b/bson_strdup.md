---
title: "bson_strdup(3)"
name: "bson_strdup"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strdup/"
description: "bson_strdup() – Copies str into a new string. If str is NULL, then NULL is returned."
---

<h2>NAME</h2>
<p> bson_strdup() &#8211; Copies str into a new string. If str is NULL, then NULL is returned.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_strdup(const char *str);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></p>
<dd> A string.</dl>
<h2>DESCRIPTION</h2>
<p> Copies <code>str</code> into a new string. If <code>str</code> is NULL, then NULL is returned. </p>
<h2>RETURNS</h2>
<p> A newly allocated string that should be freed with bson_free(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
