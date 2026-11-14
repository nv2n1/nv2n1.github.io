---
title: "mongoc_rand_status(3)"
name: "mongoc_rand_status"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_rand_status/"
---

mongoc_rand_status() - The status of the mongoc random number generator.
<h2>Synopsis</h2><pre>int
mongoc_rand_status(void);</pre><h2>Description</h2>The status of the mongoc random number generator. 

<h2>Returns</h2>Returns 1 if the PRNG has been seeded with enough data, 0 otherwise. 

 

<h2>Colophon</h2>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" HREF="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a>
