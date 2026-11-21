---
title: "bson_iter_utf8(3)"
name: "bson_iter_utf8"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_utf8/"
description: "bson_iter_utf8() – The bson_iter_utf8() function shall retrieve the contents of a BSON_TYPE_UTF8 element currently observed by iter."
---
<h2>NAME</h2>
<p> bson_iter_utf8() - The bson_iter_utf8() function shall retrieve the contents of a BSON_TYPE_UTF8 element currently observed by iter.  </p>
<h2>SYNOPSIS</h2>
<pre><code>#define BSON_ITER_HOLDS_UTF8(iter) \
   (bson_iter_type ((iter)) == BSON_TYPE_UTF8)
const char *
bson_iter_utf8 (const bson_iter_t *iter,
                uint32_t *length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></dt>
<dd> <p> A <code>bson_iter_t</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>length</code></dt>
<dd> <p> An optional location for the length of the resulting UTF-8 encoded string. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_utf8/">bson_iter_utf8</a>(3)</code> function shall retrieve the contents of a BSON_TYPE_UTF8 element currently observed by <code>iter</code> \&amp;. </p>
<p> It is invalid to call this function while observing an element other than BSON_TYPE_UTF8. </p>
<h2>RETURNS</h2>
<p> A UTF-8 encoded string that has not been modified or freed. </p>
<p> It is suggested that the caller validate the content is valid UTF-8 before using this in other places. That can be done by calling <code><a href="/docs/linux/man/3-bson_utf8_validate/">bson_utf8_validate</a>(3)</code> or validating the underlying <code>bson_t</code> before iterating it. </p>
<p> Note that not all drivers use multi-byte representation for <code>\0</code> in UTF-8 encodings (commonly referred to as modified-UTF8). You probably want to take a look at the length field when marshaling to other runtimes. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
