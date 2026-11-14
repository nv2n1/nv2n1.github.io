---
title: "mongoc_server_description_t(3)"
name: "mongoc_server_description_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_server_description_t/"
description: "mongoc_server_description_t – Server description"
---

<p>mongoc_server_description_t &#8211; Server description</p>
<h2>Synopsis</h2>
<pre>#include &lt;mongoc.h&gt;
typedef struct _mongoc_server_description_t mongoc_server_description_t</pre>
<p><code>mongoc_server_description_t</code> holds information about a mongod server to which the driver has connected. </p>
<h2>Lifecycle</h2>
<p>It is required that this object be cleaned up with <code><a href="/docs/linux/man/3-mongoc_server_description_destroy/">mongoc_server_description_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
