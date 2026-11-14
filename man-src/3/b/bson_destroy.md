---
title: "bson_destroy(3)"
name: "bson_destroy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_destroy/"
description: "bson_destroy() – The bson_destroy() function shall free an allocated bson_t structure."
---

<h2>NAME</h2>
<p> bson_destroy() &#8211; The bson_destroy() function shall free an allocated bson_t structure.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_destroy(bson_t *bson);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> function shall free an allocated <code>bson_t</code> structure. </p>
<p> This function should always be called when you are done with a <code>bson_t</code> unless otherwise specified. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
