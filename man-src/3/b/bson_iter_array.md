---

title: "bson_iter_array(3)"
name: "bson_iter_array"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_array/"
description: "bson_iter_array() – The bson_iter_array() function shall retrieve the raw buffer of a sub-array from iter. iter MUST be on an element that is of type BSON_TYPE_ARRAY. This can be verified with bson..."
---

<h2>NAME</h2>
<p> bson_iter_array() &#8211; The bson_iter_array() function shall retrieve the raw buffer of a sub-array from iter. iter MUST be on an element that is of type BSON_TYPE_ARRAY. This can be verified with bson_iter_type() or the BSON_ITER_HOLDS_ARRAY() macro.</p>
<pre><code>
void bson_iter_array(const bson_iter_t *iter,
                     uint32_t *array_len,
                     const uint8_t **array);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></dt>
<dd> A <code>bson_iter_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>array_len</code></dt>
<dd> A location for the buffer length.</dd></dl>
<dl>
<dt><code>array</code></dt>
<dd> A location for the immutable buffer.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_iter_array/">bson_iter_array</a>(3)</code> function shall retrieve the raw buffer of a sub-array from <code>iter</code> \&amp;. <code>iter</code> </p>
<p> <code>MUST</code> be on an element that is of type BSON_TYPE_ARRAY. This can be verified with <code><a href="/docs/linux/man/3-bson_iter_type/">bson_iter_type</a>(3)</code> or the <code>BSON_ITER_HOLDS_ARRAY(3)</code> macro. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
