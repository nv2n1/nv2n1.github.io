---
title: "bson_context_destroy(3)"
name: "bson_context_destroy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_context_destroy/"
description: "bson_context_destroy() – The bson_context_destroy() function shall release all resources associated with context."
---

<h2>NAME</h2>
<p> bson_context_destroy() &#8211; The bson_context_destroy() function shall release all resources associated with context.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_context_destroy(bson_context_t *context);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>context</code></p>
<dd> A <code>bson_context_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_context_destroy/">bson_context_destroy</a>(3)</code> function shall release all resources associated with <code>context</code> \&amp;. </p>
<p> This should be called when you are no longer using a <code>bson_context_t</code> that you have allocated with <code><a href="/docs/linux/man/3-bson_context_new/">bson_context_new</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
