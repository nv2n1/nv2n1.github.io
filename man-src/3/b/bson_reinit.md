---
title: "bson_reinit(3)"
name: "bson_reinit"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reinit/"
description: "bson_reinit() – The bson_reinit() function shall be equivalent to calling bson_destroy() and bson_init()."
---

<h2>NAME</h2>
<p> bson_reinit() &#8211; The bson_reinit() function shall be equivalent to calling bson_destroy() and bson_init().</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_reinit(bson_t *b);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>b</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_reinit/">bson_reinit</a>(3)</code> function shall be equivalent to calling <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> and <code><a href="/docs/linux/man/3-bson_init/">bson_init</a>(3)</code> \&amp;. </p>
<p> However, if the <code>bson_t</code> structure contains a malloc()&#8217;d buffer, it may be reused. To be certain that any buffer is freed, always call <code>bson_destroy</code> on any <code>bson_t</code> structure, whether initialized or reinitialized, after its final use. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
