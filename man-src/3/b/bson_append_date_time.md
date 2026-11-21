---

title: "bson_append_date_time(3)"
name: "bson_append_date_time"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_date_time/"
description: "bson_append_date_time() – The bson_append_date_time() function shall append a new element to a bson document containing a date and time with no timezone information. value is assumed to be in UTC f..."
---

<h2>NAME</h2>
<p> bson_append_date_time() &#8211; The bson_append_date_time() function shall append a new element to a bson document containing a date and time with no timezone information. value is assumed to be in UTC format of milliseconds since the UNIX epoch. value MAY be negative.</p>
<pre><code>
bool bson_append_date_time(bson_t *bson,
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
<dd> The date and time as specified in milliseconds since the UNIX epoch.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_append_date_time/">bson_append_date_time</a>(3)</code> function shall append a new element to a <code>bson</code> document containing a date and time with no timezone information. <code>value</code> is assumed to be in UTC format of milliseconds since the UNIX epoch. <code>value</code> </p>
<p> <code>MAY</code> be negative. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
