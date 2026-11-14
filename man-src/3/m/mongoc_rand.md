---
title: "mongoc_rand(3)"
name: "mongoc_rand"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_rand/"
description: "mongoc_rand – MongoDB Random Number Generator"
---

<p>mongoc_rand &#8211; MongoDB Random Number Generator</p>
<h2>Synopsis</h2>
<pre>void
mongoc_rand_add (const void *buf,
 int num,
 doubel entropy);
void
mongoc_rand_seed (const void *buf,
 int num);
int
mongoc_rand_status (void);</pre>
<h2>Description</h2>
<p>The <code>mongoc_rand</code> family of functions provide access to the low level randomness primitives used by the MongoDB C Driver. In particular, they control the creation of cryptographically strong pseudo-random bytes required by some security mechanisms. </p>
<p> While we can usually pull enough entropy from the environment, you may be required to seed the PRNG manually depending on your OS, hardware and other entropy consumers running on the same system. </p>
<h2>Entropy</h2>
<p><code>mongoc_rand_add</code> and <code>mongoc_rand_seed</code> allow the user to directly provide entropy. They differ insofar as <code>mongoc_rand_seed</code> requires that each bit provided is fully random. <code>mongoc_rand_add</code> allows the user to specify the degree of randomness in the provided bytes as well. </p>
<h2>Status</h2>
<p>The <code>mongoc_rand_status</code> function allows the user to check the status of the mongoc PRNG. This can be used to guarantee sufficient entropy at program startup, rather than waiting for runtime errors to occur. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
