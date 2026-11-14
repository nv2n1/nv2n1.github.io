---
title: "bson_strdup_printf(3)"
name: "bson_strdup_printf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strdup_printf/"
description: "bson_strdup_printf() – This function performs a printf style format but into a newly allocated string."
---

<h2>NAME</h2>
<p> bson_strdup_printf() &#8211; This function performs a printf style format but into a newly allocated string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_strdup_printf(const char *format,
                   ...) BSON_GNUC_PRINTF(1, 2);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>format</code></p>
<dd> A printf style format string.</dl>
<h2>DESCRIPTION</h2>
<p> This function performs a printf style format but into a newly allocated string. </p>
<h2>RETURNS</h2>
<p> A newly allocated string that should be freed with bson_free(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
