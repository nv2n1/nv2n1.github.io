---
title: "mongoc_uri_new(3)"
name: "mongoc_uri_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_new/"
description: "mongoc_uri_new() – Parses a string containing a MongoDB style URI connection string."
---

<p>mongoc_uri_new() &#8211; Parses a string containing a MongoDB style URI connection string.</p>
<h2>Synopsis</h2>
<pre>mongoc_uri_t *
mongoc_uri_new (const char *uri_string)
 BSON_GNUC_WARN_UNUSED_RESULT;</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri_string</code></p>
<dd>A string containing a URI.</dl>
<h2>Description</h2>
<p>Parses a string containing a MongoDB style URI connection string. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_uri_t</code> if successful. Otherwise <code>NULL</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Failure to handle the result of this function is a programming error.</dl>
<h2>Examples</h2>
<p>Examples of some valid MongoDB connection strings can be seen below. </p>
<p> <code>mongodb://localhost/</code> </p>
<p> <code>mongodb://localhost/?replicaSet=myreplset</code> </p>
<p> <code>mongodb://myuser:mypass [at] localhost/</code> </p>
<p> <code>mongodb://kerberosuser%40EXAMPLE.COM [at] example.com/?authMechanism=GSSAPI</code> </p>
<p> <code>mongodb://[::1]:27017/</code> </p>
<p> <code>mongodb://10.0.0.1:27017,10.0.0.1:27018,[::1]:27019/?ssl=true</code> </p>
<p> <code>mongodb:///tmp/mongodb-27017.sock</code> </p>
<p> <code>mongodb://localhost,[::1]/mydb?authSource=mydb</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
