---
title: "mongoc_insert_flags_t(3)"
name: "mongoc_insert_flags_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_insert_flags_t/"
description: "mongoc_insert_flags_t – Flags for deletion operations"
---

<p>mongoc_insert_flags_t &#8211; Flags for deletion operations</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_INSERT_NONE = 0,
 MONGOC_INSERT_CONTINUE_ON_ERROR = 1 &lt;&lt; 0,
} mongoc_insert_flags_t;
#define MONGOC_INSERT_NO_VALIDATE (1U &lt;&lt; 31)</pre>
<h2>Description</h2>
<p>These flags correspond to the MongoDB wire protocol. They may be bitwise or&#8217;d together. They may modify how an insert happens on the MongoDB server. </p>
<h2>Flag Values</h2>
<dl COMPACT>
<dt><code>MONGOC_INSERT_NONE</code></p>
<dd>Specify no insert flags.</dl>
<dl COMPACT>
<dt><code>MONGOC_INSERT_CONTINUE_ON_ERROR</code></p>
<dd>Continue inserting documents from the insertion set even if one insert fails.</dl>
<dl COMPACT>
<dt><code>MONGOC_INSERT_NO_VALIDATE</code></p>
<dd>Do not validate insertion documents before performing an insert. Validation can be expensive, so this can save some time if you know your documents are already valid.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
