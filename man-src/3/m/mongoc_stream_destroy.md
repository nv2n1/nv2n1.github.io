---
title: "mongoc_stream_destroy(3)"
name: "mongoc_stream_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_destroy/"
description: "mongoc_stream_destroy() – This function shall release all resources associated with a mongoc_stream_t, including freeing the structure. It is invalid to use stream after calling this function."
---

<p>mongoc_stream_destroy() &#8211; This function shall release all resources associated with a mongoc_stream_t, including freeing the structure. It is invalid to use stream after calling this function.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_stream_destroy (mongoc_stream_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<p> This function shall release all resources associated with a <code>mongoc_stream_t</code> , including freeing the structure. It is invalid to use <code>stream</code> after calling this function. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
