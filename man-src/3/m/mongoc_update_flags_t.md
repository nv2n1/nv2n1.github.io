---
title: "mongoc_update_flags_t(3)"
name: "mongoc_update_flags_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_update_flags_t/"
description: "mongoc_update_flags_t – Flags for deletion operations"
---

<p>mongoc_update_flags_t &#8211; Flags for deletion operations</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_UPDATE_NONE = 0,
 MONGOC_UPDATE_UPSERT = 1 &lt;&lt; 0,
 MONGOC_UPDATE_MULTI_UPDATE = 1 &lt;&lt; 1,
} mongoc_update_flags_t;
#define MONGOC_UPDATE_NO_VALIDATE (1U &lt;&lt; 31)</pre>
<h2>Description</h2>
<p>These flags correspond to the MongoDB wire protocol. They may be bitwise or&#8217;d together. The allow for modifying the way an update is performed in the MongoDB server. </p>
<h2>Flag Values</h2>
<dl COMPACT>
<dt><code>MONGOC_UPDATE_NONE</code></dt>
<dd>No update flags set.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_UPDATE_UPSERT</code></dt>
<dd>If an upsert should be performed.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_UPDATE_MULTI_UPDATE</code></dt>
<dd>If more than a single matching document should be updated. By default only the first document is updated.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_UPDATE_NO_VALIDATE</code></dt>
<dd>Do not perform client side BSON validations when performing an update. This is useful if you already know your BSON documents are valid.</dd></dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
