---
title: "bson_strfreev(3)"
name: "bson_strfreev"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strfreev/"
description: "bson_strfreev() – This will free each string in a NULL-terminated array of strings and then the array itself."
---

<h2>NAME</h2>
<p> bson_strfreev() &#8211; This will free each string in a NULL-terminated array of strings and then the array itself.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_strfreev(char **strv);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>strv</code></p>
<dd> A NULL-terminated array of strings to free, including the array.</dl>
<h2>DESCRIPTION</h2>
<p> This will free each string in a NULL-terminated array of strings and then the array itself. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
