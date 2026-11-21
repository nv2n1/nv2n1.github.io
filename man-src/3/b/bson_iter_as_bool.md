---

title: "bson_iter_as_bool(3)"
name: "bson_iter_as_bool"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_as_bool/"
description: "bson_iter_as_bool() – Fetches the current field as if it were a boolean."
---

<h2>NAME</h2>
<p> bson_iter_as_bool() &#8211; Fetches the current field as if it were a boolean.</p>
<pre><code>
bool bson_iter_as_bool(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></dt>
<dd> A <code>bson_iter_t</code> \&amp;.</dd></dl>
<p> Fetches the current field as if it were a boolean. </p>
<p> <code><a href="/docs/linux/man/3-bson_iter_as_bool/">bson_iter_as_bool</a>(3)</code> currently knows how to determine a boolean value from the following types: </p>
<dl>
<dt>\[bu]</dt>
<dd> BSON_TYPE_BOOL</dd>
<dt>\[bu]</dt>
<dd> BSON_TYPE_DOUBLE</dd>
<dt>\[bu]</dt>
<dd> BSON_TYPE_INT32</dd>
<dt>\[bu]</dt>
<dd> BSON_TYPE_INT64</dd>
<dt>\[bu]</dt>
<dd> BSON_TYPE_NULL</dd>
<dt>\[bu]</dt>
<dd> BSON_TYPE_UNDEFINED</dd>
<dt>\[bu]</dt>
<dd> BSON_TYPE_UTF8 </dd>
<p> BSON_TYPE_UTF8 will always equate to <code>true</code> \&amp;. </p>
</dl>
<h2>RETURNS</h2>
<p> true if the field equates to non-zero. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
