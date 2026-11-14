---
title: "mongoc_server_description_id(3)"
name: "mongoc_server_description_id"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_server_description_id/"
description: "mongoc_server_description_id() – This functionr returns the server id for the given server description."
---

<p>mongoc_server_description_id() &#8211; This functionr returns the server id for the given server description.</p>
<h2>Synopsis</h2>
<pre>uint32_t
mongoc_server_description_id (const mongoc_server_description_t *description);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>description</code></p>
<dd>A <code>The server description whose id we want</code> \&amp;.</dl>
<h2>Description</h2>
<p>This functionr returns the server id for the given server description. </p>
<h2>Returns</h2>
<p>A uint32_t id for the given server description. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
