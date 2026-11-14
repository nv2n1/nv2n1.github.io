---
title: "mongoc_uri_get_hosts(3)"
name: "mongoc_uri_get_hosts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_hosts/"
description: "mongoc_uri_get_hosts() – Fetches a linked list of hosts that were defined in the URI (the comma-separated host section)."
---

<p>mongoc_uri_get_hosts() &#8211; Fetches a linked list of hosts that were defined in the URI (the comma-separated host section).</p>
<h2>Synopsis</h2>
<pre>const mongoc_host_list_t *
mongoc_uri_get_hosts (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches a linked list of hosts that were defined in the URI (the comma-separated host section). </p>
<h2>Returns</h2>
<p>A linked list of <code>mongoc_host_list_t</code> structures that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
