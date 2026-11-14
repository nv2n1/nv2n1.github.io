---
title: "bson_strdupv_printf(3)"
name: "bson_strdupv_printf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strdupv_printf/"
description: "bson_strdupv_printf() – This function is like bson_strdup_printf() except takes a va_list of parameters."
---

<h2>NAME</h2>
<p> bson_strdupv_printf() &#8211; This function is like bson_strdup_printf() except takes a va_list of parameters.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_strdupv_printf(const char *format,
                    va_list args) BSON_GNUC_PRINTF(1, 0);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>format</code></p>
<dd> A printf style format string.</dl>
<dl>
<dt><code>args</code></p>
<dd> A va_list.</dl>
<h2>DESCRIPTION</h2>
<p> This function is like <code><a href="/docs/linux/man/3-bson_strdup_printf/">bson_strdup_printf</a>(3)</code> except takes a va_list of parameters. </p>
<h2>RETURNS</h2>
<p> A newly allocated string that should be freed with bson_free(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
