---

title: "bson_append_dbpointer(3)"
name: "bson_append_dbpointer"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_dbpointer/"
description: "bson_append_dbpointer() – The dbpointer field type is DEPRECATED and should only be used when interacting with legacy systems."
---

<h2>NAME</h2>
<p> bson_append_dbpointer() &#8211; The dbpointer field type is DEPRECATED and should only be used when interacting with legacy systems.</p>
<pre><code>
bool bson_append_dbpointer(bson_t *bson,
                           const char *key,
                           int key_length,
                           const char *collection,
                           const bson_oid_t *oid);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>key</code></dt>
<dd> An ASCII C string containing the name of the field.</dd></dl>
<dl>
<dt><code>key_length</code></dt>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dd></dl>
<dl>
<dt><code>collection</code></dt>
<dd> The target collection name.</dd></dl>
<dl>
<dt><code>oid</code></dt>
<dd> The target document identifer.</dd></dl>
<p> <code>NOTE</code></p>
<dl>
<dt>
</dt><dd> The dbpointer field type is <code>DEPRECATED</code> and should only be used when interacting with legacy systems.</dd></dl>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
