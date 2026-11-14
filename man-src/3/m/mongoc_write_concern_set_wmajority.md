---
title: "mongoc_write_concern_set_wmajority(3)"
name: "mongoc_write_concern_set_wmajority"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_set_wmajority/"
description: "mongoc_write_concern_set_wmajority() – Sets if the write must have been propagated to a majority of nodes before indicating write success."
---

<p>mongoc_write_concern_set_wmajority() &#8211; Sets if the write must have been propagated to a majority of nodes before indicating write success.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_write_concern_set_wmajority (mongoc_write_concern_t *write_concern,
 int32_t wtimeout_msec);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>wtimeout_msec</code></p>
<dd>A positive <code>int32_t</code> or zero.</dl>
<h2>Description</h2>
<p>Sets if the write must have been propagated to a majority of nodes before indicating write success. </p>
<p> The timeout specifies how long, in milliseconds, the server should wait before indicating that the write has failed. This is not the same as a socket timeout. A value of zero may be used to indicate no timeout. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
