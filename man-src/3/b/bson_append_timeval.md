---
title: "bson_append_timeval(3)"
name: "bson_append_timeval"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_timeval/"
description: "bson_append_timeval() – The bson_append_timeval() function is a helper that takes a _struct timeval_ instead of milliseconds since the UNIX epoch."
---

<h2>NAME</h2>
<p> bson_append_timeval() &#8211; The bson_append_timeval() function is a helper that takes a _struct timeval_ instead of milliseconds since the UNIX epoch.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_timeval(bson_t *bson,
                         const char *key,
                         int key_length,
                         struct timeval *value);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII C string containing the name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>value</code></p>
<dd> A struct timeval.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_timeval/">bson_append_timeval</a>(3)</code> function is a helper that takes a _struct timeval_ instead of milliseconds since the UNIX epoch. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
