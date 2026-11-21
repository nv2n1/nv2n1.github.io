---

title: "bson_append_utf8(3)"
name: "bson_append_utf8"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_utf8/"
description: "bson_append_utf8() – The bson_append_utf8() function shall append a UTF-8 encoded string to bson."
---

<p> bson_append_utf8() - The bson_append_utf8() function shall append a UTF-8 encoded string to bson.  </p>
<h2>SYNOPSIS</h2>
<pre><code>bool
bson_append_utf8 (bson_t *bson,
                  const char *key,
                  int key_length,
                  const char *value,
                  int length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></dt>
<dd> <p> A <code>bson_t</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>key</code></dt>
<dd> <p> An ASCII C string containing the name of the field. </p>
 </dd></dl>
<dl>
<dt><code>key_length</code></dt>
<dd> <p> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>value</code></dt>
<dd> <p> A UTF-8 encoded string. </p>
 </dd></dl>
<dl>
<dt><code>length</code></dt>
<dd> <p> The number of bytes in <code>value</code> excluding the trailing <code>\0</code> , or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_utf8/">bson_append_utf8</a>(3)</code> function shall append a UTF-8 encoded string to <code>bson</code> \&amp;. </p>
<p> _value_ <code>MUST</code> be valid UTF-8. </p>
<p> Some UTF-8 implementations allow for <code>\0</code> to be contained within the string (excluding the termination <code>\0</code> \&amp;. This is allowed, but remember that it could cause issues with communicating with external systems that do not support it. </p>
<p> It is suggested to use modified UTF-8 which uses a 2 byte representation for embedded <code>\0</code> within the string. This will allow these UTF-8 encoded strings to used with many libc functions. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
