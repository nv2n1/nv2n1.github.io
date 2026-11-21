---

title: "bson_iter_overwrite_int32(3)"
name: "bson_iter_overwrite_int32"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_overwrite_int32/"
description: "bson_iter_overwrite_int32() – The bson_iter_overwrite_int32() function shall overwrite the contents of a BSON_TYPE_INT32 element in place."
---

<h2>NAME</h2>
<p> bson_iter_overwrite_int32() &#8211; The bson_iter_overwrite_int32() function shall overwrite the contents of a BSON_TYPE_INT32 element in place.</p>
<pre>
void
bson_iter_overwrite_int32 (bson_iter_t *iter,
                           int32_t      value);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></dt>
<dd> A <code>bson_iter_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>value</code></dt>
<dd> A int32_t.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_iter_overwrite_int32/">bson_iter_overwrite_int32</a>(3)</code> function shall overwrite the contents of a BSON_TYPE_INT32 element in place. </p>
<p> This may only be done when the underlying bson document allows mutation. </p>
<p> It is a programming error to call this function when <code>iter</code> is not obvserving an element of type BSON_TYPE_BOOL. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
