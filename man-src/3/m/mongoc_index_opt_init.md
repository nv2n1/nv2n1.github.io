---
title: "mongoc_index_opt_init(3)"
name: "mongoc_index_opt_init"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_index_opt_init/"
description: "mongoc_index_opt_init() – This function will initialize opt to the default values. It should be called before modifying any fields within the structure."
---

<p>mongoc_index_opt_init() &#8211; This function will initialize opt to the default values. It should be called before modifying any fields within the structure.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_index_opt_init (mongoc_index_opt_t *opt);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>opt</code></p>
<dd>A <code>mongoc_index_opt_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function will initialize <code>opt</code> to the default values. It should be called before modifying any fields within the structure. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
