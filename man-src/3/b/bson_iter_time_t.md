---
title: "bson_iter_time_t(3)"
name: "bson_iter_time_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_time_t/"
description: "bson_iter_time_t() – The bson_iter_time_t() function shall return the number of seconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element."
---

<h2>NAME</h2>
<p> bson_iter_time_t() &#8211; The bson_iter_time_t() function shall return the number of seconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element.</p>
<h2>SYNOPSIS</h2>
<pre><code>
time_t
bson_iter_time_t(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_time_t/">bson_iter_time_t</a>(3)</code> function shall return the number of seconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element. </p>
<h2>RETURNS</h2>
<p> A <code>time_t</code> containing the number of seconds since the UNIX epoch. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
