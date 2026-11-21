---

title: "bson_append_int64(3)"
name: "bson_append_int64"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_int64/"
description: "bson_append_int64() – The bson_append_int64() function shall append a new element to bson containing a 64-bit signed integer."
---

<h2>NAME</h2>
<p> bson_append_int64() &#8211; The bson_append_int64() function shall append a new element to bson containing a 64-bit signed integer.</p>
<pre><code>
bool bson_append_int64(bson_t *bson,
                       const char *key,
                       int key_length,
                       int64_t value);
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
<dt><code>value</code></dt>
<dd> An int64_t.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_append_int64/">bson_append_int64</a>(3)</code> function shall append a new element to <code>bson</code> containing a 64-bit signed integer. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
