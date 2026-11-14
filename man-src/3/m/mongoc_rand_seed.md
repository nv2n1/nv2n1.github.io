---
title: "mongoc_rand_seed(3)"
name: "mongoc_rand_seed"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_rand_seed/"
description: "mongoc_rand_seed() – Seeds the mongoc random number generator with num bytes of entropy."
---

<p>mongoc_rand_seed() &#8211; Seeds the mongoc random number generator with num bytes of entropy.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_rand_seed(const void *buf,
 int num);</pre>
<h2>Description</h2>
<p>Seeds the mongoc random number generator with num bytes of entropy. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>buf</code></p>
<dd>A buffer.</dl>
<dl COMPACT>
<dt><code>num</code></p>
<dd>An int of number of bytes in buf.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
