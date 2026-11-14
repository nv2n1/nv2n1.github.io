---
title: "mongoc_find_and_modify_opts_destroy(3)"
name: "mongoc_find_and_modify_opts_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_destroy/"
description: "mongoc_find_and_modify_opts_destroy() – Frees all resources associated with the find and modify builder structure."
---

<p>mongoc_find_and_modify_opts_destroy() &#8211; Frees all resources associated with the find and modify builder structure.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_find_and_modify_opts_destroy (mongoc_find_and_modify_opts_t *find_and_modify_opts);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>find_and_modify_opts</code></p>
<dd>A <code>mongoc_find_and_modify_opts_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Frees all resources associated with the find and modify builder structure. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
