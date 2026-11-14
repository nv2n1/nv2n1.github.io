---
title: "bson_oid_init_from_string(3)"
name: "bson_oid_init_from_string"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_init_from_string/"
description: "bson_oid_init_from_string() – Parses the string containing hex encoded oid and initialize the bytes in oid."
---

<h2>NAME</h2>
<p> bson_oid_init_from_string() &#8211; Parses the string containing hex encoded oid and initialize the bytes in oid.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_oid_init_from_string(bson_oid_t *oid,
                               const char *str);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<dl>
<dt><code>str</code></p>
<dd> A string containing a hex encoded version of the oid.</dl>
<h2>DESCRIPTION</h2>
<p> Parses the string containing hex encoded oid and initialize the bytes in <code>oid</code> \&amp;. </p>
<h2>EXAMPLE</h2>
<pre>
bson_oid_init_from_string (&amp;oid, &quot;012345678901234567890123&quot;);
</pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
