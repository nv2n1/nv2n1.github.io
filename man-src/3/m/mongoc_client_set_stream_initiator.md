---
title: "mongoc_client_set_stream_initiator(3)"
name: "mongoc_client_set_stream_initiator"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_set_stream_initiator/"
description: "mongoc_client_set_stream_initiator() – None"
---

<p>mongoc_client_set_stream_initiator() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_set_stream_initiator (mongoc_client_t *client,
 mongoc_stream_initiator_t initiator,
 void *user_data);</pre>
<p>The <code><a href="/docs/linux/man/3-mongoc_client_set_stream_initiator/">mongoc_client_set_stream_initiator</a>(3)</code> function shall associate a given <code>mongoc_client_t</code> with a new stream initiator. This will completely replace the default transport (buffered TCP, possibly with TLS). The <code>initiator</code> should fulfill the <code>mongoc_stream_t</code> contract. <code>user_data</code> is passed through to the <code>initiator</code> callback and may be used for whatever run time customization is necessary. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>initiator</code></p>
<dd>A <code>mongoc_stream_initiator_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>user_data</code></p>
<dd>User supplied pointer for callback function.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
