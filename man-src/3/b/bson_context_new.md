---
title: "bson_context_new(3)"
name: "bson_context_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_context_new/"
description: "bson_context_new() – Creates a new bson_context_t. This is rarely needed as bson_context_get_default() serves most use-cases."
---

<h2>NAME</h2>
<p> bson_context_new() &#8211; Creates a new bson_context_t. This is rarely needed as bson_context_get_default() serves most use-cases.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_context_t *
bson_context_new (bson_context_flags_t flags);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>flags</code></p>
<dd> A <code>bson_context_flags_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new <code>bson_context_t</code> \&amp;. This is rarely needed as <code><a href="/docs/linux/man/3-bson_context_get_default/">bson_context_get_default</a>(3)</code> serves most use-cases. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_context_t</code> that should be freed with <code>bson_context_destroy</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
