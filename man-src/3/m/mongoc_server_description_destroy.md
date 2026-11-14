---
title: "mongoc_server_description_destroy(3)"
name: "mongoc_server_description_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_server_description_destroy/"
description: "mongoc_server_description_destroy() – This function cleans up all memory associated with the given server description."
---

<p>mongoc_server_description_destroy() &#8211; This function cleans up all memory associated with the given server description.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_server_description_destroy(mongoc_server_description_t *description);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>description</code></p>
<dd>A <code>The description to destroy.</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function cleans up all memory associated with the given server description. </p>
<h2>Returns</h2>
<p>None. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
