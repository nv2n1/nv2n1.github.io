---
title: "bson_init(3)"
name: "bson_init"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_init/"
description: "bson_init() – The bson_init() function shall initialize a bson_t that is placed on the stack. This is equivalent to initializing a bson_t to BSON_INITIALIZER."
---

<h2>NAME</h2>
<p> bson_init() &#8211; The bson_init() function shall initialize a bson_t that is placed on the stack. This is equivalent to initializing a bson_t to BSON_INITIALIZER.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_init(bson_t *b);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>b</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_init/">bson_init</a>(3)</code> function shall initialize a <code>bson_t</code> that is placed on the stack. This is equivalent to initializing a <code>bson_t</code> to <code>BSON_INITIALIZER</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
