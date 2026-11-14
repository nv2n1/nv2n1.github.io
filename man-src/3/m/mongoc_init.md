---
title: "mongoc_init(3)"
name: "mongoc_init"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_init/"
description: "mongoc_init() – This function should be called at the beginning of every program using the MongoDB C driver. It is responsible for initializing global state such as process counters, SSL, and threa..."
---

<p>mongoc_init() &#8211; This function should be called at the beginning of every program using the MongoDB C driver. It is responsible for initializing global state such as process counters, SSL, and threading primatives.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_init (void);</pre>
<h2>Description</h2>
<p>This function should be called at the beginning of every program using the MongoDB C driver. It is responsible for initializing global state such as process counters, SSL, and threading primatives. </p>
<p> When your process has completed, you should also call <code>mongoc_cleanup</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
