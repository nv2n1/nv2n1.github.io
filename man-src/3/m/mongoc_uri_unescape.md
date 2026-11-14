---
title: "mongoc_uri_unescape(3)"
name: "mongoc_uri_unescape"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_unescape/"
description: "mongoc_uri_unescape() – Unescapes an URI encoded string. For example, \"%40\" would become \"@\"."
---

<p>mongoc_uri_unescape() &#8211; Unescapes an URI encoded string. For example, &quot;%40&quot; would become &quot;@&quot;.</p>
<h2>Synopsis</h2>
<pre>char *
mongoc_uri_unescape (const char *escaped_string);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>escaped_string</code></p>
<dd>A utf8 encoded string.</dl>
<h2>Description</h2>
<p>Unescapes an URI encoded string. For example, &quot;%40&quot; would become &quot;@&quot;. </p>
<h2>Returns</h2>
<p>Returns a newly allocated string that should be freed with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
