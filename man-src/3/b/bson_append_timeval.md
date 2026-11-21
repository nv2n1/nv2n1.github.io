---

title: "bson_append_timeval(3)"
name: "bson_append_timeval"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_timeval/"
description: "bson_append_timeval() – The bson_append_timeval() function is a helper that takes a _struct timeval_ instead of milliseconds since the UNIX epoch."
---

<h2>NAME</h2>
<p> bson_append_timeval() &#8211; The bson_append_timeval() function is a helper that takes a _struct timeval_ instead of milliseconds since the UNIX epoch.</p>
<pre><code>
bool bson_append_timeval(bson_t *bson,
                         const char *key,
                         int key_length,
                         struct timeval *value);
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
<dd> A struct timeval.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_append_timeval/">bson_append_timeval</a>(3)</code> function is a helper that takes a _struct timeval_ instead of milliseconds since the UNIX epoch. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
