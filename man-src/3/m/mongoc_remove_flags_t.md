---
title: "mongoc_remove_flags_t(3)"
name: "mongoc_remove_flags_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_remove_flags_t/"
description: "mongoc_remove_flags_t – Flags for deletion operations"
---

<p>mongoc_remove_flags_t &#8211; Flags for deletion operations</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_REMOVE_NONE = 0,
 MONGOC_REMOVE_SINGLE_REMOVE = 1 &lt;&lt; 0,
} mongoc_remove_flags_t;</pre>
<h2>Description</h2>
<p>These flags correspond to the MongoDB wire protocol. They may be bitwise or&#8217;d together. They may change the number of documents that are removed during a remove command. </p>
<h2>Flag Values</h2>
<dl COMPACT>
<dt><code>MONGOC_REMOVE_NONE</code></p>
<dd>Specify no removal flags. All matching documents will be removed.</dl>
<dl COMPACT>
<dt><code>MONGOC_REMOVE_SINGLE_REMOVE</code></p>
<dd>Only remove the first matching document from the selector.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
