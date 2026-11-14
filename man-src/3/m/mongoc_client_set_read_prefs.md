---
title: "mongoc_client_set_read_prefs(3)"
name: "mongoc_client_set_read_prefs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_set_read_prefs/"
description: "mongoc_client_set_read_prefs() – None"
---

<p>mongoc_client_set_read_prefs() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_set_read_prefs (mongoc_client_t *client,
 const mongoc_read_prefs_t *read_prefs);</pre>
<p>Sets the default read preferences to use with future operations upon <code>client</code> \&amp;. </p>
<p> The global default is to read from the replica set primary. </p>
<p> It is a programming error to call this function on a client from a <code>mongoc_client_pool_t</code> \&amp;. For pooled clients, set the read preferences with the <code>MongoDB URI</code> instead. </p>
<p> Please see the MongoDB website for a description of <code>Read Preferences</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
