---
title: "bson_iter_timestamp(3)"
name: "bson_iter_timestamp"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_timestamp/"
description: "bson_iter_timestamp() – The BSON_TYPE_TIMESTAMP type is not a date/time and is typically used for intra-server communication."
---

<h2>NAME</h2>
<p> bson_iter_timestamp() &#8211; The BSON_TYPE_TIMESTAMP type is not a date/time and is typically used for intra-server communication.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_TIMESTAMP(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_TIMESTAMP)
void bson_iter_timestamp(const bson_iter_t *iter,
                         uint32_t *timestamp,
                         uint32_t *increment);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>timestamp</code></p>
<dd> A uint32_t.</dl>
<dl>
<dt><code>increment</code></p>
<dd> A uint32_t.</dl>
<h2>DESCRIPTION</h2>
<p> The BSON_TYPE_TIMESTAMP type is not a date/time and is typically used for intra-server communication. </p>
<p> You probably want <code><a href="/docs/linux/man/3-bson_iter_date_time/">bson_iter_date_time</a>(3)</code> \&amp;. </p>
<p> The <code><a href="/docs/linux/man/3-bson_iter_timestamp/">bson_iter_timestamp</a>(3)</code> function shall return the contents of a BSON_TYPE_TIMESTAMP element. It is invalid to call this function while observing an element that is not of type BSON_TYPE_TIMESTAMP. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
