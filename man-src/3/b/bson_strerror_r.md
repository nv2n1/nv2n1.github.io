---
title: "bson_strerror_r(3)"
name: "bson_strerror_r"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strerror_r/"
description: "bson_strerror_r() – This is a portability wrapper around strerror()."
---

<h2>NAME</h2>
<p> bson_strerror_r() &#8211; This is a portability wrapper around strerror().</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_strerror_r(int err_code,
                char *buf,
                size_t buflen);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>err_code</code></p>
<dd> An errno.</dl>
<dl>
<dt><code>buf</code></p>
<dd> A location to store the string.</dl>
<dl>
<dt><code>buflen</code></p>
<dd> The size of <code>buf</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> This is a portability wrapper around <code><a href="/docs/linux/man/3-strerror/">strerror</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> The passed in <code>buf</code> parameter or an internal string. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
