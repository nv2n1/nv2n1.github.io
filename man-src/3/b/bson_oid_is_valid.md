---
title: "bson_oid_is_valid(3)"
name: "bson_oid_is_valid"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_is_valid/"
description: "bson_oid_is_valid() – Checks if a string containing a hex encoded string is a valid BSON ObjectID."
---

<h2>NAME</h2>
<p> bson_oid_is_valid() &#8211; Checks if a string containing a hex encoded string is a valid BSON ObjectID.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_oid_is_valid(const char *str,
                       size_t length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></p>
<dd> A string.</dl>
<dl>
<dt><code>length</code></p>
<dd> The length of <code>str</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Checks if a string containing a hex encoded string is a valid BSON ObjectID. </p>
<h2>RETURNS</h2>
<p> true if <code>str</code> could be parsed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
