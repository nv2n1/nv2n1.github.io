---
title: "bson_append_oid(3)"
name: "bson_append_oid"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_oid/"
description: "bson_append_oid() – The bson_append_oid() function shall append a new element to bson of type BSON_TYPE_OID. oid MUST be a pointer to a bson_oid_t."
---

<h2>NAME</h2>
<p> bson_append_oid() &#8211; The bson_append_oid() function shall append a new element to bson of type BSON_TYPE_OID. oid MUST be a pointer to a bson_oid_t.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_oid(bson_t *bson,
                     const char *key,
                     int key_length,
                     const bson_oid_t *oid);
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
<dt><code>oid</code></p>
<dd> A bson_oid_t.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_oid/">bson_append_oid</a>(3)</code> function shall append a new element to <code>bson</code> of type BSON_TYPE_OID. <code>oid</code> </p>
<p> <code>MUST</code> be a pointer to a <code>bson_oid_t</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
