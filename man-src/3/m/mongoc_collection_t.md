---
title: "mongoc_collection_t(3)"
name: "mongoc_collection_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_t/"
description: "mongoc_collection_t – #include <mongoc.h>"
---

<p>mongoc_collection_t &#8211; #include &lt;mongoc.h&gt; </p>
<p> typedef struct _mongoc_collection_t mongoc_collection_t;</p>
<h2>Synopsis</h2>
<pre>#include &lt;mongoc.h&gt;
typedef struct _mongoc_collection_t mongoc_collection_t;</pre>
<p><code>mongoc_collection_t</code> provides access to a MongoDB collection. This handle is useful for actions for most CRUD operations, I.e. insert, update, delete, find, etc. </p>
<h2>Read Preferences And Write Concerns</h2>
<p>Read preferences and write concerns are inherited from the parent client. They can be overridden by set_* commands if so desired. </p>
<h2>Lifecycle</h2>
<p>It is an error to call <code><a href="/docs/linux/man/3-mongoc_collection_destroy/">mongoc_collection_destroy</a>(3)</code> on a collection that has operations pending. It is required that you release <code>mongoc_cursor_t</code> structures before calling <code><a href="/docs/linux/man/3-mongoc_collection_destroy/">mongoc_collection_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
