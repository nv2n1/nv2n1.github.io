---
title: "bson_append_code_with_scope(3)"
name: "bson_append_code_with_scope"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_code_with_scope/"
description: "bson_append_code_with_scope() – The bson_append_code_with_scope() function shall perform like bson_append_code() except it allows providing a scope to the javascript function in the form of a bson ..."
---

<h2>NAME</h2>
<p> bson_append_code_with_scope() &#8211; The bson_append_code_with_scope() function shall perform like bson_append_code() except it allows providing a scope to the javascript function in the form of a bson document.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_code_with_scope(bson_t *bson,
                                 const char *key,
                                 int key_length,
                                 const char *javascript,
                                 const bson_t *scope);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII C string containing the name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>javascript</code></p>
<dd> A NULL-terminated UTF-8 encoded string containing the javascript fragment.</dl>
<dl>
<dt><code>scope</code></p>
<dd> A <code>bson_t</code> containing the scope for <code>javascript</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_code_with_scope/">bson_append_code_with_scope</a>(3)</code> function shall perform like <code><a href="/docs/linux/man/3-bson_append_code/">bson_append_code</a>(3)</code> except it allows providing a scope to the javascript function in the form of a bson document. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
