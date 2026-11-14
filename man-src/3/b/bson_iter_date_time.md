---
title: "bson_iter_date_time(3)"
name: "bson_iter_date_time"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_date_time/"
description: "bson_iter_date_time() – The bson_iter_date_time() function shall return the number of miliseconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element."
---

<h2>NAME</h2>
<p> bson_iter_date_time() &#8211; The bson_iter_date_time() function shall return the number of miliseconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_DATE_TIME(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_DATE_TIME)
int64_t
bson_iter_date_time(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The bson_iter_date_time() function shall return the number of miliseconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element. </p>
<h2>RETURNS</h2>
<p> A 64-bit integer containing the number of milliseconds since the UNIX epoch. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
