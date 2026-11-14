---
title: "mongoc_server_description_new_copy(3)"
name: "mongoc_server_description_new_copy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_server_description_new_copy/"
description: "mongoc_server_description_new_copy() – This function copies the given server description and returns a new server description object. The caller is responsible for destroying the new copy."
---

<p>mongoc_server_description_new_copy() &#8211; This function copies the given server description and returns a new server description object. The caller is responsible for destroying the new copy.</p>
<h2>Synopsis</h2>
<pre>mongoc_server_description_t *
mongoc_server_description_new_copy (const mongoc_server_description_t *description);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>description</code></p>
<dd>A <code>The server description to copy</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function copies the given server description and returns a new server description object. The caller is responsible for destroying the new copy. </p>
<h2>Returns</h2>
<p>A copy of the original server description. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
