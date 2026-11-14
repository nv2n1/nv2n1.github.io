---
title: "mongoc_server_description_host(3)"
name: "mongoc_server_description_host"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_server_description_host/"
description: "mongoc_server_description_host() – This function returns the host that the given server description is associated with. This object is owned by the server description"
---

<p>mongoc_server_description_host() &#8211; This function returns the host that the given server description is associated with. This object is owned by the server description</p>
<h2>Synopsis</h2>
<pre>mongoc_host_list_t *
mongoc_server_description_host (const mongoc_server_description_t *description);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>description</code></p>
<dd>A <code>The server description for which we&#8217;d like a host</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function returns the host that the given server description is associated with. This object is owned by the server description </p>
<h2>Returns</h2>
<p>A reference to the given server description&#8217;s <code>mongoc_host_list_t</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
