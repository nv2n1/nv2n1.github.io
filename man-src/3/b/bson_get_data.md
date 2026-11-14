---
title: "bson_get_data(3)"
name: "bson_get_data"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_get_data/"
description: "bson_get_data() – The bson_get_data() function shall return the raw buffer of a bson document. This can be used in conjunction with the len property of a bson_t if you want to copy the raw buffer a..."
---

<h2>NAME</h2>
<p> bson_get_data() &#8211; The bson_get_data() function shall return the raw buffer of a bson document. This can be used in conjunction with the len property of a bson_t if you want to copy the raw buffer around.</p>
<h2>SYNOPSIS</h2>
<pre><code>
const uint8_t *
bson_get_data(const bson_t *bson);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_get_data/">bson_get_data</a>(3)</code> function shall return the raw buffer of a bson document. This can be used in conjunction with the <code>len</code> property of a <code>bson_t</code> if you want to copy the raw buffer around. </p>
<h2>RETURNS</h2>
<p> A buffer which should not be modified or freed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
