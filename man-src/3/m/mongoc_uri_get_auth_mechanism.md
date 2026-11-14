---
title: "mongoc_uri_get_auth_mechanism(3)"
name: "mongoc_uri_get_auth_mechanism"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_auth_mechanism/"
description: "mongoc_uri_get_auth_mechanism() – Fetches the authMechanism parameter to an URI if provided."
---

<p>mongoc_uri_get_auth_mechanism() &#8211; Fetches the authMechanism parameter to an URI if provided.</p>
<h2>Synopsis</h2>
<pre>const char *
mongoc_uri_get_auth_mechanism (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the <code>authMechanism</code> parameter to an URI if provided. </p>
<h2>Returns</h2>
<p>A string which should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
