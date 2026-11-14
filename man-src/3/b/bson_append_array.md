---
title: "bson_append_array(3)"
name: "bson_append_array"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_array/"
description: "bson_append_array() – The bson_append_array() function shall append child to bson using the specified key. The type of the field will be an array, but it is the responsibility of the caller to ensu..."
---

<h2>NAME</h2>
<p> bson_append_array() &#8211; The bson_append_array() function shall append child to bson using the specified key. The type of the field will be an array, but it is the responsibility of the caller to ensure that the keys of child are properly formatted with string keys such as &quot;0&quot;, &quot;1&quot;, &quot;2&quot; and so forth.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_array(bson_t *bson,
                       const char *key,
                       int key_length,
                       const bson_t *array);
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
<dt><code>array</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_array/">bson_append_array</a>(3)</code> function shall append <code>child</code> to <code>bson</code> using the specified key. The type of the field will be an array, but it is the responsibility of the caller to ensure that the keys of <code>child</code> are properly formatted with string keys such as &quot;0&quot;, &quot;1&quot;, &quot;2&quot; and so forth. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
