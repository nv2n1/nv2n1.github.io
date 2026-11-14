---
title: "bson_set_error(3)"
name: "bson_set_error"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_set_error/"
description: "bson_set_error() – This is a helper function to set the parameters of a bson_error_t. It handles the case where error is NULL by doing nothing."
---

<h2>NAME</h2>
<p> bson_set_error() &#8211; This is a helper function to set the parameters of a bson_error_t. It handles the case where error is NULL by doing nothing.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_set_error(bson_error_t *error,
                    uint32_t domain,
                    uint32_t code,
                    const char *format,
                    ...) BSON_GNUC_PRINTF(4, 5);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>error</code></p>
<dd> A <code>bson_error_t</code> \&amp;.</dl>
<dl>
<dt><code>domain</code></p>
<dd> A <code>uint32_t</code> \&amp;.</dl>
<dl>
<dt><code>code</code></p>
<dd> A <code>uint32_t</code> \&amp;.</dl>
<dl>
<dt><code>format</code></p>
<dd> A <code><a href="/docs/linux/man/3-printf/">printf</a>(3)</code> style format string.</dl>
<h2>DESCRIPTION</h2>
<p> This is a helper function to set the parameters of a <code>bson_error_t</code> \&amp;. It handles the case where <code>error</code> is NULL by doing nothing. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
