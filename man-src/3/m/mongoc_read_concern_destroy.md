---
title: "mongoc_read_concern_destroy(3)"
name: "mongoc_read_concern_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_concern_destroy/"
description: "mongoc_read_concern_destroy() – Frees all resources associated with the read concern structure."
---

<p>mongoc_read_concern_destroy() &#8211; Frees all resources associated with the read concern structure.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_read_concern_destroy (mongoc_read_concern_t *read_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_concern</code></p>
<dd>A <code>mongoc_read_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Frees all resources associated with the read concern structure. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
