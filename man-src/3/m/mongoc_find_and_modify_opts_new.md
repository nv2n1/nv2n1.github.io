---
title: "mongoc_find_and_modify_opts_new(3)"
name: "mongoc_find_and_modify_opts_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_new/"
description: "mongoc_find_and_modify_opts_new() – None"
---

<p>mongoc_find_and_modify_opts_new() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_find_and_modify_opts_t *
mongoc_find_and_modify_opts_new (void);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<h2>Returns</h2>
<p>Creates a newly allocated find and modify builder structure that is used to create a findAndModify command. This should be freed with <code><a href="/docs/linux/man/3-mongoc_find_and_modify_opts_destroy/">mongoc_find_and_modify_opts_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
