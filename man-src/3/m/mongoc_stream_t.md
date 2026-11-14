---
title: "mongoc_stream_t(3)"
name: "mongoc_stream_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_t/"
description: "mongoc_stream_t – typedef struct _mongoc_stream_t mongoc_stream_t"
---

<p>mongoc_stream_t &#8211; typedef struct _mongoc_stream_t mongoc_stream_t</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_stream_t mongoc_stream_t</pre>
<p><code>mongoc_stream_t</code> provides a generic streaming IO abstraction based on a struct of pointers interface. The idea is to allow wrappers, perhaps other language drivers, to easily shim their IO system on top of <code>mongoc_stream_t</code> \&amp;. </p>
<p> The API for the stream abstraction is currently private and non-extensible. </p>
<h2>Stream Types</h2>
<p>There are a number of built in stream types that come with mongoc. The default configuration is a buffered unix stream. If SSL is in use, that in turn is wrapped in a tls stream. </p>
<h2>See Also</h2>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
