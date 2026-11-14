---
title: "bson_iter_find_case(3)"
name: "bson_iter_find_case"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_find_case/"
description: "bson_iter_find_case() – Advances iter until it is observing an element matching the name of key or exhausting all elements."
---

<h2>NAME</h2>
<p> bson_iter_find_case() &#8211; Advances iter until it is observing an element matching the name of key or exhausting all elements.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_iter_find_case(bson_iter_t *iter,
                         const char *key);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII string containing the field to locate.</dl>
<h2>DESCRIPTION</h2>
<p> Advances <code>iter</code> until it is observing an element matching the name of <code>key</code> or exhausting all elements. </p>
<p> <code>key</code> is not case-sensitive. The keys will be case-folded to determine a match using the current locale. </p>
<h2>RETURNS</h2>
<p> true if <code>key</code> was found. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
