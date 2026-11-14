---
title: "bson_string_append_printf(3)"
name: "bson_string_append_printf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_append_printf/"
description: "bson_string_append_printf() – Like bson_string_append() but formats a printf style string and then appends that to string."
---

<h2>NAME</h2>
<p> bson_string_append_printf() &#8211; Like bson_string_append() but formats a printf style string and then appends that to string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_string_append_printf(bson_string_t *string,
                               const char *format,
                               ...) BSON_GNUC_PRINTF(2, 3);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></p>
<dd> A <code>bson_string_t</code> \&amp;.</dl>
<dl>
<dt><code>format</code></p>
<dd> A printf style format string.</dl>
<h2>DESCRIPTION</h2>
<p> Like bson_string_append() but formats a printf style string and then appends that to <code>string</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
