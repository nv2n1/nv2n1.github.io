---

title: "bson_oid_init(3)"
name: "bson_oid_init"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_init/"
description: "bson_oid_init() – Generates a new bson_oid_t using either context or the default bson_context_t."
---

<p> bson_oid_init() &#8211; Generates a new bson_oid_t using either context or the default bson_context_t.</p>
<h2>SYNOPSIS</h2>
<pre>
void
bson_oid_init (bson_oid_t     *oid,
               bson_context_t *context);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></dt>
<dd> A <code>bson_oid_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>context</code></dt>
<dd> An <code>optional</code> </dd>
<p> <code>bson_context_t</code> or NULL.</dl>
<h2>DESCRIPTION</h2>
<p> Generates a new <code>bson_oid_t</code> using either <code>context</code> or the default <code>bson_context_t</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
