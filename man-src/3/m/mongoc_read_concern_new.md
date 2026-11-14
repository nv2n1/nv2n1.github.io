---
title: "mongoc_read_concern_new(3)"
name: "mongoc_read_concern_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_concern_new/"
description: "mongoc_read_concern_new() – None"
---

<p>mongoc_read_concern_new() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_read_concern_t *
mongoc_read_concern_new (void);</pre>
<h2>Returns</h2>
<p>Creates a newly allocated read concern that can be configured based on user preference. This should be freed with <code><a href="/docs/linux/man/3-mongoc_read_concern_destroy/">mongoc_read_concern_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
