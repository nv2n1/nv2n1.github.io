---
title: "mongoc_client_set_ssl_opts(3)"
name: "mongoc_client_set_ssl_opts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_set_ssl_opts/"
description: "mongoc_client_set_ssl_opts() – None"
---

<p>mongoc_client_set_ssl_opts() &#8211; None</p>
<h2>Synopsis</h2>
<pre>#ifdef MONGOC_ENABLE_SSL
mongoc_client_set_ssl_opts (mongoc_client_t *client,
 const mongoc_ssl_opt_t *opts);
#endif</pre>
<p>Sets the SSL options to use when connecting to SSL enabled MongoDB servers. </p>
<p> Beginning in version 1.2.0, once a client has any SSL options set, all connections use SSL, even if &quot;ssl=true&quot; is omitted from the MongoDB URI. Before, SSL options were ignored unless &quot;ssl=true&quot; was included in the URI. </p>
<p> Although the <code>mongoc_ssl_opt_t</code> struct itself is shallow-copied by the client, the strings it points to ( <code>pem_file</code> , <code>pem_pwd</code> , <code>ca_file</code> , <code>ca_dir</code> , and <code>crl_file</code> ) are not copied and must remain valid for the life of the <code>mongoc_client_t</code> \&amp;. </p>
<p> It is a programming error to call this function on a client from a <code>mongoc_client_pool_t</code> \&amp;. Instead, call <code>mongoc_client_pool_set_ssl_opts</code> on the pool before popping any clients. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>mongoc_ssl_opt_t</code> \&amp;. The struct is copied by the client, but the strings it points to are not.</dl>
<h2>Availability</h2>
<p>This feature requires that the MongoDB C driver was compiled with <code>&#8211;enable-ssl</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
