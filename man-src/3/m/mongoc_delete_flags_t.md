---
title: "mongoc_delete_flags_t(3)"
name: "mongoc_delete_flags_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_delete_flags_t/"
description: "mongoc_delete_flags_t – Flags for deletion operations"
---

<p>mongoc_delete_flags_t &#8211; Flags for deletion operations</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_DELETE_NONE = 0,
 MONGOC_DELETE_SINGLE_REMOVE = 1 &lt;&lt; 0,
} mongoc_delete_flags_t;</pre>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>These flags are deprecated and should not be used in new code.</dl>
<p> Please use <code>mongoc_remove_flags_t</code> with <code><a href="/docs/linux/man/3-mongoc_collection_remove/">mongoc_collection_remove</a>(3)</code> instead. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
