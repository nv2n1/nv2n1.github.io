---
title: "mongoc_rand_add(3)"
name: "mongoc_rand_add"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_rand_add/"
description: "mongoc_rand_add() – Mixes num bytes of data into the mongoc random number generator. Entropy specifies a lower bound estimate of the randomness contained in buf."
---

<p>mongoc_rand_add() &#8211; Mixes num bytes of data into the mongoc random number generator. Entropy specifies a lower bound estimate of the randomness contained in buf.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_rand_add(const void *buf,
 int num,
 double entropy);</pre>
<h2>Description</h2>
<p>Mixes num bytes of data into the mongoc random number generator. Entropy specifies a lower bound estimate of the randomness contained in buf. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>buf</code></p>
<dd>A buffer.</dl>
<dl COMPACT>
<dt><code>num</code></p>
<dd>An int of number of bytes in buf.</dl>
<dl COMPACT>
<dt><code>entropy</code></p>
<dd>A double of randomness estimate in buf.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
