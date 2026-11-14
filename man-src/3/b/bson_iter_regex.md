---
title: "bson_iter_regex(3)"
name: "bson_iter_regex"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_regex/"
description: "bson_iter_regex() – The bson_iter_regex() function shall retrieve the contents of a BSON_TYPE_REGEX element currently observed by iter."
---

<h2>NAME</h2>
<p> bson_iter_regex() &#8211; The bson_iter_regex() function shall retrieve the contents of a BSON_TYPE_REGEX element currently observed by iter.</p>
<h2>SYNOPSIS</h2>
<pre><code>
const char *
bson_iter_regex(const bson_iter_t *iter,
                const char **options);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>options</code></p>
<dd> A (null).</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_regex/">bson_iter_regex</a>(3)</code> function shall retrieve the contents of a BSON_TYPE_REGEX element currently observed by <code>iter</code> \&amp;. </p>
<p> It is invalid to call this function when not observing an element of type BSON_TYPE_REGEX. </p>
<h2>RETURNS</h2>
<p> A string containing the regex which should not be modified or freed. <code>options</code> is set to the options provided for the regex. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
