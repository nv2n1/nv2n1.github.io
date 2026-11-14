---
title: "bson_oid_get_time_t(3)"
name: "bson_oid_get_time_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_get_time_t/"
description: "bson_oid_get_time_t() – Fetches the generation time in seconds since the UNIX Epoch of oid."
---

<h2>NAME</h2>
<p> bson_oid_get_time_t() &#8211; Fetches the generation time in seconds since the UNIX Epoch of oid.</p>
<h2>SYNOPSIS</h2>
<pre><code>
time_t
bson_oid_get_time_t(const bson_oid_t *oid);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the generation time in seconds since the UNIX Epoch of <code>oid</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A time_t containing the seconds since the UNIX epoch of <code>oid</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
